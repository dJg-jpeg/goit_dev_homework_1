from abc import abstractmethod, ABC
import json
import pickle

PATH_TO_BIN_FILE = "pickle_data.bin"
PATH_TO_JSON_FILE = "json_data.json"


class SerializationInterface(ABC):

    def __init__(self):
        self.data = None

    @abstractmethod
    def save(self):
        """Saving data to file method"""

    @abstractmethod
    def load(self):
        """Loading from file method"""


class JsonData(SerializationInterface):
    """Serialization into json file class"""

    def save(self):
        with open(PATH_TO_JSON_FILE, 'w') as json_file:
            json.dump(self.data, json_file)

    def load(self):
        with open(PATH_TO_JSON_FILE, 'r') as json_file:
            self.data = json.load(json_file)


class BinData(SerializationInterface):
    """Serialization into bin file class"""

    def save(self):
        with open(PATH_TO_BIN_FILE, 'wb') as bin_file:
            pickle.dump(self.data, bin_file)

    def load(self):
        with open(PATH_TO_BIN_FILE, 'rb') as bin_file:
            self.data = pickle.load(bin_file)


if __name__ == "__main__":
    data_to_json = JsonData()
    data_to_json.data = {
        'key': 'value',
        '2': [1, 2, 3],
        'a': {'key': 'value'},
    }

    data_to_bin = BinData()
    data_to_bin.data = data_to_json

    data_to_json.save()
    data_to_bin.save()

    unpacked_json_data = JsonData()
    unpacked_json_data.load()

    unpacked_bin_data = BinData()
    unpacked_bin_data.load()

    print(data_to_json.data == unpacked_json_data.data)
    print(data_to_bin.data.data == unpacked_bin_data.data.data)
