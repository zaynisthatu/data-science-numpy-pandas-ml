import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data.csv')
df = df.iloc[:506]
# print(df.info())

median_rm = df['RM'].median()
# print(f'Median of RM: {median_rm}')
# df['RM'].fillna(median_rm, inplace=True)
df['RM'] = df['RM'].fillna(median_rm)
# df.info()
plt.figure(figsize=(10, 6))
sns.histplot(df['MEDV'], bins=30, kde=True)
plt.title('Distribution of MEDV')
plt.xlabel('Price ($1000s)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='RM', y='MEDV', data=df)
plt.title('Number of Rooms vs. House Price')
plt.xlabel('Number of Rooms (Average Room)')
plt.ylabel('House Price ($1000s)')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x ='LSTAT', y='MEDV', data=df)
plt.title('Percentage of Lower Status vs. House Price')
plt.xlabel('Percentage of Lower Status')
plt.ylabel('House Price ($1000s)')
plt.show()

cor_mtx = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(cor_mtx, cmap='coolwarm')
# sns.heatmap(cor_mtx, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()


X = df[['RM', 'LSTAT']] 
Y = df['MEDV']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)

# Y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, predictions)
print(f'Mean Squared Error: {mse}')
print(f"Model ka Root Mean Squared Error: {np.sqrt(mse)}")