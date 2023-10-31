import requests

from datetime import datetime as dt
from decouple import config

APP_ID = config("APP_ID")
APP_KEY = config("APP_KEY")
SPREADSHEET = config("SHEETY_SPREADSHEET")
SHEET_TOKEN = config("SHEETY_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

spreadsheet_endpoint = SPREADSHEET

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

user_query = input("Which exercises were performed? ")

exercise_sets = int(input("How many sets of the exercise was performed?"))

paramaters = {
    "query": user_query,
    "gender": "male",
    "weight_kg": 86,
    "height_cm": 175,
    "age": 38
}

response = requests.post(
    url = exercise_endpoint,
    json = paramaters,
    headers = exercise_headers
)

response.raise_for_status()

query_response = response.json()

exercise_calories = query_response["exercises"][0]["nf_calories"]
exercise_duration = query_response["exercises"][0]["duration_min"]
exercise_name = query_response["exercises"][0]["name"]

now = dt.now()

trainings = {
    "training" : {
        "date": now.strftime("%d/%m/%Y"),
        "sets": exercise_sets,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

spreadsheet_headers = {
    "Authorization": SHEET_TOKEN
}

spreadsheet_response = requests.post(
    url = SPREADSHEET,
    headers = spreadsheet_headers,
    json = trainings
)