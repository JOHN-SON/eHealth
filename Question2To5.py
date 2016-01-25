
#+++++++++++CHARACTERS IN STRING
#QUESTION 2
#Implement a function with signature find_chars(string1, string2) that takes two strings and returns a string that
#contains only the characters found in string1 and string two in the order that they are found in string1. Implement
#a version of order N*N and one of order N

#VERSION OF ORDER N*N
def find_chars(string1, string2):
    found = ''.join([c for c in string1 if c in string2])
    return found
	

#VERSION OF ORDER N	
def find_char_fast(string1, string2):
    d = d = set(string2)
	return "".join([char for char in string1 if char in d])

#QUESTION 3

def removeDuplicates(array):
    element = array[0]
    position     = 1
    while (position < len(array)):
        if element == array[position]:
            del array[position]
        else:
            prev = array[position]
            position += 1
    return len(array)

#QUESTION 4

def rotate(array, npos):
    if len(array):
        # position must be positive
        npos = abs(npos) % len(array)
        if npos:
            chunk = array[-npos:]
            del array[-npos:]
            
            chunk.reverse()
            for x in chunk:
                array.insert(0, x)
    return array

#QUESTION 5

###First define a gcd(greatest common divisor) function. Returns result by recursion
def gcd(i,j):
	if(i<j):
		return gcd (i,j)
	if(i%j):
		return gcd(j, i%j)
	else:
		return j

def lcm (a,b):
	result =(a*b)/gcd(a,b)
	return result

##Call the lcm function  recursively
def lcmOfArray(int[] arr,int startPos, int endPos):
	if(len(arr)<2):
		print("Invalid array")
		return -1;
	else:
		return (lcm(arr[startPos],lcmOfArray(arr,startPos+1, endPos)))

		




	
