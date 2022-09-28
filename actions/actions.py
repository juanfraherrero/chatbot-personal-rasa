# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from time import sleep
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from swiplserver import PrologMQI, PrologThread
import os.path
import json
#

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

class Action_consultar_cant_materias_carrera(Action): # listo

    def name(self) -> Text:
        return "action_consultar_cantidad_materias_carrera"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(f"materias_totales_fa(Materias).")
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
                prolog_thread.query_async(f"materias_totales_fa(Materias).", find_all=False)
                result = prolog_thread.query_async_result()
                result = result[0]['Materias']
                print("las materias de la carrera son:" + str(result)) 
        for materia in result:
            dispatcher.utter_message(text = materia)  
        dispatcher.utter_message(text="esas son todas las materias de la carrera")
        return


class Action_consultar_legajo(Action): # listo

    def name(self) -> Text:
        return "action_consultar_legajo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        datos = OperarArchivo.cargarArchivo()
        dispatcher.utter_message(text="mi legajo es " + str(datos["datosPersonales"]["legajo"]))
        return []

class Action_consultar_dni(Action): # listo

    def name(self) -> Text:
        return "action_consultar_dni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        datos = OperarArchivo.cargarArchivo()
        dispatcher.utter_message(text="mi dni es " + str(datos["datosPersonales"]["dni"]))
        return []

class Action_consultar_materias_aprobadas(Action): # listo

    def name(self) -> Text:
        return "action_consultar_materias_aprobadas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(f"materias_aprobadas_fa(Materias).")
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
                prolog_thread.query_async(f"materias_aprobadas_fa(Materias).", find_all=False)
                result = prolog_thread.query_async_result()
                result = result[0]['Materias']
                print("las materias aprobadas son:" + str(result)) 
        for materia in result:
            dispatcher.utter_message(text = materia)  
        dispatcher.utter_message(text="esas son todas las materias aprobadas")
        return []

class Action_consultar_materias_restantes(Action): # listo

    def name(self) -> Text:
        return "action_consultar_materias_restantes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(f"materias_restantes_fa(Materias).")
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
                prolog_thread.query_async(f"materias_restantes_fa(Materias).", find_all=False)
                result = prolog_thread.query_async_result()
                result = result[0]['Materias']
                print("las materias restantes son:" + str(result)) 
        for materia in result:
            dispatcher.utter_message(text = materia)  
        dispatcher.utter_message(text="estas son todas las materias que me quedan")
        return []


class Action_consultar_materias_de_anio(Action): # listo

    def name(self) -> Text:
        return "action_consultar_materias_de_anio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        anio = tracker.get_slot("anio")
        print("anio es:" + str(anio))
        print(f"materias_de_22({anio}, Materias).")
        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
                prolog_thread.query_async(f"materias_de_fa({anio}, Materias).", find_all=False)
                result = prolog_thread.query_async_result()
                result = result[0]['Materias']
                print("las materias son:" + str(result)) 
        for materia in result:
            #sleep(0.3)
            dispatcher.utter_message(text = materia)  
        dispatcher.utter_message(text=f"estas son todas las materias de {anio}")
        return []

class Action_consultar_gusta_materia(Action): # 

    def name(self) -> Text:
        return "action_consultar_gusta_materia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("la materia por entidad es: " + str(next(tracker.get_latest_entity_values("materia"), None)))
        print("la materia por slot es:" + str(tracker.get_slot("materia")))
        if (next(tracker.get_latest_entity_values("materia"), None) != None):
            materia = tracker.get_slot("materia")
        else:
            materia = None
        if (materia):
            try:
                materiaNew = OperarArchivo.cargarArchivo()["tranformacionesDeNombresMaterias"][materia.lower()]
                with PrologMQI(port=8000) as mqi:
                    with mqi.create_thread() as prolog_thread:
                        prolog_thread.query_async("consult('/home/juan/Documentos/AAUniversidad/3Tercero/9-ProgramacionExploratoria/rasaProject/personal-bot/data/conocimiento_mis_materias.pl').", find_all=False)
                        prolog_thread.query_async(f"le_gusta_materia_nombre(\"{materiaNew}\").", find_all=False)
                        result = prolog_thread.query_async_result()
                        if (result == True):
                            dispatcher.utter_message(text=f"sisi, me gusta {materia}")
                            return [SlotSet("gusta", "True")]
                        else:
                            dispatcher.utter_message(text=f"nop, no me gusta {materia}")
                            return [SlotSet("gusta", "False")]
            except:
                dispatcher.utter_message(text=f"{materia} no es de Ingeniearia de Sistemas, si querés preguntame por otra materia")
                return [SlotSet("gusta", "False")]
        else:
            dispatcher.utter_message(text=f"jajajja no te entendí, cómo?")

class Action_consultar_gusta_materia(Action): # 

    def name(self) -> Text:
        return "action_consultar_que_gusta_de_materia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        materia = tracker.get_slot("materia")
        if (materia):
            le_gusta = tracker.get_slot("gusta")
            if (le_gusta == "True"):
                respuesta = OperarArchivo.cargarArchivo()["marteriasGustaArreglo"][materia.lower()]
                dispatcher.utter_message(text=f"{respuesta}")
            else:
                dispatcher.utter_message(text=f"nose, no me gusta {materia}")
        else:
            dispatcher.utter_message(text=f"???")

        return []
#         return []