def encrypt(name, tmp): 
    rlt = ""  
    tmp=tmp-1
    
    for i in range(len(name)):  
        char = name[i]  
        if (char.isupper()):  
            rlt += chr((ord(char) + tmp - 64) % 26 + 65)  
        elif(char.islower()): 
            rlt += chr((ord(char) + tmp - 96) % 26 + 97)  
        else:
            rlt+= char
    return rlt  

test = "Ekta Nariya"  #Name
key = 4               #Birthdate
  
print("Plain text : " + test)  
print("Encrypted text: " + encrypt(test, key))
