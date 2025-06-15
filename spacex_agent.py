import requests

def get_next_launch():
    url = "https://api.spacexdata.com/v5/launches/upcoming"
    res = requests.get(url).json()
    if not res:
        return None
    next_launch = res[0]
    return {
        "name": next_launch["name"],
        "launchpad": next_launch["launchpad"]
    }
