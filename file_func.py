# Define a function to read an entire text file
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

file_path = 'myfile.txt'
file_content = read_text_file(file_path)
print(file_content)
