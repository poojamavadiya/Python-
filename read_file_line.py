# Define a function to read a file line by line and store each line into a list
def read_file_to_list(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


file_path = 'myfile.txt'
lines_list = read_file_to_list(file_path)
print(lines_list)
