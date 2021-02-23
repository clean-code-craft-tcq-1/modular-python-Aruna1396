import cable_colors


def get_color_from_pairnumber(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(cable_colors.MINOR_COLORS)
    if major_index >= len(cable_colors.MAJOR_COLORS):
        raise Exception('Major Color index out of range')
    minor_index = zero_based_pair_number % len(cable_colors.MINOR_COLORS)
    if minor_index >= len(cable_colors.MINOR_COLORS):
        raise Exception('Minor Color index out of range')
    return cable_colors.MAJOR_COLORS[major_index], cable_colors.MINOR_COLORS[minor_index]


def get_pairnumber_from_color(major_color, minor_color):
    try:
        major_index = cable_colors.MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major Color index out of range')
    try:
        minor_index = cable_colors.MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor Color index out of range')
    return major_index * len(cable_colors.MINOR_COLORS) + minor_index + 1
