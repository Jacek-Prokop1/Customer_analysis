import pandas as pd
from models import Client_activity
from sklearn.model_selection import train_test_split

def load_data():
    df = pd.DataFrame(
        Client_activity.query.with_entities(
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

def split_x_y():
    df = load_data()
    x = df
    y = df['sales_value']
    return x,y

def get_train_test_split():

    x,y = split_x_y()

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

