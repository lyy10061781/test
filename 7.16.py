class List_context:
    def __init__(self):
        self.data_list = []

    def add_item(self, item):
        self.data_list.append(item)

    def remote_item(self, item):
        if item in self.data_list:
            return self.data_list.remove(item)
        else:
            print(f'{item} not found in the list.')

    def updata_item(self, old_item, new_item):
        index = self.data_list.index(old_item)
        self.data_list[index] = new_item

    def find_item(self, item):
        if item in self.data_list:
            return self.data_list.index(item)
        else:
            print(f'{item} not found in the list')

    def get_list(self):
        return self.data_list[:]


if __name__ == '__main__':
    data = List_context()
    data.add_item('apple')
    data.add_item('banana')
    data.add_item('oriage')
    print(data.get_list())
    #
    #
    data.remote_item('applee')
    #
    #
    data.updata_item('apple', 'pear')
    print(data.get_list())
    #
    print(data.find_item('oriage'))
    # print(data.get_list())