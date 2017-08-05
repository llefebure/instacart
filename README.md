# Instacart Market Basket Analysis
This project is my approach to [Instacart's prediction competition](https://www.kaggle.com/c/instacart-market-basket-analysis) hosted on Kaggle. The goal is to predict the items that will be in a user's next order out of those he or she has ordered in the past. To achieve this goal, we're provided user order history and information about products.

## Approach
The core of my approach to the problem is framing it as binary classification. Specifically, I look at all the user/product candidate pairs (pairs where the given user has ordered the given product in the past) and predict whether or not the product will be in the user's next order. Once I have those predictions, I can aggregate at the user level to get the full basket prediction.

The steps I took can be reduced to the following:

1. Generating candidate pairs

2. Creating features

3. Building the binary classification model on user/product pairs

4. Reducing the output of the model to the final basket prediction

### Generating Candidate Pairs

Contained in the provided data is information on orders (order id, user id, order day of week, days since previous order, etc.) as well as information on products within each order (order id, product id, etc.). Therefore, to generate candidate pairs I join these two data sources together for users' previous orders and select the distinct user id/product id pairs. The result of this operation is a user id/product id pair that indicates that the given user has ordered the given product at least once in the past. For users in the training set, I additional capture the boolean value specifying whether the product was in the user's next order. This is the response that we want to predict.

### Creating Features

The next step is to build a set of features that can be attached to each candidate pair. I break these down into user features, order features, product features, and user-product features. After generating these features, I join with the candidate pairs to build the full training and test feature matrices.

#### User Features

User features capture information about a user's overall behavior. This includes things like the total number of orders that the user has made in the past, their average basket size, their average reorder rate, and more.

#### Order Features

Order features contain information about the specific order that we are trying to predict the basket for. This includes the day of the week of the order, the time of the order, what number order this is for the user, and more.

#### Product Features

Product features describe users' aggregate behavior with the given product. This includes the total number of times the product was ordered, the total number of reorders of the product, the reorder probability (out of users who have ordered the product in the past, how many reordered it at least once), and more.

#### User-Product Features

User-Product features capture information about a user's history with the given product. This includes how many times the user has ordered this product, the number of orders/days since their last order of this product. The proportion of their orders that contained this product, and more.

### User/Product Binary Classification

Once the feature matrices are built, it becomes a binary classification problem.

#### Validation Strategy

To validate performance of my model offline, I could use cross-validation or simply hold out a random fraction of the training data and evaluate performance of the binary classifier on that validation set. However, since the end goal is to predict the basket for a user, I need to be able to validate performance on that task as well. For that reason, I select 30% of user ids in the training set and mark all of the candidate pairs for that user as part of the validation set. This ensures that for a given user, all of their candidate pairs end up in either the validation set or not.

### Aggregating User/Product Predictions

After retrieving the predicted probabilities from the binary classifier, I still need to figure out how to use them to build the predicted basket for each user.

#### Global Threshold

The simplest approach is to choose a global threshold on the predicted probability that decides whether the product should be in the user's predicted basket. Through experimentation on the validation set, the best threshold value ended up being around .2.

#### Dynamic Threshold

Another approach would be to find what would have been the best threshold for each user in the training set, train a model on this threshold, and then use this model to predict a dynamic threshold for each user in the test set.

#### Basket Size Prediction

Instead of using a threshold value, I also tried predicting the number of reorders in a user's basket. Using this model, I sort the predicted probabilities for a user and choose the top N, where N is the predicted number of reorders for the user.
