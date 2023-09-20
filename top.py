import json
import os
GLOBAL_VAR_ROOT_FILE_NAME = "/Users/mac/kizk/project/PY/Top_shell/"
class Top:
    def __init__(self, top_name: str):
        self.my_top_name_file_html = None
        self.my_top_name_file_json = None
        self.my_top_root_folder_name = None
        self.my_top_root_html_folder_name = None
        self.my_top_name_html_folder_name = None
        self.my_top_root_file_name = GLOBAL_VAR_ROOT_FILE_NAME
        self.my_top_name = top_name
        self.my_top_json_dict = {}
        self.my_top_is_first_create_json = False
        self.method_init_file(top_name)

    def method_init_file(self, top_name: str):
        self.my_top_root_folder_name = self.my_top_root_file_name + top_name + "/"
        if not os.path.exists(self.my_top_root_folder_name):
            os.makedirs(self.my_top_root_folder_name)
        self.my_top_name_file_json = self.my_top_root_folder_name + top_name + ".json"
        self.my_top_name_file_html = self.my_top_root_folder_name + top_name + ".html"
        self.my_top_name_html_folder_name = self.my_top_root_folder_name + 'html'
        self.my_top_root_html_folder_name = self.my_top_root_file_name + 'top_html/'
        self.method_init_json_dict()

    def method_init_json_dict(self):
        try:
            with open(self.my_top_name_file_json, 'r') as f:
                self.my_top_json_dict = json.load(f)
        except FileNotFoundError:
            self.my_top_is_first_create_json = True
        if not os.path.exists(self.my_top_root_folder_name + 'html'):
            print('kizk')
            local_var_create_html_file_name = f'cp -r {self.my_top_root_html_folder_name[:-1]} {self.my_top_name_html_folder_name}'
            print(local_var_create_html_file_name)
            pass
            os.system(local_var_create_html_file_name)
    def method_write_to_json(self):
        with open(self.my_top_name_file_json, 'w') as f:
            json.dump(self.my_top_json_dict, f)

    def method_read_from_json(self):
        with open(self.my_top_name_file_json, 'r') as f:
            self.my_top_json_dict = json.load(f)
        pass

    def method_add_content(self, source: str, target: str):
        pass


    def method_show_content(self):
        pass
def func_test():
    d = {}
    with open('tops.json', 'r') as f:
        d = json.load(f)
    print(d)

def main():
    func_test()
    pass

if __name__ == '__main__':
    main()