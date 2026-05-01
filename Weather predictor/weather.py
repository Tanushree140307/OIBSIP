import requests

api_key = "e82a31ef53100660ad892ea317a20533"
city = input("🌍 Enter city (e.g. Chennai,IN): ").strip()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\n🌦️ ===== WEATHER REPORT ===== 🌦️")
        print(f"📍 Location      : {city_name}, {country}")
        print(f"🌡️ Temperature   : {temp}°C")

        print(f"💧 Humidity      : {humidity}%")
        print(f"🌥️ Condition     : {weather}")

    else:
        print("City not found! Check spelling.")

except Exception as e:
    print("Error:", e)