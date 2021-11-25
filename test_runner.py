import xmlrunner
import unittest
import sys
import getopt

def main(argv):
    # Get the arguments
    # usage: test_runner.py -d path/to/input/folder -p search-pattern
    opts, args = getopt.getopt(argv, 'd:p:')

    # default values for the arguments when they are not specified
    base_dir = './'
    test_dir = ''
    pattern = '*_*tests.py'

    for opt, arg in opts:
        if opt == '-d':
            test_dir = arg
        elif opt == '-p':
            pattern = arg

    output_dir = base_dir +  test_dir + '/test-reports'
    input_dir = base_dir + test_dir

    result = xmlrunner.XMLTestRunner(output=output_dir).run(unittest.TestLoader().discover(input_dir, pattern))

    return result

if __name__ == '__main__':
    result = main(sys.argv[1:])
    sys.exit(not result.wasSuccessful())
