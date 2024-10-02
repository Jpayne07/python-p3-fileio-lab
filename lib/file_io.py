def write_file(file_name, file_content) :
    with open(f"{file_name}.txt", mode='w' ) as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a') as a_file:
        a_file.write(append_content)

def read_file(file_name):
    with open (f"{file_name}.txt", encoding='UTF-8') as test_file:
        return test_file.read()