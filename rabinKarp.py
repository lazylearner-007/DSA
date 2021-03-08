def rabinKarp(string,pattern):
	if string == '' or pattern == '':
		return 'Invalid Input'

	patLength = len(pattern)
	prime = 3   #use bigger prime number for better results
  	resultHash = computeHash(pattern,prime) 
	hashValue = computeHash(string[0:patLength],prime) 
	limit = len(string)-patLength+1

	for k in range(1,limit):
		if hashValue == resultHash:
			return k-1
		hashValue = int((hashValue - ord(string[k-1]))/prime) + (ord(string[k+patLength-1])*(prime**(patLength-1)))
		
def computeHash(pattern,prime):
	ans = 0
	for i in range(len(pattern)):
		ans+= ord(pattern[i]) * (prime**i)
	return ans


if __name__=='__main__':
	#sample test cases
	string = "abcd2fabc"
	pattern1 = 'abc' #expected output 0
	pattern2 = 'd2f' #expected output 3
	pattern3 = 'fab' #expected output 5
	pattern4 = ''    #invalid input

	for pattern in [pattern1,pattern2,pattern3,pattern4]:
		print(rabinKarp(string,pattern))

