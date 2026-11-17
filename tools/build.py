#LICENSE
#
#Copyright (C) 2026  sterling motuz <Sterling@dexabyte.ca>
#
#for https://github.com/printer-buddy/printer-buddy
#
#SPDX-License-Identifier: AGPL-3.0-only
#
#Additional term (AGPL-3.0 section 7b, keep author credit): keep this header
#
#Additional term (AGPL-3.0 section 7c, mark changed versions): if you make any changes, you must include a CHANGELOG with all changes and their dates
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "print-buddy-timelapse"


def build(out):
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{NAME}.tar.gz"
    with tarfile.open(path, "w:gz") as tar:
        tar.add(ROOT / "pb_timelapse", arcname=f"{NAME}/pb_timelapse", filter=lambda t: None if "__pycache__" in t.name else t)
        for f in ("LICENSE", "NOTICE"):
            tar.add(ROOT / f, arcname=f"{NAME}/{f}")
    print(path)


if __name__ == "__main__":
    build(Path(sys.argv[1] if len(sys.argv) > 1 else "dist"))
