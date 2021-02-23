from color_coder_test import execute_unittests
from reference_manual_generator import create_reference_manual

if __name__ == '__main__':
    execute_unittests()
    reference_manual = create_reference_manual()
    print("\n Reference Manual for Telecomm Insulation Wire color codes \n", reference_manual)
    print('Done :)')
