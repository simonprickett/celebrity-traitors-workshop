# Celebrity Traitors: UK Series 2 Workshop

![Celebrity Traitors Workshop](images/grot_celebrity_traitors_workshop.png)

This repository contains workshop resources for learning about TODO in Grafana with data from series 2 of the UK Celebrity Traitors show. TODO more details...

## Pre-requisites

- A laptop with Wi‑Fi, running Linux, macOS, or Windows
- [Git](https://git-scm.com/install/), if you're going to clone this repo locally
- **Optional**: IDE such as [VS Code](https://code.visualstudio.com/download) or [Cursor](https://cursor.com/download)
- **Optional**: A local install of [Python 3](https://www.python.org/downloads/) if you want to run the data viewer utility locally (not required to be successful with this workshop)
- A free tier [Grafana Cloud](https://grafana.com/auth/sign-up/create-user/) account (or install and run Grafana locally).  Cloud is preferred in order to more easily benefit from the AI assistant technology.
- TODO other things...

## Image Credits

Images are from the press pack from the BBC / Studio Lambert / Cody Burridge / BBC Creative. The Grot image above is courtesy of Ward Bekker at Grafana Labs.

## Get Familiar with the Data

All of the data for the workshop is in the [`data/`](data/README.md) folder. It covers series 2 of the UK Celebrity Traitors: who took part, what happened to each player in every episode, how the end game played out, and how much prize money was won.

### Datasets

| Dataset | What it contains |
|---|---|
| Contestants | The 21 people who took part: name, profession, age, gender, nationality and a Wikipedia link. |
| Main game | One row per player per episode or round table: their status (faithful, traitor, and so on), shield, who they voted for, votes received, outcome, recruitment and power. |
| End game | One row per player per end game round: status, decision, who they voted for and the outcome. |
| Prize fund | One row per episode: the prize money offered and the amount won. |

### Formats and locations

Every dataset is available in two formats, with the same field names and the same content. Use whichever suits the tool you are working with.

| Format | Location | Documentation |
|---|---|---|
| CSV | [`data/csv/`](data/csv/) | [CSV data README](data/csv/README.md) |
| JSON | [`data/json/`](data/json/) | [JSON data README](data/json/README.md) |
| Images | [`data/images/`](data/images/) | See below |

The [data README](data/README.md) describes the conventions used throughout (nulls, dates, player ids and so on). If you edit one format, the conversion script described in the [tools README](tools/README.md) keeps the other in step.

### Hosted version

A hosted copy of the data is available, so you can use it without cloning this repository. The files are the same as in `data/`, and the URLs follow the same layout:

| Data | URL |
|---|---|
| CSV | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/<dataset>.csv` |
| JSON | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/<dataset>.json` |
| Images | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/<name>.webp` |

For example, [`contestants.csv`](https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/csv/contestants.csv) and [`amol.webp`](https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/images/amol.webp). The full list of URLs is in the [data README](data/README.md#hosted-data).

### Images

Contestant photos are in [`data/images/`](data/images/) in WebP format. Each contestant has two images:

- `<name>.webp`: the regular image, showing the contestant in the game.
- `<name>_out.webp`: the `_out` image, showing the same contestant after leaving the game.

For example, `kenny.webp` and `kenny_out.webp`. The `<name>` part is the same short id used as `name` in the contestants data and as `player` in the game data, so you can match images to records directly. There is also `ensemble.webp`, a group shot of the cast with no `_out` equivalent.

## Using the Data Viewer Utility

`utils/viewer.html` is a browser-based viewer for the contestant images and data in `data/images/` and `data/json/contestants.json`. It fetches the JSON and image files using relative paths (`../data/images/...` and `../data/json/...`), so it must be served from the **repository root**, not from inside `utils/`.

From the repository root, run:

```
python -m http.server
```

Then open:

```
http://localhost:8000/utils/viewer.html
```

Opening `viewer.html` directly from disk (`file://`) will not work in most browsers, since `fetch()` of local files is blocked under the `file://` protocol.

## Documentation and other resources

- TODO
