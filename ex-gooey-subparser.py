"""
    Шаблон использования Gooey 

    используется:
        Ubuntu 19.10
        Gooey==1.0.3   (https://github.com/chriskiehl/Gooey)
"""

# запуск команды:
# python3 tst-gooey.py --ignore-gooey step0

from gooey import Gooey, GooeyParser


@Gooey(program_name='ПР', default_size=(900,700), language='russian', dump_build_config=True)
def main():
    
    my_parser = GooeyParser()

    parser = GooeyParser()

    subs = parser.add_subparsers(help='commands', dest='command')
    # ------ Шаг 0 --------------
    step0_parser = subs.add_parser('команда_1', help=' помощь для команды 1')
    step0_parser.add_argument('-flag_all',  default=False, metavar="",
    action='store_true', help="")

    # END ------ Шаг 0 --------------

    # ------ Шаг 1 --------------
    step1_parser = subs.add_parser('команда_2', help='помощь для команды 2')

    step1_parser.add_argument('username',
                            help='username', type=str, default="user")
    step1_parser.add_argument('password',
                            type=str, widget='PasswordField')

    step1_parser.add_argument('input_namefile', 
    metavar='Файл Ежедневное планирование менеджера',    
    help="выберите файл", widget='FileChooser') 

    step1_parser.add_argument('-flag_tst',  default=False,
    metavar='Флаг теста (только для разработчиков)',
    action='store_true',
    help="включите если отлаживаете программу")

    step1_parser.add_argument('-flag_get_url',  default=True,
    metavar='Загружать урлы для работ',
    action='store_true',
    help="включите если получаем ссылки на работы")
    # ------ END Шаг 1 --------------
        

    args = parser.parse_args()
    commands = args.command

    print(args)
    print(type(args))
    print(vars(args))

    if(commands == "команда_1"):
        print("Выбрана команда 1")

    if(commands == "команда_2"):
        print("Выбрана команда 2")

   


#print(main) #  <function Gooey.<locals>.build.<locals>.inner2 at 0x7f2276425cb0>

main()



    
