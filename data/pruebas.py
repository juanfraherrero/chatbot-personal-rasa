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


s2 = "programacion expl"
materia = get_name_materia_similar(s2,OperarArchivo.cargarArchivo()["marteriasArreglo"])
if(materia):
    print("la cadena mas parecida es: ", materia)
else:
    print("no se encontro una cadena parecida")


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
    





#pruebas de prolog
# materias_de(X).
# materias_de_fa(X, Result).
# materias_totales_fa(Result).
# materias_aprobadas_fa(Result).
# materias_restantes_fa(Result).
# le_gusta_materia_nombre(NombreMateria).
# materias_con_una_correlativa.
# plan_is.


# with PrologMQI(port=8000) as mqi:
#     with mqi.create_thread() as prolog_thread:
#         prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
        
#         print("materias de (1).\n")
#         prolog_thread.query_async(f"materias_de(1).", find_all=False)
#         # print(prolog_thread.query_async_result())
        
#         print("\n\nmaterias de fa (1).\n")
#         prolog_thread.query_async(f"materias_de_fa(1, Result).", find_all=False)
#         # print(prolog_thread.query_async_result())
        
#         print("\n\nmaterias totales fa (1).\n")
#         prolog_thread.query_async(f"materias_totales_fa(Result).", find_all=False)
#         # print(prolog_thread.query_async_result())
        
#         print("\n\nmaterias aprobadas fa (1).\n")
#         prolog_thread.query_async(f"materias_aprobadas_fa(Result).", find_all=False)
#         # print(prolog_thread.query_async_result())
        
#         print("\n\nmaterias restantes fa (1).\n")
#         prolog_thread.query_async(f"materias_restantes_fa(Result).", find_all=False)
#         # print(prolog_thread.query_async_result())
        
#         print("\n\nle gusta materia quimica fa .\n")
#         prolog_thread.query_async(f"le_gusta_materia_nombre(Quimica).", find_all=False)
#         # print(prolog_thread.query_async_result())

#         print("\n\nplan is.\n")
#         prolog_thread.query_async(f"plan_is.", find_all=False)
#         # print(prolog_thread.query_async_result())