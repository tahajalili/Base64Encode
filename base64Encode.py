"""
 This is an implementation of algorithm to convert string of characters to Base64. 

GitHub: http://github.com/tahajalili
"""

#Base64 Table
table = {'0':'A', '1':'B', '2':'C', '3':'D', '4':'E', '5':'F', '6':'G', '7':'H', '8':'I', '9':'J', '10':'K', '11':'L', '12':'M', '13':'N', '14':'O', '15':'P', '16':'Q', '17':'R', '18':'S', '19':'T', '20':'U', '21':'V', '22':'W', '23':'X', '24':'Y', '25':'Z', '26':'a', '27':'b','28':'c', '29':'d', '30':'e', '31':'f', '32':'g', '33':'h', '34':'i', '35':'j', '36':'k', '37':'l', '38':'m', '39':'n', '40':'o', '41':'p', '42':'q', '43':'r', '44':'s', '45':'t', '46':'u', '47':'v', '48':'w', '49':'x', '50':'y', '51':'z', '52':'0', '53':'1', '54':'2', '55':'3', '56':'4', '57':'5', '58':'6', '59':'7', '60':'8', '61':'9', '62':'+', '63':'/'}

#variables 

ARRAY_OF_DECIMAL_VALUES = []
FINAL_VAL = ''
FINAL_LIST = []



#functions
def decToBin(decimal_num):
	power = 0
	binary_value = 0

	while decimal_num > 0:
		binary_value += 10 ** power * (decimal_num % 2)
		decimal_num //= 2
		power += 1

	if len(str(binary_value)) < 8:
		binary_value = str(binary_value).zfill(8)
	return binary_value

def binToDec(binary_num):
	power = 0
	decimal_value = 0

	while binary_num > 0:
		decimal_value += 2 ** power * (binary_num % 10)
		binary_num //= 10
		power += 1

	return decimal_value

#Its a bit complicated. sorry for that!
def chunkstring(string, length):
    return list((string[0+i:length+i] for i in range(0, len(string), length)))


def encode(list_of_6bit_values):
	for item in list_of_6bit_values:
		if len(item) == 6:
			FINAL_LIST.append(table[str(binToDec(int(item)))])
			
		elif len(item) < 6:
			number_of_zeros = 6 - len(item)
			padding = int(number_of_zeros / 2) * '=' 
			item += ('0' * number_of_zeros)

			FINAL_LIST.append(table[str(binToDec(int(item)))])
			FINAL_LIST.append(padding)

def show():
	result = ""
	for item in FINAL_LIST:
		result+= item
	# print('Data to encode: {}'.format(USER_INPUT))
	print('Base64: " {} "'.format(result))

USER_INPUT = input('Input: ')
for char in USER_INPUT:
	decimal_val = ord(char) #ord() is a python pre-built function to return unicode decimal value of any character.
	binary_val = decToBin(decimal_val)

	ARRAY_OF_DECIMAL_VALUES.append(binary_val)

for a in range(len(ARRAY_OF_DECIMAL_VALUES)):
	FINAL_VAL += ARRAY_OF_DECIMAL_VALUES[a]

_6bit_values = chunkstring(FINAL_VAL,6)

# print(FINAL_VAL)


encode(_6bit_values)
show()




