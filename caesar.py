def encrypt(text, rot)
    new_text = ''
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWUXYZ'
    low_aplha = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if char is.alpha():
            if char is.upper():
                position = up_alpha.index(char)
                new_text += up_alpha[position + (rot % 26)]
            elif char is.lower():
                position = low_aplha.index(char)
                new_text += low_aplha[position + (rot % 26)]
        elif char == ' ':
            new_text += ' '
        else:
            new_text += char
    return new_text

def main():
    text = input("Type a message:")
    rot = input("Rotate by:")
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()