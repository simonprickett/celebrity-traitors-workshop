# Tools

## `convert.py`

Converts the workshop data between CSV (`data/csv/`) and JSON (`data/json/`), in either direction. Each dataset exists in both formats on purpose, and this script is how the two are kept in step. It uses only the Python 3 standard library, so there is nothing to install.

Run it from the repository root:

```
python3 tools/convert.py to-json [dataset ...]
python3 tools/convert.py to-csv  [dataset ...]
```

With no dataset names, all four are converted: `contestants`, `end_game`, `main_game`, `prize_fund`.

| Option | Meaning |
|---|---|
| `--check` | Write nothing. Convert, compare with the file already on disk, report any difference and exit with status 1. JSON is compared as data (formatting is ignored); CSV is compared byte for byte. |
| `--indent N` | Indent width for generated JSON (default 4). |

Examples:

```
# Regenerate main_game.json after editing main_game.csv
python3 tools/convert.py to-json main_game

# Confirm every JSON file matches its CSV, and the reverse
python3 tools/convert.py to-json --check
python3 tools/convert.py to-csv --check
```

### Conversion rules

| CSV | JSON |
|---|---|
| Empty field | `null` |
| `true` / `false` | `true` / `false` (boolean) |
| Whole number in a numeric column | JSON number |
| Anything else | string |

- **Numeric columns** are listed per dataset in `DATASETS` at the top of `convert.py` (for example `age`, `round`, `episode`, `roundTable`, `votes`, `prizeOffered`, `prizeWon`). A value in one of these columns that is not a whole number is an error.
- **Boolean columns** are also listed there (`shield`). Values must be exactly `true` or `false`.
- **Every JSON object has every key**, in the same order as the CSV columns. A missing value is `null`, never an omitted key.
- **Dates** are not converted. They stay as `DD/MM/YYYY` strings in both formats.
- **Empty strings are not allowed in JSON.** `to-csv` stops with an error if it finds `""`, because it could not be told apart from `null` in the CSV.
- **CSV output** uses CRLF line endings, with a line ending after the last row, to match the existing files.
- **JSON output** uses LF line endings and ends with a newline.

`null` carries more than one meaning in the data. In `main_game`, for example, an empty `votedFor` can mean there was no round table, or that the player did not vote.

### Adding or changing a column

1. Change the CSV header and rows.
2. If the column is numeric or boolean, add it to the `int` or `bool` list for that dataset in `convert.py`. Otherwise it is treated as a string.
3. Run `python3 tools/convert.py to-json <dataset>`, then `python3 tools/convert.py to-csv --check` to confirm the round trip.

Regenerating an existing JSON file rewrites its formatting (4-space indent). `contestants.json` currently uses 2 spaces, so `--indent 2` keeps it as it is.
