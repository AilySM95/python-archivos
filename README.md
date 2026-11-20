# Lectura y escritura de archivos en Python

Ejercicio de práctica: un programa que crea un archivo de texto,
escribe en él, lo lee, añade una línea al final y controla el error
que ocurre cuando el archivo no existe.

## Archivos

- `archivos.py`: el programa, con las funciones para escribir, añadir y leer.

## Cómo ejecutarlo

    python3 archivos.py

Al ejecutarlo se crea el archivo `notas.txt` en la carpeta actual
(por eso no está incluido en el repositorio).

## Qué se practica

- `open()` con los modos `"w"` (escribir), `"a"` (añadir) y `"r"` (leer).
- `with`, que cierra el archivo automáticamente.
- `try/except` para controlar `FileNotFoundError`.

## Requisitos

Solo Python 3. No hay que instalar nada más.
