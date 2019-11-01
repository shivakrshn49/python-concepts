import argparse as _argparse

parser = _argparse.ArgumentParser(description="Learning Argparse module")

parser.add_argument('-buildVersion', action='store', #dest="",
                    help='Store a simple value')


parser.add_argument('-buildVersion_store_const', '-beta', action='store_const', dest='buildVersion_store_const',
                    const='value-to-store',
                    help='Store a constant value', )

parser.add_argument('-t', action='store_true', default=True,
                    dest='boolean_switch',
                    help='Set a switch to true')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list', type=int,
                    )

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')

parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

parser.add_argument(
            '-i', '--ignore', action='append', default=[],
            dest='ignore_patterns', metavar='PATTERN',
            help="Ignore files or directories matching this glob-style "
                 "pattern. Use multiple times to ignore more.",
        )

results = parser.parse_args()
print results
print dir(results)
# import ipdb;ipdb.set_trace()