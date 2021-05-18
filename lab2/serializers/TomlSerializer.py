import toml
from serializers.Converter import from_dict, to_dict

class TomlSerializer:
    def dumps(self, object):
        return toml.dumps(to_dict(object))

    def dump(self, object, filePath):
        with open(filePath, "wb") as file:
            toml.dump(to_dict(object), file)
    
    def loads(self, string):
        return from_dict(toml.loads(string))


    def load(self, filePath):
        with open(filePath, "rb") as file:
            return from_dict(toml.load(file))