# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', 
    ' ': '/'
}

def text_to_morse(text):
    text = text.upper()  # Convert to uppercase
    morse_code = []
    for letter in text:
        if letter in morse_code_dict:
            morse_code.append(morse_code_dict[letter])
        else:
            morse_code.append('?')  # For unsupported characters
    return ' '.join(morse_code)

def morse_to_text(morse):
    morse_words = morse.split(' / ')  # Split words
    decoded_message = []
    
    # Reverse the morse_code_dict for decoding
    reverse_dict = {value: key for key, value in morse_code_dict.items()}
    
    for word in morse_words:
        morse_letters = word.split()  # Split letters
        decoded_word = ''.join(reverse_dict.get(letter, '?') for letter in morse_letters)
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)

def main():
    while True:
        choice = input("Choose an option:\n1. Text to Morse\n2. Morse to Text\n3. Exit\nEnter your choice: ")
        
        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print("Morse Code:", text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code to convert to text (use '/' to separate words): ")
            print("Decoded Text:", morse_to_text(morse))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
