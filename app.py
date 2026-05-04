import pandas as pd 
import numpy as np
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('Crop_recommendation.csv')

print(df.head())

# print(df.isnull().sum())

X = df.drop('label',axis=1)

y = df['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Model
model = RandomForestClassifier()

# Sent Trained Data to Model
model.fit(X_train,y_train)

# Make model do prediction on test data
prediction = model.predict(X_test)

# Score
accuracy_score = accuracy_score(y_test,prediction)
print("Model Accuracy: ", accuracy_score)

# Save model in file
with open('crop_model.pkl','wb') as f:
    pickle.dump(model,f)
print("Model is Saved")

# Manual Testing

test_data = [[80, 50, 40, 25, 80, 6.5, 150]]
result = model.predict(test_data)
print("Manual testing Result: ", result[0])

