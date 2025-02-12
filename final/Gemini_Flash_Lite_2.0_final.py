from openai import OpenAI

from final import Final




preprompt = """
You are writing the outcome of events for the ending of the board game "Bunker";
your task, using the data obtained, is to describe the further history of the characters who entered the bunker,
write whether they survived or not, and come up with different interesting situations using facts
from the received data. it is necessary to take into account the number of players, their condition, bunker, disaster. Your answer should contain only the general ending for all players and nothing extra (EXCLUSIVELY GENERAL ENDING) without a description of the game and players, without describing the ending of each player. But your answer must take into account all factors, i.e. the characteristics of each player, bunker, disaster, duration of stay."""




class Gemini_Flash_Lite_2_final(Final):

    client = OpenAI(api_key="")


    def get_final(self,game_data:str):
        response = self.client.chat.completions.create(
        model="google/gemini-2.0-flash-lite-preview-02-05:free",
            messages=[
                {"role":"ADMIN","content":game_data},
                {   
                    "role": "user",
                    "content": preprompt
                }
                {
                    "role": "user",
                    "content": game_data
                }
            ]
            )

        final = response.choices[0].message.content
        
        return final