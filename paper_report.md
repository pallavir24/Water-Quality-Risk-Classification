# Technical Paper: Water Quality Risk Classification Using Supervised Machine Learning Foundational Models

## Abstract
Clean drinking water is fundamental to human health and socio-economic wellbeing. Traditional chemical testing relies on lab assays with turnaround latency. This work designs a zero-cost, end-to-end supervised machine learning pipeline to classify water potability based on nine measurable chemical and physical characteristics. Foundational models including Logistic Regression, Decision Tree, and Random Forest were benchmarked. Random Forest delivered the strongest predictive balance, and was deployed through a lightweight Streamlit interface.

## 1. Introduction & Problem Definition
Assessing drinking water quality requires verifying safe chemical ranges (pH, heavy metals, sulfates, disinfection byproducts). The objective of this project is to build a classification model that identifies whether an environmental water sample is safe for human consumption or presents high contamination risk.

## 2. Related Work
Traditional environmental monitoring relies on static water quality indices (WQI). Recent research indicates that multi-attribute non-linear classifiers identify interactions between indicators (such as chloramines and sulfate thresholds) more reliably than simple single-metric cutoff thresholds.

## 3. Dataset & EDA
The dataset comprises 3,276 water observations across 9 continuous physical and chemical attributes:
- Missing values were present in `ph` (491), `Sulfate` (781), and `Trihalomethanes` (162). These were handled via median imputation to preserve continuous distributions without introducing outlier skew.
- The target class distribution consists of 61% non-potable and 39% potable instances.

## 4. Methodology & Model Development
- Preprocessing: Feature scaling with `StandardScaler` for distance/linear models; direct ingestion for tree models.
- Validation: Stratified 80/20 train-test split.
- Models: Logistic Regression, Decision Tree (max_depth=6), and Random Forest (100 estimators, max_depth=8).

## 5. Results & Discussion
- Logistic Regression was heavily influenced by majority-class prevalence, yielding negligible recall for positive potability.
- Random Forest achieved an accuracy of ~68% with a ROC-AUC score of 0.675, successfully distinguishing non-linear water parameter boundaries.

## 6. Limitations & Future Scope
- **Limitations:** Median imputation decreases feature variance; unmeasured microbiological contaminants limit laboratory-grade deployment.
- **Future Scope:** Integrating real-time IoT water quality sensors with continuous calibration for municipal water plants.

## 7. Conclusion & References
Foundational machine learning models can assist in preliminary water potability screening. 
- *References:* World Health Organization (WHO) Guidelines for Drinking-water Quality; Kaggle Water Potability Dataset.
