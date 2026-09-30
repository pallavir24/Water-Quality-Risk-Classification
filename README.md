# Water Quality Risk Classification

An end-to-end, zero-cost machine learning system to classify water samples into safe (potable) or high-risk (non-potable) categories based on measurable physical and chemical characteristics.

---

## 📌 Project Overview
- **Domain:** Environment / Public Health
- **Task:** Binary Classification
- **Dataset:** Kaggle Water Potability Dataset (3,276 records)
- **Primary Model:** Random Forest Classifier (Evaluated against Logistic Regression & Decision Tree baselines)
- **Deployment:** Streamlit Web Application

---

## 📊 Dataset & Citation
- **Source:** Kaggle Water Potability Dataset (`adityakadiwal/water-potability`)
- **Features Used:**
  - `ph`: Acidity/Alkalinity level (0–14)
  - `Hardness`: Capacity of water to precipitate soap (mg/L)
  - `Solids`: Total Dissolved Solids / TDS (ppm)
  - `Chloramines`: Disinfection chemical concentration (ppm)
  - `Sulfate`: Dissolved sulfate salts (mg/L)
  - `Conductivity`: Electrical conductivity (μS/cm)
  - `Organic_carbon`: Total organic carbon content (ppm)
  - `Trihalomethanes`: Byproducts of chlorination (μg/L)
  - `Turbidity`: Measure of light emitting properties / clarity (NTU)
- **Target:** `Potability` (0 = Non-Potable / High Risk, 1 = Potable / Safe)

---

## 📈 Model Performance & Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.610 | 0.000 | 0.000 | 0.000 | 0.521 |
| Decision Tree | 0.625 | 0.531 | 0.385 | 0.446 | 0.612 |
| **Random Forest (Final)** | **0.680** | **0.640** | **0.420** | **0.507** | **0.675** |

### Evaluation Insights
- Linear models struggle due to non-linear chemical thresholds.
- The Random Forest model achieved the highest ROC-AUC and minimized false positives, helping ensure contaminated water is not flagged as safe.

---

## 📁 Repository Folder Structure

```text
Water-Quality-Risk-Classification/
├── README.md
├── requirements.txt
├── app.py
├── water_quality_analysis.ipynb
├── water_model.pkl
├── confusion_matrix.png
└── paper_report.md
