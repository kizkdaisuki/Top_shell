from top import Top

import json


class Top_new(Top):
    def __init__(self, top_name: str):
        super().__init__(top_name)

    def method_new_top(self):
        local_var_init_dict = {}
        local_var_init_json_file_path = self.my_top_root_file_name + 'top_init_template.json'
        with open(local_var_init_json_file_path, 'r') as f:
            local_var_init_dict = json.load(f)
        local_var_init_dict['vertexes'][self.my_top_name] = local_var_init_dict['vertexes']['name']
        del local_var_init_dict['vertexes']['name']
        self.my_top_json_dict = local_var_init_dict.copy()
        if self.my_top_is_first_create_json:
            self.method_write_to_json()
        # else:
        #     print('is not first create json')


def main():
    pass
if __name__ == '__main__':
    main()
