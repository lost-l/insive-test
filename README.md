# Prueba Técnica - Insive SpA

Esta es una prueba técnica para avanzar en el proceso de selección con la empresa Insive SpA.

Este repositorio contiene los archivos necesarios para completar la prueba técnica. A continuación, encontrarás instrucciones sobre cómo proceder.

## Descripción del proyecto

El proyecto consiste en un script que puede identificar qué combinación del alfabeto inglés es necesaria para descifrar un mensaje previamente cifrado.

## Requerimientos

Para ejecutar el proyecto, es necesario tener instalado [Python](https://www.python.org/downloads/).

## Instrucciones

Después de haber clonado el proyecto, dirígete al directorio del proyecto y ejecuta el script `test.py` mediante el siguiente comando en una terminal:

```bash
python test.py
```


### Resolución del problema

Básicamente, la prueba suministra los detalles necesarios para pensar en la solución. Especifica que la llave consta de 4 caracteres que cumplen un regex de `[a-z]`, lo que sugiere una combinación de 4 caracteres del alfabeto.

El proceso de realizar el XOR se explica en detalle en la prueba, por lo que solo es necesario 'trasladarlo' al código.
