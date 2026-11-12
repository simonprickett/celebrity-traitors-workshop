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
