import random

from shelter_utils import shelter, characteristics

games = [shelter.Game(
    name=f"игра {i}",
    catastrophe=shelter.Catastrophe(
        name="ядерная война",
        description="произошла война"
    ),
    cards = [shelter.Card(
    number=i,
    profession=random.choice(characteristics.professions),
    bio_characteristics=random.choice(characteristics.biological_characteristics),
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
    for i  in range (5) ],
    shelter=shelter.Shelter(
    name="палатка",
    description="палатка",
    rooms="1",
    loot="1",
    size="1",
    time="1")

) for i in range(10)]

print(games)
print(games[1].get_card_names()[0].get_all_characteristics())
print(games[1].get_card_names())
print(games[2].get_shelter())
print(games[3].get_shelter())