# 🦠 Coronavirus Data Analysis Using Python & Pandas

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Data Science](https://img.shields.io/badge/Topic-Data%20Science-orange)

---

## 📘 Overview

This project demonstrates **data cleaning, analysis, and visualization** using **Python’s Pandas library** on a **Coronavirus (COVID-19)** dataset.
It helps to explore real-world data, handle missing values, and extract meaningful insights about global cases, deaths, recoveries, and population statistics.

The goal is to give **beginners in Data Science** a hands-on project to understand the **Pandas workflow** — from loading data to analyzing it.

---

## 🚀 Features

✅ Load and explore large CSV datasets
✅ Display dataset information and summaries
✅ Clean missing or invalid data using `fillna()`
✅ Analyze:

* Top countries by total cases, deaths, and recoveries
* Countries with highest and lowest population
  ✅ Export the cleaned dataset as `Clean_Data.csv`

---

## 🧠 Technologies Used

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| **Python 3.8+**       | Programming Language           |
| **Pandas**            | Data analysis and manipulation |
| **Jupyter / VS Code** | Development environment        |
| **CSV Dataset**       | Source data format             |

---

## 📊 Dataset Description

| Column                           | Description                    |
| -------------------------------- | ------------------------------ |
| `total_confirmed`                | Total confirmed COVID-19 cases |
| `total_deaths`                   | Total number of deaths         |
| `total_recovered`                | Total number of recoveries     |
| `active_cases`                   | Currently active cases         |
| `serious_or_critical`            | Critical condition patients    |
| `total_cases_per_1m_population`  | Cases per million people       |
| `total_deaths_per_1m_population` | Deaths per million people      |
| `total_tests`                    | Total tests conducted          |
| `total_tests_per_1m_population`  | Tests per million              |
| `population`                     | Country population             |

---

## ⚙️ How It Works

### 1️⃣ Import Libraries

```python
import pandas as pd
```

### 2️⃣ Load Dataset

```python
df = pd.read_csv("Clean_Data.csv")
```

### 3️⃣ Explore Data

```python
print(df.head())
print(df.info())
print(df.describe())
```

### 4️⃣ Handle Missing Values

```python
fill_cols = ["total_deaths", "total_recovered", "active_cases"]
df[fill_cols] = df[fill_cols].fillna(0)
```

### 5️⃣ Perform Analysis

```python
print("🌍 Country with Highest Population:")
print(df.loc[df["population"].idxmax()])

print("\n⚰️ Country with Highest Deaths:")
print(df.loc[df["total_deaths"].idxmax()])
```

### 6️⃣ Export Cleaned Data

```python
df.to_csv("Clean_Data.csv", index=False)
print("✅ Clean data saved successfully!")
```

---

## 📈 Example Output

```
🌍 Country with Highest Population:
India - Population: 1,366,000,000

⚰️ Country with Highest Deaths:
USA - Total Deaths: 1,234,567

✅ Clean data saved successfully!
```

---

## 🧩 Skills You’ll Learn

* Data Cleaning & Preprocessing
* Working with Missing Values
* Sorting and Filtering in Pandas
* Data Summarization using `.describe()`
* Real-world Data Analysis Project

---

## 📁 Project Structure

```
📦 Coronavirus-Data-Analysis
├── Clean_Data.csv
├── Coronavires.py
├── README.md
└── requirements.txt
```

---

## 🧾 Requirements

Install all dependencies using:

```bash
pip install pandas
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 📸 Demo Screenshot



<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/86b796cb-bb6f-48c9-8c06-4e4c4826c981" />



---

## 📚 Learning Outcome

After completing this project, you’ll be able to:

* Use **Pandas** for data analysis
* Clean and organize real-world data
* Perform descriptive analytics
* Build beginner-friendly Data Science projects

---
          
## 🧑‍💻 Author

**👨‍💻 Created by:** Jatin Sharma
**📧 Contact:** factallforyou@gmail.com 
**🌐 GitHub:** [https://github.com/codewithjatin70/-Coronavirus-Data-Analysi](https://github.com/codewithjatin70/-Coronavirus-Data-Analysis)





