# 🌊 Flood Prediction System – Week 1 & 2 Project

## 📌 Project Overview
This repository contains my work for the **Climate Risk and Disaster Management** project.  
The goal is to analyze a dataset related to floods and build a predictive system.

---

## 📂 Dataset
- File: **flood.csv**  
- Shape: 50,000 rows × 21 columns  
- Target Column: **FloodProbability**  
- Features include: MonsoonIntensity, TopographyDrainage, Urbanization, ClimateChange, DamsQuality, PopulationScore, etc.  

---

## 🛠️ Week 1 Work
- Imported dataset and libraries  
- Performed initial data exploration: `.info()`, `.describe()`, `.isnull().sum()`  
- Verified dataset is **clean** with no missing values  

---

## 🛠️ Week 2 Work
- Performed **Exploratory Data Analysis (EDA)**:
  - Correlation Heatmap
  - Distribution of FloodProbability
- Applied **Data Transformation** (MinMax Scaling)  
- Conducted **Feature Selection** using RandomForest  
- **Top 5 Important Features:**
  1. TopographyDrainage  
  2. DamsQuality  
  3. PopulationScore  
  4. IneffectiveDisasterPreparedness  
  5. RiverManagement  

---

## 📓 Files in this Repo
- `Flood_Prediction_W1.ipynb` → Week 1 Notebook  
- `Flood_Prediction_W2.ipynb` → Week 2 Notebook  
- `flood.csv` → Dataset file  
- `README.md` → Project documentation  

---

## 🚀 Next Steps
- Perform advanced visualization  
- Train ML models for Flood Prediction  
- Evaluate performance with metrics (R², MAE, RMSE)  

