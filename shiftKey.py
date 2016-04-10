import string
def shift(char):
	shiftDict = {"1":"!","2":"@","3":"#",
				"4":"$","5":"%","6":"^",
				"7":"&","8":"*","9":"(",
				"0":")","-":"_","=":"+",
				"[":"{","]":"}","\\":"|",
				";":":", "'":"\"", ",":"<",
				".":">","/":"?"}
	if (char in string.punctuation or char 
		in string.digits):
		return shiftDict[char]
	elif (char in string.lowercase):
		return char.upper()