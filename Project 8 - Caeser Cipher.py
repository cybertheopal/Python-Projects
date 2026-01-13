alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser_cipher(original_text, shift_num, encode_decode): #Creates the ceaser_cipher function with the parameters in (). similar to creating a variable.
    cipher_text = "" #variable that will cold translated cipher text.
    if encode_decode == "decode":  # Dictates if text will be encrypted or decrypted by making the shift number a negative if decoded is selected.
        shift_num *= -1
    for letter in original_text: #Loops through all the letters in the input text.
        if letter in alphabet: #Loops through alphabet list. and executes the following if it finds the letter.
            new_index = (alphabet.index(letter) + shift_num) % 26 #find the index number (place in table) of the letter, pulls it and add the shift number to it then modulos it to ensure looping the table can happen if need be.
            new_text = alphabet[new_index] #Takes the new index location and identifies what letter it is.
            cipher_text += new_text #Adds the new letter to the cipher text variable.
        else:
            cipher_text += letter #If letter is not in alphabet (ex. spaces and symbols), just add it straight to the cipher_text variable as is.
    print(cipher_text)

end_cipher = False #Sets condition for loop
while not end_cipher: #Begins loop
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() #Input form user
    text = input("Type your message:\n").lower() #Input form user
    shift = int(input("Type the shift number:\n")) #Input form user
    caeser_cipher(text, shift, direction) #Calls the function we created. Used the user input as arguments.

    loop_end = input("Would you like to encrypt/decrypt anything else? Y/N: ").lower() #Asking user if they are done encoding.
    if loop_end != "y": #If answer is anything but "Y/y" the while loop will end.
        end_cipher = True #Changed condition for while loop so loop ends.
        print("Cipher decipher complete.")
