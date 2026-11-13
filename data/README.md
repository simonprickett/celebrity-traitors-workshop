# Data

Data from series 2 of the UK Celebrity Traitors.

| Folder | Contents |
|---|---|
| [`csv/`](csv/README.md) | The datasets as CSV files: one header row, then one row per record. Easy to open in a spreadsheet or load into a database. |
| [`json/`](json/README.md) | The same datasets as JSON: one object containing a flat array of records. Easy to use from code, APIs and dashboards. |
| `images/` | Contestant photos in WebP format. `<name>.webp` is the contestant; `<name>_out.webp` is the same contestant after leaving the game. `ensemble.webp` is the group shot. |

## Two formats, on purpose

Every dataset is available as both CSV and JSON, so you can pick the format that suits the tool you are using. The duplication is intentional. The two formats hold the same data with the same field names (camelCase), and they are kept in step by the conversion script in [`tools/`](../tools/README.md).

| Dataset | CSV | JSON | JSON root key |
|---|---|---|---|
| Contestants | `csv/contestants.csv` | `json/contestants.json` | `contestants` |
| Main game | `csv/main_game.csv` | `json/main_game.json` | `mainGame` |
| End game | `csv/end_game.csv` | `json/end_game.json` | `endGame` |
| Prize fund | `csv/prize_fund.csv` | `json/prize_fund.json` | `prizeFund` |

## Hosted data

The same files are hosted, so you can load them directly from a URL in tools such as Grafana's Infinity data source, without cloning this repository. The base URL is:

```
https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/
```

### CSV and JSON

| Dataset | CSV | JSON |
|---|---|---|
| Contestants | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/contestants.csv` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/contestants.json` |
| Main game | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/main_game.csv` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/main_game.json` |
| End game | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/end_game.csv` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/end_game.json` |
| Prize fund | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/prize_fund.csv` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/prize_fund.json` |

### Images

There are too many images to list individually. Each contestant has two, named after their `name` in the contestants data:

| Image | URL pattern | Example |
|---|---|---|
| Regular | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/<name>.webp` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/amol.webp` |
| After leaving the game | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/<name>_out.webp` | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/amol_out.webp` |
| Group shot | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/ensemble.webp` | |

Use the ids from the `name` column of `contestants.csv` (for example `kenny`, `james_a` or `leigh-anne`) in place of `<name>`.

## Conventions

- **Field names** are camelCase and identical in CSV and JSON.
- **Empty values**: an empty CSV field is `null` in JSON.
- **Numbers and booleans**: numeric fields are JSON numbers and `shield` is a JSON boolean. In CSV they are plain `1` and `true` / `false`.
- **Dates** are UK format, `DD/MM/YYYY`, in both formats.
- **Player ids**: `player` in the game datasets, and `name` in contestants, hold a short lower-case id such as `james_a` or `leigh-anne`. These are the same ids as in the image file names, and `player` always matches a contestant's `name`.
- **Prize money** is a whole number.

## Editing the data

If you change one format, regenerate or check the other with the script in [`tools/`](../tools/README.md):

```
python3 tools/convert.py to-json --check
python3 tools/convert.py to-csv --check
```
