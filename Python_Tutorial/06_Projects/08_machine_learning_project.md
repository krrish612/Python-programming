# Project 2: Machine Learning with Python

## What is Machine Learning?
Computers learning from data to make predictions.

## Types of ML
1. **Supervised Learning** - Learn from labeled data
2. **Unsupervised Learning** - Find patterns in unlabeled data
3. **Reinforcement Learning** - Learn from rewards

## Simple ML Example (Linear Regression)
```python
# Linear Regression - Predict from data
import numpy as np
from sklearn.linear_model import LinearRegression

# Data (study hours) -> Scores
X = np.array([[1], [2], [3], [4], [5]])  # Hours
y = np.array([50, 55, 65, 70, 80])       # Scores

model = LinearRegression()
model.fit(X, y)

# Predict score for 6 hours
prediction = model.predict([[6]])
print(f"Score for 6 hours: {prediction[0]}")
```

## Classification Example
```python
# Iris flower classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
```

## Libraries to Learn
| Library | What it's for |
|---------|--------------|
| numpy | Numerical computing |
| pandas | Data analysis |
| matplotlib | Visualization |
| scikit-learn | ML algorithms |
| tensorflow | Deep learning |
| pytorch | Deep learning |

## Simple Data Analysis
```python
import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# Basic info
print(df.head())     # First few rows
print(df.describe()) # Statistics
print(df.info())     # Data types

# Filter
print(df[df["age"] > 20])

# Group
print(df.groupby("city").mean())
```

## Steps for ML Project
1. Define problem
2. Collect data
3. Clean data
4. Train model
5. Evaluate
6. Deploy