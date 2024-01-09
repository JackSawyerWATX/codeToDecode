def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers from each line and build the pyramid
    pyramid = []
    for line in lines:
        words = line.split()
        numbers = [int(word) for word in words if word.isdigit()]
        pyramid.append(numbers)

    # Flatten the pyramid to get the selected words
    selected_words = [word for row in pyramid for word in row]

    # Read the corresponding words from the file
    decoded_message = []
    with open(message_file, 'r') as file:
        words = file.read().split()
        for number in selected_words:
            decoded_message.append(words[number - 1])

    # Combine the words into a string
    result = ' '.join(decoded_message)
    
    return result

# Example usage
message_file = 'example.txt'
decoded_message = decode(message_file)
print(decoded_message)
