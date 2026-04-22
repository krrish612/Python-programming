# Project 1: Automation with Python

## What is Automation?
Automating repetitive tasks using Python scripts.

## Common Automation Tasks
1. File organization
2. PDF processing
3. Excel automation
4. Web scraping
5. Sending emails

## Example: Organize Files
```python
import os
import shutil
from pathlib import Path

def organize_downloads():
    downloads = Path("C:/Users/Downloads")
    
    extensions = {
        "Images": [".jpg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Archives": [".zip", ".rar", ".7z"]
    }
    
    for file in downloads.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for folder, exts in extensions.items():
                if ext in exts:
                    dest = downloads / folder
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(file), str(dest / file.name))
                    print(f"Moved {file.name} to {folder}")
                    break

# Uncomment to run:
# organize_downloads()
```

## Web Scraping Example
```python
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("span", class_="text")
    for quote in quotes[:10]:
        print(quote.text)
```

## Excel Automation
```python
import openpyxl

def create_spreadsheet():
    wb = openpyxl.Workbook()
    ws = wb.active
    
    # Add data
    ws["A1"] = "Name"
    ws["B1"] = "Age"
    ws["A2"] = "Krrish"
    ws["B2"] = "15"
    
    wb.save("data.xlsx")
    print("Saved!")
```

## Next Steps
1. Learn `openpyxl` for Excel
2. Learn `selenium` for browser automation
3. Learn `requests` and `beautifulsoup` for web scraping
4. Learn `smtplib` for sending emails