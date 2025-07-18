# JSON to CSV Converter 🔄

A simple Python script that converts JSON files to CSV format with proper error handling and flexible input options.

## 📋 What This Project Does

This project provides a Python script that:
- Reads JSON data from a file
- Converts it to CSV format with proper headers
- Handles various JSON structures (single objects, arrays of objects)
- Provides detailed error messages and success feedback
- Creates sample data if input file doesn't exist

## ✨ Features

- **Flexible Input**: Accepts single JSON objects or arrays of objects
- **Smart Headers**: Automatically detects all unique keys across objects
- **Error Handling**: Comprehensive error handling with helpful messages
- **UTF-8 Support**: Properly handles Urdu/Arabic text and special characters
- **Sample Data**: Creates sample JSON file if none exists
- **Command Line Support**: Can be run with custom file paths

## 🚀 How to Run

### Method 1: Basic Usage (Default Files)
```bash
python json_to_csv.py
```
This will:
- Look for `data.json` in the current directory
- Convert it to `data.csv`
- If `data.json` doesn't exist, it creates a sample file first

### Method 2: Custom Input File
```bash
python json_to_csv.py input.json
```
This will:
- Convert `input.json` to `input.csv`

### Method 3: Custom Input and Output Files
```bash
python json_to_csv.py input.json output.csv
```
This will:
- Convert `input.json` to `output.csv`

## 📁 File Structure

```
project/
├── json_to_csv.py    # Main conversion script
├── README.md         # This file
├── data.json         # Sample JSON file (created automatically)
└── data.csv          # Generated CSV file
```

## 📊 Supported JSON Formats

### Format 1: Array of Objects (Recommended)
```json
[
    {"name": "Ali Khan", "age": 30, "city": "Karachi"},
    {"name": "Sara Malik", "age": 25, "city": "Lahore"},
    {"name": "Imran", "age": 40, "city": "Islamabad"}
]
```

### Format 2: Single Object
```json
{"name": "Ali Khan", "age": 30, "city": "Karachi"}
```

## 📈 Sample Output

For the sample JSON data, the script generates this CSV:

```csv
age,city,name
30,Karachi,Ali Khan
25,Lahore,Sara Malik
40,Islamabad,Imran
```

## 🛠️ Requirements

- **Python 3.6+**: The script uses built-in libraries only
- **No external dependencies**: Uses standard `json`, `csv`, `os`, and `sys` modules

## ⚡ Quick Start

1. **Download the script**:
   ```bash
   # Save the Python script as json_to_csv.py
   ```

2. **Run the script**:
   ```bash
   python json_to_csv.py
   ```

3. **Check the results**:
   - If `data.json` didn't exist, it will be created with sample data
   - `data.csv` will be generated with the converted data
   - Success message will show number of records processed

## 🔧 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `File not found` | Ensure the JSON file exists in the specified path |
| `Invalid JSON format` | Check that your JSON file has valid syntax |
| `Permission denied` | Check file permissions or run with appropriate privileges |
| `Empty output` | Ensure your JSON contains data in supported format |

### Error Messages

The script provides clear error messages:
- ✅ Success messages with record counts
- ❌ Error messages with specific problem descriptions
- 📝 Information about automatic file creation

## 🔍 Example Usage Session

```bash
$ python json_to_csv.py

🔄 JSON to CSV Converter
==============================
Input file: data.json
Output file: data.csv
==============================
❌ Input file 'data.json' does not exist.

📝 Creating sample data.json file...
✅ Sample file 'data.json' created successfully!
🔄 Now converting to CSV...
✅ Successfully converted data.json to data.csv
📊 Converted 3 records with 3 columns
```

## 🌐 Language Support

- Full UTF-8 encoding support
- Works with English, Urdu, Arabic, and other Unicode characters
- Preserves special characters in names and text fields

## 📝 Notes

- Column order in CSV is alphabetically sorted for consistency
- Missing fields in JSON objects will appear as empty cells in CSV
- The script automatically handles mixed object structures
- File encoding is set to UTF-8 for international character support

## 🤝 Contributing

Feel free to enhance this script by adding features like:
- Support for nested JSON objects
- Custom delimiter options
- Data validation features
- Batch processing capabilities

---

**Happy Converting! 🎉**