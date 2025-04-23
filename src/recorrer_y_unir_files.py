from constants import DATA_OUT_PATH, FILES_DIRECTORY

def unir_files():
    #Defino en variables la ruta de salida para cada archivo
    arch_salida_hogar= DATA_OUT_PATH / "usus_hogar.csv"
    arch_salida_ind= DATA_OUT_PATH / "usus_individual.csv"

    #Abro los archivos creados anteriormente
    with arch_salida_hogar.open("w") as salida_hogar, \
        arch_salida_ind.open("w") as salida_ind:    
        
        #Recorro los elementos en la carpeta 'files'    
        for archivo in FILES_DIRECTORY.iterdir():
            
            #Escribo el contenido de los archivos 'usu_hogar_T...' en uno global(usus_hogar)
            if archivo.name.startswith("usu_hogar"):
                with archivo.open() as a:
                    for line in a:
                        salida_hogar.write(line)
            #Escribo el contenido de los archivos 'usu_individual_T...' en uno global(usus_individual)            
            elif archivo.name.startswith("usu_individual"):
                with archivo.open() as f:
                    for line in f:
                        salida_ind.write(line)
                    
                            
                        
                
            