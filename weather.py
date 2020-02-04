import requests

city = input("Enter the city's name: ")
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=' 
url = api_address + city + "&appid=b4191f92e8287bce468438b5c66824f8"
json_data = requests.get(url).json()
#print(json_data)

#formatted_data = json_data['weather'][0]['main'] + "\n" + json_data['weather'][0]['description']

#print(formatted_data)

temperatureKelvin = json_data['main']['temp'] 
temp = (temperatureKelvin - 273) * 1.8 + 32
print(temp)
print(json_data['weather'][0]['main'] + " in " + city + ", with a temperature of %.2f F" %temp)
