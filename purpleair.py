from helper import *


class PurpleAirAPI():
    def __init__(self, user_input):
        self.user_input = user_input

    def get_air_quality_info(self) -> dict:
        """
        Obtain air quality information from PurpleAir's API.
        Return data as a dict.
        """
        PurpleAirURL = "https://www.purpleair.com/data.json"
        return download_api_data(PurpleAirURL, False)


class PurpleAirFile():
    def __init__(self, user_input):
        self.user_input = user_input

    def get_air_quality_info(self, user_input):
        """
        Obtain air quality information from files.
        Return data as a dict.
        """
        return read_json_file(user_input[4][2])
