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
