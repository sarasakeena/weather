import requests

BASE_URL = "http://127.0.0.1:8000"  # Replace if deployed elsewhere

def get_weather(city: str):
    url = f"{BASE_URL}/weather"
    params = {"city": city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print(f"Error: {data['error']}")
        else:
            print(f"Weather in {data['city']}:")
            print(f"  Temperature: {data['temperature_C']}°C")
            print(f"  Condition: {data['weather']}")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
