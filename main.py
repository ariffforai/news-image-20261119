#!/usr/bin/env python3
"""Ship the 19 November 2026 news front page.

The front page itself is a pre-rendered 1024x1024 PNG that lives next to
this file as entry.png. This program copies it into the output directory
named by MAKEFUN_OUTPUT_DIR (default /output) and then proves the copy
is a genuine, complete 1024x1024 PNG: it checks the PNG signature, the
13-byte IHDR chunk and its declared width and height, and finally
re-reads the destination and compares it byte for byte with the source.

Standard library only (os, shutil, struct, sys). No network, no
randomness, no clock: the same input always produces the same result.
Any failure is reported on stderr and the program exits non-zero.
"""

import os
import shutil
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    """Report a problem on stderr and stop with a non-zero exit code."""
    print("main.py: error: %s" % message, file=sys.stderr)
    sys.exit(1)


def check_png(data, label):
    """Verify bytes look like a 1024x1024 PNG; fail otherwise."""
    if len(data) < 8 or data[:8] != PNG_SIGNATURE:
        fail("%s is not a PNG file (bad 8-byte signature)" % label)
    if len(data) < 24:
        fail("%s is too short to hold a PNG header" % label)
    chunk_length = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_length != 13 or chunk_type != b"IHDR":
        fail("%s does not start with a 13-byte IHDR chunk" % label)
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail("%s declares %dx%d, expected %dx%d"
             % (label, width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    if len(data) < 12 or data[-12:-8] != b"\x00\x00\x00\x00" \
            or data[-8:-4] != b"IEND":
        fail("%s does not end with a proper IEND chunk (file may be "
             "truncated)" % label)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")

    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (source, exc))

    check_png(data, source)

    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory %s: %s" % (out_dir, exc))

    try:
        with open(dest, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (dest, exc))

    try:
        with open(dest, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        fail("cannot re-read %s for verification: %s" % (dest, exc))

    if copied != data:
        fail("copied file %s differs from %s (%d bytes vs %d bytes)"
             % (dest, source, len(copied), len(data)))

    check_png(copied, dest)

    print("wrote %s (%d bytes, %dx%d PNG)"
          % (dest, len(copied), EXPECTED_WIDTH, EXPECTED_HEIGHT))


if __name__ == "__main__":
    main()
