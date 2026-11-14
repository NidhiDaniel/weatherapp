import requests

city=input("Enter city name: ")


key="b13e77cd2cfca6657d2b39d6d9ab62a3"
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
weather_data=requests.get(url).json()

if weather_data["cod"]=="404":
    print("City not found.")
else:
    weather=weather_data["weather"][0]["main"]
    temperature=weather_data["main"]["temp"]
    print(f"Weather in {city}: {weather}")
    print(f"Temperature in {city}: {temperature}K")