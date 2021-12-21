MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "/"}


def start_program():
    try:
        entry = ""
        while entry != 'QUIT':
            print("This program encodes your message into Morse Code.")
            print("If you want to quit the program, type 'quit'")
            entry = input("Please enter your message: ")
            entry = entry.upper()
            morse = ""
            for letter in entry:
                morse += f"{MORSE_CODE_DICT[letter]} "
            print(morse)
    except KeyboardInterrupt:
        print("\nProgram finished with click interception.")


if __name__ == '__main__':
    start_program()
    print("Thank you for using the program.")
