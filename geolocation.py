from geopy.geocoders import Nominatim


def get_location(name: str):
    # calling the Nominatim tool
    loc = Nominatim(user_agent="Freeze Map")
    
    # entering the location name
    location = loc.geocode(name)
    
    return location