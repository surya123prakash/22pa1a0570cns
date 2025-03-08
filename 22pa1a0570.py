def caesar_cipher(text, shift):
    result = ""
    
    for char in text:    
        if char.isupper():        
            result += chr((ord(char) + shift - 65) % 26 + 65)     
        elif char.islower():          
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:           
            result += char
            
    return result


if __name__ == "__main__":
    text = "This Is Surya!"  
    shift = 3  
    encrypted = caesar_cipher(text, shift)  
    print(f"Encrypted Text: {encrypted}")

    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted Text: {decrypted}")
def caesar_cipher(text, shift):
    result = ""
        
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower(): 
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else: 
            result += char
            
    return result

# Test the Caesar Cipher
if __name__ == "__main__":
    text = "This Is Surya!"  
    shift = 3 
    encrypted = caesar_cipher(text, shift)
    print(f"Encrypted Text: {encrypted}")

    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted Text: {decrypted}")
