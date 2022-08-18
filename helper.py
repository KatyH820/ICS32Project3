import math
import json
import urllib.error
import urllib.request
from pathlib import Path
import os.path


def read_json_file(file_name: str) -> dict:
    """Read json file from computer and return data as a dict"""
    abspath = os.path.abspath(file_name)
    path = Path(abspath)
    try:
        with open(path, 'r') as file:
            json_text = file.read()
            return json.loads(json_text)
    except OSError:
        file_error(path)
        print('MISSING')
    except ValueError:
        file_error(path)
        print('FORMAT')


def file_error(path: Path) -> None:
    """Print the file error output"""
    print("FAILED")
    print(f'{path}')


def API_failure(error, url: str) -> None:
    """Print the API failure output"""
    print("FAIlED")
    print(f'{error.code} {url}')


def download_api_data(url: str, refer: bool) -> dict:
    """Download data from API and return data as a dict"""
    try:
        if refer == True:
            request = urllib.request.Request(url, headers={
                                             'Referer': 'https://www.ics.uci.edu/~thornton/ics32/ProjectGuide/Project3/katyh1'})
        else:
            request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as error:
        API_failure(error, url)
        print("NOT 200")
    except urllib.error.URLError:
        print('FAIlED')
        print(url)
        print('NETWORK')
    else:
        try:
            json_text = response.read().decode(encoding="utf-8")
            response.close()
            return json.loads(json_text)
        except json.JSONDecodeError as error:
            API_failure(error, url)
            print('FORMAT')


def convert_sec_to_hour(sec: float) -> float:
    """Given seconds, convert it to number of hours"""
    return (sec / 60 / 60)


def determine_distances(lat1: str, lon1: str, lat2: str, lon2: str) -> float:
    """Given two locations, determine the distances between them"""
    dlat = math.radians(float(lat2))-math.radians(float(lat1))
    dlon = math.radians(float(lon2))-math.radians(float(lon1))
    alat = (math.radians(float(lat1))+math.radians(float(lat2)))/2
    R = 3958.8
    x = dlon * math.cos(alat)
    return math.sqrt(x**2 + dlat**2)*R


def calculate_AQI(concentration: float) -> int:
    """Given concentration, convert it to AQI value"""
    if 0.0 <= concentration < 12.1:
        return round((((concentration-0)*(50))/(12.0-0))+0)
    elif 12.1 <= concentration < 35.5:
        return round((((concentration-12.1)*(49))/(35.4-12.1))+51)
    elif 35.5 <= concentration < 55.5:
        return round((((concentration-35.5)*(49))/(55.4-35.5))+101)
    elif 55.5 <= concentration < 150.5:
        return round((((concentration-55.5)*(49))/(150.4-55.5))+151)
    elif 150.5 <= concentration < 250.5:
        return round((((concentration-150.5)*(99))/(250.4-150.5))+201)
    elif 250.5 <= concentration < 350.5:
        return round((((concentration-250.5)*(99))/(350.4-250.5))+301)
    elif 350.5 <= concentration < 500.5:
        return round((((concentration-350.5)*(99))/(500.4-350.5))+401)
    elif concentration >= 500.5:
        return 501


def _determine_sign_of_lat(lat: float) -> str:
    """Given latitude, determine whether it is South or North"""
    if lat < 0:
        return '/S'
    else:
        return '/N'


def _determine_sign_of_lon(lon: float) -> str:
    """Given longtitude, determine whether it is West or East"""
    if lon < 0:
        return '/W'
    else:
        return '/E'


def determine_sign_of_lat_lon(lat: float, lon: float) -> tuple:
    """Determine sign of latitude and longitude, return as a tuple"""
    lat_sign = _determine_sign_of_lat(lat)
    lon_sign = _determine_sign_of_lon(lon)
    return lat_sign, lon_sign
