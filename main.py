import color_coder_test as test
from reference_manual_generator import *

if __name__ == '__main__':
    test.execute_unittests()
    reference_manual = create_reference_manual()
    print("\n Reference Manual for Telecomm Insulation Wire color codes \n", reference_manual)
    print('Done :)')
