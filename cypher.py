import string
import random
from os import system, name
from time import sleep 
alphabet = list(string.ascii_lowercase)

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
   
    else: 
        _ = system('clear') 

def crypt(message,key) :
    crypted = list()
    for i in range(len(message)) :
        rotation = key[i % len(key)].lower()
        crypted.append(alphabet[(alphabet.index(rotation) + alphabet.index(message[i].lower())) % 26])
    return "".join(crypted)

def decrypt(crypted,key) :
    message =list()
    for i in range(len(crypted)) :
        rotation = key[i % len(key)].lower()
        message.append(alphabet[(26 + alphabet.index(crypted[i].lower()) - alphabet.index(rotation)) % 26])
    return "".join(message)

def showMenu() :
    print("---------------------")
    print("|--vigenère cypher--|")
    print("---------------------")
    print("|1-Crypt a message  |")
    print("---------------------")
    print("|2-decrypt a message|")
    print("---------------------")
    print("|3-change key       |")
    print("---------------------")
    print("|4-quit program     |")
    print("---------------------")

def keyMenu() :
    print("---------------------")
    print("|--vigenère cypher--|")
    print("---------------------")
    print("|1-enter key        |")
    print("---------------------")
    print("|2-random key       |")
    print("---------------------")

turn = 0
message =''
key= list()
answer= 0
while(answer!=1 and answer!=2) :
    keyMenu()
    answer=int(input("Choose an option : "))
    if(answer==1) :
        key=input("Enter key : ")
    elif(answer==2):
        key=''
        for i in range (random.randint(3,15)) :
            key.append(alphabet[random.randint(0,25)])
        key=str(key)
    else :
        print("wrong option!")

while(answer!=4) :
    
    
    
    answer=0
    while(answer!=3 and answer!=4) :
        clear()
        showMenu()
        answer=int(input("choose your answer : "))
        if(answer == 1) :
            message=input("enter message you want to encrypt : ")
            print("Message : "+message)
            print("encrypted message : "+crypt(message,key))
            input()
        elif(answer == 2) :
            message=input("enter message you want to decrypt : ")
            print("encrypted message : "+message)
            print("decrypted message : "+decrypt(message,key))
            input()
            
        elif(answer == 3) :
            while(answer!=1 and answer!=2) :
                clear()
                keyMenu()
                answer=int(input("Choose an option : "))
                if(answer==1) :
                    key=input("Enter key : ")
                elif(answer==2):
                    key=''
                    for i in range (random.randint(3,15)) :
                        key.append(alphabet[random.randint(0,25)])
                    key=str(key)
                else :
                    print("wrong option!")
        
        elif(answer == 4) :
            pass

        else :
            print("wrong answer ")
            sleep(2)






