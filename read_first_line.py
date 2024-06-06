# Define a function to read the first n lines of a text file
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break  
                print(line, end='')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'myfile.txt'
n=3
read_first_n_lines(file_path, n)
