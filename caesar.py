import string

def alphabet_position(letter):
    letter = letter.lower()   # force lower case
    position = ord(letter) - ord("a")     # position based on delta from "a"
    return (position)

def rotate_character(char, rot):
    if char.lower() in string.ascii_lowercase:
        rotate_char_pos = (alphabet_position(char) + rot) % 26   # determine position of rotated char
        rotate_char = chr(ord("a") + rotate_char_pos)
        if char in string.ascii_uppercase:
            return rotate_char.upper()
        else:
            return rotate_char
    else:    # non alpha character
        return char     # just return input

def encrypt(text, rot):
    encrypt_str = ""    # start with empty string
    for char in text:
        encrypt_str = encrypt_str + rotate_character(char, rot)
    return encrypt_str
