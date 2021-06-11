from serializer import *

fp = open('file.json', 'r')

ser = JsonSerializer()

obj = {"pepega": 223, "2": (1, 2, "string")}
new_obj =ser.load(fp)

print(obj == new_obj)
print(new_obj)
