CLEAR_SKY = 'Clear Sky'
CIRRUS = 'Cirrus'
CIRROCUMULUS = 'Cirrocumulus'
CIRROSTRATUS = 'Cirrostratus'
ALTOCUMULUS = 'Altocumulus'
CUMULUS = 'Cumulus'
STRATOCUMULUS = 'Stratocumulus'
ALTOSTRATUS = 'Altostratus'
STRATUS = 'Stratus'
CUMULONIMBUS = 'Cumulonimbus'
NIMBOSTRATUS = 'Nimbostratus'

CUMULUS_INFO = """Cumulus clouds form when the air within the cloud is warmer
                    than the surrounding air. Since warm air rises, the cloud
                    will expand upwards creating the puffy heaped look."""
CUMULONIMBUS_INFO = """ Cumulonimbus clouds grow to such great heights that
                            the water droplets within the top cloud will freeze
                            and fall to the earth as heavy rain."""
STRATUS_INFO = """The featureless flat stratus clouds that expand across the visible
                        sky form when a warm air mass collides with a cool air mass.
                        This causes the warm air to lift upwards and cool down enough
                        to form a cloud layer."""
STRATOCUMULUS_INFO = """Stratocumulus clouds typically form when warmer more
                               stable air traps moisture rising from the sea or earth
                               after heavy rain. The moisture will form into a flat layer
                               of puffy clouds."""
ALTOCUMULUS_INFO = """Though altocumulus clouds appear similar to stratocumulus
                             , these clouds reside at a higher altitude and form due
                             to unstable wind conditions. The rising air forms the
                             familiar cumulus look while sinking air breaks the cloud
                             apart."""

ALTOSTRATUS_INFO = """Altostratus is very similar to the appearance of
                            stratus clouds, however altostratus clouds are found
                            at a higher altitude. Altostratus clouds will not appear as
                            heavy as stratus clouds and can also be translucent, revealing
                            the sun or planes."""

NIMBOSTRATUS_INFO = """ Much like all stratus clouds, the nimbostratus cloud expands across
                            the sky due to a cool air mass pushing up a warmer air mass.
                            Nimbostratus clouds however, produce rain. Rain from nimbostratus
                            clouds will cover a large area of the earth and usually produce rain
                            for a long time."""

CIRRUS_INFO = """ Unlike all other cloud types, cirrus clouds reside at the highest altitude
                        and are composed of ice crystals instead of water droplets."""

CIRROCUMULUS_INFO = """ Cirrocumulus clouds """

CIRROSTRATUS_INFO = """ cirrostratus clouds """


def lookup_cloud_info(cloud_name):
    cloud_info = {
        CUMULUS: CUMULUS_INFO,
        CUMULONIMBUS: CUMULONIMBUS_INFO,
        STRATUS: STRATUS_INFO,
        STRATOCUMULUS: STRATOCUMULUS_INFO,
        ALTOCUMULUS: ALTOCUMULUS_INFO,
        ALTOSTRATUS: ALTOSTRATUS_INFO,
        NIMBOSTRATUS: NIMBOSTRATUS_INFO,
        CIRRUS: CIRRUS_INFO,
        CIRROCUMULUS: CIRROCUMULUS_INFO,
        CIRROSTRATUS: CIRROSTRATUS_INFO,
    }

    if cloud_name == 'all_clouds':
        return "Supported clouds: {}".format(list(cloud_info.keys()))

    return cloud_info.get(cloud_name, 'Cloud not found! It evaporated')
