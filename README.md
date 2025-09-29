# Entrega1

# Análisis de anotaciones genómicas en formato GFF3

Este proyecto tiene como objetivo transformar datos genómicos en bruto (en formato GFF3) en un archivo tabulado sencillo de manejar. Con el script incluido, es posible extraer información clave de los genes y organizarla en un archivo TSV que puede abrirse y analizarse fácilmente.

---

## Carpetas y programas del proyecto

-   `src/procesar_gff3.py`: Script principal que hace la lectura y procesamiento del GFF3.
-   `data/Fusarium_oxysporum.FO2.62.chr.gff3.gz`: Archivo de anotaciones genómicas comprimido (ejemplo).
-   `output/genes_tabla.tsv`: Archivo generado con la información procesada.
-   `README.md`: Documento de referencia y guía de uso.

---

## Librerías necesarias

Para ejecutar el proyecto necesitas tener instalado **Python 3.8 o superior**.


---

## Cómo Ejecutar el Proyecto

Sigue estos pasos para poner en marcha el script.

### 1. Clona el Repositorio
Abre tu terminal y clona el proyecto en tu máquina local.

```bash
git clone [https://github.com/tu_usuario/procesamiento_gff3.git](https://github.com/tu_usuario/procesamiento_gff3.git)
c dprocesamiento_gff3
```
*(No olvide reemplazar `tu_usuario` por tu nombre de usuario en GitHub)*

###  Ejecute el Script
Una vez dentro de la carpeta del proyecto, ejecute el siguiente comando:

```bash
python src/procesar_gff3.py
```

El script procesará el archivo de entrada y guardará el resultado automáticamente.
### Archivo generado
El archivo generará las siguiente columnas:

cromosome	type	start	end	strand	ID

Cromosome: es el número al cual el gen pertenece.

Type: si es mRNA, exon, o cualquier caracteristica que la base de datos en formato gff3 proporcione.

Start y End: desde que posición empieza a cual termina.

ID: la id que el archivo le da a cada gen en específico.
