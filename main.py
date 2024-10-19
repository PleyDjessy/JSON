import json
from JSONWorker import JSONWorker


data = [{"shop": "1", "magazine": "2", "smth": "3"}, {"why": "not"}, {"X": "D"}]
my_data = JSONWorker(data)

print(my_data.create_json_file("beginning"))
print(my_data.json_reader("beginning"))
print(my_data.json_reader("beginning.json"))

print(my_data.json_reader("begin"))