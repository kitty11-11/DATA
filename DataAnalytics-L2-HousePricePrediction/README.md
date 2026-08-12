# Task 1: House Price Prediction using Linear Regression

## 📌 Project Overview

This project focuses on predicting house sale prices using Machine Learning.

The Ames Housing dataset is used to explore the relationship between different house features and their sale prices. A Linear Regression model is trained and evaluated, followed by a comparison with Ridge Regression.

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Check missing values and duplicate records
- Analyze the distribution of house sale prices
- Identify important features related to house prices
- Handle numerical and categorical features
- Apply One-Hot Encoding to categorical variables
- Split the data into training and testing sets
- Build a Linear Regression model
- Evaluate the model using MSE, RMSE and R²
- Analyze model coefficients
- Visualize actual vs predicted prices
- Analyze model residuals
- Compare Linear Regression with Ridge Regression

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 📂 Dataset

The project uses the Ames Housing dataset containing **2,930 records and 82 columns**.

The target variable is:

**SalePrice** — the final sale price of the house.

## 🔍 Exploratory Data Analysis

The dataset was examined using:

- `head()`
- `info()`
- `describe()`
- Missing-value analysis
- Duplicate-value analysis
- Correlation analysis
- Sale price distribution visualization

The SalePrice distribution is right-skewed, with most houses concentrated in the lower-to-middle price range and fewer houses having very high sale prices.

## ⚙️ Data Preprocessing

The features were divided into:

- Numerical features
- Categorical features

Categorical features were converted into numerical form using **One-Hot Encoding**.

A preprocessing pipeline was used to handle the transformations before training the model.

## 🤖 Machine Learning Model

### Linear Regression

Linear Regression was trained using the preprocessed features.

The dataset was divided into:

- Training data: 80%
- Testing data: 20%

### Evaluation Metrics

The Linear Regression model was evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Linear Regression Results

- RMSE: approximately **45,959**
- R² Score: approximately **0.7365**

The model explains approximately 73.65% of the variation in house sale prices on the test data.

## 📊 Visualizations

The project includes:

1. Distribution of house sale prices
2. Correlation heatmap
3. Actual vs Predicted house prices
4. Residual plot

## 📈 Coefficient Analysis

The coefficient analysis showed that features such as:

- Gr Liv Area
- Total Bsmt SF
- 1st Flr SF
- BsmtFin SF 1
- 2nd Flr SF
- Garage Area

had relatively large positive coefficients, indicating a strong positive relationship with predicted house prices in the fitted model.

## 🧲 Ridge Regression

Ridge Regression was also tested as a bonus model using L2 regularization.

### Ridge Results

- RMSE: approximately **86,673**
- R² Score: approximately **0.0630**

For this particular implementation and dataset split, Linear Regression performed better than Ridge Regression because it achieved a higher R² score and lower RMSE.

## 📝 Conclusion

This project demonstrates an end-to-end machine learning workflow, starting from data exploration and preprocessing to model training, evaluation, visualization, and interpretation.

The Linear Regression model provided better performance than the Ridge Regression model in this experiment.

## 📁 Project Files

- `AmesHousing.csv` — Dataset
- `Task1_House_Price_Prediction.ipynb` — Jupyter Notebook

## 👩‍💻 Author

**Kirti**