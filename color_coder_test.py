import colorpair_generator as color


def test_colorpair_for_pairnumber(pair_number,
                                  expected_major_color, expected_minor_color):
    major_color, minor_color = color.get_color_from_pairnumber(pair_number)
    assert (major_color == expected_major_color)
    assert (minor_color == expected_minor_color)


def test_pairnumber_for_colorpair(major_color, minor_color, expected_pair_number):
    pair_number = color.get_pairnumber_from_color(major_color, minor_color)
    assert (pair_number == expected_pair_number)


def execute_unittests():
    test_colorpair_for_pairnumber(4, 'White', 'Brown')
    test_colorpair_for_pairnumber(5, 'White', 'Slate')
    test_pairnumber_for_colorpair('Black', 'Orange', 12)
    test_pairnumber_for_colorpair('Violet', 'Slate', 25)
    test_pairnumber_for_colorpair('Red', 'Orange', 7)
