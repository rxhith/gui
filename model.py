import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the data from a CSV file
data = pd.read_csv('flexxx.csv')

# Separate features (flex sensor values) and labels (gesture labels)
features = data.iloc[:, :-2]  # All columns except the last two
labels = data.iloc[:, -1]  # Last column only

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a Random Forest classifier
classifier = RandomForestClassifier()

# Train the classifier on the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = classifier.predict(X_test)

# Print the predicted labels
print("Predicted Gesture Labels:")
for prediction in predictions:
    print(prediction)
