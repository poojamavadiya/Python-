# Define a function to count the number of lines in a text file
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

file_path = 'myfile.txt'
line_count = count_lines_in_file(file_path)

print(f"The file {file_path} has {line_count} lines.")
