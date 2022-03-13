Hyperparameter optimization (HPO) is the process by which we aim to improve the performance of a model by choosing the right set of hyperparameters.
Some Hyperparameter Examples:
criterion
max_depth
min_samples_split


Grid Search
In grid search, we try every combination of the set of hyperparameters that the user-specified.
Grid search is implemented in scikit-learn under the name of GridSearchCV
Grod Search should be used if the model you are tuning does not have too many parameters, or if you don’t have too much training data.



 In HPO, we generally :
Select a set of hyperparameters to test
Train a model with those hyperparameters on validation data
Evaluate the performance of the model
Move on to the next set of hyperparameters
Keep the hyperparameters which improve the performance the most






#Hyperperameter Algorithm:Grid search
#Random Forest
from sklearn.model_selection import GridSearchCV
# Define the hyperparameter configuration space
rf_params = {
    'n_estimators': [10, 20, 30],
    #'max_features': ['sqrt',0.5],
    'max_depth': [15,20,30,50],
    #'min_samples_leaf': [1,2,4,8],
    #"bootstrap":[True,False],
    "criterion":['gini','entropy']
}
clf = RandomForestClassifier(random_state=0)
grid = GridSearchCV(clf, rf_params, cv=3, scoring='accuracy')
grid.fit(X, y)
print(grid.best_params_)
print("Accuracy:"+ str(grid.best_score_))
