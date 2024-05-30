from final import Final

from g4f.client import Client
from g4f.Provider import Liaobots


preprompt = """
You are writing the outcome of events for the ending of the board game "Bunker";
your task, using the data obtained, is to describe the further history of the characters who entered the bunker,
write whether they survived or not, and come up with different interesting situations using facts
from the received data. it is necessary to take into account the number of players, their conditions, the bunker, the disaster. Your answer must contain only the general ending for all players and nothing extra (EXCLUSIVELY GENERAL FINALE) without a description of the game and players, without a description of the ending of each player.
"""

test_game_data = """
{'catastrophe': {'name': 'Global radiation catastrophe', 'description': 'Simultaneous releases of radiation in all parts of the planet, causing mass mutations and mortality.'}, 'shelter': {'name': 'Shady island', 'description': 'Located on a small island, surrounded by dense thickets and rocks.', 'rooms': ['Bedroom', 'Kitchen', 'Bathroom', 'Observation Room', 'Warehouse'], 'loot ': ['Refrigerator or freezer', 'Water tank', 'Electric generator', 'Chess or checkers'], 'size': '341 m²', 'time': '14 years'}, 'cards': {card number: 1: {'profession': ['Forester', True], 'biological_characteristics': ['male 65 years old, hetero', False], 'health': ['Low blood pressure', False], ' hobby': ['Gardening', False], 'phobia': ['Amichetophobia (fear of dust)', True], 'character': ['Sociable', False], 'additional_information': ['Cultural knowledge', True ], 'knowledge': ['Knowledge of Zoology', False], 'baggage': ['Tablets for water purification', False], 'action_card': ['🛠in development🛠', True], 'condition_card': [ '🛠in development🛠', True]}, card number: 2: {'profession': ['Programmer', False], 'biological_characteristics': ['woman 22 years old, hetero pregnant', False], 'health': ['Chronic heart disease', True], 'hobby': ['Roller skating', False], 'phobia': ['Claustrophobia (fear of enclosed spaces)', False], 'character': ['Impulsive', False], 'additional_information': ['Ability to make a fire', False], 'knowledge': ['Knowledge of Eastern philosophies', False], 'baggage': ['Kettle', True], 'action_card': ['🛠 under development🛠', True], 'condition_card': ['🛠under development🛠', True]}, card number: 3: {'profession': ['Linguist', True], 'biological_characteristics': ['woman 40 years, bi', True], 'health': ['Migraines', True], 'hobby': ['Roller skating', True], 'phobia': ['Agoraphobia (fear of open spaces)', True] , 'character': ['Emotionally unstable', True], 'additional_information': ['Ability to find food', True], 'knowledge': ['Art knowledge', True], 'baggage': ['Map of the area' , True], 'action_card': ['🛠under development🛠', True], 'condition_card': ['🛠under development🛠', True]}, card number: 4: {'profession': ['Electrician', False], 'biological_characteristics': ['48 year old male, bi', False], 'health': ['Varicose veins', False], 'hobby': ['Snowboarding', False], 'phobia': [ 'Chionophobia (fear of snow)', False], 'character': ['Introvert', False], 'additional_information': ['Information technology', False], 'knowledge': ['Fire safety knowledge', False], 'baggage': ['Flashlight', False], 'action_card': ['🛠under development🛠', True], 'condition_card': ['🛠under development🛠', True]}}}"""

class G4FFinal(Final):
    client = Client(provider=Liaobots)

    def get_final(self,game_data:str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"ADMIN","content":preprompt},
                {   
                    "role": "user",
                    "content": game_data
                }
            ]
        )
        return response.choices[0].message.content
    
    def get_character_final(self,game_data:str,character_id:int):
        pass
    

if __name__ == "__main__":
    print(G4FFinal().get_final(game_data=test_game_data))