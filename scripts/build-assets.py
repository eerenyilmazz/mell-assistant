#!/usr/bin/env python3
"""Build README graphics with embedded, subset web fonts.

Sources live in docs/assets/src/*.svg and reference fonts by family name.
This script subsets the fonts to the characters each SVG uses, embeds them as
base64 WOFF2 @font-face rules, and writes the result to docs/assets/*.svg, so
the graphics render identically on GitHub without network font loading.

Fonts (SIL Open Font License 1.1), from the @fontsource npm packages:
  @fontsource/instrument-serif, @fontsource/instrument-sans, @fontsource/geist-mono

Usage:
  python3 scripts/build-assets.py --fonts <node_modules/@fontsource>
Requires: fonttools, brotli.
"""
import argparse, base64, io, pathlib, re, html
from fontTools import subset
from fontTools.ttLib import TTFont

FACES = [  # (css family, package, file stem, weight)
    ("Instrument Serif", "instrument-serif", "instrument-serif", 400),
    ("Instrument Sans", "instrument-sans", "instrument-sans", 400),
    ("Instrument Sans", "instrument-sans", "instrument-sans", 500),
    ("Instrument Sans", "instrument-sans", "instrument-sans", 600),
    ("Geist Mono", "geist-mono", "geist-mono", 400),
    ("Geist Mono", "geist-mono", "geist-mono", 500),
]
RANGES = {"latin": None, "latin-ext": None}


def used_text(svg: str) -> str:
    texts = re.findall(r">([^<>]+)<", svg)
    chars = set(html.unescape("".join(texts)))
    return "".join(sorted(chars | set(" ")))


def subset_woff2(path: pathlib.Path, text: str) -> tuple[bytes, list[int]] | None:
    font = TTFont(path)
    cmap = font.getBestCmap()
    keep = [c for c in text if ord(c) in cmap]
    if not keep:
        return None
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    sub = subset.Subsetter(opts)
    sub.populate(text="".join(keep))
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return buf.getvalue(), sorted(ord(c) for c in keep)


def unicode_range(codepoints: list[int]) -> str:
    return ",".join(f"U+{cp:04X}" for cp in codepoints)


def build(src: pathlib.Path, out: pathlib.Path, fonts: pathlib.Path) -> None:
    svg = src.read_text(encoding="utf-8")
    text = used_text(svg)
    rules = []
    for family, pkg, stem, weight in FACES:
        if f"'{family}'" not in svg:
            continue
        remaining = text
        for rng in RANGES:
            path = fonts / pkg / "files" / f"{stem}-{rng}-{weight}-normal.woff2"
            if not path.exists():
                continue
            result = subset_woff2(path, remaining)
            if result:
                data, cps = result
                remaining = "".join(c for c in remaining if ord(c) not in cps)
                b64 = base64.b64encode(data).decode()
                rules.append(
                    f"@font-face{{font-family:'{family}';font-weight:{weight};"
                    f"unicode-range:{unicode_range(cps)};"
                    f"src:url(data:font/woff2;base64,{b64}) format('woff2');}}"
                )
    style = "<style>" + "".join(rules) + "</style>"
    svg = re.sub(r"(<svg[^>]*>)", r"\1" + style, svg, count=1)
    out.write_text(svg, encoding="utf-8")
    print(f"{out.name}: {len(rules)} faces, {out.stat().st_size // 1024} KB")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True, type=pathlib.Path)
    root = pathlib.Path(__file__).resolve().parent.parent / "docs" / "assets"
    args = ap.parse_args()
    for src in sorted((root / "src").glob("*.svg")):
        build(src, root / src.name, args.fonts)


if __name__ == "__main__":
    main()
