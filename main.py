def display(l):
    res = ""
    for x in l:
        res += x 
    print(res)

def caesarCipher(s,n):
    s = list(s)
    new_str = []
    for x in s:
        if(ord(x) + n > 122): 
            new_str.append(chr(ord(x) + n - 26))
        else:
            new_str.append(chr(ord(x) + n))
    return str(new_str)



while(True):
    user_input = input("Enter '0' to exit the program | Enter the string you want to encrypt:\n")
    if(user_input == str(0)):
        break
    encryption_method = input("Select the encryption method:\n")

    if(encryption_method == str(1)):
        caesar_val = input("Enter the number of rotation (between 1-25):\n")
        res = caesarCipher(user_input, int(caesar_val))
        display(res)