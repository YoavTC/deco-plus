# Recipe CSV Workflow

This folder contains scripts to manage Minecraft recipe data via CSV.

## Scripts

### `populate_csv_from_recipes.py`
Reads all JSON recipe files and generates/updates the `items.csv` file.

**Usage:**
```bash
python scripts/populate_csv_from_recipes.py
```

**What it does:**
- Scans all recipe JSON files in `src/data/decoplus/recipe/`
- Extracts recipe data (keys, pattern, texture, hitbox, author, URL)
- Removes "minecraft:" prefix from item names for cleaner CSV
- Preserves tags like `#minecraft:small_flowers` and `#spruce_logs`
- Writes to `scripts/items.csv`

### `generate_recipes.py`
Reads the `items.csv` file and generates recipe JSON files.

**Usage:**
```bash
python scripts/generate_recipes.py
```

**What it does:**
- Reads recipe data from `scripts/items.csv`
- Adds "minecraft:" prefix back to item names
- Preserves original key letter mappings (C, R, G, B, etc.)
- Preserves original custom names and deco_ids
- Generates JSON files in `temp_recipes/` folder for review
- Output files are identical to originals (byte-for-byte)

## CSV Format

The `items.csv` file uses tab-separated values with these columns:

| Column | Description | Example |
|--------|-------------|---------|
| id | Recipe identifier | `controller` |
| recipe keys | Comma-separated ingredients (without minecraft: prefix) | `black_concrete,red_dye,lime_dye` |
| recipe pattern | Numeric pattern representation | `650412030` |
| texture | Base64-encoded player head texture | `eyJ0ZXh0dXJlcyI6...` |
| hitbox | Size category | `small`, `default`, `large`, or `tall` |
| author | Model creator name | `DaftCraftYT` |
| url | Reference URL | `bde.gg/b/943` |

## Workflow

1. **Edit recipes via CSV:** Modify `items.csv` with cleaner, more readable item names
2. **Generate recipes:** Run `generate_recipes.py` to create JSON files
3. **Review:** Check the generated files in `temp_recipes/`
4. **Deploy:** Copy verified files from `temp_recipes/` to `src/data/decoplus/recipe/`

## Notes

- All paths are relative, so scripts work from any location
- Tags (starting with `#`) are preserved as-is
- Original key letters and custom names are preserved when generating from existing recipes
- The workflow maintains perfect fidelity - generated files match originals exactly
