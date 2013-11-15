#!/usr/bin/python

def encrypt(plaintext=None, key=None):
    
	if plaintext is None:
		plaintext = raw_input("Enter plaintext: ")
	if key is None:
		key       = raw_input("Enter the key: ")
	plaintext = plaintext.lower()
	key = key.lower()
	plaintext_intlist      = []
	key_intlist            = []
	for letter in plaintext:
		plaintext_intlist.append((ord(letter)-96))
	for letter in key:
		key_intlist.append((ord(letter)-96))
	i = 0
	encrypted_intlist      = []
	for z in plaintext_intlist:
		if z + key_intlist[i] > 26:
			encrypted_intlist.append((z + key_intlist[i])-26)
		else:
			encrypted_intlist.append(z + key_intlist[i])
		i+=1
	secret_text = ""
	for z in encrypted_intlist:
		secret_text += chr(z+96)
        
	return secret_text
    
    
    
def decrypt(encryptedtext=None, key=None):
    
	if encryptedtext is None:
		encryptedtext = raw_input("Enter encrypted text: ")
	if key is None:
		key           = raw_input("Enter the key: ")
	encryptedtext = encryptedtext.lower()
	key = key.lower()
	encryptedtext_intlist      = []
	key_intlist            = []
	for letter in encryptedtext:
		encryptedtext_intlist.append((ord(letter)-96))
	for letter in key:
		key_intlist.append((ord(letter)-96))
	i = 0
	decrypted_intlist      = []
	for z in encryptedtext_intlist:
		if z - key_intlist[i] < 1:
			decrypted_intlist.append((z - key_intlist[i])+26)
		else:
			decrypted_intlist.append(z - key_intlist[i])
		i+=1
	real_text = ""
	for z in decrypted_intlist:
		real_text += chr(z+96)
        
	return real_text
    
    
    

def generatekey(encryptedtext=None, plaintext=None):
        
        if encryptedtext is None:
            encryptedtext = raw_input("Enter encrypted text: ")
        if plaintext is None:
            plaintext     = raw_input("Enter the key: ")
        
        encryptedtext     = encryptedtext.lower()
        plaintext         = plaintext.lower()
        
        encryptedtext_intlist = []
        plaintext_intlist     = []
    	for letter in encryptedtext:
    		encryptedtext_intlist.append((ord(letter)-96))
    	for letter in plaintext:
    		plaintext_intlist.append((ord(letter)-96))
            
    	i = 0
    	key_intlist      = []
    	for z in plaintext_intlist:
            if encryptedtext_intlist[i]-plaintext_intlist[i] < 1:
                key_intlist.append(encryptedtext_intlist[i]-plaintext_intlist[i]+26)
            else:
                key_intlist.append(encryptedtext_intlist[i]-plaintext_intlist[i])
            i+=1
            
        key_text = ""
        for z in key_intlist:
            key_text += chr(z+96)
            
        return key_text
            
        
            
            
            
            
            
            
            






