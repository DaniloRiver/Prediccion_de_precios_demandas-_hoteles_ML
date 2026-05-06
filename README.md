# 🏨 Hotel Demand & Price Prediction MLOps

Sistema de Machine Learning para la predicción de precios y demanda hotelera, diseñado con un enfoque **MLOps completo**, incluyendo versionamiento de datos, pipelines automatizados, API de inferencia y dashboard interactivo.

---

## 🚀 Objetivo del proyecto

Este proyecto busca predecir la demanda y/o precios en el sector hotelero utilizando modelos de Machine Learning, integrando prácticas de MLOps para asegurar:

- Reproducibilidad de experimentos  
- Versionamiento de datos y modelos  
- Despliegue escalable  
- Monitoreo y automatización del pipeline  

---

## 🧠 Arquitectura del proyecto

```bash
hotel-demand-mlops/
│
├── api/                 # API de inferencia (FastAPI o similar)
├── configs/             # Configuraciones del proyecto
├── data/
│   ├── external/
│   ├── processed/
│   └── raw/
│
├── models/              # Modelos entrenados (.pkl + DVC tracking)
├── notebook/            # Experimentación y análisis
├── outputs/             # Resultados generados
├── pipelines/           # Pipelines de ML (DVC)
├── reports/             # Reportes y métricas
├── src/                 # Código principal del ML pipeline
├── streamlit_app/       # Dashboard interactivo
├── tests/               # Pruebas unitarias
│
├── docker-compose.yml   # Orquestación de servicios
├── Dockerfile.api       # API containerizada
├── Dockerfile.streamlit # App Streamlit containerizada
├── dvc.yaml             # Pipeline de DVC
├── requirements.txt     # Dependencias
└── main.py              # Entry point
⚙️ Tecnologías utilizadas
🐍 Python
🤖 Scikit-learn / ML Models
📊 Pandas / NumPy
🔁 DVC (Data Version Control)
🐳 Docker & Docker Compose
⚡ FastAPI (API de predicción)
📈 Streamlit (Dashboard)
🧪 Pytest (Testing)
☁️ MLOps pipelines
📦 Instalación
1. Clonar repositorio
git clone https://github.com/tu-usuario/hotel-demand-mlops.git
cd hotel-demand-mlops
2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Instalar dependencias
pip install -r requirements.txt
🧪 Ejecución del pipeline (DVC)
dvc repro

Esto ejecuta todo el flujo:

Limpieza de datos
Entrenamiento del modelo
Evaluación
Guardado del modelo
🚀 Levantar con Docker
Backend API + Streamlit
docker-compose up --build
📡 API de predicción

Una vez corriendo:

POST /predict

Ejemplo:
{
  "feature1": 10,
  "feature2": 5,
  "feature3": 1
}
📊 Dashboard Streamlit

Accede a:

http://localhost:8501
Funcionalidades:
Predicciones
Métricas del modelo
Análisis exploratorio
🧪 Testing
pytest tests/
🧠 Modelo

El modelo entrenado se encuentra en:

models/hotel_cancel_model.pkl

Versionado con DVC para garantizar reproducibilidad.

🔄 MLOps Workflow
Ingesta de datos (data/raw)
Procesamiento (data/processed)
Entrenamiento (src/)
Evaluación (reports/)
Registro de modelo (models/)
Despliegue (API + Streamlit)
📌 Notas importantes
Los datos están versionados con DVC
El proyecto está listo para despliegue en contenedores
Separación clara entre entrenamiento e inferencia
Arquitectura escalable para producción
👨‍💻 Autor

Danilo Rivera
Ingeniero en Informática | AI & Big Data | MLOps Enthusiast