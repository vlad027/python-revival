import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic dataset for classification
X_class, y_class = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.3, random_state=42)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

#Plot decision boundaries for both classifiers
x_min, x_max = X_class[:, 0].min() - 1, X_class[:, 0].max() + 1
y_min, y_max = X_class[:, 1].min() - 1, X_class[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Naive bayes decision boundary
Z_nb = gnb.predict(np.c_[xx.ravel(), yy.ravel()])
Z_nb = Z_nb.reshape(xx.shape)

# Decision tree decision boundary
Z_dt = dt_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z_dt = Z_dt.reshape(xx.shape)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.contourf(xx, yy, Z_nb, alpha=0.5, cmap=plt.cm.coolwarm)
plt.scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title("Naive Bayes Decision Boundary")
plt.subplot(1, 2, 2)
plt.contourf(xx, yy, Z_dt, alpha=0.5, cmap=plt.cm.coolwarm)
plt.scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title("Decision Tree Decision Boundary")

plt.tight_layout()
plt.show()
