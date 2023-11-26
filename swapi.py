import requests

"""
url = requests.get("https://swapi.dev/api/people/1/")
data = url.json()
"""

def getPerson(index=1):
    url = requests.get("https://swapi.dev/api/people/1/{index}/")
    return result_url.json()

