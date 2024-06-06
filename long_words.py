# Define a function to find the longest words in a text file
def find_longest_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            words = content.split()
            max_length = max(len(word) for word in words)
            
            longest_words = [word for word in words if len(word) == max_length]
            
        return longest_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'myfile.txt'
longest_words = find_longest_words(file_path)
print("Longest words:", longest_words)
