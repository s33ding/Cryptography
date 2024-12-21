import json
import pickle
import sys

class FileHandler:
    def __init__(self, file_name=None):
        print("file_name:",file_name)
        self.file_name = self.get_file_name(file_name)
        self.data_handler = self.create_handler(self.file_name)

    def get_file_name(self,file_name):
        if file_name is not None:
            return file_name
        else:
            if len(sys.argv) > 1:
                return sys.argv[1]
            return input("Enter file name: ")

    def read_file(self):
        print("reading:",self.file_name)
        return self.data_handler.read_file()

    def create_handler(self, file_name):
#        print("handling:", file_name)
        print("")
        if file_name.endswith('.json'):
#            print("stating: JsonFileHandler")
            return JsonFileHandler(file_name)
        elif file_name.endswith('.pickle') or file_name.endswith('.pkl'):
#            print("stating: PickleFileHandler")
            return PickleFileHandler(file_name)
        else:
#            print("stating: TextFileHandler")
            return TextFileHandler(file_name)

    def write_file(self, data):
        print("writing:",self.file_name)
        self.data_handler.write_file(data)

class JsonFileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file_name = self.file_name 
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except Exception as e:
            print("Error:", str(e))
            return None

    def write_file(self, data):
        file_name = self.file_name 
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Error:", str(e))

class PickleFileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file_name = self.file_name 
        try:
            with open(file_name, 'rb') as f:
                data = pickle.load(f)
                print(f"Successfully read pickle file: {file_name}")
                return data
        except FileNotFoundError:
            print(f"Error: file {file_name} not found")
        except pickle.UnpicklingError:
            print(f"Error: invalid pickle file {file_name}")

    def write_file(self, data):
        file_name = self.file_name 
        try:
            # Directly from dictionary
            with open(file_name, 'wb') as outfile:
                pickle.dump(data, outfile)
        except:
            print("erro")


class TextFileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file_name = self.file_name 
        try:
            with open(self.file_name, 'r') as file:
                return file.read()
        except Exception as e:
            print("Error:", str(e))
            return None

    def write_file(self, data):
        file_name = self.file_name 
        try:
            with open(file_name, 'w') as file:
                file.write(data)
        except Exception as e:
            print("Error:", str(e))
