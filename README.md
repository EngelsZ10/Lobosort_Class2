# Clase 5: Aprendizaje Federado

Este repositorio contiene el código necesario para realizar **aprendizaje federado** mediante la combinación de modelos entrenados localmente en diferentes computadoras sin compartir directamente los datos de entrenamiento.

## Contenido del Repositorio

Al clonar este repositorio obtendrás los siguientes archivos principales:

* **`TheModel.py`**: Contiene la definición del modelo utilizado en los entrenamientos. Este archivo se usa automáticamente en los otros scripts.

* **`entrenamiento_local.ipynb`**: Notebook que permite entrenar el modelo localmente. Puedes compartir este archivo con los participantes que realizarán entrenamientos en sus computadoras personales, sin necesidad de compartir sus datos con los demás.

* **`entrenamiento_global.ipynb`**: Notebook que permite generar un modelo global combinando los modelos entrenados localmente mediante técnicas de aprendizaje federado. Toma todos los modelos locales de la carpeta `modelos/` y realiza una agregación utilizando tres métodos distintos:

  * **Average (promedio simple)**
  * **Median (mediana)**
  * **Trimmed Mean (promedio recortado)**

Además, esta notebook verifica automáticamente que todos los modelos hayan sido entrenados con la misma infraestructura y muestra el rendimiento de cada modelo global generado.

## Cómo utilizar este repositorio

### Paso 1: Setup

#### Clonar repositorio
```bash
git clone <enlace-del-repositorio>
```
#### Configurar ambiente
```pwsh
uv venv
.venv/Scripts/activate
uv sync
pip install tensorflow
```

### Paso 2: Entrenamiento Local

1. Abre el notebook `entrenamiento_local.ipynb`.
2. Ejecuta el entrenamiento local.
3. Guarda el modelo resultante en la carpeta `modelos/`.

Puedes distribuir este notebook a múltiples personas que entrenarán modelos con sus propios datos de manera privada.

### Paso 3: Entrenamiento Global

1. Recoge todos los modelos entrenados localmente en la carpeta `modelos/`.
2. Abre el notebook `entrenamiento_global.ipynb`.
3. Ejecuta las celdas para generar los modelos globales y verificar rendimiento y compatibilidad.

## Resultados Esperados

Al ejecutar correctamente estos notebooks obtendrás:

* Modelos locales entrenados de manera privada.
* Modelos globales agregados con diferentes estrategias de aprendizaje federado.
* Reportes de rendimiento detallados para cada estrategia.
