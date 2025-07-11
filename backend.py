from dotenv import load_dotenv
import os
import requests
import getpass

load_dotenv()

route = os.getenv("Route")

def Auth(user,password,route = route):
    url = f"{route}/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": user,
        "password": password,
        "client_id":2,
        "client_secret":"wWEI9VQskScwjWhgRH6cgDqG0tw2G7GEqpKPQJj2",
        "grant_type":"password"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.status_code,response.json()
    else:
        raise Exception(f"Authentication failed: {response.status_code} - {response.text}")
    
def point(Token,dia):
    url = f"{ROUTE}/api/mobile/time/cards"
    headers = {"Authorization": f"Bearer {Token}", "Content-Type": "application/json"}
    data = {
          f"datetime_event":{dia},
          "geolocation":"-19.9213662,-43.9347277" ,
          "browserGeolocation":"-19.9213662,-43.9347277",
          "workplace_id":5620,
          "timecard_hour_type_id":2}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Point registered successfully")
    else:
        raise Exception(f"Failed to register point: {response.status_code} - {response.text}")
    
        