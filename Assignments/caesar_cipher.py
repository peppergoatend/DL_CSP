# DL, Caesar Cipher

def caesar_shift(message, shift):
    result = ""

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                number = ord(letter)
                number = number - ord("A")
                number = (number + shift) % 26
                number = number + ord("A")
                result += chr(number)
            else:
                number = ord(letter)
                number = number - ord("a")
                number = (number + shift) % 26
                number = number + ord("a")
                result += chr(number)
        else:
            result += letter

    return result


choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()

message = input("Enter your message: ")

shift = int(input("Enter a shift amount: "))

if choice == "E":
    result = caesar_shift(message, shift)
    print(f"Your encrypted message is: {result}")

elif choice == "D":
    result = caesar_shift(message, -shift)
    print(f"Your decrypted message is: {result}")
