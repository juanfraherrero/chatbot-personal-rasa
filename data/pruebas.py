from asyncore import read
from swiplserver import PrologMQI, PrologThread

# x = input("ingrese un numero")
# while (x != -1 ):
#     if (x == 1):
        
#     if (x == 2):
#         print("2")
#     if (x == 3):
#         print("3")
#     if (x == 4):
#         print("4")
    



anio = input("ingrese un anio")
with PrologMQI(port=8000) as mqi:
    with mqi.create_thread() as prolog_thread:
        prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
        prolog_thread.query_async(f"materias_de_fa({anio}, Materias).", find_all=False)
        result = prolog_thread.query_async_result()
        result = result[0]['Materias']
        print("las materias son:" + str(result)) 
# for materia in result:
#     #sleep(0.3)
#     dispatcher.utter_message(text = materia)  
