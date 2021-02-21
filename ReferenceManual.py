from ColorPairGenerator import *
from prettytable import PrettyTable


def createReferenceManual():
    pair_number_start_index = 1
    pair_number_end_index = 26
    reference_manual = PrettyTable(['Pair Number', 'Color Pairs'])
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        color_pair = getColor_from_PairNumber(pair_number)
        formatted_colorpair = getColorPairString(color_pair[0], color_pair[1])
        reference_manual.add_row([pair_number, formatted_colorpair])
    return reference_manual
