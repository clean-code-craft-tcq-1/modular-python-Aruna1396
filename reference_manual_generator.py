import colorpair_generator as color
from cable_colors import get_colorpair_names

"""
This function is implemented to create a reference manual with 
color names and its corresponding codes for the wiring personnel
"""


def print_reference_manual():
    pair_number_start_index = 1
    pair_number_end_index = len(color.MAJOR_COLORS) * len(color.MAJOR_COLORS) + 1
    print("{:<15} {:<15}".format('Pair Number', 'Major Minor ColorPairs'))
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = color.get_color_from_pairnumber(pair_number)
        formatted_colorpair = get_colorpair_names(major_color, minor_color)
        print("{:<20} {:<15}".format(pair_number, formatted_colorpair))
