import urllib.parse
from helper import download_api_data
import urllib.error


Reverse_Base_URL = "https://nominatim.openstreetmap.org/reverse"
Forward_Base_URL = "https://nominatim.openstreetmap.org/search"


def _build_reverse_search_url(lat: float, lon: float) -> str:
    """Build and return a reverse search url"""
    query_parameters = [('format', 'json'), ('lat', lat), ('lon', lon)]

    return f'{Reverse_Base_URL}?{urllib.parse.urlencode(query_parameters)}'


def _build_forward_search_url(address: str) -> str:
    """Build and return a forward search url"""
    query_parameters = [('format', 'json'), ('q', address)]
    return f'{Forward_Base_URL}?{urllib.parse.urlencode(query_parameters)}'


def forward_geocoding(address: str) -> list:
    """
    Given address, change it to latitude and longitude
    Return latitude and longitude as a list
    """
    url = _build_forward_search_url(address)
    data = download_api_data(url, True)
    return [data[0]['lat'], data[0]['lon']]


def reverse_geocoding(lat: float, lon: float) -> str:
    """Given latitude and longitude return the address"""
    url = _build_reverse_search_url(lat, lon)
    data = download_api_data(url, True)
    return data['display_name']
