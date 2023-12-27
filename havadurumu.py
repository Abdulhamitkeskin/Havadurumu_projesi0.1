import requests


def weather(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"

    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Hava Durumu Bilgileri - {city_name}")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Nem Oranı: {data['main']['humidity']}%")
        print(f"Rüzgar Hızı: {data['wind']['speed']} m/s")
        print(f"Hava Durumu: {data['weather'][0]['description']}")
    else:
        print(f"Hata: {response.status_code}")
        print(response.text)


while True:
    process = input("Hava durumuna bakmak için '1' çıkış yapmak için '2 basınız:")

    try:

        if int(process) == 1:

            api_key = "38ddfa48fc3d4d2222f95a4eaf2bd909"

            city_name = input("Hava durumu bilgilerini almak istediğiniz şehir adını girin: ")

            weather(api_key, city_name)
        elif int(process) == 2:
            break
        else:
            print("Lütfen beriltilen aralıkta sayı giriniz")


    except:
        print("Lütfen belirtilen aralıkta sayıyı giriniz")
        continue

    if (int(process) == 2):
        break


