# House Price Prediction
Model created to predict the estate sale price for apartments/houses in Bucharest.

## Project Overview

This project performs the following key steps:

* Data Cleaning: Prepares the dataset by removing unnecessary columns and cleaning up location categories.
* Feature Engineering: Adds new features such as price per square meter (price_per_m2) and one-hot encodes categorical columns for modeling.
* Outlier Detection: Identifies and removes outliers in apartment pricing to enhance prediction accuracy.
* Model Training and Evaluation: Trains and compares multiple models (Linear Regression, Lasso, Decision Tree) using grid search and cross-validation.
* Prediction Function: A function to predict apartment prices based on specified features.

## Data Preparation

The initial dataset is loaded from house_offers.csv. The preparation steps include:

* Column Dropping: Removes irrelevant columns.
* Price Adjustment: Applies a 45% increase to the price column to reflect updated pricing.
  * Outlier Removal:
        price_per_m2 outliers are removed per location to avoid skewing predictions.
        Additional filtering by room count helps further clean the dataset.
* Encoding: Location data is one-hot encoded for model compatibility.
* Feature Engineering: New features such as price_per_m2 are computed to aid in analysis and predictions.

## Modeling and Evaluation

The project uses multiple models to identify the best fit for predicting apartment prices:

* Linear Regression
* Lasso Regression (tuned with different alpha values)
* Decision Tree Regressor (evaluated using different split criteria)

## Model Selection

Each model undergoes hyperparameter tuning with grid search and cross-validation. The function find_best_model determines the best model and parameters for apartment price prediction.
Evaluation Metrics

Model performance is evaluated using cross-validation scores and mean squared error.
Usage

    Model Prediction: The predict_price function predicts apartment prices based on:
        location: Location of the apartment
        surface: Total surface area (in square meters)
        rooms: Number of rooms
        baths: Number of bathrooms
        balcony: Number of balconies
        level: Apartment level

    Model Export: The trained model is saved as a pickle file (bucharest_apartments_prices_model.pickle), and column names are stored in a JSON file (columns.json) for easy reference during deployment.
## Example Usage

### Predict the price of a 65m² 2-room apartment with 1 bathroom and 1 balcony, located on the 5th floor in the "Other" category.
```ruby
predicted_price = predict_price('Other', 65, 2, 1, 1, 5)
print(f"Predicted Price: {predicted_price}")
```

## Files
* house_offers.csv: The source dataset of apartment offers.
* requirements.txt: Python package dependencies.
* bucharest_apartments_prices_model.pickle: The saved machine learning model.
* columns.json: JSON file containing column names for deployment reference.
