import requests
from collections import OrderedDict

from cloudy import config
from cloudy.cloud_info import *
from cloudy.config import API_URL

RAINING_ID = 300
THUNDERSTORM_ID = 531
PROBABILITY_SMOOTHING = .01


def determine_cloud_probabilities(zipcode):
    """
    Get the probabilities of which clouds you'll see for a given zip
    
    TODO: Add these potentially 
    # current_wind_speed = api_json['wind']['speed']
    # current_description = str(api_json['weather'][0].get('description'))
    """
    api_json = _get_api_json(zipcode)

    current_temp = api_json['main']['temp']
    current_cloud_coverage = api_json['clouds']['all']
    current_identity = api_json['weather'][0].get('id')

    temp_prob = temperature_probability(current_temp)
    cloud_prob = current_cloud_coverage * PROBABILITY_SMOOTHING
    density_prob = temp_prob * cloud_prob

    is_raining = RAINING_ID < current_identity < THUNDERSTORM_ID

    potential_cloud_list = wind_rain_probability(density_prob, is_raining)

    return potential_cloud_list if potential_cloud_list else []


def temperature_probability(current_temp):
    return abs((-(pow(current_temp, 2)) + 100 * current_temp) / 2500)


def wind_rain_probability(density_prob, is_raining):
    # this wasn't a dictionary :(
    # density_dictionary = [(0.0, 'Clear Sky'), (0.10, 'Cirrus'), (0.15, 'Cirrocumulus'), (0.20, 'Cirrostratus'),
    #                       (0.40, 'Altocumulus'), (0.50, 'Cumulus'), (0.65, 'Stratocumulus'),  (0.75, 'Altostratus'),
    #                       (0.90, 'Stratus')]
    # density_dictionary = OrderedDict(density_dictionary)

    density_map = {
        CLEAR_SKY: 0.0,
        CIRRUS: .1,
        CIRROCUMULS: .15,
        CIRROSTRATUS: .2,
        ALTOCUMULUS: .4,
        CUMULUS: .5,
        STRATOCUMULUS: .65,
        ALTOSTRATUS: .75,
        STRATUS: .9,
    }
    density_map = OrderedDict(sorted(density_map.items(), key=lambda key_value: key_value[1]))

    rain_density_map = {
        CUMULONIMBUS: .7,
        NIMBOSTRATUS: .8,
    }
    rain_density_map = OrderedDict(sorted(rain_density_map.items(), key=lambda key_value: key_value[1]))
    
    potential_clouds = []

    if density_prob == 0:
        potential_clouds.append((CLEAR_SKY, density_map.get(CLEAR_SKY)))
        return potential_clouds

    min_value = 1
    max_value = 0
    min_cloud, max_cloud = None, None
    if is_raining:
        for cloud_name, density_value in rain_density_map.items():
            if density_value > density_prob:
                max_value = density_value
            else:
                min_value = 0.70
        if min_value != 1:
            min_cloud = rain_density_map.get(min_value)
            potential_clouds.append((min_value, min_cloud))
        else:
            max_cloud = rain_density_map.get(max_value)
            potential_clouds.append((max_value, max_cloud))
    else:
        for cloud_name, density_value in density_map.items():
            if density_value <= density_prob:
                min_value = density_value
                min_cloud = cloud_name
            else:
                max_value = density_value
                max_cloud = cloud_name
                break

        potential_clouds.append((min_value, min_cloud))
        potential_clouds.append((max_value, max_cloud))

    potential_clouds = _find_probabilities_for_each_cloud(density_prob, potential_clouds)
    return potential_clouds


def _find_probabilities_for_each_cloud(density_prob, potential_clouds):
    lower_bound_value = potential_clouds[0][0]
    upper_bound_value = potential_clouds[1][0]
    lower_bound_value -= lower_bound_value
    upper_bound_value -= lower_bound_value
    density_prob -= lower_bound_value

    upper_bound_prob = density_prob / upper_bound_value
    upper_bound_prob *= 100
    lower_bound_prob = 100 - upper_bound_prob

    lower_bound_prob = '%.2f' % lower_bound_prob + '%'
    upper_bound_prob = '%.2f' % upper_bound_prob + '%'
    # subtract lowerbound from upper and density prob
    # divide density prob by upperbound
    # set lower bound to lower cloud (at 0th index)
    # set upper bound to upper cloud (at 1st index)
    # return the list :)
    new_potential_clouds = [(lower_bound_prob, potential_clouds[0][1]), (upper_bound_prob, potential_clouds[1][1])]

    return new_potential_clouds


def _get_api_json(zipcode):
    api_formatted_url = API_URL.format(zipcode, config.API_KEY)
    api_request = requests.get(api_formatted_url)
    return api_request.json()
