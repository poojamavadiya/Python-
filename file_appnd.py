# Define a function to append text to a file and then display the file content
def append_and_display(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')
            print(f"Text successfully appended to {file_path}")

        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path}:\n{content}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = 'myfile.txt'
text_to_append = "This is a new line to be appended."
append_and_display(file_path, text_to_append)
