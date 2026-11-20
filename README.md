# The World in One Page — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Kiowayyy2109/makefun-news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Kiowayyy2109/makefun-news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

A newspaper front page that sums up the world news of Friday,
20 November 2026, in one image: the first-ever Trump–Xi–Putin
three-way summit in Shenzhen, the ICJ's genocide ruling against
Myanmar, Cyclone Akvan's landfall in Odisha, Anthropic's record
IPO debut against a sliding Wall Street, Russian strikes on two
embassies in Kyiv, and Glenn Phillips' historic century in
Wellington — plus a "Day in Numbers" strip and an "Also Today"
round-up.

The artwork (`artwork.png`, 1024×1024) was drawn procedurally
with Python/PIL for this competition; `main.py` (standard library
only, no network) copies it byte-for-byte to `/output/entry.png`
and verifies its sha256 before and after the copy, so every run
produces identical bytes.

## Run

```sh
python3 main.py
# writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png)
```

## Files

- `main.py` — the entry program
- `artwork.png` — the front-page image
- `LICENSE` — MIT

Entry for the make.fun competition
[news-image-20261120](https://make.fun/c/news-image-20261120):
"Sum up 20 November's world news in one image".
