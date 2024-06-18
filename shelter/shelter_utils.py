import random
import json



from shelter.game.shelter import *

with open("shelter/characteristics.json") as c, open("shelter/shelters.json") as s:
    characteristics = json.load(c)
    shelters = json.load(s)




def _get_random_bio_characteristics() -> str:
    age = random.randint(18, 80)
    gender = random.choice(["мужчина", "женщина"])
    orientation = random.choice(["гетеро", "гомо", "би", "асексуал"])

    if gender == "мужчина":
        return f"мужчина {age} лет, {orientation}"
    if gender == "женщина":
        ret_str = f"женщина {age} лет, {orientation}"
        if random.randint(0, 100) >= 50:
            ret_str += " беременная"
        return ret_str
    else:
        return str(ret_str)


def get_random_card(card_numder: int, user_id: int, user_name: str) -> Card:
    return Card(
        user_id=user_id,
        number=card_numder,
        name=user_name,
        profession=[random.choice(characteristics["professions"]), False],
        bio_characteristics=[_get_random_bio_characteristics(), False],
        health=[random.choice(characteristics["health"]), False],
        hobby=[random.choice(characteristics["hobbies"]), False],
        phobia=[random.choice(characteristics["phobias"]), False],
        character=[random.choice(characteristics["character"]), False],
        additional_information=[
            random.choice(characteristics["additional_information"]),
            False,
        ],
        knowledge=[random.choice(characteristics["knowledge"]), False],
        baggage=[random.choice(characteristics["baggages"]), False],
        action_card=["🛠в разработке🛠", True],
        condition_card=["🛠в разработке🛠", True],
    )


def _get_random_shelter() -> Shelter:
    shelter_name = random.choice(list(shelters["shelters_dict"].keys()))
    shelter_discription = shelters["shelters_dict"][shelter_name]
    rooms = random.choice(shelters["rooms_list"])
    number_of_items = random.randint(1, 5)
    items = [random.choice(shelters["items"]) for _ in range(number_of_items)]
    size = f"{random.randint(100,550)} m²"
    time = f"{random.randint(5,15)} лет"

    return Shelter(
        name=shelter_name,
        description=shelter_discription,
        rooms=rooms,
        loot=items,
        size=size,
        time=time,
    )


def _get_random_catastrophe() -> Catastrophe:
    catastrophe_name = random.choice(list(shelters["catastrophes"].keys()))

    return Catastrophe(
        name=catastrophe_name, description=shelters["catastrophes"][catastrophe_name]
    )


def get_random_game(name: str) -> Game:

    catastrophe = _get_random_catastrophe()

    shelter = _get_random_shelter()

    return Game(name=name, catastrophe=catastrophe, shelter=shelter)


def show_characteristic(characteristic: list) -> str:
    if characteristic[1] == True:
        return characteristic[0]
    else:
        return "#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣"


def show_open_or_not(characteristic: list) -> str:
    if characteristic[1] == True:
        return "🟢"
    else:
        return "🔴"


def print_card(card: Card) -> str:

    characteristics_list = [
        characteric[0]
        for characteric in card.get_all_characteristics().values()
        if characteric[1] == True
    ]

    text = f"""
**Карточка игрока номер:**{card.number}

**Биологические характеристики:** {show_characteristic(card.characteristics["biological_characteristics"])}

**Профессия:** {show_characteristic(card.characteristics["profession"])}

**Здоровье:** {show_characteristic(card.characteristics["health"])}

**Хобби:** {show_characteristic(card.characteristics["hobby"])}

**Фобия:** {show_characteristic(card.characteristics["phobia"])}

**Характер:** {show_characteristic(card.characteristics["character"])}

**Дополнительная информация:** {show_characteristic(card.characteristics["additional_information"])}

**Знания:** {show_characteristic(card.characteristics["knowledge"])}

**Багаж:** {show_characteristic(card.characteristics["baggage"])}

**Деятельность:** {show_characteristic(card.characteristics["action_card"])}

**Состояние:** {show_characteristic(card.characteristics["condition_card"])}
"""
    return text


def print_my_card(card: Card) -> str:

    text = f"""
**Карточка игрока номер:**{card.number}

{show_open_or_not(card.characteristics["biological_characteristics"])}**Биологические характеристики:** {card.characteristics["biological_characteristics"][0]}

{show_open_or_not(card.characteristics["profession"])}**Профессия:** {card.characteristics["profession"][0]}

{show_open_or_not(card.characteristics["health"])}**Здоровье:** {card.characteristics["health"][0]}

{show_open_or_not(card.characteristics["hobby"])}**Хобби:** {card.characteristics["hobby"][0]}

{show_open_or_not(card.characteristics["phobia"])}**Фобия:** {card.characteristics["phobia"][0]}

{show_open_or_not(card.characteristics["character"])}**Характер:** {card.characteristics["character"][0]}

{show_open_or_not(card.characteristics["additional_information"])}**Дополнительная информация:** {card.characteristics["additional_information"][0]}

{show_open_or_not(card.characteristics["knowledge"])}**Знания:** {card.characteristics["knowledge"][0]}

{show_open_or_not(card.characteristics["baggage"])}**Багаж:** {card.characteristics["baggage"][0]}

{show_open_or_not(card.characteristics["action_card"])}**Деятельность:** {card.characteristics["action_card"][0]}

{show_open_or_not(card.characteristics["condition_card"])}**Состояние:** {card.characteristics["condition_card"][0]}
"""

    return text

def print_shelter(shelter: Shelter) -> str:
    text = f"""
**Название бункера:** {shelter.name}

**Описание:** {shelter.description}

**Комнаты:** {shelter.rooms}

**Предметы:** {shelter.loot}

**Размер:** {shelter.size}
**Время:** {shelter.time}
"""
    return text

def print_catastrophe(catastrophe: Catastrophe) -> str:
    text = f"""
**катастрофа:** {catastrophe.name}

**Описание:** {catastrophe.description}
"""
    return text
