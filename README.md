# File to Markdown Converter

A Python script that uses Microsoft's `markitdown` library to batch-process multiple file formats (PDF, Office files, spreadsheets, text files, and more) and automatically convert them into Markdown (`.md`) format.

## Requirements

- Python 3.10+

### Setup Virtual Environment (Recommended)

1. Create a virtual environment named `.venv`:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup & Usage

1. Open `converter.py`.
2. Configure your source and destination paths at the top of the file:

```python
ORIGIN = r"PASTE ORIGIN ROUTE"      # Folder containing files to convert
DESTINY = r"PASTE DESTINY ROUTE"    # Folder where .md files will be saved
```

3. Run the script:

```bash
python converter.py
```

## Supported Formats

- Documents & Presentations: `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls`
- Text & Data formats: `.html`, `.csv`, `.json`, `.xml`, `.txt`
- Archives: `.zip`