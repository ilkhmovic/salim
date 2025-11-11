import requests

api = "c91e236c50c6b3e07f5185b762a3e228"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

response = requests.get(url)
data = response.json()
for i in data:
    print(i)

