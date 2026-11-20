"""
archivos.py
-----------
Ejercicio: acceder a un archivo de texto con Python, escribir en él
y leer su contenido.

Conceptos que se practican:
  - open(): abrir un archivo.
  - Modos de apertura: "w" (escribir), "a" (añadir) y "r" (leer).
  - with: abre el archivo y lo cierra solo al terminar.
  - try/except: controlar el error si el archivo no existe.
"""

# Nombre del archivo con el que vamos a trabajar.
# Se creará en la misma carpeta desde la que ejecutes el programa.
ARCHIVO = "notas.txt"


def escribir_archivo(ruta, lineas):
    """Escribe cada elemento de 'lineas' en una línea del archivo.

    OJO: el modo "w" (write) BORRA el contenido anterior del archivo.
    Si el archivo no existe, lo crea.
    """
    # encoding="utf-8" hace que las tildes y la ñ se guarden bien.
    # "with ... as archivo" cierra el archivo automáticamente al salir del bloque.
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            # write() no añade salto de línea solo, por eso ponemos "\n".
            archivo.write(linea + "\n")


def agregar_linea(ruta, linea):
    """Añade una línea al FINAL del archivo sin borrar lo que ya había.

    El modo "a" (append) escribe al final. Si el archivo no existe, lo crea.
    """
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def leer_archivo(ruta):
    """Devuelve una lista con las líneas del archivo (sin el "\n" final).

    El modo "r" (read) solo permite leer.
    Si el archivo no existe, Python lanza un FileNotFoundError.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        # read() lee todo el texto de golpe; splitlines() lo separa por líneas.
        return archivo.read().splitlines()


def mostrar(titulo, lineas):
    """Imprime un título y después las líneas numeradas."""
    print(titulo)
    # enumerate(..., start=1) da a cada línea su número empezando en 1.
    for numero, linea in enumerate(lineas, start=1):
        print(f"  {numero}. {linea}")


# Este bloque solo se ejecuta al lanzar el archivo directamente
# (python3 archivos.py); no se ejecuta si otro programa lo importa.
if __name__ == "__main__":
    # 1. ESCRIBIR: creamos el archivo con 3 líneas.
    escribir_archivo(ARCHIVO, [
        "Comprar pan",
        "Estudiar programación",
        "Subir el código a GitHub",
    ])
    print(f"Archivo '{ARCHIVO}' creado.")

    # 2. LEER: comprobamos lo que se ha escrito.
    mostrar("Contenido tras escribir:", leer_archivo(ARCHIVO))

    # 3. AÑADIR: ponemos una cuarta línea al final y volvemos a leer.
    agregar_linea(ARCHIVO, "Hacer ejercicio")
    mostrar("Contenido tras añadir:", leer_archivo(ARCHIVO))

    # 4. ERROR CONTROLADO: intentamos leer un archivo que no existe.
    # Sin try/except el programa se pararía con un error largo.
    try:
        leer_archivo("no_existe.txt")
    except FileNotFoundError:
        print("Error controlado: el archivo 'no_existe.txt' no existe.")
