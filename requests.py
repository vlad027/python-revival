import requests

try:
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")