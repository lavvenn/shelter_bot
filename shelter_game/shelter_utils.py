import random

import characteristics
import shelters

from shelter import *

def _get_random_bio_characteristics() -> str:
    age = random.randint(18, 80)
    gender = random.choice(["мужчина", "женщина"])
    orientation = random.choice(["гетеро", "гомо", "би", "asexual"])

    if gender == "мужчина":
        return f"мужчина {age} лет, {orientation}"
    if gender == "женщина":
        ret_str = f"женщина {age} лет, {orientation}"
        if random.randint(0,100) >= 50:
            ret_str += " беременная"
        return ret_str 
    else:
        return ret_str

def _get_random_shelter() -> Shelter:  
    shelter_name = random.choice(list(shelters.shelters_dict.keys()))
    shelter_discription = shelters.shelters_dict[shelter_name]
    rooms = random.choice(shelters.rooms_list)
    number_of_items = random.randint(1,4)
    items = [random.choice(shelters.items) for _ in range(number_of_items)]
    size = f"{random.randint(100,550)} m²"
    time = f"{random.randint(1,5)} лет"

    return Shelter(name=shelter_name, description=shelter_discription, rooms=rooms, loot=items, size=size, time=time)

def _get_random_catastrophe() -> Catastrophe:
    catastrophe_name = random.choice(list(shelters.catastrophes.keys()))

    return Catastrophe(name=catastrophe_name, description=shelters.catastrophes[catastrophe_name])


def get_random_game(name: str, number_of_cards: int) -> Game:

    catastrophe = _get_random_catastrophe()

    cards = [Card(
        number=i,
        profession=random.choice(characteristics.professions),
        bio_characteristics= _get_random_bio_characteristics(),
        health=random.choice(characteristics.health),
        hobby=random.choice(characteristics.hobbies),
        phobia=random.choice(characteristics.phobias),
        character=random.choice(characteristics.character),
        additional_information=random.choice(characteristics.additional_information),
        knowledge=random.choice(characteristics.knowledge),
        baggage=random.choice(characteristics.baggages),
        action_card="чтото",
        condition_card="чтото",
    )
        for i  in range (number_of_cards) ]
    
    shelter = _get_random_shelter()

    return Game(name=name, catastrophe=catastrophe, cards=cards, shelter=shelter)