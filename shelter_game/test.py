import random

from shelter import Shelter, Card, Game, Catastrophe

import characteristics

catastrophe = Catastrophe(
    name="ядерная война",
    description="произошла война"
)

shelter = Shelter(
    name="палатка",
    description="палатка",
    rooms="1",
    loot="1",
    size="1",
    time="1"
)

cards = [Card(
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
    condition_card="чтото"
) for i in range (5) ]


# print(cards[1])


game = Game(
    name="игра",
    catastrophe=catastrophe,
    cards=cards,
    shelter=shelter
)


if __name__ == "__main__":
    print(game.get_catastrophe())
    print(game.get_shelter())
    print(game.get_cards())
    print(cards)

else:
    print(f"вы импортирывали модуль который не должны были --> {__name__}")



#XXX это для теста карт
# while True:
#      card_num = int(input("напиши номер карты"))
#      print(cards[card_num - 1].get_all_characteristics())
