# The following dictionary contains a mapping from latin characters to morse code.
# Write a program that requests for a message from the user, encodes that message in morse code and prints the result.
# Note: If a morse code cannot be found for a character in the user's entry,
# simply use a question mark for that character in the encoded text

morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
         "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
         "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
         "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
         "7": "--...",
         "8": "---..",
         "9": "----.",
         ".": ".-.-.-",
         ",": "--..--"
         }

#  REMEMBER ALL THE KEY WORDS ARE STRING


#  chosen_string = input('Please insert a "String" :').upper()
# new_str = []
# for i in chosen_string:
#    print(morse.get(i, '?'))


chosen_string = input('Please insert a "String" :').upper()
new_str = ''
for i in chosen_string:
    new_str += morse.get(i, '?')
print(new_str)
