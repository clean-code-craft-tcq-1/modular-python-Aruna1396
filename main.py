import color_coder_test as test
import reference_manual_generator as manual

if __name__ == '__main__':
    test.execute_unittests()
    reference_manual = manual.create_reference_manual()
    print("\n Reference Manual for Telecomm Insulation Wire color codes \n", reference_manual)
    print('Done :)')
