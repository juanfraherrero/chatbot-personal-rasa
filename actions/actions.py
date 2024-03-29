# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from cgitb import text
from time import sleep
from typing import Any, Text, Dict, List
from unicodedata import name
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

        nombre = tracker.get_slot("name") 
        if(nombre.lower() == "analia"):   
            datos = OperarArchivo.cargarArchivo()
            dispatcher.utter_message(text="mi legajo es " + str(datos["datosPersonales"]["legajo"]))
        else:
            dispatcher.utter_message(text=f"perdón {nombre}, pero no te puedo dar mi legajo")
        return []

class Action_consultar_dni(Action): # listo
    def name(self) -> Text:
        return "action_consultar_dni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nombre = tracker.get_slot("name") 
        if(nombre.lower() == "analia"):   
            datos = OperarArchivo.cargarArchivo()
            dispatcher.utter_message(text="mi dni es " + str(datos["datosPersonales"]["dni"]))
        else:
            dispatcher.utter_message(text=f"perdoname {nombre}, pero preferiría no darte mi dni")
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
        if (next(tracker.get_latest_entity_values("materia"), None) != None): #si no hay entidad materia desde las lookup tables, entonces lo saco del slot
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
                try:
                    respuesta = OperarArchivo.cargarArchivo()["marteriasGustaArreglo"][materia.lower()]
                    dispatcher.utter_message(text=f"{respuesta}")
                except(KeyError):
                    print(KeyError, "line 202")
            else:
                dispatcher.utter_message(text=f"nose, no me gusta {materia}")
        else:
            dispatcher.utter_message(text=f"???")

        return []

class Action_consultar_me_cantas_un_tema(Action): # 
    def name(self) -> Text:
        return "action_consultar_me_cantas_un_tema"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #print(tracker.latest_message["metadata"])

        nombre = tracker.get_slot("name")
        dispatcher.utter_message(response = "utter_me_cantas_un_tema", nombre=nombre)#, audio="https://github.com/juanfraherrero/rasa-personal-bot/blob/main/data/audioMio.ogg")
        return []

# ---------------------------------------prueba grupal

class Action_consultar_por_ejercicio(Action): # 
    def name(self) -> Text:
        return "action_consultar_por_ejercicio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.latest_message["metadata"])

        print(tracker.latest_message["metadata"]["message"]["from"]["id"])

        if(tracker.latest_message["metadata"]["message"]["from"]["id"] == 1387819927 and (tracker.latest_message["metadata"]["message"]["chat"]["type"] == "group" or tracker.latest_message["metadata"]["message"]["chat"]["type"] == "supergroup" )):
            print("no me respondo a mi mismo en grupos")
            return[]
        
        
        # print("la materia por entidad es: " + str(next(tracker.get_latest_entity_values("materia"), None)))
        # print("el tp de la materia es:" + str(next(tracker.get_latest_entity_values("tp"), None)))
        # print("el inciso de la materia es:" + str(next(tracker.get_latest_entity_values("inciso"), None)))
        
        # tp = tracker.get_slot("tp")
        # inciso = tracker.get_slot("inciso")
        tp = next(tracker.get_latest_entity_values("tp"), None)
        inciso = next(tracker.get_latest_entity_values("inciso"), None)

        if (next(tracker.get_latest_entity_values("materia"), None) != None):
            materia = tracker.get_slot("materia")
        else:
            materia = None

        # print(materia)
        # print(tp)
        # print(inciso)
        
        if (materia):
            try:
                datos = OperarArchivo.cargarArchivo()
                materiaLower = datos["tranformacionesDeNombresMaterias"][materia.lower()]
                ejercicio = datos["ejercicios"][materiaLower][tp][inciso]["resolucion"]
                dispatcher.utter_message(text="sisi, ahi te lo paso", image = ejercicio)
            except:
                dispatcher.utter_message(response="utter_no_tengo_ejercicio") #, tp=tp,inciso=inciso, materia=materia)
        else:
            dispatcher.utter_message(response = "utter_no_conozco_materia")
        return []


