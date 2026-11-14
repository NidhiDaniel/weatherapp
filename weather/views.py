from django.shortcuts import render

# Create your views here.
import os
import requests



def home(request):

    weather_data = None
    error = None

    if request.method == "POST":

        city = request.POST.get("city", "").strip()

        if not city:
            error = "Please enter a city name."

        else:
            api_key = os.environ.get("OPENWEATHER_API_KEY")

            if not api_key:
                error = "Weather API key is not configured."

            else:
                url = "https://api.openweathermap.org/data/2.5/weather"

                params = {
                    "q": city,
                    "appid": api_key,
                    "units": "metric"
                }

                try:
                    response = requests.get(
                        url,
                        params=params,
                        timeout=10
                    )

                    if response.status_code == 200:

                        data = response.json()

                        weather_data = {
                            "city": data["name"],
                            "country": data["sys"]["country"],
                            "temperature": data["main"]["temp"],
                            "humidity": data["main"]["humidity"],
                            "wind": data["wind"]["speed"],
                            "description": data["weather"][0]["description"],
                            "icon": data["weather"][0]["icon"]
                        }

                    elif response.status_code == 404:
                        error = "City not found."

                    else:
                        error = "Unable to retrieve weather information."

                except requests.RequestException:
                    error = "Weather service is temporarily unavailable."

    return render(
        request,
        "weather/index.html",
        {
            "weather": weather_data,
            "error": error
        }
    )