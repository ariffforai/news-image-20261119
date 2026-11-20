"""Entry program for the make.fun news-image-20261119 bounty.

The repository ships a single image, entry.png, which sums up the world
news of Thursday 19 November 2026 in one front page: 50 sourced stories,
a UTC timeline, a world map and a date check. This program copies that
image, byte for byte, to the output directory the grader provides.

The run is deterministic: every run writes exactly the same bytes,
because the program only copies a fixed file that already sits in this
repository. It uses the Python standard library only, needs no network,
and reads nothing outside this repository.
"""

import os
import shutil
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def check_png(path):
    """Confirm path is a PNG whose IHDR declares 1024x1024 pixels."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        print(f"{path}: not a PNG (bad signature)", file=sys.stderr)
        return False
    # After the 8-byte signature: a 4-byte chunk length, a 4-byte chunk
    # type, then the 13-byte IHDR (width, height, bit depth, colour
    # type, compression, filter, interlace).
    length, chunk_type = struct.unpack(">I4s", header[8:16])
    if chunk_type != b"IHDR" or length != 13:
        print(f"{path}: first chunk is not a 13-byte IHDR", file=sys.stderr)
        return False
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (1024, 1024):
        print(
            f"{path}: IHDR is {width}x{height}, expected 1024x1024",
            file=sys.stderr,
        )
        return False
    return True


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    if os.path.getsize(dest) != os.path.getsize(source):
        print("entry.png copy came out a different size", file=sys.stderr)
        return 1
    if not check_png(dest):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
