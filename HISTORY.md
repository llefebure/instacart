# Submission History

Log of Kaggle submission history including major model revisions and local validation and leaderboard scores.

### Submission 1 
| Data | Score |
| --- | --- |
| LB | 0.3801361 |
| Validation (full training set) | 0.375757 |
| Training (full training set) | 0.379792 |
| Validation (small training set) | 0.375128 |
| Training (small training set) | 0.382457 |

This was a binary classifier with a global threshold used to produce the output baskets. I trained on an initial set of basic features using XGBoost, and the parameters to the model were largely informed by those in user Fabienvs's kernel.

The goal for the next submission is to keep increasing the number and quality of features. After that, I can think about incorporating a user level basket size prediction instead of using a global threshold on the binary classifier.

### Submission 2
| Data | Score |
| --- | --- |
| LB | 0.3821141  |
| Validation (small training set) | 0.378477 |
| Training (small training set) | 0.387111 |

I added several more features including days since last order of product. I also did some tuning of the xgboost model: raised the number of rounds/trees and lowered the learning rate. There is still some finer tuning that could be done.

Next I want to create a dynamic threshold for my classifier. I see two ways of doing this: predict basket size per user and take that many of the top predicted products or train a separate model for learning the proper threshold per user. 

### Submission 3-6
| Data | Score |
| LB | .3829204 |

For these I tested various threshold prediction methods. For the training predictions, a calculated the threshold for each user that would've produced the best f1. I trained a model on these thresholds, and then used it to predict the best threshold for each user in the test set. The submissions were different versions of this dynamic threshold: the first used the predicted threshold as is and the rest shrunk it towards the best global threshold of .19 according to (thr + n*.19)/ (n+1) for n = 1, 2, 3. The variant with n=2 produced the best score and an improvement over the global threshold, but it was very small.