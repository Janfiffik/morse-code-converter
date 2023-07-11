import time as tm
import os

print("______________Morse code encoder/decoder___________")
morse_alpha = ["._", '_...', "_._.", "_..", ".", '.._.', '__.',
               '....', '..', ".___", '_._', '._..', '__',
               '_.', '___', '.__.', '__._', '._.', '...', '_',
               '.._', '..._', '.__', '_.._', '_.__', '__..',
               " ",
               '.____', '..___', '...__', '...._', '.....',
               '_....', '__...', '___..', '____.', '_____']

alphabet = ['a', 'b', "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z",
            " ",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def encode(word):
    word = word.replace(" ", ', ')
    coded_word = ""
    for i in word:
        if i == ",":
            coded_word += ","
            continue
        i_ind = alphabet.index(i)
        coded_word += '{} '.format(morse_alpha[i_ind])
    print(coded_word)


def decode(morse_word):
    morse_word_list = [i for char in morse_word.split() for i in (char, ' ')]

    dec_word = ''
    for i in morse_word_list:
        if i == " ":
            continue
        elif i == ',':
            dec_word += " "
            continue

        i_ind = morse_alpha.index(i)
        dec_word += alphabet[i_ind]
    print(f"Translation: {dec_word}")


conv_m = True
while conv_m:
    de_en_ex = input("For encoding morse code: 'encode', for decoding morse code: 'decode' or exit 'exit':\n")
    if de_en_ex == 'encode':
        word = input("Enter your sentence for encoding to morse code:\n").lower()
        try:
            encode(word)
        except ValueError:
            print("Invalid input only letters and numbers.")
            tm.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        esc = input("For continue 'continue' or exit 'exit'?\n")

        if esc == 'continue':
            continue
        elif esc == 'exit':
            conv_m = False
        else:
            print("wrong input.")
            continue

    elif de_en_ex == 'decode':
        morse_word = input("Enter your morse code for decode:\n")
        decode(morse_word)

        esc = input("For continue 'continue' or exit 'exit'?\n")
        if esc == 'con':
            continue
        elif esc == 'exit':
            conv_m = False
        else:
            print("wrong input.")
            continue

    elif de_en_ex == 'exit':
        conv_m = False

    else:
        print("Invalid input. Just 'encode' for encoding, 'decode' for decoding or 'exit'.")
        continue
