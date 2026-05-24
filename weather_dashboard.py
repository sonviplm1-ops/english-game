import tkinter as tk
from tkinter import messagebox, ttk
import requests
import json
import os
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO

# OpenWeatherMap API Configuration
API_KEY = "0ee4a52ca961cbbac5c8a3c1ef7d0814"  # Free API Key (replace with your own)
BASE_URL = "https://api.openweathermap.org/data/2.5"

class WeatherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Dashboard")
        self.root.geometry("900x700")
        self.root.config(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        self.weather_data = None
        self.forecast_data = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#0d47a1", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="🌤️ Weather Dashboard", 
                        font=("Arial", 24, "bold"), bg="#0d47a1", fg="white")
        title.pack(pady=10)
        
        # Search Frame
        search_frame = tk.Frame(header_frame, bg="#0d47a1")
        search_frame.pack(fill="x", padx=20)
        
        tk.Label(search_frame, text="City:", font=("Arial", 10, "bold"), bg="#0d47a1", fg="white").pack(side="left", padx=5)
        
        self.city_entry = tk.Entry(search_frame, font=("Arial", 11), width=30, relief="solid", borderwidth=1)
        self.city_entry.pack(side="left", padx=5)
        self.city_entry.bind('<Return>', lambda e: self.search_weather())
        
        search_btn = tk.Button(search_frame, text="Search", command=self.search_weather,
                              font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=15)
        search_btn.pack(side="left", padx=5)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#1a1a1a")
        content_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Current Weather Frame
        current_frame = tk.LabelFrame(content_frame, text="Current Weather", 
                                     font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white",
                                     relief="solid", borderwidth=1)
        current_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        # Weather Info Grid
        info_frame = tk.Frame(current_frame, bg="#2a2a2a")
        info_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # City Name and Temperature
        city_temp_frame = tk.Frame(info_frame, bg="#2a2a2a")
        city_temp_frame.pack(anchor="w", pady=10)
        
        self.city_label = tk.Label(city_temp_frame, text="Select a city", 
                                  font=("Arial", 20, "bold"), bg="#2a2a2a", fg="white")
        self.city_label.pack(anchor="w")
        
        self.temp_label = tk.Label(city_temp_frame, text="-- °C", 
                                  font=("Arial", 48, "bold"), bg="#2a2a2a", fg="#FFD700")
        self.temp_label.pack(anchor="w")
        
        # Weather Description
        self.description_label = tk.Label(info_frame, text="", 
                                         font=("Arial", 14), bg="#2a2a2a", fg="#87CEEB")
        self.description_label.pack(anchor="w", pady=5)
        
        # Details Grid
        details_frame = tk.Frame(info_frame, bg="#2a2a2a")
        details_frame.pack(fill="x", pady=15)
        
        # Column 1
        col1 = tk.Frame(details_frame, bg="#2a2a2a")
        col1.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        tk.Label(col1, text="Feels Like", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w")
        self.feels_like_label = tk.Label(col1, text="-- °C", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.feels_like_label.pack(anchor="w")
        
        tk.Label(col1, text="Humidity", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w", pady=(10, 0))
        self.humidity_label = tk.Label(col1, text="--%", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.humidity_label.pack(anchor="w")
        
        # Column 2
        col2 = tk.Frame(details_frame, bg="#2a2a2a")
        col2.pack(side="left", fill="both", expand=True, padx=(10, 10))
        
        tk.Label(col2, text="Wind Speed", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w")
        self.wind_label = tk.Label(col2, text="-- m/s", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.wind_label.pack(anchor="w")
        
        tk.Label(col2, text="Pressure", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w", pady=(10, 0))
        self.pressure_label = tk.Label(col2, text="-- hPa", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.pressure_label.pack(anchor="w")
        
        # Column 3
        col3 = tk.Frame(details_frame, bg="#2a2a2a")
        col3.pack(side="left", fill="both", expand=True, padx=(10, 0))
        
        tk.Label(col3, text="Visibility", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w")
        self.visibility_label = tk.Label(col3, text="-- km", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.visibility_label.pack(anchor="w")
        
        tk.Label(col3, text="UV Index", font=("Arial", 10), bg="#2a2a2a", fg="#999").pack(anchor="w", pady=(10, 0))
        self.uv_label = tk.Label(col3, text="--", font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white")
        self.uv_label.pack(anchor="w")
        
        # 5-Day Forecast Frame
        forecast_frame = tk.LabelFrame(content_frame, text="5-Day Forecast", 
                                      font=("Arial", 14, "bold"), bg="#2a2a2a", fg="white",
                                      relief="solid", borderwidth=1)
        forecast_frame.pack(fill="x")
        
        self.forecast_inner = tk.Frame(forecast_frame, bg="#2a2a2a")
        self.forecast_inner.pack(fill="x", padx=15, pady=15)
        
        # Status Label
        status_frame = tk.Frame(self.root, bg="#1a1a1a")
        status_frame.pack(fill="x", padx=15, pady=5)
        
        self.status_label = tk.Label(status_frame, text="Ready to search", 
                                    font=("Arial", 9), bg="#1a1a1a", fg="#999")
        self.status_label.pack(anchor="w")
    
    def search_weather(self):
        """Search for weather data"""
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Empty City", "Please enter a city name!")
            return
        
        self.status_label.config(text="⟳ Fetching weather data...")
        self.root.update()
        
        try:
            # Get current weather
            current_url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(current_url, timeout=5)
            response.raise_for_status()
            self.weather_data = response.json()
            
            # Get forecast
            forecast_url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(forecast_url, timeout=5)
            response.raise_for_status()
            self.forecast_data = response.json()
            
            self.display_weather()
            self.status_label.config(text=f"✓ Weather updated at {datetime.now().strftime('%H:%M:%S')}")
            
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Failed to connect to weather service!")
            self.status_label.config(text="✗ Connection error")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                messagebox.showerror("City Not Found", "City not found! Please try another.")
            else:
                messagebox.showerror("API Error", f"Weather service error: {response.status_code}")
            self.status_label.config(text="✗ City not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            self.status_label.config(text="✗ Error fetching data")
    
    def display_weather(self):
        """Display weather information"""
        if not self.weather_data:
            return
        
        # Current weather
        data = self.weather_data
        
        # Update labels
        city = f"{data['name']}, {data['sys'].get('country', '')}"
        self.city_label.config(text=city)
        
        temp = int(data['main']['temp'])
        self.temp_label.config(text=f"{temp}°C")
        
        description = data['weather'][0]['description'].capitalize()
        self.description_label.config(text=description)
        
        feels_like = int(data['main']['feels_like'])
        self.feels_like_label.config(text=f"{feels_like}°C")
        
        humidity = data['main']['humidity']
        self.humidity_label.config(text=f"{humidity}%")
        
        wind = data['wind']['speed']
        self.wind_label.config(text=f"{wind:.1f} m/s")
        
        pressure = data['main']['pressure']
        self.pressure_label.config(text=f"{pressure} hPa")
        
        visibility = data['visibility'] / 1000
        self.visibility_label.config(text=f"{visibility:.1f} km")
        
        # UV Index (from weather data if available)
        uv_index = data.get('clouds', {}).get('all', 'N/A')
        self.uv_label.config(text=str(uv_index) if uv_index != 'N/A' else "N/A")
        
        # Display forecast
        self.display_forecast()
    
    def display_forecast(self):
        """Display 5-day forecast"""
        if not self.forecast_data:
            return
        
        # Clear previous forecast
        for widget in self.forecast_inner.winfo_children():
            widget.destroy()
        
        # Get forecast data at noon each day
        forecasts = {}
        for item in self.forecast_data['list']:
            date = item['dt_txt'].split()[0]
            time = item['dt_txt'].split()[1]
            
            if time == '12:00:00' and date not in forecasts:
                forecasts[date] = item
        
        # Display up to 5 days
        forecast_items = list(forecasts.items())[:5]
        
        for date, item in forecast_items:
            day_frame = tk.Frame(self.forecast_inner, bg="#333333", relief="solid", borderwidth=1)
            day_frame.pack(side="left", fill="both", expand=True, padx=5, pady=0)
            
            # Date
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            day_name = date_obj.strftime("%a")
            date_str = date_obj.strftime("%m/%d")
            
            tk.Label(day_frame, text=f"{day_name}", font=("Arial", 10, "bold"), 
                    bg="#333333", fg="#FFD700").pack(pady=(8, 0))
            tk.Label(day_frame, text=f"{date_str}", font=("Arial", 9), 
                    bg="#333333", fg="#999").pack()
            
            # Temperature
            temp = int(item['main']['temp'])
            tk.Label(day_frame, text=f"{temp}°C", font=("Arial", 12, "bold"), 
                    bg="#333333", fg="white").pack(pady=5)
            
            # Description
            desc = item['weather'][0]['main']
            tk.Label(day_frame, text=desc, font=("Arial", 8), 
                    bg="#333333", fg="#87CEEB", wraplength=80).pack(pady=(0, 5))
            
            # Humidity
            humidity = item['main']['humidity']
            tk.Label(day_frame, text=f"💧 {humidity}%", font=("Arial", 8), 
                    bg="#333333", fg="#87CEEB").pack(pady=(0, 8))

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDashboard(root)
    
    # Auto-load default city
    root.after(500, lambda: app.city_entry.insert(0, "Hanoi") or app.search_weather())
    
    root.mainloop()
