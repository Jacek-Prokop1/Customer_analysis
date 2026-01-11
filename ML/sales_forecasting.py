from sklearn.linear_model import LinearRegression
from ML.data import get_train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_model_regression(client_id=None):
    X_train, X_test, y_train, y_test, error = get_train_test_split(client_id)

    if error:
        return None, error

    try:
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("mse ", mse)
        print("r2 ", r2)
    except Exception as e:
        return None, f"Wystąpił błąd podczas trenowania modelu: {str(e)}"

    return y_pred, None