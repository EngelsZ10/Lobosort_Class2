# Análisis y Predicción de Bancarrota de Empresas con PCA y XGBoost 🚀  

## Descripción del Proyecto  
Este proyecto tiene como objetivo analizar datos financieros de empresas mediante técnicas de reducción de dimensionalidad y modelos de clasificación. Se trabajó con un conjunto de datos que contiene *más de 95 variables, por lo que se aplicó **Principal Component Analysis (PCA)* para reducir la dimensionalidad a solo *9 componentes principales* sin perder información relevante.

Posteriormente, se entrenó un modelo de *clasificación binaria XGBoost, capaz de determinar si una empresa está en **bancarrota* o no, basado en sus características financieras.  

### 🏗 *Arquitectura del Proyecto*  
1️⃣ *Preprocesamiento de Datos*  
   - Carga y limpieza del conjunto de datos.  

2️⃣ *Reducción de Dimensionalidad con PCA*  
   - Separación del dataset en entrenamiento y prueba.  
   - Aplicación de *PCA solo en el conjunto de entrenamiento*.  
   - Transformación del conjunto de prueba con los componentes obtenidos.  

3️⃣ *Entrenamiento del Modelo XGBoost*  
   - Configuración y optimización de hiperparámetros.  
   - Evaluación del desempeño con métricas de clasificación.  

4️⃣ *Despliegue en Azure Cloud*  
   - Se desplegó en *Azure* por la naturaleza financiera y escalabilidad del proyecto.  
   - Integración con servicios de almacenamiento y procesamiento en la nube.  

## 🚀 Tecnologías Utilizadas  
✅ *Python* (Pandas, Scikit-Learn, XGBoost, Matplotlib)  
✅ *Machine Learning* (PCA, XGBoost)  
✅ *Cloud Computing* (Azure Cloud)  

## 🛠 Instalación y Uso  
1️⃣ Clona el repositorio:  
   ```bash
   git clone https://github.com/lobosort