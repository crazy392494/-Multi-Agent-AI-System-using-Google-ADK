def summarize(weather_data):
    weather = weather_data["weather"][0]["main"]
    if weather in ["Thunderstorm", "Rain", "Snow"]:
        return f"🚫 Launch may be delayed due to {weather.lower()}."
    else:
        return "✅ Launch is likely to proceed on time."
