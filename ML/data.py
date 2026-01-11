import pandas as pd
from models import Client_activity
from sklearn.model_selection import train_test_split

def load_data(client_id):
    query = Client_activity.query

    if client_id is not None:
        query = query.filter_by(client_id=client_id)

    df = pd.DataFrame(
        query.with_entities(
            Client_activity.numbers_visits,
            Client_activity.numbers_purchases,
            Client_activity.average_basket_value,
            Client_activity.numbers_purchases_day
        ).all(),
        columns=[
            "numbers_visits",
            "numbers_purchases",
            "average_basket_value",
            "numbers_purchases_day"
        ]
    )

    if df.empty:
        df = pd.DataFrame(columns=[
            "numbers_visits",
            "numbers_purchases",
            "average_basket_value",
            "numbers_purchases_day",
            "sales_value"
        ])
    else:
        df['sales_value'] = df['numbers_purchases'] * df['average_basket_value']

    return df

def split_x_y(client_id=None):
    df = load_data(client_id)
    if df.empty:
        return pd.DataFrame(), pd.Series(dtype=float)  # brak danych
    x = df.drop(columns=['sales_value'])
    y = df['sales_value']
    return x, y

def get_train_test_split(client_id=None, test_size=0.2, random_state=42):
    x, y = split_x_y(client_id)

    if x.empty or len(x) < 2:
        return None, None, None, None, "Za mało danych do trenowania modelu."

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test, None