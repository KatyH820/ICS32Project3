def _read_center_input() -> list:
    """
    Read center info from user and return the center_info as a
    list if the inputs are Valid else it will raise Exception
    """
    center_info = input().split(' ', 2)
    if (center_info[0] == "CENTER" and (center_info[1] == "NOMINATIM" or center_info[1] == "FILE")):
        return center_info
    else:
        raise Exception("Invalid center input.")


def _read_range_input() -> list:
    """
    Read range info from user and return the range_info as a
    list if the inputs are Valid else it will raise Exception
    """
    range_input = input().split()
    if (len(range_input) == 2 and range_input[0] == "RANGE" and int(range_input[1]) >= 0):
        return range_input
    else:
        raise Exception("Invalid range input.")


def _read_threshold_input() -> list:
    """
    Read threshold info from user and return the threshold_input
    as a list if the inputs are Valid else it will raise Exception
    """
    threshold_input = input().split()
    if (len(threshold_input) == 2 and threshold_input[0] == "THRESHOLD" and int(threshold_input[1]) >= 0):
        return threshold_input
    else:
        raise Exception("Invalid threshold input.")


def _read_max_input() -> list:
    """
    Read max number of locations from user and return the max_input
    as a list if the inputs are Valid else it will raise Exception
    """
    max_input = input().split()
    if (len(max_input) == 2 and max_input[0] == "MAX" and int(max_input[1]) >= 0):
        return max_input
    else:
        raise Exception("Invalid max input.")


def _read_AQI_input() -> list:
    """
    Read way to obtain AQI data from user and return the AQI_info
    as a list if the inputs are Valid else it will raise Exception
    """
    AQI_info = input().split()
    if (AQI_info[0] == "AQI"):
        if AQI_info[1] == "PURPLEAIR" and len(AQI_info) == 2:
            return AQI_info
        elif AQI_info[1] == "FILE" and len(AQI_info) == 3:
            return AQI_info
    else:
        raise Exception("Invalid AQI input.")


def _read_reverse_input(max_num: int) -> list:
    """
    Read way to reverse geocoding from user and return the reverse_input
    as a list if the inputs are Valid else it will raise Exception
    """
    reverse_input = input().split()
    if reverse_input[0] == 'REVERSE':
        if reverse_input[1] == "NOMINATIM" and len(reverse_input) == 2:
            return reverse_input
        elif reverse_input[1] == "FILES" and len(reverse_input) >= (2 + int(max_num)):
            return reverse_input
        else:
            raise Exception("Invalid reverese input")


def read_input() -> list:
    """Read input from user and return the informations as a list"""
    center_info = _read_center_input()
    range_info = _read_range_input()
    threshold_info = _read_threshold_input()
    max_info = _read_max_input()
    AQI_info = _read_AQI_input()
    reverse_info = _read_reverse_input(max_info[1])
    return [center_info, range_info, threshold_info, max_info, AQI_info, reverse_info]
