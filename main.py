# import the requests library to make HTTP requests
import requests

# set the API key and base URL for the OpenWeatherMap API
API_KEY = "YOUR API KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# prompt the user to enter a city name
city = input("Enter a city name: ")

# construct the request URL with the user's input and API key
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# send an HTTP GET request to the API with the constructed URL
response = requests.get(request_url)

# if the response status code is 200 (OK), process the data
if response.status_code == 200:

    # extract the JSON data from the response
    data = response.json()

    # extract the weather description from the JSON data
    weather = data['weather'][0]['description']
    print("Weather:", weather)

    # extract the temperature from the JSON data and convert it to Celsius
    temperature = round(data["main"]["temp"] - 272.15, 3)
    print("Temperature:", temperature, "celsius")

# if the response status code is not 200, print an error message with the status code
else:
    print("Error {} occurred.".format(response.status_code))
