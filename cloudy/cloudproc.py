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

    cloud_info = {'cumulus': cumulusinfo,
                  'cumulonimbus': cumulonimbusinfo,
                  'stratus': stratusinfo,
                  'stratocumulus': stratocumulusinfo,
                  'altocumulus': altocumulusinfo,
                  'altostratus': altostratusinfo,
                  }

    if cloud_name == 'all_clouds':
        return "Supported clouds: {}".format(list(cloud_info.keys()))

    return cloud_info.get(cloud_name, 'Cloud not found! It evaporated')


def determine_cloud_probabilities(zipcode):
    pass
