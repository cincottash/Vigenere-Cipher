#Created by Shane Cincotta 3/28/2019
#A simple vigenere cipher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def shift(shift_amount):
        shifted_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        while(shift_amount > 0):
            temp = shifted_alphabet[0]
            for i in range(0,25):
                shifted_alphabet[i] = shifted_alphabet[i+1]
            shifted_alphabet[25] = temp
            shift_amount -= 1
        return(shifted_alphabet)

#making the tabula recta
grid = list()
for i in range(0,26):
    grid.append([])
    grid[i] = shift(i)


run = 1
while(run):
	plaintext = list(input("Enter a message to decrypt\n"))
	keylen = len(plaintext)
	keyword = list(input("Enter the keyword\n"))
	keywordlen = len(keyword)

	newkeyword = []
	i = 0
	while(len(newkeyword) < len(plaintext)): #making our key the same len as the palintext
	    if(i == keywordlen):
	        i = 0
	    newkeyword.append(keyword[i])
	    i += 1



	plaintextcords = [] #converting our plaintext letters into a coord based on it's position in the alphabet: i.e "a" = 0
	while len(plaintextcords) < len(plaintext):
	    for i in range(0, keylen):
	        for j in range(len(alphabet)):
	            if(alphabet[j] == plaintext[i]):
	                plaintextcords.append(j)

	newkeywordcords=[] #doing the same as above for newkeyword
	while len(newkeywordcords) < len(newkeyword):
	    for i in range(keywordlen):
	        for j in range(len(alphabet)):
	            if(alphabet[j] == newkeyword[i]):
	                newkeywordcords.append(j)



	ciphertext = []
	for i in range(keylen):
	        ciphertext.append(grid[plaintextcords[i]][newkeywordcords[i]])


	ciphertext = ''.join(ciphertext)
	print("Encrypted message: ", ciphertext)


	valid_response = 0
	while(valid_response == 0):
		response = input("Do you want to run again? (y/n):\n")

		if(response == "n"):
			print("Exiting...\n")
			run = 0
			valid_response = 1

		elif(response == "y"):
			run = 1
			valid_response = 1

		else:
			print("Invalid response\n")
			valid_response = 0

