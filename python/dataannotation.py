def decode(message_file):
    word_dict = {}
    
    with open(message_file, "r") as f:
        for line in f:
            number, word = line.strip().split()
            number = int(number)
            word_dict[number] = word
    
    decoded_words = []
    
    pyramid_size = len(word_dict)
    for i in range(1, pyramid_size + 1):
        decoded_words.append(word_dict[i])
    
    return " ".join(decoded_words)

file_path = "coding_qual_input.txt"
decoded_message = decode(file_path)
print(decoded_message)
