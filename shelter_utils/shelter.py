class Catastrophe:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Card:
    def __init__(self, profession: str, 
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


class Shelter:
    def __init__(self, name: str, description: str, rooms: str, loot:str, size: int, time: int):
        self.name = name
        self.description = description
        self.rooms = rooms
        self.loot = loot
        self.size = size
        self.time = time


class Game:

    def __init__(self, catastrophe: Catastrophe, cards: list[Card], bunker: Shelter):
        self.catastrophe = catastrophe
        self.cards = cards
        