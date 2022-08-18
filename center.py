from nominatim import *
from helper import *


class CenterFile():
    def __init__(self, user_input):
        self.user_input = user_input

    def find_center_latitude_longitude(self, user_input: list) -> list:
        """
        Given user_input, find center latitude and 
        longitude and return as a list
        """
        data = read_json_file(user_input[0][2])
        return [data[0]['lat'], data[0]['lon']]


class CenterAPI():
    def __init__(self, user_input):
        self.user_input = user_input

    def find_center_latitude_longitude(self, user_input: list) -> list:
        """
        Given user_input, find center latitude and 
        longitude and return as a list
        """
        return forward_geocoding(user_input[0][2])
