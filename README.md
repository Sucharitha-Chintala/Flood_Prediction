# 🌊 Flood Prediction System using Machine Learning

## 📌 Abstract
Floods are one of the most frequent natural disasters, causing significant loss of life, property damage, and environmental degradation.  
This project builds a **Flood Prediction System** using machine learning techniques to estimate flood probability based on multiple risk factors such as drainage quality, dams condition, population density, and preparedness levels.

---

## 🎯 Problem Statement
Floods disrupt lives, agriculture, and infrastructure, and their frequency is increasing due to climate change, rapid urbanization, and poor drainage management. Traditional monitoring methods are often delayed and inefficient.  
There is a strong need for a predictive system that can **forecast flood probability in advance** using multiple contributing factors.

---

## ✅ Solution
We developed a **Random Forest-based Flood Prediction Model** in Google Colab.

- Dataset: 50,000 rows × 21 features (geographical, environmental, and socio-economic factors)  
- Steps performed:
  - Data Preprocessing
  - Exploratory Data Analysis (EDA)
  - Feature Selection
- The model identified **TopographyDrainage, DamsQuality, and PoliticalFactors** as the most significant contributors to flood probability.

---

## 🛠️ Tools & Technologies
- **Platform:** Google Colab  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Model:** Random Forest Regressor  
- **Version Control:** GitHub

---

## 📊 Results
- **R² Score:** ~0.45  
- **Mean Absolute Error (MAE):** ~0.03  
- **Root Mean Squared Error (RMSE):** ~0.0013  

**Top 5 Important Features:**
1. TopographyDrainage  
2. DamsQuality  
3. PoliticalFactors  
4. IneffectiveDisasterPreparedness  
5. PopulationScore  

**Residual Plot:** ![Residual Plot](Residual_plot.png)  
**Final Model Screenshot:** ![Final Screenshot](Final_screenshot.png)  

---

## 🚀 How to Run in Google Colab
1. Open the notebook directly in Google Colab.
2. Upload the dataset `flood.csv` if it’s not already linked in the notebook.
3. Run all cells to reproduce the results.

---

## 🔮 Future Scope
- Improve prediction accuracy using **deep learning models**.  
- Integrate with **real-time IoT sensor data** for early warning systems.  
- Deploy as a **web app / mobile app** for disaster management authorities.

---

