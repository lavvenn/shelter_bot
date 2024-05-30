from google.cloud import translate
from g4f.Provider import Liaobots

from g4f.client import Client

preprompt = """
You are writing the outcome of events for the finale of the board game bunker;
your task, using the data received, is to describe the further history of the characters who went into the bunker,
write whether they survived or not, and come up with various interesting situations using facts
from the data received. you have to take into account the number of players, and their conditions, bunker, disaster
"""


class Final:
    def __init__(self, language, model):

        self.language = language
        # self.translator = translate.TranslationServiceClient()
        self.client = Client()
        self.tclient = translate.TranslationServiceClient()
        self.model = model

    def generate(self, game_data: str) -> str:
        response = self.client.chat.completions.create(
        model=self.model,
        messages=[{"role":"user", "content": preprompt},
                 {"role": "user", "content": game_data}]
        )
        return self.tclient.translate(response.choices[0].message.content, target_language=self.language).translated_text 
