from agents.spacex_agent import get_next_launch
from agents.location_agent import get_launch_location
from agents.weather_agent import get_weather
from agents.summary_agent import summarize

def main():
    print("🚀 AI Multi-Agent System Starting...\n")

    launch = get_next_launch()
    if not launch:
        print("No launch info available.")
        return
    
    print(f"📦 Next Launch: {launch['name']}")
    
    location = get_launch_location(launch["launchpad"])
    print(f"📍 Location: {location['name']}")

    weather = get_weather(location["lat"], location["lon"])
    print(f"🌤 Weather: {weather['weather'][0]['description']}")

    result = summarize(weather)
    print(f"\n✅ Final Output: {result}")

if __name__ == "__main__":
    main()
