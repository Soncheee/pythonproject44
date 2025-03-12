# import json
# import random
# from http.client import responses
import os
import requests
from unittest.mock import patch
from dotenv import load_dotenv

load_dotenv("../.env")

# book_info = {"name": "1984", "author": "George Orwell", "genres": ["non fiction", "antiutopia"]}
#
# with open("data.json", "w") as json_file:
#     json.dump(book_info, json_file)


# str_book_info = '{"name": "1984", "author": "George Orwell", "genres": ["non fiction", "antiutopia"]}'
#
# book_info = json.loads(str_book_info)
#
# print(type(book_info))
#
# with open("data.json") as json_file:
#     book_info = json.load(json_file)
#
#     print(type(book_info))

# def generate_users(first_names: list[str], last_names: list[str], cities:list[str]) -> dict:
#
#     while True:
#         user = {
#             "first_name": random.choice(first_names),
#                 "last_name": random.choice(last_names),
#             'age': random.randint(18, 65),
#             "city": random.choice(cities)
#         }
#         yield user
#
# if __name__ == '__main__':
#     cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
#     first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
#     last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']
#
#
#     users = generate_users(first_names, last_names, cities)
#
#     user_group1 = [next(users) for i in range(4)]
#     user_group2 = [next(users) for i in range(6)]
#
#
#     print("User group #1")
#     print(json.dumps(user_group1, indent=4))
#
#     print("User group #2")
#     print(json.dumps(user_group2, indent=4))
#
#
# API_KEY = os.getenv('API_KEY')
#
# def get_coords(city: str) -> tuple:
#     '''Получение координат по названию города'''
#
#     response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
#
#     lat = response.json()[0]['lat']
#     lon = response.json()[0]['lon']
#
#     return lat, lon
#
# def get_weather(lat: float, lon: float) -> str:
#     '''Получение погоды по координатам'''
#
#     response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
#
#     return response.json()['main']['temp']
#
# @patch('requests.get')
# def test_get_weather(mock_get):
#     mock_get.return_value.json.return_value = {'main': {'temp': 1}}
#     assert get_weather(1, 1) == 1
#     mock_get.assert_called_once_with(f'https://api.openweathermap.org/data/2.5/weather?lat=1&lon=1&appid={API_KEY}')
#
#
# if __name__ == "__main__":
#     lat, lon = get_coords("Moscow")
#     print(get_weather(lat, lon))
