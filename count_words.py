from collections import Counter
import re

def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_count = Counter(words)
    
    return word_count

if __name__ == "__main__":
    file_path = 'myfile.txt'  
    word_frequencies = count_word_frequency(file_path)
    
    for word, freq in word_frequencies.items():
        print(f"{word}: {freq}")
