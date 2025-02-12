from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
)

test_game_data = "{'catastrophe': {'name': 'Глобальная эпидемия плесени2', 'description': 'Интенсивный рост плесени по всему миру, приводящий к разрушению имущества и риску для здоровья.'}, 'shelter': {'name': 'Мрачный утес', 'description': 'Расположен на берегу, отличается своими тёмными скалами и бурными волнами.', 'rooms': ['Комната отдыха', 'Кухня', 'Санузел', 'Спальня', 'Комната наблюдения'], 'loot': ['Канистры для воды', 'Спальные мешки', 'Средства гигиены', 'Канистры для топлива'], 'size': '319 m²', 'time': '5 лет'}, 'cards': {card number: 1: {'profession': ['Архитектор', False], 'biological_characteristics': ['женщина 26 лет, асексуал', False], 'health': ['Легкая анемия', False], 'hobby': ['Катание на роликах', False], 'phobia': ['Демофобия (боязнь толпы)', False], 'character': ['Лояльный', False], 'additional_information': ['Способность находить еду', False], 'knowledge': ['Знание экологии', False], 'baggage': ['Рюкзак', False], 'action_card': ['🛠в разработке🛠', True], 'condition_card': ['🛠в разработке🛠', True]}}}"

preprompt = """
You are writing the outcome of events for the ending of the board game "Bunker";
your task, using the data obtained, is to describe the further history of the characters who entered the bunker,
write whether they survived or not, and come up with different interesting situations using facts
from the received data. it is necessary to take into account the number of players, their condition, bunker, disaster. Your answer should contain only the general ending for all players and nothing extra (EXCLUSIVELY GENERAL ENDING) without a description of the game and players, without describing the ending of each player. But your answer must take into account all factors, i.e. the characteristics of each player, bunker, disaster, duration of stay."""


completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="google/gemini-2.0-flash-lite-preview-02-05:free",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": preprompt
        },
        {
            "type": "text",
            "text": test_game_data
        }
      ]
    }
  ]
)
print(completion.choices[0].message.content)