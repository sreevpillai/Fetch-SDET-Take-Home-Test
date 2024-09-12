import requests
import json

ENDPOINT="http://api.openweathermap.org/geo/1.0/"
key="f897a99d971b5eef57be6fafa0d83239"

## Utility which takes  multiple locations of either city/state/country or zip location
def coordinates_by_city_zip(city_names, zip_codes):
    responses=[]
    if city_names:
        city_list=city_names.split(";")
        for city in city_list:
            responses.append(requests.get(ENDPOINT + f"direct?q={city}&appid={key}").json())
    if zip_codes:
        zip_code_list = zip_codes.split(",")
        for zip in zip_code_list:
            responses.append(requests.get(ENDPOINT+f"zip?zip={zip}&appid={key}").json())
    return responses


# Testing the utility by passing multiple locations of city/state/country and multiple locations of zipcodes
def test_utility_multiple_locations():
    coordinates = coordinates_by_city_zip("Madison,WI,US;“Chicago,IL,US","12345,10001")
    print(*coordinates, sep = "\n")
    name=coordinates[0][0]['name']
    assert name=="Madison"
    state = coordinates[0][0]['state']
    assert state=="Wisconsin"
    country = coordinates[0][0]['country']
    assert country=='US'
    name = coordinates[1][0]['name']
    assert name == "Chicago"
    state = coordinates[1][0]['state']
    assert state == "Illinois"
    country = coordinates[1][0]['country']
    assert country == 'US'
    zip = coordinates[2]['zip']
    assert zip=="12345"
    zip = coordinates[3]['zip']
    assert zip=="10001"

# Testing the utility by passing single location of city/state/country and single location of zipcode
def test_utility_single_location():
    coordinates = coordinates_by_city_zip("Madison, WI,US","10001")
    print(*coordinates, sep = "\n")
    name=coordinates[0][0]['name']
    assert name == "Madison"
    zip = coordinates[1]['zip']
    assert zip == "10001"

# Testing the utility by passing single location of city/state/country and multiple locations of zipcodes
def test_utility_multilocations_zip():
    coordinates = coordinates_by_city_zip("Chicago, IL,US","12345,10001")
    print(*coordinates, sep = "\n")
    name = coordinates[0][0]['name']
    assert name == "Chicago"
    zip = coordinates[1]['zip']
    assert zip == "12345"
    zip = coordinates[2]['zip']
    assert zip == "10001"

# Testing the utility by passing multiple locations of city/state/country and single location of zipcode
def test_utility_multilocations_city():
    coordinates = coordinates_by_city_zip("Chicago, IL,US;Madison, WI,US","10001")
    print(*coordinates, sep = "\n")
    name = coordinates[0][0]['name']
    assert name == "Chicago"
    name = coordinates[1][0]['name']
    assert name == "Madison"
    zip = coordinates[2]['zip']
    assert zip == "10001"
