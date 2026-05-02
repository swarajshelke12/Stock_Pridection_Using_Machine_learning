# 📦 Stock Amount Prediction Using Machine Learning

[![Python >=3.8](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup & Installation](#setup--installation)
- [Running the Pipeline](#running-the-pipeline)
- [Implementation Details](#implementation-details)
- [Results & Visualisations](#results--visualisations)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🎯 Project Overview
This repository provides a **machine‑learning pipeline** that predicts product sales (stock amounts) for Big Mart stores. It loads the **Big Mart Sales** dataset, preprocesses the data, engineers features, and trains two regression models—**Linear Regression** and **Random Forest**—to forecast `Item_Outlet_Sales`. Model performance is evaluated with MAE, RMSE, and R², and visualisations are generated for data distribution, actual vs. predicted values, feature importance, and model comparison.

---

## 📂 Repository Structure
```
ML Practical/
├─ StockPridiction.py      # Main script
├─ archive/
│  ├─ Train.xlsx           # Training data
│  └─ Test.xlsx            # Test data
├─ ml_env/                # Optional Python virtual environment
├─ model_results.png      # Visualisation output
└─ README.md              # This file
```

---

## ⚙️ Setup & Installation
### Prerequisites
- Python **3.8+**
- `pip` for package management

### Option 1 – Use the provided virtual environment *(recommended)*
```bash
cd "C:/Users/aditi/Desktop/ML Practical"
ml_env\Scripts\python.exe StockPridiction.py
```

### Option 2 – Create a fresh environment
```bash
cd "C:/Users/aditi/Desktop/ML Practical"
python -m venv ml_env
ml_env\Scripts\activate
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
python StockPridiction.py
```

---

## ▶️ Running the Pipeline
The script performs the following steps:
1. **Load data** from `archive/Train.xlsx`.
2. **Preprocess** missing values and normalise categorical fields.
3. **Engineer** a derived feature `Outlet_Age`.
4. **Encode** categoricals with `LabelEncoder`.
5. **Train** two models:
   - *Linear Regression* (baseline)
   - *Random Forest* (100 trees, best performance)
6. **Evaluate** with MAE, RMSE, and R².
7. **Save visualisations** to `model_results.png`.

---

## 📊 Results & Visualisations
| Model               | MAE   | RMSE   | R² Score |
|---------------------|------:|-------:|--------:|
| Linear Regression   | 854.9 | 1136.5 | 0.5247 |
| **Random Forest**   | 754.3 | 1080.2 | **0.5707** |

The Random Forest model consistently outperforms the baseline.

![Model visualisations](model_results.png)

---

## 🛠️ Implementation Details
- **Data Loading** – Reads `archive/Train.xlsx` (8,523 rows × 12 columns).
- **Preprocessing** – Handles missing values, normalises categorical entries, and creates `Outlet_Age`.
- **Feature Engineering** – Encodes categoricals via `LabelEncoder`.
- **Model Training** – Baseline Linear Regression vs. Random Forest (100 trees).
- **Evaluation** – Computes MAE, RMSE, R² for both models.
- **Visualisation** – Saves a PNG with sales distribution, actual vs. predicted, feature importance, and performance comparison.

---

## 🐞 Troubleshooting
- **Missing packages** – Activate the virtual environment before running the script.
- **FileNotFoundError for `archive/Train.xlsx`** – Ensure you run the script from the repository root.
- **Graph not displaying** – The script saves `model_results.png`. Open the file manually if the plot window does not appear.

---

## 📄 License
This project is provided for educational purposes. Feel free to fork, modify, and use it under the terms of the **MIT License**.
