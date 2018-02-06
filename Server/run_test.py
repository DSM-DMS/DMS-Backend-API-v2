from argparse import ArgumentParser

import unittest as ut

from server import app

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--testing')
    args = parser.parse_args()

    app.config['TESTING'] = True if args.skip_apply_time_limits else False

    all_tests = ut.TestLoader().discover('tests', '*.py')
    ut.TextTestRunner().run(all_tests)
