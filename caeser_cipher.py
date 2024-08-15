def caesar_cipher(text, shift, direction):
    result=""
    for ch in text:
        if ch.isalpha():
            shift_amount=shift if direction=="encrypt" else -shift
            shifted_char=chr((ord(ch) - 65 + shift_amount) % 26 + 65) if ch.isupper() else chr((ord(ch) - 97 + shift_amount) % 26 + 97)
            result+=shifted_char
        else:
            result+=ch
    return result

def main():
    while True:
        direction = input("Input 'encrypt' to encrypt OR 'decrypt' to decrypt : ").lower()
        if direction not in ['encrypt','decrypt'] :
            print("Invalid Input, Kindly enter a valid input")
            continue
        message = input("Enter your message : ")
        shift = int(input("Enter the shift value : "))
        result = caesar_cipher(message, shift, direction)
        print(f"The {direction}ed message is {result}")
        if input("Do you want to attempt again? (yes/no) : ").lower() == 'no':
            break

if __name__ == "__main__":
    main()
