import tkinter as tk
import requests

# OpenWeatherMap API endpoint and API key
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "e91d6cd84fdd054b307d3a3fa8be4f9c"

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        
        # Create and position widgets
        self.location_label = tk.Label(master, text="Location:")
        self.location_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.location_entry = tk.Entry(master)
        self.location_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.weather_label = tk.Label(master, text="")
        self.weather_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        
    def get_weather(self):
        location = self.location_entry.get()
        
        # Make API request
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        response = requests.get(API_ENDPOINT, params=params)
        
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"].capitalize()
            
            # Update weather label
            self.weather_label.config(text=f"Temperature: {temperature}°C, {description}")
        else:
            self.weather_label.config(text="ERROR: Enter Valid Location")
            
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()