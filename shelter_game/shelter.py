class Catastrophe:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Card:
    def __init__(
        self,
        user_id: int,
        number: int,
        name: str,
        profession: list[str, bool],
        bio_characteristics: list[str, bool],
        health: list[str, bool],
        hobby: list[str, bool],
        phobia: list[str, bool],
        character: list[str, bool],
        additional_information: list[str, bool],
        knowledge: list[str, bool],
        baggage: list[str, bool],
        action_card: list[str, bool],
        condition_card: list[str, bool],
    ):
        self.user_id = user_id
        self.number = number + 1

        self.name = name

        self.characteristics = {
            "profession": profession,
            "biological_characteristics": bio_characteristics,
            "health": health,
            "hobby": hobby,
            "phobia": phobia,
            "character": character,
            "additional_information": additional_information,
            "knowledge": knowledge,
            "baggage": baggage,
            "action_card": action_card,
            "condition_card": condition_card,
        }

        self.kiсked = False

        self.online = True

    def __str__(self):
        return f"card number: {self.number}"

    __repr__ = __str__

    def leave(self):
        self.online = False

    def join(self):
        self.online = True

    def open_characteristic(self, characteristic: str):
        try:
            self.characteristics[characteristic][1] = True
            return f"Вы открыли характеристику {characteristic}"
        except:
            return f"Характеристика {characteristic} не существует"

    def get_closed_characteristic(self) -> list[str]:
        return [key for key, value in self.characteristics.items() if value[1] == False]

    def get_all_characteristics(self) -> dict:
        return {key: value for key, value in self.characteristics.items()}


class Shelter:
    def __init__(
        self,
        name: str,
        description: str,
        rooms: list[str],
        loot: list[str],
        size: int,
        time: int,
    ):
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
        self.started = False

    def __str__(self) -> str:
        return f"game: {self.name}\n"

    __repr__ = __str__

    def start(self):
        self.started = True

    def add_card(self, card: Card):
        self.cards.append(card)

    def kick_user(self, card_id: int):
        self.cards[card_id].kiсked = True

    def reborn_user(self, card_id: int):
        self.cards[card_id].kiсked = False

    def get_users_id(self) -> list[int]:
        return [card.user_id for card in self.cards]

    def get_cards(self) -> list[Card]:
        return self.cards

    def get_catastrophe(self) -> dict:

        catastrophe = self.catastrophe

        return {"name": catastrophe.name, "description": catastrophe.description}

    def get_shelter(self) -> dict:

        shelter = self.shelter

        return {
            "name": shelter.name,
            "description": shelter.description,
            "rooms": shelter.rooms,
            "loot": shelter.loot,
            "size": shelter.size,
            "time": shelter.time,
        }

    def get_card_by_user_id(self, user_id: int) -> Card | str:
        for card in self.cards:
            if card.user_id == user_id:
                return card
        else:
            return "нет карты у пользователя с таким id"
        
    def get_survivors(self) -> list[Card]:
        return [survivor for survivor in self.cards if not survivor.kiсked]
        
    def get_final(self):
        final = {
            "catastrophe": self.get_catastrophe(),
            "shelter": self.get_shelter(),
            "cards": {card:card.characteristics for card in self.get_survivors()},
        }
        return str(final)
