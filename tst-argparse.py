import argparse

parser = argparse.ArgumentParser(description='My example explanation')

parser.add_argument(
    '-flag1',
    type=bool,
    default=False,
    help='включите Флаг1' #,
    #action='store_true'   
)

my_namespace = parser.parse_args()
print(my_namespace)



"""
my_parser.add_argument('-flag1',  default=True, metavar="Флаг1",
action='store_true', help="включите Флаг1")
"""