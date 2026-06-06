################## ord() method is used to get the ASCII value of a character and chr() method is used to get the character from the ASCII value. ######################
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord(' '))
print(chr(97))
print(chr(65))
print(chr(48))
print(chr(32))  

######## Python3 and unicode please explain       ############
print(ord('H'))
print(ord('e'))
print(ord('l'))
print(ord('o'))
print(ord(' '))
print(ord('W'))
print(ord('r'))
print(ord('d'))
print(ord('!'))         


######### when we talk to a network resource using sockets or talk to a database we have to encode and decode data usually in UTF-8 format. so we have to use encode() method to convert the string into bytes and decode() method to convert the bytes into string. ############
x = 'Hello World'
y = x.encode()  ### this will convert the string into bytes and the default encoding is UTF-8
print(y)
print(type(y))
z = y.decode()  ### this will convert the bytes into string and the default encoding is UTF-8
print(z)    
print(type(z))    

########## encoding mean byte representation of a string and decoding mean converting the byte representation back to string. ############