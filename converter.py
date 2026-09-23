from pathlib import Path
from markitdown import MarkItDown

EXTENSIONS = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls", 
    ".html", ".csv", ".json", ".xml", ".zip", ".txt"
}

ORIGIN = r"PASTE ORIGIN ROUTE"      # Folder containing files to convert
DESTINY = r"PASTE DESTINY ROUTE"    # Folder where .md files will be saved

def convert_folder(
    or_route = ORIGIN, 
    dest_route = DESTINY,
    remove_original = False  # Change false if want to delete original
):
    md = MarkItDown()
    
    origin = Path(or_route)
    destiny = Path(dest_route)
    
    destiny.mkdir(parents=True, exist_ok=True)
    
    files = [f for f in origin.iterdir() if f.is_file() and f.suffix.lower() in EXTENSIONS]
    
    if not files:
        print(f"No compatible files were found in: {origin.resolve()}")
        return

    print(f"Found {len(files)} file(s) to convert")
    
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}/{len(files)}] PROCESSING: {file.name}")
        print("-" * 60)
        
        try:
            result = md.convert(str(file))
            text_md = result.markdown
            
            save_file = destiny / f"{file.stem}.md"
            save_file.write_text(text_md, encoding="utf-8")
            print(f"Successfully saved to: {save_file.resolve()}")

            if remove_original:
                file.unlink()
                print(f"Original removed: {file.name}")
            
        except Exception as e:
            print(f"[ERROR] Cannot convert {file.name}: {e}")
        
        print("-" * 60)

if __name__ == "__main__":
    convert_folder(remove_original=False)