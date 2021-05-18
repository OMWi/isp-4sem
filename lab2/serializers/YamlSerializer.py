import yaml
from serializers.Converter import from_dict, to_dict

class YamlSerializer:
    def dumps(self, object):
        return yaml.dumps(to_dict(object))

    def dump(self, object, filePath):
        with open(filePath, "wb") as file:
            yaml.dump(to_dict(object), file)
    
    def loads(self, string):
        return from_dict(yaml.loads(string))


    def load(self, filePath):
        with open(filePath, "rb") as file:
            return from_dict(yaml.load(file))