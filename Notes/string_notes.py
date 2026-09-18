# DL, String Notes

last_name ='Le'
first_name = "Dara"

# concatentition => add two string together
name = first_name + " " + last_name

# escape character lets the program ignore the next character in the string
print(f'{first_name} told the class "You can\'t drive my car."')

user = input("Please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence = "The quick brown fox jumped over the lazy dog."

print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", "cat"))
print(sentence.replace("dog",name))