# Análisis de algoritmos de ordenamiento

Este proyecto tiene como objetivo analizar y comparar el rendimiento de distintos algoritmos de ordenamiento implementados en **Python**, evaluando su tiempo de ejecución bajo diferentes condiciones de entrada para identificar cuál resulta más eficiente empíricamente.  
La investigación se basa en un análisis de datos estructurado en seis etapas, combinando enfoques teóricos y experimentales.

---

## 🧭 Introducción

El análisis de algoritmos es un área fundamental dentro de la informática y la ciencia de datos, ya que permite comprender cómo el rendimiento de una solución computacional varía en función de los recursos utilizados.  
Entre los problemas más clásicos se encuentra el **ordenamiento de datos**, una operación presente en innumerables aplicaciones como la clasificación de información, búsqueda eficiente y optimización de procesos.

A pesar de la existencia de numerosos algoritmos de ordenamiento, su desempeño puede variar considerablemente dependiendo del **tamaño, tipo y distribución de los datos**. Por ello, resulta esencial evaluar su comportamiento empírico en contextos reales, utilizando herramientas de análisis de datos para obtener conclusiones objetivas.

Este proyecto busca aplicar un enfoque experimental de análisis de datos para comparar distintos algoritmos de ordenamiento implementados en **Python**, observando cómo sus tiempos de ejecución se comportan bajo diversas condiciones. Con ello se busca vincular la teoría de complejidad algorítmica con resultados medibles, fortaleciendo la comprensión práctica del rendimiento computacional.

---

## 💡 Justificación del tema

La elección de este tema se fundamenta en la necesidad de **comprender empíricamente cómo los algoritmos responden ante volúmenes crecientes de información**, una situación común en el análisis y procesamiento de datos.  
Si bien los libros de algoritmos suelen presentar análisis teóricos basados en notación Big-O, en la práctica los resultados pueden variar por factores como la implementación, el lenguaje de programación o las características del hardware.

Mediante este proyecto se busca:
- Aplicar la metodología de análisis de datos a un problema computacional clásico.  
- Desarrollar habilidades en la **medición, registro y visualización de datos experimentales**.  
- Promover una visión crítica que relacione la teoría algorítmica con la práctica.  

En síntesis, este trabajo contribuye a fortalecer el pensamiento analítico y la capacidad de evaluar empíricamente la eficiencia de soluciones informáticas, competencias esenciales tanto en ciencia de datos como en desarrollo de software.

---
## 🤔 Pregunta de investigación

> ¿Qué algoritmo de ordenamiento (*Bubble Sort*, *Insertion Sort*, *Merge Sort* o *Quick Sort*) presenta mejor rendimiento en términos de tiempo de ejecución según el tamaño y tipo de los datos de entrada, al ser evaluado en Python durante un período de dos semanas de análisis experimental?

---

## 🎯 Objetivo general

Analizar y comparar el rendimiento de distintos algoritmos de ordenamiento implementados en Python, evaluando su tiempo de ejecución bajo diferentes condiciones de entrada para identificar cuál resulta más eficiente empíricamente.

---

## 🎯 Objetivos específicos

- Implementar en Python los algoritmos *Bubble Sort*, *Insertion Sort*, *Merge Sort* y *Quick Sort*.  
- Ejecutar los algoritmos con conjuntos de datos de distintos tamaños y características.  
- Registrar los tiempos de ejecución y operaciones realizadas por cada algoritmo.  
- Analizar los resultados mediante herramientas de análisis y visualización de datos.  
- Identificar el algoritmo con mejor desempeño promedio según el contexto de ejecución.

---

## 🔍 Metodología de análisis de datos (6 etapas)

1. **Planteamiento del problema:**  
   Definir la pregunta de investigación y los objetivos del análisis.

2. **Recolección de datos:**  
   Generar conjuntos de datos aleatorios y/o parcialmente ordenados de distintos tamaños (100, 1.000, 10.000, 50.000 y 100.000 elementos).

3. **Limpieza y preparación de los datos:**  
   Asegurar la integridad de los conjuntos, eliminando duplicados o valores anómalos y normalizando los formatos de entrada.

4. **Análisis exploratorio de datos (EDA):**  
   Medir y registrar el tiempo promedio de ejecución de cada algoritmo bajo diferentes condiciones.

5. **Visualización de resultados:**  
   Representar gráficamente los resultados mediante **matplotlib** y **pandas**, comparando desempeño y crecimiento de tiempo según el tamaño de entrada.

6. **Conclusión y comunicación:**  
   Interpretar los resultados y presentar conclusiones sobre la eficiencia empírica de los algoritmos.

---

## 🧠 Algoritmos analizados

- Bubble Sort  
- Insertion Sort  
- Merge Sort  
- Quick Sort  

---

## 🧰 Tecnologías utilizadas

- Python 3.11  
- pandas  
- matplotlib  
- numpy  
- Jupyter Notebook / PyCharm  

---

## 📁 Estructura del proyecto
```
sorting-algorithms-analysis/
│
├── data/ # Conjuntos de datos generados
├── notebooks/ # Análisis exploratorio y visualizaciones
├── scripts/ # Implementaciones y pruebas de algoritmos
├── results/ # Resultados y gráficos generados
├── .gitignore
└── README.md
```

---

## 📈 Resultados esperados

- Determinar el algoritmo con mejor rendimiento promedio según tamaño y tipo de datos.  
- Establecer una relación entre la complejidad teórica y el rendimiento empírico.  
- Visualizar comparativamente los tiempos de ejecución mediante gráficos y métricas.

---

## 🧑‍💻 Autor

**Nombre:** Germán R. S.  
**Curso:** Análisis de Datos  
**Año:** 2025  
