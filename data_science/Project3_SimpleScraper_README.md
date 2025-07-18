# Wikipedia GDP Data Scraper

## Project Description (Urdu/Hindi)
یہ project Wikipedia سے countries by GDP (nominal) کا table scrape کرتا ہے اور اسے CSV file میں save کرتا ہے۔ یہ ایک simple web scraper ہے جو BeautifulSoup اور requests library استعمال کرتا ہے۔

## Project Description (English)
This project scrapes the "List of countries by GDP (nominal)" table from Wikipedia and saves it as a CSV file. It's a simple web scraper built using Python with BeautifulSoup and requests libraries.

## What This Project Does
- Wikipedia سے GDP data scrape کرتا ہے
- Table کو clean کرتا ہے (references aur extra characters remove کرتا ہے)
- Data کو CSV format میں save کرتا ہے
- User-friendly output دیتا ہے

## Features
- **Simple & Clean**: Easy to understand code
- **Error Handling**: Proper error messages اگر کچھ غلط ہو جائے
- **Data Cleaning**: References [1], [2] etc. remove کرتا ہے
- **CSV Export**: Standard CSV format میں save کرتا ہے
- **Progress Updates**: Scraping process کے دوران updates دیتا ہے

## Prerequisites
Python 3.6+ installed ہونا چاہیے آپ کے system میں۔

## Installation

### Step 1: Clone/Download
```bash
# اگر Git ہے تو
git clone <repository-url>
cd gdp-scraper

# یا پھر files download کر کے folder میں رکھیں
```

### Step 2: Install Required Packages
```bash
pip install requests beautifulsoup4 pandas
```

یا requirements file سے:
```bash
pip install -r requirements.txt
```

## How to Run

### Method 1: Direct Run
```bash
python scraper.py
```

### Method 2: Python Module
```bash
python -m scraper
```

## Output
Script run کرنے کے بعد:
- `gdp_data.csv` file create ہو جائے گی same directory میں
- Console میں progress messages آئیں گے
- Success message کے ساتھ summary show ہو گی

## File Structure
```
gdp-scraper/
│
├── scraper.py          # Main scraping script
├── README.md           # Ye file
├── requirements.txt    # Required packages
└── gdp_data.csv       # Output file (after running script)
```

## Sample Output
```
=== Wikipedia GDP Data Scraper ===
Countries by GDP (nominal) ka data scrape kar rahe hain...

Wikipedia page fetch kar rahe hain...
Page successfully fetch ho gaya!
Table data extract kar rahe hain...
Total 195 countries ka data extract ho gaya!
Data ko gdp_data.csv mein save kar rahe hain...
✅ Data successfully save ho gaya: gdp_data.csv
Total rows: 195

=== Summary ===
Headers: 4
Countries: 195

First few entries:
1. United States
2. China
3. Germany
4. Japan
5. India
```

## Requirements.txt
```
requests>=2.25.1
beautifulsoup4>=4.9.3
pandas>=1.3.3
```

## Common Issues & Solutions

### Issue 1: Module Not Found Error
```
ModuleNotFoundError: No module named 'requests'
```
**Solution**: 
```bash
pip install requests beautifulsoup4 pandas
```

### Issue 2: Permission Error
```
PermissionError: [Errno 13] Permission denied: 'gdp_data.csv'
```
**Solution**: CSV file کو close کر دیں اگر open ہے، یا different filename use کریں

### Issue 3: Network Error
```
Error fetching page: Connection timeout
```
**Solution**: Internet connection check کریں، یا proxy settings adjust کریں

## Customization

### Different Output Filename
```python
save_to_csv(headers, data, "my_custom_name.csv")
```

### Different Wikipedia Page
```python
url = "https://en.wikipedia.org/wiki/Your_Target_Page"
```

## Technical Details
- **Language**: Python 3.6+
- **Libraries Used**: requests, beautifulsoup4, pandas, csv
- **Data Source**: Wikipedia
- **Output Format**: CSV
- **Encoding**: UTF-8

## Future Enhancements
- Multiple table scraping support
- JSON output option
- Automatic data updates
- GUI interface
- Database storage option

## Contributing
Contributions welcome ہیں! Issues aur pull requests create کر سکتے ہیں۔

## License
Open source - freely use کر سکتے ہیں۔

## Contact
Questions یا suggestions کے لیے GitHub issues استعمال کریں۔

---
**Happy Scraping! 🚀**