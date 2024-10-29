from sklearn.datasets import make_classification, make_regression
import numpy as np
import keras
from keras import layers
from keras import ops
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)
# Generate a dataset with features suitable for both classification and regression
X_class, y_class = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0,n_clusters_per_class=1)
X_reg, y_reg = make_regression(n_samples=200, n_features=2, noise=15.0)

#making a classification mode with a softmax activation function.
classification_model = keras.Sequential([
    layers.Dense(64, activation='relu', input_dim=2),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')  
])
#making a regression model with a linear activation function.
regression_model = keras.Sequential([
    layers.Dense(64, activation='relu', input_dim=2),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='linear')
])

classification_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
)

regression_model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

classification_model.fit(
    X_class,
    y_class,
    epochs=20,
)

regression_model.fit(
    X_reg,
    y_reg,
    epochs=20,
)

# Plotting decision boundary for classification.
x_min, x_max = X_class[:, 0].min() - 1, X_class[:, 0].max() + 1
y_min, y_max = X_class[:, 1].min() - 1, X_class[:, 1].max() + 1
xx,yy = np.meshgrid(np.arange(x_min,x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = classification_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = np.argmax(Z, axis=1)
Z = Z.reshape(xx.shape)
plt.figure(figsize=(10, 5))
plt.contourf(xx, yy, Z, alpha=0.5, cmap=plt.cm.coolwarm)
plt.scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title("Neural Netwrok Classification Decision Boundary")
plt.show()

# Plotting regression line
y_pred = regression_model.predict(X_reg)
plt.figure(figsize=(10, 5))
plt.scatter(X_reg[:, 0], y_reg, color='blue', label='True Values')
plt.scatter(X_reg[:, 0], y_pred, color='red', label='Predicted Values')
plt.title("Neural Network Regression Prediction")
plt.legend()
plt.show()