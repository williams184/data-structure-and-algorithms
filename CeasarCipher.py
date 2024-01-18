def rot13(str):
    decoded_str = ""
    for char in str:
        char_code = ord(char)

        if 65 <= char_code <= 90:  # Uppercase letters
            if char_code > 77:
                decoded_str += chr(char_code - 13)
            else:
                decoded_str += chr(char_code + 13)
        else:
            decoded_str += char

    return decoded_str

result = rot13('SERR PBQR PNZC')
print(result)
