import toml
from Converter import to_dict, from_dict

#not working

class TomlSerializer:
    def dumps(self, object):
        return toml.dumps(to_dict(object))

    def dump(self, object, filePath):
        with open(filePath, "w") as file:
            toml.dump(to_dict(object), file)
    
    def loads(self, string):
        return from_dict(toml.loads(string))


    def load(self, filePath):
        with open(filePath, "r") as file:
            return from_dict(toml.load(file))