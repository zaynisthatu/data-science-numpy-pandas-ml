# Data Science: NumPy, Pandas and Machine Learning

A NumPy basics notebook, a pandas script that combines three business data sources into one summary report, and a Boston Housing regression with scikit-learn. Written in July 2025.

## Contents

The files are in `data_science/`. Each one has a note next to it, `<name>.README.md`, with its original path.

| File | What it does |
|---|---|
| `1.ipynb` | NumPy basics: creating 1D and 2D arrays, shape and size, indexing and assignment, multiplying a list versus an array, and `np.zeros` |
| `boston_housing_ML.py` | Boston Housing regression: fills missing `RM` values with the median, plots the `MEDV` distribution, rooms and `LSTAT` against price, and a correlation heatmap, then fits a scikit-learn `LinearRegression` on `RM` and `LSTAT` (80/20 split) and prints the MSE and RMSE |
| `multi_source_business_summary.py` | Reads `sales.csv`, `marketing.csv` and `support.csv`, computes total sales, quantity and top category, marketing budget, leads, conversions and conversion rate, ticket counts and average resolution time, and writes `master_summary_report.xlsx` |
| `numpy_timing_test.py` | Imports for a list-versus-NumPy timing comparison |

## Setup

```
pip install numpy pandas scikit-learn matplotlib seaborn openpyxl
```

`boston_housing_ML.py` expects `data.csv` (the Boston Housing dataset) and `multi_source_business_summary.py` expects the three CSV files, all in the working directory. The data files are not included.
