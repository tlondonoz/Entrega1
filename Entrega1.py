import gzip

# Archivo de entrada (comprimido en formato .gz)
filename = r"C:\Users\tomas\Desktop\BLAST\RESULTADOS\Prog_Entrega_1\Fusarium_oxysporum.FO2.62.chr.gff3.gz"

# El archivo de salida tendrá el mismo nombre pero en formato .tsv
output_file = filename.split('.')[0] + '_mod.tsv'

# Listas para guardar los datos (ejemplo de estructura básica)
crom_list = []
tipo_list = []
start_list = []
end_list = []
strand_list = []
id_list = []

# Abrimos el archivo de entrada y el de salida
with gzip.open(filename, 'rt') as entrada, open(output_file, "w") as salida:

    # Escribimos la fila de encabezados
    salida.write("cromosome\ttype\tstart\tend\tstrand\tID\n")

    # Leemos línea por línea
    for linea in entrada:

        # Ignoramos las líneas que son comentarios
        if linea.startswith("#"):
            continue

        # Separamos la línea en 9 columnas
        columnas = linea.strip().split("\t")

        # Si no tiene 9 columnas, no sirve
        if len(columnas) != 9:
            continue

        crom = columnas[0]
        tipo = columnas[2]
        start = columnas[3]
        end = columnas[4]
        strand = columnas[6]
        atributos = columnas[8]

        # Buscamos el ID dentro de los atributos
        ID = "."
        if "ID=" in atributos:
            ID = atributos.split("ID=")[1].split(";")[0]

        # Guardamos los datos en listas
        crom_list.append(crom)
        tipo_list.append(tipo)
        start_list.append(start)
        end_list.append(end)
        strand_list.append(strand)
        id_list.append(ID)

        # Escribimos en el archivo de salida
        salida.write(f"{crom}\t{tipo}\t{start}\t{end}\t{strand}\t{ID}\n")

print("✅ Listo, archivo guardado en:", output_file)
