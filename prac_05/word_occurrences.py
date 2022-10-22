word_to_occurrences = {}
words = input("Text: ")
words = words.split()
words = sorted(words)
for word in words:
    try:
        word_to_occurrences[word] += 1
    except KeyError:
        word_to_occurrences[word] = 1
max_length = max(len(string) for string in list(word_to_occurrences.keys()))
for string, occurrences in word_to_occurrences.items():
    print(f"{string:{max_length}} : {occurrences}")
