# Assets

Graphics used by the README and the plan. Edit the sources, then rebuild.

| Path | Purpose |
| --- | --- |
| `src/*.svg` | Editable sources; fonts referenced by family name |
| `*.svg` | Built files with subset fonts embedded; do not edit by hand |
| `licenses/` | SIL Open Font License texts for the embedded fonts |

## Build

```bash
# once: fetch the fonts (not committed) into a scratch folder
npm install --ignore-scripts @fontsource/instrument-serif @fontsource/instrument-sans @fontsource/geist-mono
pip install fonttools brotli

python3 scripts/build-assets.py --fonts node_modules/@fontsource
```

## Visual language

Tokens and the list of avoided patterns are defined in [`PLAN.md` Section 16](../PLAN.md#16-ui-sketches-v01). In short: warm near-black surfaces, hairline separators instead of nested cards, one signal-orange accent, Instrument Serif for utterances and headings, Instrument Sans for interface text, Geist Mono for data. No gradients, glows or glass effects.

## Fonts

Instrument Serif, Instrument Sans and Geist Mono are licensed under the SIL Open Font License 1.1; see `licenses/`.
