from config.db import get_table_entregas
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestRegressor



df=get_table_entregas()
def model_generate():
    X=pd.get_dummies(df.drop(columns=['id','tiempo_entrega_dias']))
    y=df['tiempo_entrega_dias']
    X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.2, random_state=42)

    model= RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return joblib.dump(model, 'delivery_model.pkl')

def test_variables():
    X=pd.get_dummies(df.drop(columns=['id','tiempo_entrega_dias']))
    y=df['tiempo_entrega_dias']
    X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.2, random_state=42)

    model= RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return X_test,y_test, model


def columns_models():
    X = pd.get_dummies(df.drop(columns=['id', 'tiempo_entrega_dias']))
    y = df['tiempo_entrega_dias']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return joblib.dump(X.columns.tolist(), "columns_entrenamiento.pkl")




if __name__ == '__main__':
    print(model_generate())