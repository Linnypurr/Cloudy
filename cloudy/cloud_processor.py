import requests
from collections import OrderedDict

from cloudy import config


def determine_cloud_probabilities(zipcode):
    api_json = _get_api_json(zipcode)

    current_temp = api_json['main']['temp']
    current_wind_speed = api_json['wind']['speed']
    current_cloud_coverage = api_json['clouds']['all']
    # current_description = str(api_json['weather'][0].get('description'))
    current_identity = api_json['weather'][0].get('id')

    temp_prob = temperature_probability(current_temp)
    cloud_prob = current_cloud_coverage * .01

    if 300 < current_identity < 531:
        is_raining = True
    else:
        is_raining = False
    density_prob = temp_prob * cloud_prob
    cloud_list = wind_rain_probability(density_prob, current_wind_speed, is_raining)
    return str(cloud_list)


def _get_api_json(zipcode):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(zipcode,
                                                                                                   config.API_KEY)
    api_request = requests.get(api_url)
    return api_request.json()


def temperature_probability(current_temp):
    return abs((-(pow(current_temp, 2)) + 100 * current_temp) / 2500)


def wind_rain_probability(density_prob, wind_speed, is_raining):
    density_dictionary = [(0.0, 'Clear Sky'), (0.10, 'Cirrus'), (0.15, 'Cirrocumulus'), (0.20, 'Cirrostratus'),
                          (0.40, 'Altocumulus'), (0.50, 'Cumulus'), (0.65, 'Stratocumulus'),  (0.75, 'Altostratus'),
                          (0.90, 'Stratus')]

    density_dictionary = OrderedDict(density_dictionary)

    rain_density_dictionary = [(0.70, 'Cumulonimbus'), (0.85, 'Nimbostratus')]
    rain_density_dictionary = OrderedDict(rain_density_dictionary)

    chosen_cloud = [density_prob]
    min_value = 1
    max_value = 0
    min_cloud = ''
    max_cloud = ''
    if is_raining:
        for density_value in rain_density_dictionary.items():
            if density_value > density_prob:
                max_value = density_value
            else:
                min_value = 0.70

        if min_value != 1:
            min_cloud = rain_density_dictionary.get(min_value)
            chosen_cloud.append((min_value, min_cloud))
        else:
            max_cloud = rain_density_dictionary.get(max_value)
            chosen_cloud.append(max_value, max_cloud)
    else:
        for density_value, cloud_name in density_dictionary.items():
            if density_value < density_prob:
                min_value = density_value
                min_cloud = cloud_name
            if density_value > density_prob:
                max_value = density_value
                max_cloud = cloud_name
                break

        chosen_cloud.append((min_value, min_cloud))
        chosen_cloud.append((max_value, max_cloud))

    return chosen_cloud

# def get_cloud_picture(cloud_name):