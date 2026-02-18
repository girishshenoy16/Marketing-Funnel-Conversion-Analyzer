# 📊 arketing Funnel & Conversion Drop-Off Analyzer

An end-to-end analytics system built to analyze ecommerce marketing funnel performance, identify drop-off points, and uncover conversion optimization opportunities.

This project demonstrates real-world funnel analytics, cohort retention modeling, and statistical experiment validation using production-style data architecture.

---

## 🚀 Project Objective

Businesses lose revenue due to inefficiencies across the marketing funnel.

This system helps answer:

- Where are users dropping off in the funnel?
- What is the true sequential conversion rate?
- Which product categories convert best?
- How strong is customer retention?
- Are A/B experiments statistically significant?

---
## 🔍 Core Funnel Flow

```

View → Cart → Purchase

```

The platform validates both:

- Standard funnel progression
- True sequential conversion logic
- Drop-off percentage at each stage

---


## 🏗 Architecture

```

Raw Event Data
↓
Data Cleaning
↓
Session-Level Funnel Engineering
↓
Category & Cohort Metrics
↓
Precomputed Summary Tables
↓
Streamlit Executive Dashboard

```

Heavy computation is separated from the dashboard layer to ensure sub-second load performance.

---

## 📁 Project Structure

```

Marketing-Funnel-Conversion-Analyzer/
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

## 📈 Dashboard Modules

### 🔹 Executive Overview
- Total Sessions
- Revenue
- Overall Conversion Rate
- Monthly Revenue Trend

### 🔹 Funnel Analysis
- View → Cart → Purchase breakdown
- Drop-off percentage per stage
- True sequential conversion validation

### 🔹 Category-Level Conversion
- Top converting categories
- Category-wise conversion rate

### 🔹 Retention & Cohort Analysis
- Repeat purchase rate
- Monthly cohort retention heatmap

### 🔹 A/B Testing Simulation
- Two-proportion z-test
- Statistical significance validation
- Experiment-based conversion comparison

---

## 🧠 Engineering Highlights

- Modular data pipeline using subprocess orchestration
- Precomputed aggregation layer for performance optimization
- Session-level funnel engineering
- Cohort index calculation using month differences
- Statistical hypothesis testing for experiments
- Dashboard load time optimized under 1 second

---

## 📊 Dataset

Source: Kaggle Ecommerce Events Dataset  
~885,000+ behavioral events  
Real-world marketing funnel structure  

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

## 4️⃣ Run data pipeline

```bash
python src/main.py
```

## 5️⃣ Launch dashboard

```bash
streamlit run dashboard/app.py
```

## 6️⃣ Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📌 Business Insights Example

* High drop-off between View → Cart suggests UX optimization opportunity.
* Low month-1 retention aligns with electronics category purchasing behavior.
* Category-level variation highlights merchandising strategy gaps.
* Experiment module enables rapid validation of marketing hypotheses.

---

## 🎯 What This Project Demonstrates

* Funnel analytics expertise
* Conversion optimization thinking
* Statistical testing capability
* Performance-aware architecture design
* Business-focused storytelling
* 
---

## 🚀 Future Improvements

* Real experiment integration
* Automated ETL scheduling
* Database-backed architecture
* Lift & confidence interval reporting
* Deployment to Streamlit Cloud
