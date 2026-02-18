# 📊 Ecommerce Growth Analytics Platform

An end-to-end growth analytics system built to analyze ecommerce performance, customer behavior, and retention trends using real-world event data.

This project demonstrates production-style data engineering, metric aggregation, and an executive-level BI dashboard built with Streamlit.

---

## 🚀 Project Overview

This platform answers key business questions:

- What is our conversion funnel performance?
- Which product categories convert best?
- How strong is customer retention?
- Are A/B experiments statistically significant?
- How does revenue trend over time?

The system separates heavy data processing from the visualization layer to ensure high performance and scalability.

---

## 🏗 Architecture

```

Raw Events (Kaggle Dataset)
↓
Data Cleaning
↓
Session-Level Funnel Engineering
↓
Metric & Cohort Aggregation
↓
Precomputed Summary Tables
↓
Streamlit Executive Dashboard

```

The dashboard consumes only precomputed summary tables for sub-second load performance.

---

## 📁 Project Structure

```

ecommerce-growth-analytics-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_cleaning.py
│   ├── funnel_engineering.py
│   ├── metrics_engineering.py
│   └── main.py
│ 
├── outputs/
│   ├── brand_revenue.py
│   └── summary_metrics.py
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

## ⚡ Key Features

### 📈 Executive Dashboard
- Total Sessions
- Revenue
- Conversion Rate
- Monthly Revenue Trend

### 🔍 Funnel Analysis
- View → Cart → Purchase
- Sequential conversion validation
- Drop-off visibility

### 🛍 Category Performance
- Category-wise conversion rate
- Top converting categories

### 🔁 Cohort Retention
- Monthly cohort analysis
- Repeat purchase rate
- Customer lifecycle behavior

### 🧪 A/B Testing Simulation
- Two-proportion z-test
- Statistical significance validation
- Conversion comparison between groups

---

## 🧠 Engineering Highlights

- Modular data pipeline orchestration using `main.py`
- Subprocess-based step execution
- Precomputed aggregation layer
- Dashboard decoupled from raw event data
- Optimized load time (<1 second)
- Clean separation of data engineering and analytics layer

---

## 📊 Dataset

Source: Kaggle Ecommerce Events Dataset  
~885,000+ events  
Real-world behavioral event structure  

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Statsmodels

---

## ▶ How To Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/girishshenoy16/Ecommerce-Growth-Analytics-Platform.git
cd Marketing-Funnel-Conversion
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```


### 3️⃣ Install dependencies

```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
````

## 4️⃣ Run the System

### Step 1 — Run data pipeline

```bash
python src/main.py
```

### Step 2 — Launch dashboard

```bash
streamlit run dashboard/app.py
```

### 5️⃣ Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📌 Business Insights Example

* Low Month-1 retention indicates electronics purchasing behavior.
* Category-level variation highlights merchandising opportunities.
* Funnel drop-off between View → Cart suggests UX improvement scope.
* A/B test module allows rapid experiment validation.

---

## 🎯 What This Project Demonstrates

* Real-world analytics thinking
* Data pipeline design
* Performance optimization
* Statistical validation
* Executive storytelling
* Portfolio-ready BI development

---

## 📈 Future Improvements

* Real experiment integration
* Lift & confidence interval reporting
* Deployment to Streamlit Cloud
* Database-backed architecture
* Automated ETL scheduling