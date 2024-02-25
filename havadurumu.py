import tkinter as tk
from PIL import Image, ImageTk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "38ddfa48fc3d4d2222f95a4eaf2bd909"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:
        temperature_label.config(text=f"Sıcaklık: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Nem Oranı: {weather_data['main']['humidity']}%")
        wind_label.config(text=f"Rüzgar Hızı: {weather_data['wind']['speed']} m/s")
        description_label.config(text=f"Hava Durumu: {weather_data['weather'][0]['description']}")
    else:
        temperature_label.config(text="Hava durumu bilgileri alınamadı.")
        humidity_label.config(text="")
        wind_label.config(text="")
        description_label.config(text="")


window = tk.Tk()
window.title("Hava Durumu Programı")
window.geometry("900x800")

# Arka plan resmi
background_image = Image.open("background_image.jpg")
background_image = background_image.resize((900, 800))
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Şehir giriş kutusu ve Buton
city_label = tk.Label(window, text="Şehir Adı:", bg="white", font=("Arial", 12))
city_label.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.05)

city_entry = tk.Entry(window, bg="white", font=("Arial", 12))
city_entry.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.05)

get_weather_button = tk.Button(window, text="Hava Durumu Getir", command=get_weather, bg="lightblue", font=("Arial", 12))
get_weather_button.place(relx=0.3, rely=0.18, relwidth=0.4, relheight=0.05)

# Hava Durumu Bilgileri Etiketleri
temperature_label = tk.Label(window, text="", bg="white", font=("Arial", 12))
temperature_label.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)

humidity_label = tk.Label(window, text="", bg="white", font=("Arial", 12))
humidity_label.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)

wind_label = tk.Label(window, text="", bg="white", font=("Arial", 12))
wind_label.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)

description_label = tk.Label(window, text="", bg="white", font=("Arial", 12))
description_label.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.1)

window.mainloop()

