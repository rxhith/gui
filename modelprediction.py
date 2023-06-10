import tkinter as tk
import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('flexxx.csv')
features = data.iloc[:, :-2]
labels = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

def get_most_recent_data():
    with open('flexxx.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        most_recent_row = data[-1]  # Assuming the most recent data is at the end of the file
        most_recent_sum = most_recent_row[:-2]  # Exclude the last two columns
        print(f"Most recent sum: {most_recent_sum}") # Change this line to do something else with the sum
        prediction2 = classifier.predict(np.array(most_recent_sum).reshape(1, -1))
        print(prediction2)
        random_input = np.array([91,100,0]).reshape(1, -1)
        prediction1 = classifier.predict(random_input)

        print(f"Predicted Gesture Label for Random Input: {prediction1}")

window = tk.Tk()

button = tk.Button(window, text="Get Most Recent Data", command=get_most_recent_data)
button.pack()

window.mainloop()
