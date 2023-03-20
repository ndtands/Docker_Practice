import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Split the data into features and target
X = data[['sq_ft']]
y = data['price']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[2500]])

# Print the prediction
print('Prediction:', prediction)