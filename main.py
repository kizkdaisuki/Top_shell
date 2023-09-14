import sys

from top import Top
from top_add import Top_add
from top_list import Top_list
from top_new import Top_new
from top_set import Top_set
from top_show import Top_show
from message import func_print_message as message_func_print_message


def func_cmd_top_new(func_param_top_name: str) -> None:
    local_var_top_new = Top_new(func_param_top_name)
    local_var_top_new.method_new_top()

def func_cmd_top_add(func_param_top_name: str, func_param_source: str, func_param_target: str, func_param_relation = '') -> None:
    local_var_top_add = Top_add(func_param_top_name, func_param_source, func_param_target, func_param_relation)
    local_var_top_add.method_add_top()
    pass

def main(func_param_args: list) -> None:
    print(*func_param_args)
    local_var_args_len = len(func_param_args)
    if not local_var_args_len:
        message_func_print_message()
        return
    local_var_cmd = str(func_param_args[0])
    if local_var_cmd == 'new':
        try:
            local_var_top_name = str(func_param_args[1])
            func_cmd_top_new(local_var_top_name)
            print('is_ok')
        except IndexError:
            message_func_print_message()
    elif local_var_cmd == 'add':
        try:
            local_var_top_name, local_var_source, local_var_target = str(func_param_args[1]), str(func_param_args[2]), str(func_param_args[3])
            print(local_var_top_name, local_var_source, local_var_target)
            func_cmd_top_add(local_var_top_name, local_var_source, local_var_target)
        except IndexError:
            message_func_print_message()


if __name__ == '__main__':
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
