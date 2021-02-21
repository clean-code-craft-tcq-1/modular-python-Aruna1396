from Test import *
from ReferenceManual import *

if __name__ == '__main__':
    test_ColorPair_for_PairNumber(4, 'White', 'Brown')
    test_ColorPair_for_PairNumber(5, 'White', 'Slate')
    test_PairNumber_for_ColorPair('Black', 'Orange', 12)
    test_PairNumber_for_ColorPair('Violet', 'Slate', 25)
    test_PairNumber_for_ColorPair('Red', 'Orange', 7)
    referenceManual = createReferenceManual()
    print("\n Reference Manual for Telecomm Insulation wire color codes \n", referenceManual)
    print('Done :)')
