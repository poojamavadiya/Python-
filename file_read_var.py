# Define a function to read a file line by line and store each line into a variable
def read_file_to_variable(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'myfile.txt'
lines_variable = read_file_to_variable(file_path)
for line in lines_variable:
    print(line, end='')
