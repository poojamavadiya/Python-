def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")


data_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
file_path = 'myfile.txt'  
write_list_to_file(file_path, data_list)

print(f"Data has been written to {file_path}")
