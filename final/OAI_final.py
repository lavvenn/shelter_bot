from final import Final

from openai import OpenAI

from googletrans import Translator

preprompt = """
You are writing the outcome of events for the ending of the board game "Bunker";
your task, using the data obtained, is to describe the further history of the characters who entered the bunker,
write whether they survived or not, and come up with different interesting situations using facts
from the received data. it is necessary to take into account the number of players, their condition, bunker, disaster. Your answer should contain only the general ending for all players and nothing extra (EXCLUSIVELY GENERAL ENDING) without a description of the game and players, without describing the ending of each player. But your answer must take into account all factors, i.e. the characteristics of each player, bunker, disaster, duration of stay."""


class OAIFinal(Final):

    client = OpenAI(api_key="")
    translator = Translator()

    def get_final(self,game_data:str):
        game_data_en = self.translator.translate(game_data, dest="en").text
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
            messages=[
                {"role":"ADMIN","content":preprompt},
                {   
                    "role": "user",
                    "content": game_data_en
                }
            ]
            )

        final = response.choices[0].message.content
        
        return self.translator.translate(final, dest="ru").text


    def get_character_final(self,game_data:str,character_id:int):
        pass