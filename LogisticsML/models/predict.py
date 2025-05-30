
import pandas as pd
import joblib



def prediction(distancia_km:float, clima: str, proveedor: str) -> float:
    """Prediccion de nuevas entradas"""
    ni=pd.DataFrame([{
        'distancia_km':distancia_km,
        'clima':clima,
        'proveedor':proveedor
    }])
    try:

        X=joblib.load('models/columns_entrenamiento.pkl')

        input_process= pd.get_dummies(ni)
        input_process=input_process.reindex(columns=X, fill_value=0)


        charged_model = joblib.load('models/delivery_model.pkl')
        y_pred=charged_model.predict(input_process)
        return y_pred[0]

    except FileNotFoundError as e:
        return f'Modelo o Columnas ausentes: {e}'


if __name__ == '__main__':
    print(prediction(75,'lluvia','C'))

