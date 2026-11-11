#!/usr/bin/env python3
"""Convert the workshop data between CSV and JSON.

    python3 tools/convert.py to-json [dataset ...] [--indent N] [--check]
    python3 tools/convert.py to-csv  [dataset ...] [--check]

With no dataset names, every dataset is converted. Datasets are:
contestants, end_game, main_game, prize_fund.

Conversion rules (see tools/README.md):
  * An empty CSV field is a JSON null, and the other way round.
  * Columns listed under "int" below become JSON numbers; "bool" columns
    become true/false. Every other column stays a string.
  * Every JSON object has every key, in CSV column order.

--check writes nothing. It converts and compares the result with the file
already on disk (JSON compared as data, CSV byte for byte), and exits 1 if
they differ.

Uses only the Python standard library.
"""

import argparse
import csv
import io
import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# JSON root key and typed columns for each dataset. Column names are the same
# in the CSV header and in the JSON keys.
DATASETS = {
    "contestants": {"root": "contestants", "int": ["age"], "bool": []},
    "end_game": {"root": "endGame", "int": ["round"], "bool": []},
    "main_game": {
        "root": "mainGame",
        "int": ["episode", "roundTable", "votes"],
        "bool": ["shield"],
    },
    "prize_fund": {
        "root": "prizeFund",
        "int": ["episode", "prizeOffered", "prizeWon"],
        "bool": [],
    },
}

CSV_NEWLINE = "\r\n"


class ConversionError(Exception):
    pass


def csv_path(name):
    return DATA_DIR / "csv" / f"{name}.csv"


def json_path(name):
    return DATA_DIR / "json" / f"{name}.json"


def parse_cell(name, column, value, spec, where):
    if value == "":
        return None
    if column in spec["int"]:
        try:
            return int(value)
        except ValueError:
            raise ConversionError(f"{where}: {column} must be a whole number, got {value!r}")
    if column in spec["bool"]:
        if value in ("true", "false"):
            return value == "true"
        raise ConversionError(f"{where}: {column} must be true or false, got {value!r}")
    return value


def csv_to_data(name):
    spec = DATASETS[name]
    path = csv_path(name)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        records = []
        for line, row in enumerate(reader, start=2):
            where = f"{path.name} line {line}"
            if len(row) != len(header):
                raise ConversionError(f"{where}: expected {len(header)} fields, got {len(row)}")
            records.append(
                {col: parse_cell(name, col, val, spec, where) for col, val in zip(header, row)}
            )
    for col in spec["int"] + spec["bool"]:
        if col not in header:
            raise ConversionError(f"{path.name}: typed column {col!r} is not in the header")
    return {spec["root"]: records}


def render_json(data, indent):
    return json.dumps(data, indent=indent, ensure_ascii=False) + "\n"


def render_cell(name, column, value, where):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        if value == "":
            raise ConversionError(f"{where}: {column} is an empty string; use null for no value")
        return value
    raise ConversionError(f"{where}: {column} has unsupported value {value!r}")


def data_to_csv(name):
    spec = DATASETS[name]
    path = json_path(name)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if list(data) != [spec["root"]]:
        raise ConversionError(f"{path.name}: expected a single key {spec['root']!r}, got {list(data)}")
    records = data[spec["root"]]
    if not records:
        raise ConversionError(f"{path.name}: no records")
    header = list(records[0])
    out = io.StringIO()
    writer = csv.writer(out, lineterminator=CSV_NEWLINE)
    writer.writerow(header)
    for i, rec in enumerate(records):
        where = f"{path.name} entry {i}"
        if list(rec) != header:
            raise ConversionError(f"{where}: keys differ from the first entry")
        writer.writerow([render_cell(name, col, rec[col], where) for col in header])
    return out.getvalue()


def to_json(name, indent, check):
    data = csv_to_data(name)
    path = json_path(name)
    if check:
        if not path.exists():
            return f"{path.name}: missing"
        with open(path, encoding="utf-8") as f:
            if json.load(f) != data:
                return f"{path.name}: differs from {csv_path(name).name}"
        return None
    path.write_text(render_json(data, indent), encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(DATA_DIR.parent)}")
    return None


def to_csv(name, check):
    text = data_to_csv(name)
    path = csv_path(name)
    if check:
        if not path.exists():
            return f"{path.name}: missing"
        if path.read_bytes() != text.encode("utf-8"):
            return f"{path.name}: differs from {json_path(name).name}"
        return None
    path.write_bytes(text.encode("utf-8"))
    print(f"wrote {path.relative_to(DATA_DIR.parent)}")
    return None


def main():
    parser = argparse.ArgumentParser(description="Convert workshop data between CSV and JSON.")
    parser.add_argument("direction", choices=["to-json", "to-csv"])
    parser.add_argument("datasets", nargs="*", metavar="dataset", help=", ".join(DATASETS))
    parser.add_argument("--indent", type=int, default=4, help="JSON indent (default 4)")
    parser.add_argument("--check", action="store_true", help="compare only, write nothing")
    args = parser.parse_args()

    unknown = [d for d in args.datasets if d not in DATASETS]
    if unknown:
        parser.error(f"unknown dataset(s): {', '.join(unknown)}")
    names = args.datasets or list(DATASETS)

    problems = []
    for name in names:
        try:
            if args.direction == "to-json":
                problem = to_json(name, args.indent, args.check)
            else:
                problem = to_csv(name, args.check)
        except (ConversionError, OSError, json.JSONDecodeError) as e:
            problem = str(e)
        if problem:
            problems.append(problem)

    for p in problems:
        print(f"error: {p}", file=sys.stderr)
    if args.check and not problems:
        print("ok: files match")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
