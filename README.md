# Mira Resource Pack

Official server resource pack for the **Mira Minecraft plugin ecosystem**.

The pack supplies custom item models/textures used by authenticated MiraItems and related Mira systems while deliberately leaving ordinary vanilla items unchanged.

## Compatibility

- Primary target: **Minecraft 26.2**
- Supported compatibility range: **Minecraft 1.21.11 through 26.2**
- Primary resource-pack format: **88**
- Minimum supported format: **75**

The build publishes:

```text
dist/Mira-Resourcepack-26.2.zip
dist/Mira-Resourcepack-26.2.zip.sha1
```

A legacy `Mira-Resourcepack-1.21.11.zip` alias is generated with identical bytes for existing server URLs where configured.

## Design Rule

Mira model keys are assigned only to the specific authenticated/custom item that owns them.

For example, a signed MiraItems Pyro Axe can receive:

```text
minecraft:item_model = mira:pyro_axe
```

while a normal Netherite Axe remains completely vanilla.

This is the core resource-pack rule across the suite: **custom Mira content gets custom visuals; ordinary Minecraft items do not get globally replaced.**

## Permanent Model Registry

Permanent model identifiers are treated as collectible ABI. Once a model key ships for a Mira item, that key is not recycled for a different item.

The source of truth is:

```text
model-registry.json
```

Current registered permanent item models include:

| Item / Family | Model key |
| --- | --- |
| Pyro Axe | `mira:pyro_axe` |
| Excalibur | `mira:excalibur` |
| Lochaber Axe | `mira:lochaber_axe` |
| Empower! | `mira:empower` |
| Rank voucher | `mira:voucher_rank` |
| Pinata Call voucher | `mira:voucher_pinata` |
| Airdrop Call voucher | `mira:voucher_airdrop` |
| Permanent Fly voucher | `mira:voucher_fly` |
| Home Upgrade voucher | `mira:voucher_home_upgrade` |
| Jelly Legs voucher | `mira:voucher_jellylegs` |
| Temporary Kit voucher | `mira:voucher_temp_kit` |
| Dark Rider Helmet inventory model | `mira:dark_rider_helmet` |
| Dark Rider Chestplate inventory model | `mira:dark_rider_chestplate` |
| Dark Rider Leggings inventory model | `mira:dark_rider_leggings` |
| Dark Rider Boots inventory model | `mira:dark_rider_boots` |

Dark Rider inventory icons/models are permanent Mira identifiers. Worn 3D armor geometry is handled by the MythicArmors pipeline rather than by ordinary vanilla armor-model replacement.

## Crate Key Model

MiraCrates physical keys can use the dedicated model:

```text
mira:crate_key
```

The pack contains the item definition, baked model and custom texture for the crate key so MiraCrates can visually distinguish issued physical keys without replacing vanilla key-carrier items globally.

## Current Visual Pass

The current 26.2 pack includes purpose-built visuals for major Mira collectibles and vouchers, including:

- Pyro Axe
- Excalibur
- Lochaber Axe
- Empower!
- crate keys
- rank vouchers
- Pinata Call vouchers
- Airdrop Call vouchers
- Home Upgrade vouchers
- Jelly Legs vouchers
- Permanent Fly vouchers
- temporary kit vouchers
- Dark Rider armor inventory presentation

The weapon/voucher pass uses Minecraft-friendly full-frame sprites and custom handheld/item definitions while preserving a consistent icy/infernal/fantasy Mira visual language where appropriate to the item.

## Resource Structure

Modern item definitions live under:

```text
assets/mira/items/
```

Baked models live under:

```text
assets/mira/models/item/
```

Textures live under:

```text
assets/mira/textures/item/
```

A typical model flow is:

```text
MiraItems item_model component
        ↓
assets/mira/items/<id>.json
        ↓
assets/mira/models/item/<id>.json
        ↓
assets/mira/textures/item/<id>.png
```

## MiraItems Integration

MiraItems is responsible for deciding **which authenticated item receives which model key**.

The resource pack does not attempt to identify special items by material alone. This allows custom Mira weapons/vouchers to coexist with ordinary Minecraft items that use the same base material.

MiraItems also continuously re-enforces canonical models on valid claimed MiraItems where required so normal inventory handling does not silently strip the intended presentation.

## MythicArmors Integration

Custom 3D worn armor can be produced/rendered through MythicArmors while the Mira pack retains stable inventory-side item identities and supporting assets.

This keeps inventory presentation and worn-armor geometry as separate concerns instead of forcing vanilla armor replacement across all players/items.

## Building

The repository contains source-controlled assets and generation/build tooling. GitHub Actions produces the distributable 26.2 ZIP and SHA-1 used by the forced server resource-pack configuration.

Important generated/distribution outputs include:

```text
pack.png
dist/Mira-Resourcepack-26.2.zip
dist/Mira-Resourcepack-26.2.zip.sha1
```

Some artwork/generator sources are intentionally retained in-repo so shipped binary textures can be reproduced deterministically.

## Stability Rule

Do not reuse a shipped permanent Mira model identifier for a different collectible.

New permanent models should be added to `model-registry.json` so item/model identity remains stable across server updates, player inventories and future resource-pack revisions.
