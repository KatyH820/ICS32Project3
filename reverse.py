from nominatim import *


class ReverseAPI():
    def __init__(self, user_input, result):
        self.user_input = user_input
        self.result = result

    def find_address(self, user_input: list, results: list) -> list:
        """
        Given user_input and results locations, return a list of address of top AQI.
        The number of address in the list depend on the the max number from the user_input.
        """
        max_result = int(user_input[3][1])
        lst = []
        for result in results[:max_result]:
            lst.append(reverse_geocoding(result[1], result[2]))
        return lst


class ReverseFile():
    def __init__(self, filtered):
        self.filtered = filtered

    def find_address(self, filtered: list) -> list:
        """Return a list of display names from the filtered locations"""
        lst = []
        for result in filtered:
            lst.append(result[3])
        return lst
