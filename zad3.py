

class Tree:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.child = []
        self.parent = None

    def add_child(self, child):
        self.child.append(child)
        child.parent = self

    def remove_child(self, child):
        for n in range(len(self.child)):
            if self.child[n] == child:
                self.child[n].parent = None
                del self.child[n]

    def get_child(self):
        return self.child

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def walk_down(self, value_list=[]):

        for i in self.child:
            value_list.append(i.value)
            i.walk_down(value_list)
        return value_list

    def walk_up(self, value_list=[]):

        value_list.append(self.value)
        if self.parent != None:
            value_list = self.parent.walk_up(value_list)
        return value_list

    @property
    def min_value(self):
        root = self
        while(root.parent != None):
            root = root.parent
        all_value =[]
        root.walk_down(all_value)
        all_value.append(root.value)
        print(all_value)
        return min(all_value)



if __name__ == "__main__":
    root = Tree("Root", 1)
    child_1 = Tree("Child_1", 10)
    child_2 = Tree("Child_2", 20)
    child_3 = Tree("Child_3", 30)
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child(child_3)

    print(child_3.min_value)
    print(child_1.min_value)