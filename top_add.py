from top import Top
from top_new import Top_new
class Top_add(Top):
    def __init__(self, top_name: str, source: str, target: str, relation = ''):
        super().__init__(top_name)
        self.my_top_source = source
        self.my_top_target = target
        self.my_top_relation = relation
    def method_add_top(self):
        print("Enter this add top")
        try:
            with open(self.my_top_name_file_json, 'r') as f:
                pass
        except FileNotFoundError:
            Top_new(self.my_top_name)
        self.method_read_from_json()
        if self.my_top_source not in self.my_top_json_dict['vertexes']:
            local_var_init_dict = {"edges": {self.my_top_target : self.my_top_relation}, "color": "b", "count": 0}
            self.my_top_json_dict['vertexes'][self.my_top_source] = local_var_init_dict
        else:
            self.my_top_json_dict['vertexes'][self.my_top_source]["edges"][self.my_top_target] = self.my_top_relation
        print(self.my_top_json_dict)
        self.method_write_to_json()

def main():
    pass

if __name__ == '__main__':
    main()