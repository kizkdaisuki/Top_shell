from collections import deque, defaultdict
import json
import sys
import os


#  "source": "前端",
#     "target": "框架",
#     "attr": "事件",
#     "rela": "",
#     "elementId": 1
#   },
class Show_json:
    def __init__(self, top_name: str, root_file_path: str, index_file_path: str, dict_json_file_path: str):
        # 将所有的都打包之后显示 根据dict里面的内容
        self.my_index_file_path = index_file_path
        self.my_top_dict = {}
        self.my_html_root = root_file_path if root_file_path[-1] == '/' else root_file_path + '/'
        self.my_html_file = [''] + [self.my_html_root + 'page' + str(val) + '.html' for val in range(1, 6)]
        self.my_html_content = [''] + [''] * 5  # 每一个文件应该写入的内容
        self.my_json_file_path = dict_json_file_path
        self.my_top_name = top_name
        self.my_top_in_degree = defaultdict(int)  # 每个点的入度 初始为0
        self.my_top_graph = defaultdict(list)  # 存的图
        self.my_top_element_id = 0
        self.my_all_tops = ['const data = [']
        self.method_init_html_page_odd()  # 1 3 5
        self.method_init_html_page_title()  # 2

    def method_init_html_page_odd(self):
        for i in range(1, 6):
            if i % 2 == 1:
                with open(self.my_html_file[i], 'r') as f:
                    self.my_html_content[i] = str(f.read())

    def method_init_html_page_title(self):
        self.my_html_content[2] = '<title>' + self.my_top_name + '</title>'

    def method_init_html_page_relations(self):
        self.my_all_tops.append('];')
        local_var_all_tops_str = ''.join(self.my_all_tops)
        self.my_html_content[4] = local_var_all_tops_str

    def method_get_color(self, source_name):
        if source_name not in self.my_top_dict['vertexes']:
            return 'c'
        return self.my_top_dict['vertexes'][source_name]['color']

    def method_read_from_json(self):
        with open(self.my_json_file_path, 'r') as f:
            self.my_top_dict = json.load(f)
        for source_name, information in self.my_top_dict['vertexes'].items():
            if source_name not in self.my_top_in_degree:
                self.my_top_in_degree[source_name] = 0
            for vertex, relation in information['edges'].items():
                self.my_top_graph[source_name].append((vertex, relation))
                self.my_top_in_degree[vertex] += 1
        self.method_get_top_sort()

    def method_top_make_relation(self, source_name: str, target_name: str, attr: str, relation=''):
        local_var_dict = {'source': source_name, 'target': target_name, 'attr': attr, 'rela': relation,
                          'elementId': self.my_top_element_id}
        self.my_top_element_id += 1
        local_var_json_str = str(json.dumps(local_var_dict))
        if len(self.my_all_tops) == 1:
            self.my_all_tops.append(local_var_json_str)
        else:
            self.my_all_tops.append(', ' + local_var_json_str)

    def method_get_top_sort(self):
        local_var_queue = deque()
        for key, val in self.my_top_in_degree.items():
            if val == 0:
                local_var_queue.append(key)
        while len(local_var_queue):
            t = local_var_queue.popleft()
            for val in self.my_top_graph[t]:
                self.my_top_in_degree[val[0]] -= 1
                if self.my_top_in_degree[val[0]] == 0:
                    local_var_queue.append(val[0])
                    self.method_top_make_relation(t, val[0], self.method_get_color(val[0]))
        self.method_make_html_index()

    def method_make_html_index(self):
        self.method_init_html_page_relations()
        for i in range(1, 6):
            with open(self.my_html_file[i], 'w') as f:
                f.write(self.my_html_content[i])
        with open(self.my_index_file_path, 'w') as f:
            f.write('\n'.join(self.my_html_content[1:]))
        os.system(f'open {self.my_index_file_path}')


def main():

    pass


if __name__ == '__main__':
    main()