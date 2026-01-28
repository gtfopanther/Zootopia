import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns a list of animals (list of dicts).
    """
    if not animal_name or not API_KEY:
        return []

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()
    return data if isinstance(data, list) else []
