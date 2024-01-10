"""
Weather Forecast GUI

This simple Tkinter-based weather application allows users 
to retrieve real-time weather information for a specified city. 
The application utilizes the OpenWeatherMap API to fetch data 
such as temperature, humidity, wind speed, and pressure.

Instructions:
1. Enter the desired city in the provided input field.
2. Click the "Search" button to fetch and display the current weather information.

Author: Mahmoud Khalil
Date: 13-12-2023
"""

# Import necessary libraries
from tkinter import messagebox
from tkinter import *
import requests
import random

# Function to get weather information from OpenWeatherMap API
def get_weather():
    # Retrieve the city name entered by the user
    city = loc_entry.get().lower()

    # Check if the city name is provided
    if not city:
        messagebox.showinfo("Error", "Please enter a city.")
        return

    with open('OpenWeather_API_Key.txt', 'r') as file:
        api_key = file.read()

    # OpenWeatherMap API endpoint and parameters
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,  # Replace with your API key
        'units': 'metric'
    }

    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(base_url, params=params)
        status = response.status_code

        # Check if the API request was successful (status code 200)
        if status == 200:
            result = response.json()

            # Update GUI labels with weather information
            temp.set("Temperature: " + str(result['main']['temp']) + "°C")
            humidity.set("Humidity: " + str(result['main']['humidity']) + "%")
            wind_speed.set("Wind Speed: " + str(result['wind']['speed']) + "km/h")
            pressure.set("Pressure: " + str(result['main']['pressure']) + "hPa")
            
            # Simulate precipitation data (random value between 0 and 100%)
            precip.set("Precipitation: " + str(random.randint(0, 100)) + "%")

        # If the API request was not successful, display an error message
        else:
            messagebox.showinfo(f"Error {status}", "Unable to make the API request.")

    # Handle exceptions that may occur during the API request
    except requests.exceptions.RequestException as e:
        messagebox.showinfo("Error", "Unable to make the API request.")

# Create a Tkinter window
window = Tk()

# Create frames for input and data display
input_frame = Frame(master=window)
data_frame = Frame(master=window)

# Tkinter variables to store weather information
temp = StringVar(data_frame, value="Temperature: ")
humidity = StringVar(data_frame, value="Humidity: ")
wind_speed = StringVar(data_frame, value="Wind Speed")
pressure = StringVar(data_frame, value="Pressure: ")
precip = StringVar(data_frame, value="Precipitation")

# Create labels, entry, and button widgets
loc_label = Label(master=input_frame, text="Location: ", font="Helvetica 15")
loc_entry = Entry(master=input_frame, width=20)
search_button = Button(master=input_frame, text="Search", command=get_weather)

temp_label = Label(master=data_frame, textvariable=temp, font="Helvetica 15")
humid_label = Label(master=data_frame, textvariable=humidity, font="Helvetica 15")
wind_label = Label(master=data_frame, textvariable=wind_speed, font="Helvetica 15")
pressure_label = Label(master=data_frame, textvariable=pressure, font="Helvetica 15")
precip_label = Label(master=data_frame, textvariable=precip, font="Helvetica 15")

# Pack widgets into the frames
input_frame.pack(side=TOP, anchor='e', padx=18, pady=5)
loc_label.pack(side=LEFT, anchor='e')
loc_entry.pack(side=LEFT, anchor='e', padx=50)
search_button.pack(side=RIGHT, padx=5)

data_frame.pack(anchor='w')
temp_label.pack(padx=(50, ), pady=18)
humid_label.pack(padx=(50, ), pady=18)
wind_label.pack(padx=(50, ), pady=18)
pressure_label.pack(padx=(50, ), pady=18)
precip_label.pack(padx=(50, ), pady=18)

# Start the Tkinter event loop
window.mainloop()
