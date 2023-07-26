"""
This code creates some test agent and registers until the user stops the process.
For this we wait for SIGINT.
"""

import logging
import os
from sc_client.models import ScAddr, ScLinkContentType

from sc_client.constants import sc_types

from sc_kpm import ScAgentClassic, ScModule, ScResult, ScServer
from sc_kpm.utils import create_link, get_link_content_data
from sc_kpm.utils.action_utils import (
    create_action_answer,
    finish_action_with_status,
    get_action_arguments,
)
from sc_kpm.utils import check_edge, create_edge
from sc_kpm.utils import create_link

from sc_kpm.utils import get_element_by_role_relation, get_element_by_norole_relation

import requests

from sc_kpm import ScKeynodes

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="[%d-%b-%y %H:%M:%S]"
)

logging.basicConfig(level=logging.INFO)


class WeatherAgent(ScAgentClassic):
    def on_event(self, event_element: ScAddr, event_edge: ScAddr, action_element: ScAddr) -> ScResult:
        result = self.run(action_element)
        is_successful = result == ScResult.OK
        finish_action_with_status(action_element, is_successful)
        self.logger.info("Agent finished %s", "successfully" if is_successful else "unsuccessfully")
        return result
    
    def run(self, action_node: ScAddr) -> ScResult:
        self.logger.info("Agent began to run")        

        messageAddr = get_action_arguments(action_node, 1)[0]

        show_weather_answer_phrase = ScKeynodes.resolve("show_weather_answer_phrase", None)

        messageType = ScKeynodes.resolve("concept_message_about_weather", None)
        # Делаем запрос для получения погоды
        if check_edge(sc_types.EDGE_ACCESS_VAR_POS_PERM, messageType, messageAddr):
            response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=53.9&longitude=27.57&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")      
            # Обрабатываем ответ  
            weather_data = response.json()        
            main_data = weather_data["current_weather"]
            # Получаем значение температуры
            temperature = main_data["temperature"]       
            
            link = create_link(str(temperature), ScLinkContentType.STRING, link_type = sc_types.LINK_CONST)  
            tempArc = create_edge(sc_types.EDGE_ACCESS_CONST_POS_PERM, show_weather_answer_phrase, link)

            create_action_answer(action_node, link)

        return ScResult.OK

SC_SERVER_HOST = os.getenv('host', 'localhost')

SC_SERVER_URL = f'ws://{SC_SERVER_HOST}:8090/ws_json'
server = ScServer(SC_SERVER_URL)
with server.connect():
    module = ScModule(WeatherAgent("action_show_weather"))
    server.add_modules(module)
    with server.register_modules():
        server.serve()
        