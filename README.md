🌊 Flood Prediction System using Machine Learning
📌 Abstract

Floods are one of the most frequent natural disasters, causing significant loss of life, property damage, and environmental degradation. This project builds a Flood Prediction System using machine learning techniques to estimate flood probability based on multiple risk factors such as drainage quality, dams condition, population density, and preparedness levels.

🎯 Problem Statement

Floods disrupt lives, agriculture, and infrastructure, and their frequency is increasing due to climate change, rapid urbanization, and poor drainage management. Traditional monitoring methods are often delayed and inefficient. There is a strong need for a predictive system that can forecast flood probability in advance using multiple contributing factors.

✅ Solution

We developed a Random Forest based Flood Prediction Model in Google Colab.

The dataset (50,000 rows × 21 features) includes geographical, environmental, and socio-economic factors.

Data preprocessing, Exploratory Data Analysis (EDA), and feature selection were performed.

The final model identified TopographyDrainage, DamsQuality, and PoliticalFactors as the most significant contributors to flood probability.

🛠️ Tools & Technologies

Platform: Google Colab

Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Model: Random Forest Regressor

Version Control: GitHub

📂 Project Structure
Flood_Prediction_Project/
│
├── Week1_Flood_Prediction.ipynb   
├── Week2_Flood_Prediction.ipynb   
├── Week3_Flood_Prediction_Final.ipynb   
│
├── flood.csv                      
├── outputs/                       
│    ├── Residual_plot.png
│    └── Final_screenshot.png
│
└── README.md

📊 Results

R² Score: ~0.45

MAE: ~0.03

RMSE: ~0.0013

Top 5 Important Features:

TopographyDrainage

DamsQuality

PoliticalFactors

IneffectiveDisasterPreparedness

PopulationScore

🚀 How to Run in Google Colab

Open the notebook directly in Google Colab by clicking:


Upload the dataset (flood.csv) if it’s not already linked in the code.

Run all cells to reproduce results.

🔮 Future Scope

Improve prediction accuracy using deep learning models.

Integrate with real-time IoT sensor data for early warning systems.

Deploy as a web app / mobile app for disaster management authorities.
