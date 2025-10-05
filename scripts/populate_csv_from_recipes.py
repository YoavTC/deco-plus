import json
import os
import csv

def pattern_to_numeric(pattern, keys):
    """Convert recipe patterns to numeric format"""
    # Create a mapping of keys to numbers
    key_list = list(keys.keys())
    key_to_num = {key: str(idx) for idx, key in enumerate(key_list, 1)}
    key_to_num[' '] = '0'
    
    # Convert pattern to numeric string
    result = ''
    for row in pattern:
        for char in row:
            result += key_to_num.get(char, '0')
    
    return result

def strip_minecraft_prefix(item):
    """Remove 'minecraft:' prefix from item names"""
    if item.startswith('minecraft:'):
        return item[10:]  # Remove 'minecraft:' (10 characters)
    return item

def main():
    # Paths (relative to script location)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    recipe_dir = os.path.join(project_root, 'src', 'data', 'decoplus', 'recipe')
    output_file = os.path.join(script_dir, 'items.csv')
    
    entries = []
    
    for filename in os.listdir(recipe_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(recipe_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract id from filename
            item_id = filename.replace('.json', '')
            
            # Extract recipe keys and strip minecraft: prefix
            keys = data.get('key', {})
            recipe_keys = ','.join([strip_minecraft_prefix(v) for v in keys.values()])
            
            # Extract pattern
            pattern = data.get('pattern', [])
            recipe_pattern = pattern_to_numeric(pattern, keys)
            
            # Extract texture
            texture = data['result']['components']['minecraft:profile']['properties'][0]['value']
            
            # Extract hitbox (deco_size)
            hitbox = data['result']['components']['minecraft:custom_data'].get('deco_size', 'default')
            
            # Extract author and URL from lore
            lore = data['result']['components'].get('minecraft:lore', [])
            author = ''
            url = ''
            if len(lore) > 0:
                author_text = lore[0][0].get('text', '')
                if author_text.startswith('Model by '):
                    author = author_text.replace('Model by ', '')
            if len(lore) > 1:
                url = lore[1][0].get('text', '')
            
            entries.append([item_id, recipe_keys, recipe_pattern, texture, hitbox, author, url])
    
    # Sort entries by id
    entries.sort(key=lambda x: x[0])
    
    # Write all entries
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['id', 'recipe keys', 'recipe pattern', 'texture', 'hitbox', 'author', 'url'])
        for entry in entries:
            writer.writerow(entry)
    
    print(f'Processed {len(entries)} recipes')
    print(f'CSV written to: {output_file}')

if __name__ == '__main__':
    main()
