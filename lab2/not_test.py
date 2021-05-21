from JsonSerializer import JsonSerializer
from PickleSerializer import PickleSerializer
from YamlSerializer import YamlSerializer
from TomlSerializer import TomlSerializer
from Converter import *



def someFunc(a):
    return a**3

def anotherFunc():
    print("!dlrow olleh")

glob = 4

class UselessClass:
    uselessVariable = 1
    def __init__(self, number):
        self.usefulVariable = number

def main():
    simple_dict = {
        "something" : 42,
        "name" : "omwi",
        "location" : "nowhere"
    }
    complex_dict = {
        "person" : {
            "name" : "vladislav",
            "age" : 18,
            "location" : "minsk",
        },
        "computer" : 1
    }
    list = [1, 2, "something"]
    set = {1, 2, "3"}
    tuple = ()
    class_object = UselessClass(4)
    print(dir(class_object))



    print("simple_dict:\n", to_dict(simple_dict))
    print("complex_dict\n", to_dict(complex_dict))
    print("list:\n", to_dict(list))
    print("class:\n", to_dict(UselessClass))
    print("class_object:\n", to_dict(class_object))
    print("func:\n", to_dict(someFunc))
    print("glob:\n", glob)
    print("\nchecking builtin json\n")
    my_json = JsonSerializer()

    #res = json.dumps(class_object)
    #print(res)
    res = my_json.dumps(someFunc)
    print(res)
    new = my_json.loads(res)
    new()



if __name__ == '__main__':
    main()