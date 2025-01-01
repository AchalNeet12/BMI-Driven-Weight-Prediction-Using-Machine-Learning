# Weight Prediction Using Machine Learning
---
## 📜 Project Description:
   - This project aims to build a predictive model that estimates an individual’s weight based on their height. By leveraging machine learning algorithms, we analyze the relationships between height and 
     weight, evaluate various models for accuracy, and deploy the best-performing model for real-time use via a web application. The project emphasizes simplicity, interpretability, and ease of use, making it 
     accessible for non-technical users.
---
## 📦 Dataset:
The dataset used for this project includes:
  - Input Feature: Height (in feet).
  - Target Feature: Weight (in kilograms).
  - Size: rows=2500,columns=2.
  - The dataset represents a linear relationship between height and weight, ideal for testing regression models.
---
## 🤖 Technology Stack:
  1.Programming Language: `Python.`
  2.Libraries:
  - Data Processing: `NumPy`, `pandas`.
  - Modeling: `scikit-learn`.
  - Deployment: `Streamlit`.
  - Utilities: Pickle for saving and loading models.
---
## 🔍 Data Preprocessing:
The preprocessing steps ensure data quality and prepare it for modeling:
 - **Handling Missing Data:** Checked for and managed any missing or invalid entries in the dataset.
 - **Feature Scaling:** Standardized the data (if needed) to enhance model performance.
 - **Splitting Data:** Divided into 80% training and 20% testing sets for evaluation.
---
## ⚙ Algorithms Evaluated:
Three machine learning algorithms were applied and compared based on Mean Squared Error (MSE):
1 Linear Regression:
 - Simplest and most interpretable model.
 - Achieved the best `MSE = 21.6973.`
2 Random Forest Regression:
 - Ensemble method that reduces overfitting.
 - `MSE = 2708.3037.`
3 Decision Tree Regression:
 - Captures non-linear relationships but prone to overfitting.
 - `MSE = 41.5075.`
- **Conclusion:** Linear Regression outperformed other models due to the dataset's linear nature and was selected for deployment.
---
## 📌 Model Deployment:
  - **Platform:** Deployed the Linear Regression model using Streamlit, an open-source Python library for building interactive web applications.
  - **Features:**
    - User inputs height (in feet).
    - Model predicts and displays the corresponding weight (in kilograms).
 - **Integration:** The trained model was saved using Pickle and loaded within the app for efficient real-time predictions.
---
## 🔑 Features:
 - Interactive web app built using Streamlit.
 - User input for height in feet.
 - Real-time prediction of weight displayed on the app.
 - Clean and intuitive interface.
---
## 🎯 Results:
 - **Best Model:** Linear Regression, with the lowest error `(MSE =21.6973).`
 - **App Usability:** The deployed Streamlit app is user-friendly, with a simple interface for prediction.
---
## 📊 Conclusion:
   This project highlights the effectiveness of Linear Regression for datasets with a linear relationship. By comparing different models, it demonstrates the importance of selecting the right algorithm for 
   the data at hand. The deployment via Streamlit makes the solution accessible and practical for real-world use, showcasing the power of machine learning in predictive tasks.








