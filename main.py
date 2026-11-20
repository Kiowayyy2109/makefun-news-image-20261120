#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120.

Writes the pre-rendered front-page image to /output/entry.png.

The artwork is a newspaper front page, "THE WORLD IN ONE PAGE -
20 NOVEMBER 2026", drawn procedurally for this competition. It is
stored in the repository as artwork.png and copied here byte for
byte, so two runs always produce identical output. Standard library
only; no network access.
"""

import hashlib
import os
import shutil
import struct
import sys

ARTWORK_SHA256 = "5287425534b698acdabe972299a4551f84c3f9ab1bd8ed51f32e8cefb19b0081"
ARTWORK_NAME = "artwork.png"
MAX_BYTES = 1048576
MAX_SIDE = 1024


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_size(path):
    """Return (width, height) from the PNG IHDR chunk; reject non-PNGs."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("artwork.png is not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("artwork.png has no IHDR chunk")
    return struct.unpack(">II", header[16:24])


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ARTWORK_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if sha256_file(source) != ARTWORK_SHA256:
        print("artwork.png failed its sha256 self-check", file=sys.stderr)
        return 1

    try:
        width, height = png_size(source)
    except ValueError as exc:
        print("artwork.png failed validation: %s" % exc, file=sys.stderr)
        return 1
    if width > MAX_SIDE or height > MAX_SIDE:
        print("artwork.png is %dx%d, over the 1024px limit"
              % (width, height), file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    if os.path.getsize(target) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    if sha256_file(target) != ARTWORK_SHA256:
        print("entry.png failed its sha256 self-check", file=sys.stderr)
        return 1

    print("wrote %s (%d bytes, sha256 %s)"
          % (target, os.path.getsize(target), ARTWORK_SHA256))
    return 0


if __name__ == "__main__":
    sys.exit(main())
