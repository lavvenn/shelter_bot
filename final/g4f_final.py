from final import Final

from g4f.client import Client
from g4f.Provider import Liaobots

from translate import Translator


preprompt = """
You are writing the outcome of events for the ending of the board game "Bunker";
your task, using the data obtained, is to describe the further history of the characters who entered the bunker,
write whether they survived or not, and come up with different interesting situations using facts
from the received data. it is necessary to take into account the number of players, their condition, bunker, disaster. Your answer should contain only the general ending for all players and nothing extra (EXCLUSIVELY GENERAL ENDING) without a description of the game and players, without describing the ending of each player. But your answer must take into account all factors, i.e. the characteristics of each player, bunker, disaster, duration of stay."""


class G4FFinal(Final):
    client = Client(provider=Liaobots)
    translator_1 = Translator(from_lang="ru", to_lang="en")
    translator_2 = Translator(from_lang="en", to_lang="ru")

    def get_final(self,game_data:str):
        game_data_en = self.translator_1.translate(game_data)
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
        
        return self.translator_2.translate(final)
    
    def get_character_final(self,game_data:str,character_id:int, contex:str):
        pass
    

if __name__ == "__main__":
    test_game_data = "{'catastrophe': {'name': 'Глобальная эпидемия плесени2', 'description': 'Интенсивный рост плесени по всему миру, приводящий к разрушению имущества и риску для здоровья.'}, 'shelter': {'name': 'Мрачный утес', 'description': 'Расположен на берегу, отличается своими тёмными скалами и бурными волнами.', 'rooms': ['Комната отдыха', 'Кухня', 'Санузел', 'Спальня', 'Комната наблюдения'], 'loot': ['Канистры для воды', 'Спальные мешки', 'Средства гигиены', 'Канистры для топлива'], 'size': '319 m²', 'time': '5 лет'}, 'cards': {card number: 1: {'profession': ['Архитектор', False], 'biological_characteristics': ['женщина 26 лет, асексуал', False], 'health': ['Легкая анемия', False], 'hobby': ['Катание на роликах', False], 'phobia': ['Демофобия (боязнь толпы)', False], 'character': ['Лояльный', False], 'additional_information': ['Способность находить еду', False], 'knowledge': ['Знание экологии', False], 'baggage': ['Рюкзак', False], 'action_card': ['🛠в разработке🛠', True], 'condition_card': ['🛠в разработке🛠', True]}}}"
    print(G4FFinal().get_final(game_data=test_game_data))