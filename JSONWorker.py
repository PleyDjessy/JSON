import json


class JSONWorker:
    def __init__(self, json_data):
        if type(json_data) is list and len(json_data) == 3:
            if type(json_data[0]) is dict and type(json_data[1]) is dict and type(json_data[2]) is dict:
                self.__json_data = json_data
            else:
                print("Некорректный тип данных!")
                raise ValueError
        else:
            print("Некорректный тип данных!")
            raise ValueError

    def create_json_file(self, filename):
        json_file = f"{filename}.json"
        with open(json_file, "w", encoding="utf-8") as file:
            data = json.dumps(self.__json_data, ensure_ascii=False, indent=2)
            file.write(data)
        return "Запись успешна"

    @staticmethod
    def json_reader(filename):
        try:
            with open(filename, "r", encoding="utf-8") as fp:
                data = json.load(fp)
            return data
        except FileNotFoundError:
            return "Такого файла нет!"


