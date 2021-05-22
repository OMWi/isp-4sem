import pytest
from JsonSerializer import JsonSerializer
from PickleSerializer import PickleSerializer
from YamlSerializer import YamlSerializer
from TomlSerializer import TomlSerializer
from Factory import Factory

factory = Factory()
    
def list_test(format : str):
    serializer = factory.createSerializer(format)
    fileName = "test." + format
    list = [[1, 2], "string", 0.45]
    loaded = serializer.loads(serializer.dumps(list))
    assert list == loaded
    serializer.dump(list, fileName)
    loaded = serializer.load(fileName)
    assert list == loaded

def set_test(format : str):
    serializer = factory.createSerializer(format)
    fileName = "test." + format
    set = {"cow", 1, False, None}
    loaded = serializer.loads(serializer.dumps(set))
    for elem in set:
        assert elem in set
    serializer.dump(set, fileName)
    loaded = serializer.load(fileName)
    for elem in set:
        assert elem in set

def tuple_test(format : str):
    serializer = factory.createSerializer(format)
    fileName = "test." + format
    tuple = ((1, 2), 3)
    loaded = serializer.loads(serializer.dumps(tuple))
    assert tuple == loaded
    serializer.dump(tuple, fileName)
    loaded = serializer.load(fileName)
    assert tuple == loaded
    
def dict_test(format : str):
    serializer = factory.createSerializer(format)
    fileName = "test." + format
    dict = {
        "person" : {
            "name" : "vladislav",
            "age" : 18,
            "location" : "minsk",
        },
        "computer" : 1
    }
    loaded = serializer.loads(serializer.dumps(dict))
    assert dict == loaded
    serializer.dump(dict, fileName)
    loaded = serializer.load(fileName)
    assert dict == loaded

def simple_func_test(format : str):
    serializer = factory.createSerializer(format)
    fileName = "test." + format
    def simple_func():
        return 5
    loaded = serializer.loads(serializer.dumps(simple_func))
    assert loaded() == simple_func()
    serializer.dump(simple_func, fileName)
    loaded = serializer.load(fileName)
    assert loaded() == simple_func()

def recursion_func_test(format : str):
    serializer = factory.createSerializer(format)    
    fileName = "test." + format
    def recursion_func(num):
        if num < 0:
            return 1
        return num * recursion_func(num // 3)
    loaded = serializer.loads(serializer.dumps(recursion_func))
    assert loaded(4) == recursion_func(4)
    assert loaded(-432) == recursion_func(-432)
    serializer.dump(recursion_func, fileName)
    loaded = serializer.load(fileName)
    assert loaded(4) == recursion_func(4)
    assert loaded(-432) == recursion_func(-432)

var = 24
def globs_builtins_func_test(format : str):
    serializer = factory.createSerializer(format)  
    
    fileName = "test." + format 
    def foo():
        print("hello", var)
        return var
    loaded = serializer.loads(serializer.dumps(foo))
    assert foo() == loaded()
    serializer.dump(foo, fileName)
    loaded = serializer.load(fileName)
    assert foo() == loaded()
    

def lambda_test(format : str):
    serializer = factory.createSerializer(format)
    
    fileName = "test." + format
    foo = lambda x : x // 2
    loaded = serializer.loads(serializer.dumps(foo))
    assert foo(4) == loaded(4)
    assert foo(-123) == loaded(-123)
    serializer.dump(foo, fileName)
    loaded = serializer.load(fileName)
    assert foo(4) == loaded(4)
    assert foo(-123) == loaded(-123)
    

class UselessClass:
    uselessVariable = 1
    def __init__(self, number):
        self.usefulVariable = number

def class_test(format : str):
    serializer = factory.createSerializer(format)
    # todo: segmentation error in toml here
    # todo: differences in classes here
    fileName = "test." + format
    loaded = serializer.loads(serializer.dumps(UselessClass))
    assert loaded.uselessVariable == UselessClass.uselessVariable
    # assert dir(loaded) == dir(UselessClass)
    serializer.dump(UselessClass, fileName)
    loaded = serializer.load(fileName)
    assert loaded.uselessVariable == UselessClass.uselessVariable
    # assert dir(loaded) == dir(UselessClass)
    
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

#json tests

@pytest.mark.json
def test_1_json():
    list_test("json")

@pytest.mark.json
def test_2_json():
    set_test("json")

@pytest.mark.json
def test_3_json():
    tuple_test("json")

@pytest.mark.json
def test_4_json():
    dict_test("json")

@pytest.mark.json
def test_5_json():
    simple_func_test("json")

@pytest.mark.json
def test_6_json():
    recursion_func_test("json")

@pytest.mark.json
def test_7_json():
    globs_builtins_func_test("json")

@pytest.mark.json
def test_8_json():
    lambda_test("json")

@pytest.mark.json
def test_9_json():
    class_test("json")

@pytest.mark.json
def test_10_json():
    object_test("json")

#pickle tests

@pytest.mark.pickle
def test_1_pickle():
    list_test("pickle")

@pytest.mark.pickle
def test_2_pickle():
    set_test("pickle")

@pytest.mark.pickle
def test_3_pickle():
    tuple_test("pickle")

@pytest.mark.pickle
def test_4_pickle():
    dict_test("pickle")

@pytest.mark.pickle
def test_5_pickle():
    simple_func_test("pickle")

@pytest.mark.pickle
def test_6_pickle():
    recursion_func_test("pickle")

@pytest.mark.pickle
def test_7_pickle():
    globs_builtins_func_test("pickle")

@pytest.mark.pickle
def test_8_pickle():
    lambda_test("pickle")

@pytest.mark.pickle
def test_9_pickle():
    class_test("pickle")

@pytest.mark.pickle
def test_10_pickle():
    object_test("pickle")

#yaml tests

@pytest.mark.yaml
def test_1_yaml():
    list_test("yaml")

@pytest.mark.yaml
def test_2_yaml():
    set_test("yaml")

@pytest.mark.yaml
def test_3_yaml():
    tuple_test("yaml")

@pytest.mark.yaml
def test_4_yaml():
    dict_test("yaml")

@pytest.mark.yaml
def test_5_yaml():
    simple_func_test("yaml")

@pytest.mark.yaml
def test_6_yaml():
    recursion_func_test("yaml")

@pytest.mark.yaml
def test_7_yaml():
    globs_builtins_func_test("yaml")

@pytest.mark.yaml
def test_8_yaml():
    lambda_test("yaml")

@pytest.mark.yaml
def test_9_yaml():
    class_test("yaml")

@pytest.mark.yaml
def test_10_yaml():
    object_test("yaml")


#toml tests

@pytest.mark.toml
def test_1_toml():
    list_test("toml")

@pytest.mark.toml
def test_2_toml():
    set_test("toml")

@pytest.mark.toml
def test_3_toml():
    tuple_test("toml")

@pytest.mark.toml
def test_4_toml():
    dict_test("toml")

@pytest.mark.toml
def test_5_toml():
    simple_func_test("toml")

@pytest.mark.toml
def test_6_toml():
    recursion_func_test("toml")

@pytest.mark.toml
def test_7_toml():
    globs_builtins_func_test("toml")

@pytest.mark.toml
def test_8_toml():
    lambda_test("toml")

@pytest.mark.toml
def test_9_toml():
    class_test("toml")

@pytest.mark.toml
def test_10_toml():
    object_test("toml")