import pytest
from JsonSerializer import JsonSerializer
from PickleSerializer import PickleSerializer
from YamlSerializer import YamlSerializer
from TomlSerializer import TomlSerializer
from Factory import Factory

factory = Factory()

name = "user"

def foo():
    print("hello, {}".format(name))

def foo_recursion(num):
    if num == 0:
        return 0
    return foo_recursion(num / 3)

class UselessClass:
    uselessVariable = 1

    def __init__(self, number):
        self.usefulVariable = number

    def say(self, name):
        print("hello, {}".format(name))

    
def list_test(format : str):
    serializer = factory.createSerializer(format)


def func_test(format : str):
    serializer = factory.createSerializer(format)



def object_test(format : str):
    serializer = factory.createSerializer(format)
    exmp = UselessClass(13)
    exmp.list = [[1, 2], 3]
    exmp.tuple = (1, (2, 3))
    exmp.set = {1, 2 , 3}
    exmp.none = None
    exmp_copy = serializer.loads(serializer.dumps(exmp))
    assert exmp_copy.uselessVariable == exmp.uselessVariable
    assert exmp_copy.usefulVariable == exmp.usefulVariable
    assert exmp_copy.list == exmp.list
    assert exmp_copy.tuple == exmp.tuple
    assert exmp_copy.set == exmp.set
    assert exmp_copy.none == exmp.none
    file_name = "testfile." + format
    serializer.dump(exmp, file_name)
    exmp_copy = serializer.load(file_name)
    assert exmp_copy.uselessVariable == exmp.uselessVariable
    assert exmp_copy.usefulVariable == exmp.usefulVariable
    assert exmp_copy.list == exmp.list
    assert exmp_copy.tuple == exmp.tuple
    assert exmp_copy.set == exmp.set
    assert exmp_copy.none == exmp.none


def class_test(format : str):
    serializer = factory.createSerializer(format)

@pytest.mark.json
def test_json():
    format = "json"
    list_test(format)
    func_test(format)
    object_test(format)
    class_test(format)


@pytest.mark.yaml
def test_yaml():
    format = "yaml"
    list_test(format)
    func_test(format)
    object_test(format)
    class_test(format)

@pytest.mark.pickle
def test_pickle():
    format = "pickle"
    list_test(format)
    func_test(format)
    object_test(format)
    class_test(format)

@pytest.mark.toml
def test_toml():
    format = "toml"
    list_test(format)
    func_test(format)
    object_test(format)
    class_test(format)

test_json()
test_pickle()
test_yaml()
test_toml()