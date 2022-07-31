from nbformat import read


def read_file():
    with open('logs.txt', 'r') as file:
        data = file.read()
    return data
        
logs = read_file()