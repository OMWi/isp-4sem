from serializers.JsonSerializer import JsonSerializer
from serializers.PickleSerializer import PickleSerializer
from serializers.YamlSerializer import YamlSerializer
from serializers.TomlSerializer import TomlSerializer
from serializers.Converter import *


class UselessClass:
    uselessVariable = 1
    def __init__(self, number):
        self.usefulVariable = number

def main():
    print(type(None))
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
    print(list_to_dict(list))

    #json = JsonSerializer()

    #json.dump(simple_dict, "simple.json")
    #json.dump(complex_dict, "complex.json")

if __name__ == '__main__':
    main()