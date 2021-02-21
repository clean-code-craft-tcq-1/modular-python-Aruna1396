from ColorPairGenerator import *


def test_ColorPair_for_PairNumber(pair_number,
                                  expected_major_color, expected_minor_color):
    major_color, minor_color = getColor_from_PairNumber(pair_number)
    assert (major_color == expected_major_color)
    assert (minor_color == expected_minor_color)


def test_PairNumber_for_ColorPair(major_color, minor_color, expected_pair_number):
    pair_number = get_PairNumber_from_Color(major_color, minor_color)
    assert (pair_number == expected_pair_number)
