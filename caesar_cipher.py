#Caesar Cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
j='yes'
while j=='yes':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt : \n")
    text = input("Type your message : ").lower()
    shift = int(input("Type the shift number:\n"))
    zo=1
    if shift>26:
        shift=shift%26
                
                
            
    def caesar(plain_text, shift_amount):
        #print("jola")
        char=""
        j="yes"
        
        if direction == 'encode':
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_pos = position+shift_amount
                    char+=alphabet[new_pos]
                else:
                    char+=letter
            print("Encrypted text : ",char)
            
        elif direction == 'decode':
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_pos = position-shift_amount
                    char+=alphabet[new_pos]
                else:
                    char+=letter
            print("Decrypted text : ",char)
                
        else:
            print("Enter correct keyword")
        #    j=input("Enter 'yes' if you wanna continue or else 'no'")
        
    caesar(plain_text=text,shift_amount=shift)
    j=input("if you wanna continue enter 'yes' or else enter 'no' : \n")


        