# Submission History

Log of Kaggle submission history including major model revisions and local validation and leaderboard scores.

### Submission 1 (LB: 0.3801361, Val: 0.375757, Training: 0.379792)
This was a binary classifier with a global threshold used to produce the output baskets. I trained on an initial set of basic features using XGBoost, and the parameters to the model were largely informed by those in user Fabienvs's kernel.

The goal for the next submission is to keep increasing the number and quality of features. After that, I can think about incorporating a user level basket size prediction instead of using a global threshold on the binary classifier.