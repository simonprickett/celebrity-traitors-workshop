# Celebrity Traitors: UK Series 2 Workshop

![Celebrity Traitors Workshop](images/grot_celebrity_traitors_workshop.png)

## Pre-requisites

TODO

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
