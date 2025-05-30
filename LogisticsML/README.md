# Predicción de Tiempo de Entrega - Proyecto ML + Dash + PostgreSQL

Este proyecto implementa un sistema completo de aprendizaje automático que predice el tiempo estimado de entrega de un pedido, usando Python, PostgreSQL y un dashboard interactivo con Dash.

---

## 🚀 Tecnologías utilizadas

- **Python 3.12+**
- **Pandas, scikit-learn, SQLAlchemy**
- **PostgreSQL** como base de datos
- **Dash & Dash Bootstrap Components** para visualización
- **Jupyter Notebook** para experimentación
- **dotenv** para manejo de variables de entorno

---

## 🧱 Estructura del proyecto

```
pythonProject/
│
├── main.py                 # Lanza la app Dash
├── .env                   # Variables de conexión a PostgreSQL
├── requirements.txt       # Dependencias del proyecto
│
├── app/
│   ├── layout.py          # Layout y estructura visual
│   ├── callbacks.py       # Callbacks interactivos
│
├── assets/                # Archivos estáticos (CSS, imágenes, etc.)
│
├── config/
│   └── db.py              # Conexión con PostgreSQL (SQLAlchemy)
│
├── models/
│   ├── train_model.py     # Entrenamiento del modelo y guardado .pkl
│   └── predict.py         # Predicción a partir del modelo
│
├── notebooks/
│   └── entrenamiento_modelo.ipynb # Análisis exploratorio y prueba del modelo
```

---

## ⚙️ Configuración inicial

1. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # en Linux/macOS
.venv\Scripts\activate   # en Windows
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu archivo `.env` con tus credenciales de PostgreSQL:

```env
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=LogisticsEnterprise
```

---

## 🧠 Entrenar el modelo

```bash
python models/train_model.py
```

Esto entrena el modelo con datos de la tabla `entregas` y guarda un archivo `modelo_entrega.pkl`.

---

## 🖥️ Ejecutar la app Dash

```bash
python main.py
```

Luego abre tu navegador en: [http://localhost:8050](http://localhost:8050)

---

## ✨ Funcionalidades

- Conexión directa a la base de datos PostgreSQL
- Entrenamiento de modelo automático desde tabla `entregas`
- Predicción interactiva desde el dashboard
- Visualización con Dash y Bootstrap

---

## 📌 Notas

- La tabla `entregas` debe tener los campos:
  - `id`, `distancia_km`, `clima`, `proveedor`, `tiempo_entrega_dias`
- Asegúrate que PostgreSQL está corriendo y accesible en `localhost:5432`

---

## 📫 Autor

Ing. Maximiliano Serrano Molina

---
