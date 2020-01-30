"""

    используется:
        Ubuntu 19.10
        Gooey==1.0.3   (https://github.com/chriskiehl/Gooey)

    скрипт который показывает неверное обработка визуальных элементов 
    типа флажок:

    если по умолчанию установлен True, то когда убираем отметку,
    все равно после запуска параметр установлен в True, хотя должен быть False.

    step0_parser.add_argument('-flag1',  default=True, metavar="Флаг1",
        action='store_true', help="включите Флаг1")

    если параметр default=False, то отрабатывает как положено.

"""

# запуск команды:
# python3 tst-gooey.py --ignore-gooey step0

from gooey import Gooey, GooeyParser


@Gooey(dump_build_config=True)
def main():

    my_parser = GooeyParser()

    my_parser.add_argument('-flag1',  default=True, metavar="Флаг1",
                           action='store_true', help="включите Флаг1")

    args = my_parser.parse_args()

    print(args)
    print(type(args))
    print(vars(args))

    #commands = args.command

main()
