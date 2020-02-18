from geopy.geocoders import Nominatim
from geopy import distance
import reverse_geocode
import folium
from tqdm import tqdm

year_input = input('Please enter a year you would like to have a map for: ')
location_input = input('Please enter your location (format: lat, long): ')
print('Please wait...')

with open('locations.list.txt', 'r', encoding='latin-1') as locations:
    places, names = [], []
    for i in locations:
        space = i.find('\t')
        place = i[space:].strip()
        name_year = i[:space]
        year = name_year[(name_year.find('" (') + 3):(name_year.find('" (') + 7)]
        name = name_year[1:name_year.find(year) - 3]
        if year_input == year:
            names.append(name)
            places.append(place)

loc = (float(location_input[0:location_input.find(',')]), float(location_input[location_input.find(',') + 1:]))

coordinates = loc, (31.76, 35.21)
country = reverse_geocode.search(coordinates)[0]['country']

len_places = len(places)
new_places, new_names = [], []

for i in range(len_places):
    if country == 'United States':
        country = 'USA'
    if country in places[i]:
        new_places.append(places[i])
        new_names.append(names[i])

my_map = folium.Map(location=list(loc), zoom_start=10)

fg1 = folium.FeatureGroup(name='10 closest films')
fg2 = folium.FeatureGroup(name=('Distance'))
geolocator = Nominatim(user_agent="specify_your_app_name_here")
ltln = []
k = 0

for k in tqdm(range(len(new_places))):

    try:

        location = geolocator.geocode(new_places[k])
        ltln.append([location.latitude, location.longitude])
        dist = distance.distance(loc, ltln[-1]).km

        fg1.add_child(folium.Marker(location=ltln[-1], popup=new_names[k], icon=folium.Icon()))
        my_PolyLine = folium.PolyLine(locations=[loc, ltln[-1]], weight=3, tooltip=(str(dist) + ' km'),
                                      color='red'
                                      if float(dist) >= 1000
                                      else 'orange' if float(dist) >= 500
                                      else 'green')

        fg2.add_child(my_PolyLine)

    except AttributeError:
        continue

my_map.add_child(fg1)

my_map.add_child(fg2)

my_map.add_child(folium.LayerControl())
my_map.save('my_map.html')
