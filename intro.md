# Curso de herramientas de optimización con Python

:::{figure} ./img/favicon.png
:width: 15%
:align: center
:::

```{admonition} Bienvenido
En esta página web se presenta todo el material del curso de **Herramientas de optimización con Python** impartido en el congreso de la [SGAPEIO XVII](http://xviicongreso.sgapeio.es/index.html) celebrado en Ourense del 23 al 25 de octubre del 2025.

![SGAPEIOXVII](http://xviicongreso.sgapeio.es/images/slider/nivo/001.jpg)
```

## 🎯 Objetivo del curso
El objetivo principal del curso es ofrecer una introducción práctica a algunas de las principales herramientas de optimización disponibles en Python.

Aunque el curso se imparte en Python, **no es necesario tener un conocimiento avanzado del lenguaje**. Incluye una breve introducción a los **conceptos básicos** mínimos necesarios para poder seguir el contenido sin dificultad.

## 🧰 Herramientas que se trabajarán
La herramientas concretas que se trabajarán en este curso serán:
- [Pyomo](https://pyomo.readthedocs.io/en/stable/): Lenguaje de modelado algebraico en Python.
- [Google OR-Tools](https://developers.google.com/optimization): Conjunto de herramientas de Google enfocadas a la optimización (API de Python).
- [Gurobi Python API](https://www.gurobi.com/documentation/): Interfaz oficial del solver Gurobi para Python.

## ⚙️ Requisitos e instalación opcional

```{note} Nota
Este curso se puede seguir **sin necesidad de instalar nada localmente**, ya que todos los cuadernos incluirán un **botón para ejecutarlos directamente en Binder**. 
  
![Launch on Binder](https://mybinder.org/badge_logo.svg)
```

Si prefieres trabajar en tu propio entorno, se recomienda usar:

- **Python 3.13 o inferior**
- Los siguientes paquetes instalados:
  ```bash
  pip install pyomo ortools gurobipy jupyterlab
  ```
- Un entorno interactivo como **JupyterLab** para ejecutar los notebooks.
