from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = 'dce2563415e74f2e8819acf8b8b36533'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')