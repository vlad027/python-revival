import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate synthetic dataset for classification
X_reg, y_reg = make_regression(n_samples=200, n_features=1, noise=15.0)

#Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

#Create and train the llinear regression model (Lecture Slide 17)
lr = LinearRegression()
lr.fit(x_train, y_train)

# K Nearest Neighbors Regression with k=5
knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(x_train, y_train)

#Prediction
y_pred_lr = lr.predict(x_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

# KNN Regression predictions
y_pred_knn = knn_regressor.predict(x_test)
mse_knn = mean_squared_error(y_test, y_pred_knn)

# 3. Plotting Results (Linear Regression plot)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_reg, y_reg, color='blue', label='Data')
plt.plot(X_reg, lr.predict(X_reg), color='red', label='Linear Regression')
plt.title("Linear Regression")
plt.legend()
plt.subplot(1, 2, 2)
plt.scatter(X_reg, y_reg, color='blue', label='Data')
plt.plot(X_reg, knn_regressor.predict(X_reg), color='green', label='KNN Regression')
plt.title("K-Nearest Neighbors Regression")
plt.legend()
plt.tight_layout()
plt.show()

print(f"Linear Regression MSE: {mse_lr}")
print(f"KNN Regression MSE: {mse_knn}")
