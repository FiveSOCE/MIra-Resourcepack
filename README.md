## 26.2 compatibility fix

The pack now declares explicit compatibility from resource-pack format 75 (Minecraft 1.21.11) through format 88 (Minecraft 26.2). The distribution filename remains unchanged so existing forced-pack URLs keep working.

# Mira Resource Pack

Official resource pack for the FiveSOCE Mira Minecraft plugin ecosystem.

Target: **Minecraft 1.21.11 through 26.2**  
Resource pack formats: **75 through 88**

## Pyro Axe

The Pyro Axe is the first permanent custom MiraItem visual.

Permanent model key:

```
mira:pyro_axe
```

Minecraft resolves that component to:

```
assets/mira/items/pyro_axe.json
```

which selects the baked handheld model:

```
assets/mira/models/item/pyro_axe.json
```

using:

```
assets/mira/textures/item/pyro_axe.png
```

MiraItems must assign `minecraft:item_model = mira:pyro_axe` **only** to an authenticated/signed Pyro Axe.

There is deliberately no override of any vanilla axe model, so ordinary axes keep their vanilla appearance.

## Visual direction

The generated v1 Pyro Axe is a symmetrical double-sided blackened-steel battle axe with:

- infernal orange/red cutting edges
- ember cracks
- central fire core
- long wrapped haft
- Minecraft-native 64x64 pixel-art silhouette

The generator is source controlled at `tools/generate_pyro_axe.py`, so the binary texture can be rebuilt deterministically.

## Permanent identifiers

Model identifiers are collectible ABI. Once a Mira model key ships, it is never reused for a different item.

The permanent registry is `model-registry.json`.

## Build

GitHub Actions builds:

- `assets/mira/textures/item/pyro_axe.png`
- `pack.png`
- `dist/Mira-Resourcepack-1.21.11.zip`
- `dist/Mira-Resourcepack-1.21.11.zip.sha1`

The ZIP can be hosted directly as the server-forced resource pack.
