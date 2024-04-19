class Catastrophe:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Card:
    def __init__(self,
                 number: int,
                 profession: str, 
                 bio_characteristics: str, 
                 health: str, 
                 hobby: str, 
                 phobia: str,
                 character: str, 
                 additional_information: str,
                 knowledge: str,
                 baggage: str,
                 action_card: str,
                 condition_card: str):
        
        self.number = number
        self.profession = profession
        self.bio_characteristics = bio_characteristics
        self.health = health
        self.hobby = hobby
        self.phobia = phobia
        self.character = character
        self.additional_information = additional_information
        self.knowledge = knowledge
        self.baggage = baggage
        self.action_card = action_card
        self.condition_card = condition_card


    def get_all_characteristics(self):
        return {"номер": self.number,
                "професия": self.profession,
                "био" : self.bio_characteristics,
                "здоровье" : self.health,
                "хобби" : self.hobby,
                "фобия" : self.phobia,
                "характер" : self.character,
                "доп. инфо" : self.additional_information,
                "знания" : self.knowledge,
                "багаж" : self.baggage,
                "действие" : self.action_card,
                "условие" : self.condition_card
                }
    


class Shelter:
    def __init__(self, name: str, description: str, rooms: str, loot:str, size: int, time: int):
        self.name = name
        self.description = description
        self.rooms = rooms
        self.loot = loot
        self.size = size
        self.time = time


class Game:

    def __init__(self, catastrophe: Catastrophe, cards: list[Card], shelter: Shelter):
        self.catastrophe = catastrophe
        self.cards = cards


    def get_cards(self):
        pass

    def get_catastrophe(self):

        catastrophe = self.catastrophe

        return {"name": catastrophe.name, "description": catastrophe.description}
    
    def get_shelter(self):

        shelter = self.shelter

        return {"name": shelter.name, "description": shelter.description, "rooms": shelter.rooms, "loot":shelter.loot, "size":shelter.size, "time":shelter.time}