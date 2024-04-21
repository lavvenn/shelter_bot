import random

import characteristics

from shelter import *

def _get_random_bio_characteristics() -> str:
    age = random.randint(1, 100)
    gender = random.choice(["мужчина", "женщина"])
    orientation = random.choice(["гетеро", "гомо", "би", "а"])

    if gender == "мужчина":
        return f"мужчина {age} лет, {orientation}"
    if gender == "женщина":
        return f"женщина {age} лет, {orientation}, {random.choice(['беременная', ''])}"


def get_random_game(name: str) -> Game:

    catastrophe = Catastrophe(
        name="ядерная война",
        description="произошла война"
    )

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
        for i  in range (5) ]
    
    shelter = Shelter(
        name="палатка",
        description="палатка",
        rooms="1",
        loot="1",
        size="1",
    )

    return Game(name=name, catastrophe=catastrophe, cards=cards, shelter=shelter)