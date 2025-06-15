import requests

def get_launch_location(pad_id):
    url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
    pad = requests.get(url).json()
    return {
        "name": pad["name"],
        "lat": pad["latitude"],
        "lon": pad["longitude"]
    }
