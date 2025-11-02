#  Cryptocurrency Liquidity Prediction for Market Stability

###  Machine Learning | Flask Deployment 

---

##  Project Overview

Cryptocurrency markets are **highly volatile**, and liquidity plays a crucial role in market stability.  
This project builds a **Machine Learning model** to predict the **liquidity level of cryptocurrencies** based on key market factors like **trading volume**, **transaction patterns**, **exchange listings**, and **social media activity**.

By forecasting liquidity variations, this project helps **traders and exchanges** detect liquidity crises early and make **data-driven risk management decisions**.

---

##  Key Features

-  **Exploratory Data Analysis (EDA):** Trends, distributions, and correlation heatmaps.  
-  **Data Preprocessing:** Handling missing values, scaling, and outlier treatment.  
-  **Feature Engineering:** Liquidity-related metrics derived from trading & social data.  
-  **Model Training:** Multiple ML models compared (Linear, Random Forest, etc.).  
-  **Hyperparameter Tuning:** Using GridSearchCV for optimized Random Forest.  
-  **Model Evaluation:** RMSE, MAE, and R² for performance comparison.  
-  **Flask Web App:** Predict liquidity based on new input data.  
-  **Deployable on Render / Streamlit / Localhost**.


## Dataset Information

- Source: Historical cryptocurrency market data (CoinGecko datasets)
- Duration: 2016–2017
- Columns include:  
  `coin`, `symbol`, `price`, `1h`, `24h`, `7d`, `24h_volume`, `mkt_cap`, `date`
  
After feature engineering, derived features include:
- `trading_volume`
- `transaction_pattern`
- `exchange_listing`
- `social_media_activity`


