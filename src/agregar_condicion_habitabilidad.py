from pathlib import Path
from constants import FILES_DIRECTORY
import csv

def calificar_condicion(line : dict):
    """
    Devuelve la condicion de habitabilidad de la vivienda recibida como parametro:

    Categorías:
    - Insuficiente: agua fuera del terreno, agua con bomba manual u otra fuente desconocida, baño fuera del terreno o inexistente.
    - Regular: agua fuera de la vivienda pero dentro del terreno, baño fuera de la vivienda pero dentro del terreno, o baño letrina.
    - Saludables: agua por cañería dentro de la vivienda con bomba a motor, o baño dentro de la vivienda con inodoro sin botón / cadena y con arrastre de agua (a balde).
    - Buena: agua por cañería dentro de la vivienda y de red pública, o baño dentro de la vivienda con inodoro con botón / mochila / cadena y arrastre de agua.

    Parameters:
        line(dict): Un hogar de la tabla.
    
    Returns:
        str: La condicion de habitabilidad de la vivienda.
    """
    if line['IV6'] == '3' or int(line['IV7']) >= 3 or line['IV8'] == '2' or line['IV9'] == '3':
        return 'insuficiente'
    if line['IV6'] == '2' or line['IV9'] == '2' or line['IV10'] == '3':
        return 'regular'
    if (line['IV6'] == '1' and line['IV7'] == '2') or (line['IV9'] == '1' and line['IV10'] == '2'):
        return 'saludables'
    if (line['IV6'] == '1' and line['IV7'] == '1') or (line['IV9'] == '1' and line['IV10'] == '1'):
        return 'buena'
    return ''

if __name__ == '__main__':
    path_file = Path(FILES_DIRECTORY/'usu_hogar_T324.txt')

    # Leer el archivo
    with open(path_file,encoding='utf-8') as csv_file:
        csv_dict = list(csv.DictReader(csv_file,delimiter=';'))

    # Evaluar la condición de habitabilidad
    for line in csv_dict:
        line['CONDICION_DE_HABITABILIDAD'] = calificar_condicion(line)

    # Escribir el archivo actualizado   
    with open(path_file, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=csv_dict[0].keys(), delimiter=';')
        csv_writer.writeheader()
        csv_writer.writerows(csv_dict)