# Instacart Market Basket Analysis
This project is my approach to [Instacart's prediction competition](https://www.kaggle.com/c/instacart-market-basket-analysis) hosted on Kaggle. The goal is to predict the items that will be in a user's next order out of those he or she has ordered in the past. To achieve this goal, we're provided user order history and information about products.

## Approach
The core of my approach to the problem is framing it as binary classification. Specifically, I look at all the user/product candidate pairs and predict whether or not the given product will be in the user's next order. Once I have those predictions, I can aggregate at the user level to get the full basket prediction.

The steps I took can be reduced to the following:

1. Generating candidate pairs

2. Creating features

3. Building the binary classification model on user/product pairs

4. Reducing the output of the model to the final basket prediction

### Generating Candidate Pairs

### Creating Features

### User/Product Binary Classification

### Aggregating User/Product Predictions
