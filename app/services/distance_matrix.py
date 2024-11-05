import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")
ORS_URL = "https://api.openrouteservice.org/v2/matrix/driving-car"

def get_distance_matrix(locations):
    headers = {"Authorization": ORS_API_KEY, "Content-Type": "application/json"}
    data = {"locations": locations, "metrics": ["distance", "duration"]}
    response = requests.post(ORS_URL, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch distance matrix")
    

# Sample usage test in the same file
locations = [[-3.7038, 40.4168], [-0.3757, 39.4699]]  # Sample locations
print(get_distance_matrix(locations))
