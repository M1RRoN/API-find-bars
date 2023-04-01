import requests


# def get_venues(latitude, longitude, radius, category):
#     CLIENT_ID = 'your_client_id'
#     CLIENT_SECRET = 'fsq3TwhcybMY5XmzoJhAbaL6FKwoWfZCm7IHVQIB9rgTzCg='
#     VERSION = '20220101'
#
#     url = 'https://api.foursquare.com/v2/venues/search'
#     params = {
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET,
#         'v': VERSION,
#         'll': f'{latitude},{longitude}',
#         'radius': radius,
#         'categoryId': category
#     }
#
#     response = requests.get(url, params=params)
#     venues = response.json()['response']['venues']
#
#     return venues

url = "https://api.foursquare.com/v3/places/nearby"

headers = {
    "accept": "application/json",
    "Authorization": "fsq3TwhcybMY5XmzoJhAbaL6FKwoWfZCm7IHVQIB9rgTzCg="
}

response = requests.get(url, headers=headers)


data = response.json()
for venue in data:
    print(venue)
