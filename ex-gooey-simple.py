"""
    Простой шаблон использования Gooey

    используется:
        Ubuntu 19.10
        Gooey==1.0.3   (https://github.com/chriskiehl/Gooey)
"""

# запуск команды:
# python3 tst-gooey.py --ignore-gooey step0

from gooey import Gooey, GooeyParser


@Gooey(program_name='Простой шаблон использования Gooey', default_size=(900,700), language='russian', dump_build_config=True)
def main():
    
    my_parser = GooeyParser()

    my_parser.add_argument('-flag1', metavar="Флаг1", action='store_true',
    help="включите Флаг1")
    my_parser.add_argument('username',
                            help='username', type=str, default="значение по умолчанию")
    

    args = my_parser.parse_args()

    print(args)
    print(type(args))
    print(vars(args))

    #commands = args.command


#print(main) #  <function Gooey.<locals>.build.<locals>.inner2 at 0x7f2276425cb0>

main()



    
