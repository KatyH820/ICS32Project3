from input import read_input
from center import *
from purpleair import *
from reverse import *


def find_result_location(user_input: list, air_data: dict, center_lat: str, center_lon: str) -> list:
    """
    Given user_input, air_data dictionary, center_lat, and center_lon,
    find locations that are within the given range and that their AQI values are
    above the threshold. Return locations as a list with order from highest AQI to
    lowest AQI. Each location is a list of [AQI, lat, lon].
    """
    lst = []
    for data in air_data['data']:
        lat, lon, type = data[27], data[28], data[25]
        age = convert_sec_to_hour(data[4])
        if lat != None and lon != None and data[1] != None:
            if determine_distances(center_lat, center_lon, lat, lon) <= float(user_input[1][1]):
                if calculate_AQI(data[1]) >= int(user_input[2][1]):
                    if age <= 1 and type == 0:
                        lst.append([calculate_AQI(data[1]), lat, lon])
    lst.sort(reverse=True)
    return lst


def data_of_location_from_json_file(user_input: list) -> list:
    """
    Given user_input, get latitude, longitude, and display name from
    locations that are given as json file in the reverse file input.
    Return the information of locations as a list.
    Each location is a tuple of (lat,lon,display_name)
    """
    files = user_input[5][2:]
    infos = []
    for file in files:
        data = read_json_file(file)
        infos.append((data['lat'], data['lon'], data['display_name']))
    return infos


def filter_result_area_with_given_file(user_input: list, infos: list, results: list) -> list:
    """
    Given infos and results, return a list of location informations where
    the locations are in both results and infos. The order of the locations
    is from high AQI to low AQI. The number of location return depend on the
    max number from the user_input.
    Each location information is a list [AQI, lat, lon, display_name].
    """
    max_result = int(user_input[3][1])
    lst = []
    for result in results:
        for info in infos:
            if f'{float(result[1]):.3f}' == f'{float(info[0]):.3f}' and f'{float(result[2]):.3f}' == f'{float(info[1]):.3f}':
                result.append(info[2])
                lst.append(result)
    return lst[:max_result]


def final_report(user_input: list, center_lat: str, center_lon: str, results: list, display_address: list) -> None:
    """
    Print the final report from the given user_input, center_lat,
    center_lon, results, and display_address.
    Print a report of locations where their AQI above the threshold.
    The order of the locations is from high AQI to low AQI.
    Locations print are within the given range from center.
    Number of Locations print are depend on the user_input.
    """
    if user_input[5][1] == 'FILES':
        infos = data_of_location_from_json_file(user_input)
        results = filter_result_area_with_given_file(
            user_input, infos, results)
    elif user_input[5][1] == 'NOMINATIM':
        max_result = int(user_input[3][1])
        results = results[:max_result]
    center_lat = float(center_lat)
    center_lon = float(center_lon)
    clat_sign, clon_sign = determine_sign_of_lat_lon(center_lat, center_lon)
    print(f'CENTER {abs(center_lat)}{clat_sign} {abs(center_lon)}{clon_sign}')
    for num in range(len(results)):
        print(f'AQI {results[num][0]}')
        lat_sign, lon_sign = determine_sign_of_lat_lon(
            results[num][1], results[num][2])
        print(
            f'{abs(results[num][1])}{lat_sign} {abs(results[num][2])}{lon_sign}')
        print(display_address[num])


def center_lat_lon(user_input: list) -> list:
    """Create center object and return latitude and longitude of the center"""
    if user_input[0][1] == 'NOMINATIM':
        center_object = CenterAPI(user_input)
    elif user_input[0][1] == 'FILE':
        center_object = CenterFile(user_input)
    center_lat, center_lon = center_object.find_center_latitude_longitude(
        user_input)
    return [center_lat, center_lon]


def get_air_data(user_input: list) -> dict:
    """Create data_object and return a dictionary of air data"""
    if user_input[4][1] == 'PURPLEAIR':
        data_object = PurpleAirAPI(user_input)
        return data_object.get_air_quality_info()
    elif user_input[4][1] == "FILE":
        data_object = PurpleAirFile(user_input)
        return data_object.get_air_quality_info(user_input)


def get_address(user_input: list, results: list) -> list:
    """Given user_input and results return a list of address"""
    if user_input[5][1] == 'FILES':
        infos = data_of_location_from_json_file(user_input)
        filtered = filter_result_area_with_given_file(
            user_input, infos, results)
        address = ReverseFile(filtered)
        return address.find_address(filtered)
    elif user_input[5][1] == 'NOMINATIM':
        address = ReverseAPI(user_input, results)
        return address.find_address(user_input, results)


def run():
    """Run the program"""
    try:
        user_input = read_input()
        center_lat, center_lon = center_lat_lon(user_input)
        air_data = get_air_data(user_input)
        results = find_result_location(
            user_input, air_data, center_lat, center_lon)
        display_address = get_address(user_input, results)
        final_report(user_input, center_lat, center_lon,
                     results, display_address)
    except TypeError:
        pass


if __name__ == '__main__':
    run()
