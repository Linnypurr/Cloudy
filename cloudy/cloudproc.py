import requests
from collections import OrderedDict


def lookup_cloud_info(cloud_name):

    cumulusinfo = """Cumulus clouds form when the air within the cloud is warmer
                    than the surrounding air. Since warm air rises, the cloud
                    will expand upwards creating the puffy heaped look."""
    cumulonimbusinfo = """ Cumulonimbus clouds grow to such great heights that
                        the water droplets within the top cloud will freeze
                        and fall to the earth as heavy rain."""
    stratusinfo = """The featureless flat stratus clouds that expand across the visible '
                    sky form when a warm air mass collides with a cool air mass.
                    This causes the warm air to lift upwards and cool down enough
                    to form a cloud layer."""
    stratocumulusinfo = """Stratocumulus clouds typically form when warmer more '
                           stable air traps moisture rising from the sea or earth
                           after heavy rain. The moisture will form into a flat layer
                           of puffy clouds."""
    altocumulusinfo = """Though altocumulus clouds appear similar to stratocumulus
                         , these clouds reside at a higher altitude and form due
                         to unstable wind conditions. The rising air forms the
                         familiar cumulus look while sinking air breaks the cloud
                         apart."""

    altostratusinfo = """Altostratus is very similar to the appearance of
                        stratus clouds, however altostratus clouds are found
                        at a higher altitude. Altostratus clouds will not appear as
                        heavy as stratus clouds and can also be translucent, revealing
                        the sun or planes."""

    nimbostratusinfo = """ Much like all stratus clouds, the nimbostratus cloud expands across
                        the sky due to a cool air mass pushing up a warmer air mass.
                        Nimbostratus clouds however, produce rain. Rain from nimbostratus
                        clouds will cover a large area of the earth and usually produce rain
                        for a long time."""

    cirrusinfo = """ Unlike all other cloud types, cirrus clouds reside at the highest altitude
                    and are composed of ice crystals instead of water droplets."""

    cirrocumulusinfo = """ Cirrocumulus clouds """

    cirrostratusinfo = """ cirrostratus clouds """

    cloud_info = {'cumulus': cumulusinfo,
                  'cumulonimbus': cumulonimbusinfo,
                  'stratus': stratusinfo,
                  'stratocumulus': stratocumulusinfo,
                  'altocumulus': altocumulusinfo,
                  'altostratus': altostratusinfo,
                  'nimbostratus': nimbostratusinfo,
                  'cirrus': cirrusinfo,
                  'cirrocumulus': cirrocumulusinfo,
                  'cirrostratus': cirrostratusinfo,
                  }

    if cloud_name == 'all_clouds':
        return "Supported clouds: {}".format(list(cloud_info.keys()))

    return cloud_info.get(cloud_name, 'Cloud not found! It evaporated')


def determine_cloud_probabilities(zipcode):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(zipcode, api_key)
    api_request = requests.get(api_url)
    api_json = api_request.json()

    current_temp = api_json['main']['temp']
    current_wind_speed = api_json['wind']['speed']
    current_cloud_coverage = api_json['clouds']['all']
    # current_description = str(api_json['weather'][0].get('description'))
    current_identity = api_json['weather'][0].get('id')

    temp_prob = temperature_probability(current_temp)
    cloud_prob = current_cloud_coverage * .01

    if current_identity > 300 and current_identity < 531:
        is_raining = True
    else:
        is_raining = False
    density_prob = temp_prob * cloud_prob
    cloud_list = wind_rain_probability(density_prob, current_wind_speed, is_raining)
    return str(cloud_list)


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