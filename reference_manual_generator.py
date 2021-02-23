from colorpair_generator import get_color_from_pairnumber
from cable_colors import get_colorpair_names
from prettytable import PrettyTable

"""
This function creates a reference manual with color pair names
and color codes in a tabular format. External Library is
used for formatting purposes to improve readability.
"""


def create_reference_manual():
    pair_number_start_index = 1
    pair_number_end_index = 26
    reference_manual = PrettyTable(['Pair Number', 'Color Pairs'])
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        color_pair = get_color_from_pairnumber(pair_number)
        formatted_colorpair = get_colorpair_names(color_pair[0], color_pair[1])
        reference_manual.add_row([pair_number, formatted_colorpair])
    return reference_manual
