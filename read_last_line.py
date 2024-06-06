# Define a function to read the last n lines of a text file
def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'rb') as file:
            file.seek(0, 2)
            pointer = file.tell()
            lines = []
            buffer = bytearray()
            while pointer >= 0 and len(lines) < n:
                file.seek(pointer)
                buffer.extend(file.read(1))
                if buffer.endswith(b'\n'):
                    lines.append(buffer.decode('utf-8')[::-1])
                    buffer = bytearray()
                pointer -= 1
            if buffer:
                lines.append(buffer.decode('utf-8')[::-1])
            for line in reversed(lines[:n]):
                print(line, end='')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'myfile.txt'

n = 3
read_last_n_lines(file_path, n)
