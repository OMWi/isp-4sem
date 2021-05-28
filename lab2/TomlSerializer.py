import toml
from Converter import to_dict, from_dict

#not working

class TomlSerializer:
    def dumps(self, object):
        return toml.dumps(object)

    def dump(self, object, filePath):
        with open(filePath, "w") as file:
            toml.dump(object, file)
    
    def loads(self, string):
        return toml.loads(string)


    def load(self, filePath):
        with open(filePath, "r") as file:
            return toml.load(file)