from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text,shift_amount,cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
        shift_amount *= -1
  for letter in start_text:
    if  letter in alphabet:

      position = alphabet.index(letter)
      new_position = position + shift_amount      
      new_position = new_position % len(alphabet)
      end_text += alphabet[new_position]

    else:
      end_text += letter

  print(f"your {cipher_direction}d text is : '{end_text}'")
  

print(logo)
restart_1 = True
while restart_1:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(start_text=text,shift_amount=shift,cipher_direction=direction)


  restart_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if restart_again == "yes":
    restart_1 = True
  elif restart_again =="no":
    print("GOOD BYE !")
    restart_1 = False
