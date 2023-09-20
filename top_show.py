from top import Top
from show_json import Show_json

class Top_show(Top):
    def __init__(self, top_name: str):
        super().__init__(top_name)
        self.my_top_show_json = None
        self.method_show_top()

    def method_show_top(self):
        self.my_top_show_json = Show_json(self.my_top_name, self.my_top_root_html_folder_name, self.my_top_root_folder_name + 'index.html', self.my_top_name_file_json)
        print("kizkdaisuki")
        self.my_top_show_json.method_read_from_json()
    def print_info(self):
        pass

def main():
    pass
if __name__ == '__main__':
    main()
