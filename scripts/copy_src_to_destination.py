import shutil
from pathlib import Path
from config import DESTINATION_PATH

def main():
    src_dir = Path(__file__).parent.parent / "src"
    dest_path = Path(DESTINATION_PATH)
    
    # Create destination directory
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Remove existing contents
    if dest_path.exists():
        for item in dest_path.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    
    # Copy src contents to destination
    for item in src_dir.iterdir():
        if item.is_dir():
            shutil.copytree(item, dest_path / item.name)
        else:
            shutil.copy2(item, dest_path / item.name)

if __name__ == "__main__":
    main()