import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[1,2], [3,4], [5,6],[7,8],[9,10]])
y_train = np.array([3,7,11,15,19])

model = LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

X_test = np.array([[100,100], [2,2], [125,5]])
y_pred = model.predict(X_test)

print(y_pred)