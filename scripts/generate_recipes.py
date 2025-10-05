import json
import csv
import os

def load_original_keys(item_id, original_recipe_dir):
    """Load the original key mappings, custom name, and deco_id from existing recipe file"""
    original_file = os.path.join(original_recipe_dir, f'{item_id}.json')
    if os.path.exists(original_file):
        with open(original_file, 'r', encoding='utf-8') as f:
            original_recipe = json.load(f)
            return {
                'keys': original_recipe.get('key', {}),
                'custom_name': original_recipe['result']['components']['minecraft:custom_name']['text'],
                'deco_id': original_recipe['result']['components']['minecraft:custom_data']['deco_id']
            }
    return None

def numeric_to_pattern(numeric_pattern, keys):
    """Convert numeric pattern back to recipe pattern with keys"""
    # Create mapping of numbers to keys
    key_list = list(keys.keys())
    num_to_key = {str(idx): key for idx, key in enumerate(key_list, 1)}
    num_to_key['0'] = ' '
    
    # Determine pattern dimensions based on length
    pattern_length = len(numeric_pattern)
    if pattern_length == 6:  # 2x3 pattern
        rows = 2
        cols = 3
    elif pattern_length == 9:  # 3x3 pattern
        rows = 3
        cols = 3
    else:
        # Try to infer dimensions
        rows = (pattern_length + 2) // 3  # Round up division
        cols = 3
    
    # Convert numeric string to pattern
    pattern = []
    for i in range(rows):
        row = ''
        for j in range(cols):
            idx = i * cols + j
            if idx < len(numeric_pattern):
                row += num_to_key.get(numeric_pattern[idx], ' ')
            else:
                row += ' '
        pattern.append(row)
    
    return pattern

def create_recipe_json(item_id, recipe_keys, recipe_pattern, texture, hitbox, author, url, original_data=None):
    """Create a recipe JSON structure from CSV data"""
    # Parse recipe keys
    key_items = [k.strip() for k in recipe_keys.split(',')]
    
    # Add minecraft: prefix if not present
    key_items = [f'minecraft:{item}' if not item.startswith('minecraft:') and not item.startswith('#') else item for item in key_items]
    
    # Use original keys if available, otherwise create new mapping
    if original_data and 'keys' in original_data:
        keys = original_data['keys']
    else:
        # Create key mapping
        # Standard single character keys
        key_chars = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        keys = {}
        for i, item in enumerate(key_items):
            if i < len(key_chars):
                keys[key_chars[i]] = item
    
    # Convert numeric pattern to recipe pattern
    pattern = numeric_to_pattern(recipe_pattern, keys)
    
    # Use original custom name if available, otherwise generate from item_id
    if original_data and 'custom_name' in original_data:
        custom_name = original_data['custom_name']
    else:
        custom_name = f"{item_id.replace('_', ' ').title()} Decoration"
    
    # Use original deco_id if available, otherwise use item_id
    if original_data and 'deco_id' in original_data:
        deco_id = original_data['deco_id']
    else:
        deco_id = item_id
    
    # Create the full recipe structure
    recipe = {
        "type": "minecraft:crafting_shaped",
        "key": keys,
        "pattern": pattern,
        "result": {
            "components": {
                "minecraft:profile": {
                    "properties": [
                        {
                            "name": "textures",
                            "value": texture
                        }
                    ]
                },
                "minecraft:attribute_modifiers": [
                    {
                        "type": "minecraft:block_interaction_range",
                        "id": "block_interaction_range",
                        "amount": -5,
                        "operation": "add_multiplied_total",
                        "slot": "hand"
                    }
                ],
                "minecraft:tooltip_display": {
                    "hidden_components": [
                        "minecraft:attribute_modifiers"
                    ]
                },
                "minecraft:equippable": {
                    "slot": "chest",
                    "equip_sound": "minecraft:ui.cartography_table.take_result",
                    "allowed_entities": "minecraft:armor_stand"
                },
                "minecraft:custom_data": {
                    "deco": True,
                    "deco_id": deco_id,
                    "deco_size": hitbox
                },
                "minecraft:custom_name": {
                    "text": custom_name,
                    "color": "#ffbf00",
                    "bold": False,
                    "italic": False
                },
                "minecraft:lore": [
                    [
                        {
                            "text": f"Model by {author}",
                            "color": "dark_gray",
                            "bold": False,
                            "italic": False
                        }
                    ],
                    [
                        {
                            "text": url,
                            "color": "dark_gray",
                            "bold": False,
                            "italic": False
                        }
                    ]
                ]
            },
            "count": 1,
            "id": "minecraft:player_head"
        },
        "show_notification": False
    }
    
    return recipe

def main():
    # Paths (relative to script location)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    csv_file = os.path.join(script_dir, 'items.csv')
    output_dir = os.path.join(project_root, 'temp_recipes')
    original_recipe_dir = os.path.join(project_root, 'src', 'data', 'decoplus', 'recipe')
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Read CSV and generate recipes
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        
        for row in reader:
            item_id = row['id']
            recipe_keys = row['recipe keys']
            recipe_pattern = row['recipe pattern']
            texture = row['texture']
            hitbox = row['hitbox']
            author = row['author']
            url = row['url']
            
            # Load original keys to preserve key letter mappings
            original_data = load_original_keys(item_id, original_recipe_dir)
            
            # Generate recipe JSON
            recipe = create_recipe_json(item_id, recipe_keys, recipe_pattern, texture, hitbox, author, url, original_data)
            
            # Write to file
            output_file = os.path.join(output_dir, f'{item_id}.json')
            with open(output_file, 'w', encoding='utf-8') as out_f:
                json.dump(recipe, out_f, indent=2, ensure_ascii=False)
            
            print(f'Generated: {item_id}.json')
    
    print(f'\nAll recipes generated in: {output_dir}')

if __name__ == '__main__':
    main()
