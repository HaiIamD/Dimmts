#!/usr/bin/env python
# coding: utf-8

# In[7]:


## PLAYFAIR CHIPER

##  Antka Ananda - 4332111018          ##
##  Dimas Toriq Sibarani - 4332111006  ##
##  Shinta Aishah - 4332111024         ##
##  ABDULLAH HASIHOLAN - 4332111004    ##
##  Muhammad Fadilla A - 4332111028    ##
##  Tsania putri maharani - 4332111011 ##


# Memasukkan Key dan menghapus spasi pada key serta membuat key menjadi upper case
key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: 
    if c not in result:# Mengubah huruf J ke I
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #Menyimpan karakter sebanyak 25 aplhabet
    if chr(i) not in result:
        if i==73 and chr(74) not in result: # Memeriksa huruf i dan j
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) # Membuat matrik dengan besar 5 x 5 
for i in range(0,5): 
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): # Mencari tempat setiap karakter yang ada dalam matrix
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Melakukan encryptsi pada playfair
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):# mencari lokasi setiap karakter yang ada 
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]: # menambah tabel pada matrix untuk memperluas kunci yang baru
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #Melakukan decrypt pada playfair
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):# mencari lokasi setiap karakter yang ada 
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1): # Pilihan menu awal untuk memilih enkrip or dekripsi
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")


# In[ ]:





# In[ ]:





# In[9]:


## VIGENERE CHIPER


from string import punctuation # Mengimpor library


class payload:     # pembagian class 
    def __init__(self, text=str(), key=str(), encrypted=str()):
        self.text = text
        self.key = key
        self.encrypted = encrypted
        self.intermediate_encrypted = ""

    def vigenereGenerateKeyDecryption(self, vigenere_string, vigenere_key):   # Fungsi untuk pemanggilan kunci Dekripsi
        vigenere_key = list(vigenere_key)
        if len(vigenere_string) == len(vigenere_key):
            return(vigenere_key)
        else:
            for i in range(len(vigenere_string) - len(vigenere_key)):
                vigenere_key.append(vigenere_key[i % len(vigenere_key)])
        return("" . join(vigenere_key))

    def vigenereOriginalTextDecryption(self, vigenere_decrypt_cipher_text, vigenere_key): #Fungsi untuk pemanggilan cipher text
        vigenere_orig_text = []
        for i in range(len(vigenere_decrypt_cipher_text)):
            x = (
                ord(vigenere_decrypt_cipher_text[i]) - ord(vigenere_key[i]) + 26) % 26
            x += ord('A')
            vigenere_orig_text.append(chr(x))
        return("" . join(vigenere_orig_text))

    def generateVigenereKeyEncryption(self, string, key):  #fungsi Enkripsi kunci
        count = 0
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                count += 1
                key.append(key[i % len(key)])
        return("" . join(key))

    def vcipherTextEncryption(self, string, key):   # Fungsi Enkripsi Chiper text
        vigenere_cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            vigenere_cipher_text.append(chr(x))
        return("" . join(vigenere_cipher_text))

    def encrypt(self):
        #  encryption starts ( mulai enkripsi)
        string = self.text.upper()
        keyword = self.key.upper()
        processedTextList = []
        processedText = ""

        for i in string:
            if i not in (punctuation + " " + "0123456789"):
                processedText += i
            else:
                processedTextList.append(processedText)
                processedTextList.append(i)
                processedText = ""
        if processedText != "":
            processedTextList.append(processedText)
        while '' in processedTextList:
            processedTextList.remove('')
        for i in processedTextList:
            if i not in (punctuation+" "+"0123456789"):
                key = self.generateVigenereKeyEncryption(i, keyword)
                self.intermediate_encrypted += self.vcipherTextEncryption(
                    i, key)
            else:
                self.intermediate_encrypted += i

        #  encryption starts
        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]')
        result = ""
        s = 0
        for char in self.key:
            s += ord(char)
        s = s % 26

        for char in self.intermediate_encrypted:
            if char not in special_char:
                if char.isnumeric():
                    result += chr(ord(char) + s % 10)
                elif char.isupper():
                    result += chr((ord(char) + s-65) % 26 + 65)
                elif ord(char) == 32:
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else:
                result += special_char[(special_char.index(char)+1) % len(special_char)]
        self.intermediate_encrypted = result

        #  encryption ends
        for i, char in enumerate(self.intermediate_encrypted):
            c = chr(ord(char) ^ i ^ ord(self.key[i % len(self.key)]))
            self.encrypted += c

    def decrypt(self):
        #  decryption starts
        for i, char in enumerate(self.encrypted):
            c = chr(ord(char) ^ ord(self.key[i % len(self.key)]) ^ i)
            self.text += c

        #  decryption starts
        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]')
        result = ""
        s = 0
        for char in self.key:
            s += ord(char)
        s = 26 - (s % 26)

        for char in self.text:
            if char not in special_char:
                if char.isnumeric():
                    result += chr(ord(char) - (26-s) % 10)
                elif char.isupper():
                    result += chr((ord(char) + s-65) % 26 + 65)
                elif ord(char) == 32:
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else:
                result += special_char[(special_char.index(char)-1) % len(special_char)]
        self.text = result

        
        vigenere_decrypt_cipher_text = self.text.upper()
        keyword = self.key.upper()
        processedTextList = []
        processedText = ""

        for i in vigenere_decrypt_cipher_text:
            if i not in (punctuation + " " + "0123456789"):
                processedText += i
            else:
                processedTextList.append(processedText)
                processedTextList.append(i)
                processedText = ""
        if processedText != "":
            processedTextList.append(processedText)
        while '' in processedTextList:
            processedTextList.remove('')
        result = ""
        for i in processedTextList:
            if i not in (punctuation+" "+"0123456789"):
                vigenere_key = self.vigenereGenerateKeyDecryption(i, keyword)
                result += self.vigenereOriginalTextDecryption(i, vigenere_key)
            else:
                result += i
        self.text = result

    def disp(self):     # fungsi untuk print tampilan
        print(f"Text = {self.text}")
        print(f"Key = {self.key}")
        print(f"Encrypted = {self.encrypted}")
        print("#############################\n")


if __name__ == "__main__":   # Fungsi percabangan input ketika running awalan
    option = input("Enter the option e for encryption and d for decryption: ")

    if option == "e":  # Jika memilih e maka muncul kata berikut  ( percabgan untuk enkripsi )
        inp_text = input("Enter the string to be encrypted: ")
        inp_key = input("Enter the key: ")
        p = payload(text=inp_text, key=inp_key)
        p.encrypt()
        print(f"Encrypted string: {p.encrypted}")

    if option == "d": # jika memilih d maka muncul kata berikut  ( percabangan untuk ke dekripsi)
        inp_encrypted = input("Enter the encrypted string: ")
        inp_key = input("Enter the key: ")
        q = payload(encrypted=inp_encrypted, key=inp_key)
        q.decrypt()
        print(f"Decrypted string: {q.text}")
   


# In[ ]:




