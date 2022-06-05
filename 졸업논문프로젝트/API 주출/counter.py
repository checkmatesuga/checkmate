from collections import Counter

def count_word(file_name):
        with open(file_name) as f:
                return Counter(f.read().split())

print("Frequency :",count_word("white.csv"))