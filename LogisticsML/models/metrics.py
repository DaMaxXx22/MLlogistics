import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from train_model import test_variables
import numpy as np

X_test, y_test, model = test_variables()

def metrics_model():
    y_pred=model.predict(X_test)
    mae=mean_absolute_error(y_test, y_pred)
    mse=mean_squared_error(y_test, y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(y_test, y_pred)

    """
    📌 ¿Qué significan?
MAE bajo → En promedio, el modelo no se equivoca mucho (todos los errores pesan igual).

MSE bajo → También indica buen desempeño, pero penaliza más los errores grandes porque eleva al cuadrado cada diferencia.

Si MAE y MSE son casi iguales, significa que no hay errores extremos en tus predicciones. ✅

RMSE bajo → Es la raíz del MSE, así que se expresa en las mismas unidades (en tu caso, días). Ayuda a interpretar el error en la escala original.

R² cercano a 1 → El modelo explica muy bien la variación de los datos. R² = 1 significa predicción perfecta.

R² ≈ 0 o negativo → El modelo no está aprendiendo nada útil, y es peor que simplemente predecir el promedio de los datos.
    """
    return mae, mse, rmse, r2




if __name__ == '__main__':
    print(metrics_model())

