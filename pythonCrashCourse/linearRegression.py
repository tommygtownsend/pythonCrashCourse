import numpy as np


def train_linear_regression(X, y):
    """
    Trains a linear regression model using the normal equation.

    Args:
        X: Feature matrix (numpy array).
        y: Target vector (numpy array).

    Returns:
        Weights (theta) for the linear model.
    """
    # Add a column of ones to X for the intercept term (bias)
    ones = np.ones((X.shape[0], 1))
    X_b = np.hstack((ones, X))

    # Calculate weights using the normal equation: theta = (X_b^T * X_b)^-1 * X_b^T * y
    # np.linalg.inv computes the inverse of a matrix
    # .T transposes the matrix
    # @ performs matrix multiplication
    try:
        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        return theta
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular. Cannot compute inverse.")
        return None


def predict(X_test, theta):
    """
    Predicts target values using the trained linear regression model.
    """
    # Add a column of ones for the intercept term
    ones = np.ones((X_test.shape[0], 1))
    X_test_b = np.hstack((ones, X_test))

    # Prediction: y_pred = X_test_b * theta
    predictions = X_test_b @ theta
    return predictions


# --- Run the project ---

# 1. Generate synthetic data
np.random.seed(42)  # for reproducibility
X = 2 * np.random.rand(100, 1)  # 100 samples, 1 feature
y = 4 + 3 * X + np.random.randn(100, 1)  # y = bias + weight*X + noise

print("--- Starting NumPy Linear Regression Project ---")

# 2. Train the model
weights = train_linear_regression(X, y)

if weights is not None:
    print(f"\nTraining completed.")
    print(f"Calculated weights (bias, feature_weight):\n{weights.flatten()}")
    print("\nExpected weights from data generation were close to [4, 3].")

    # 3. Make a prediction
    X_new = np.array([[0], [2]])  # New data points to predict for
    predictions = predict(X_new, weights)

    print(f"\nPredictions for new data points:\n{X_new.flatten()}")
    print(f"Predicted y values:\n{predictions.flatten()}")

print("\n--- Project Finished ---")

