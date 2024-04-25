class Catastrophe:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Card:
    def __init__(self,
                 user_id: int,
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
        
        self.user_id = user_id
        self.number = number + 1
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


    def __str__(self):
        return f"card number: {self.number}"
    
    __repr__ = __str__


    def get_all_characteristics(self)->dict:
        return {"number": self.number,
                "profession": self.profession,
                "biological characteristics": self.bio_characteristics,
                "health": self.health,
                "hobby": self.hobby,
                "phobia": self.phobia,
                "character": self.character,
                "additional information": self.additional_information,
                "knowledge": self.knowledge,
                "baggage": self.baggage,
                "action": self.action_card,
                "condition": self.condition_card
                }
    


class Shelter:
    def __init__(self, name: str, description: str, rooms: list[str], loot:list[str], size: int, time: int):
        self.name = name
        self.description = description
        self.rooms = rooms
        self.loot = loot
        self.size = size
        self.time = time


class Game:

    def __init__(self, name: str, catastrophe: Catastrophe, shelter: Shelter):
        self.name = name
        self.catastrophe = catastrophe
        self.cards = []
        self.shelter = shelter

    def __str__(self) -> str:
        return f"game: {self.name}\n"
    __repr__ = __str__

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_users_id(self)->list[int]:
        return [card.user_id for card in self.cards]

    def get_cards(self)->list[Card]:
        return self.cards

    def get_catastrophe(self)-> dict:

        catastrophe = self.catastrophe

        return {"name": catastrophe.name, "description": catastrophe.description}
    
    def get_shelter(self)-> dict:

        shelter = self.shelter

        return {"name": shelter.name, "description": shelter.description, "rooms": shelter.rooms, "loot":shelter.loot, "size":shelter.size, "time":shelter.time}