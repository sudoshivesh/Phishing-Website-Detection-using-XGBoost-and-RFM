import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

# Define the path to the data file
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, 'DataFiles', '5.urldata.csv')

# Load the dataset
data = pd.read_csv(data_file_path)

# Extract features and labels
X = data.drop(columns=['label'])
y = data['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate the Random Forest model
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f'Random Forest Accuracy: {rf_accuracy * 100:.2f}%')

# Save the Random Forest model
with open(os.path.join(current_dir, 'random_forest_model.pkl'), 'wb') as file:
    pickle.dump(rf_model, file)

# Train an XGBoost model (using GradientBoostingClassifier as a placeholder for XGBoost)
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

# Evaluate the XGBoost model
gb_pred = gb_model.predict(X_test)
gb_accuracy = accuracy_score(y_test, gb_pred)
print(f'Gradient Boosting Accuracy: {gb_accuracy * 100:.2f}%')

# Save the XGBoost model
with open(os.path.join(current_dir, 'xgboost_model.pkl'), 'wb') as file:
    pickle.dump(gb_model, file)
