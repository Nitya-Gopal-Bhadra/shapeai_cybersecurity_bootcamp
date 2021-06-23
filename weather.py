import requests

from datetime import datetime

api_key = 'ec422968528dbbd2290aca8c93002d1b'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

#creating the text file
fh=open('weather_in_text_file.txt','w+')#fh is File handler variable

# writing in the text file
fh.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
fh.write("\n-------------------------------------------------------------")
fh.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
fh.write("\nCurrent weather desc  : {}".format(weather_desc))
fh.write("\nCurrent Humidity      : {} %".format(hmdt))
fh.write("\nCurrent wind speed    : {}kmph".format(wind_spd))

fh.close()