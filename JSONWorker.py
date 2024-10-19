class JSONWorker:
    def __init__(self, json_data):
        if json_data is list and len(json_data) == 3:
            if json_data[0] is dict and json_data[1] is dict and json_data[2] is dict:
                self.__json_data = json_data
            else:
                print("Некорректный тип данных!")
                raise ValueError
        else:
            print("Некорректный тип данных!")
            raise ValueError

