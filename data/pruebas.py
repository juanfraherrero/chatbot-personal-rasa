from asyncore import read
import json
import os
from swiplserver import PrologMQI, PrologThread
from calculoDeHamming import get_name_materia_similar

    

# x = input("ingrese un numero")
# while (x != -1 ):
#     if (x == 1):
        
#     if (x == 2):
#         print("2")
#     if (x == 3):
#         print("3")
#     if (x == 4):
#         print("4")
    

class OperarArchivo():

    @staticmethod
    def guardar(AGuardar):
        with open("/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/datos","w") as archivo_descarga:
            json.dump(AGuardar, archivo_descarga, indent=4)
        archivo_descarga.close()

    @staticmethod
    def cargarArchivo(): 
        if os.path.isfile("/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/datos"):
            with open("/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/datos","r") as archivo_carga:
                retorno=json.load(archivo_carga)
                archivo_carga.close()
        else:
            retorno={}
        return retorno


datos = OperarArchivo.cargarArchivo()
materiaLower = "Diseño de Sistemas de Software"
print(datos["ejercicios"][materiaLower])
print("----------------------")
print(datos["ejercicios"][materiaLower]["1"]["1"])
print("----------------------")
try :
    print(datos["ejercicios"][materiaLower]["1"]["2"])
except:
    print("no existe")

# s2 = "programacion expl"
# materia = get_name_materia_similar(s2,OperarArchivo.cargarArchivo()["marteriasArreglo"])
# if(materia):
#     print("la cadena mas parecida es: ", materia)
# else:
#     print("no se encontro una cadena parecida")


#anio = input("ingrese un anio")
# materia = input("ingrese una materia: ")
# materiaNew = OperarArchivo.cargarArchivo()["tranformacionesDeNombresMaterias"]
# try:
#     materiaNew = materiaNew[materia.lower()]
#     print(materiaNew)
#     with PrologMQI(port=8000) as mqi:
#         with mqi.create_thread() as prolog_thread:
#             prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
#             prolog_thread.query_async(f"le_gusta_materia_nombre(\"{materiaNew}\").", find_all=False)
#             result = prolog_thread.query_async_result()
#             print(result)
            #result = result[0]['Materias']
            #rint("las materias son:" + str(result)) 
    # for materia in result:
    #     #sleep(0.3)
    #     dispatcher.utter_message(text = materia)  
# except:
#     print("no se encontro la materia")
    #dispatcher.utter_message(text = "no se encontro la materia")
    
