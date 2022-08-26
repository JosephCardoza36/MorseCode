
morse_code_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}



def morseCode(string):
    clean_string = string.lower()
    morse_code = [morse_code_dict[letter] for letter in clean_string if letter.isalpha()]

    return " ".join(morse_code)


def reverseCode(morse_code):
    word = []
    for code in morse_code.split(" "):
        keys = [word.append(k) for k, v in morse_code_dict.items() if v == code]

    return "".join(word).title()


word = input("Enter your word here: ")

print(morseCode(word))

print(reverseCode(".... . .-.. .-.. ---"))