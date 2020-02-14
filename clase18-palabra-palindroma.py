# palabra que se lee al derecho al reves
def palindrome(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0, letter)
		# print(reversed_letters)
	reversed_word = ''.join(reversed_letters)
	
	if reversed_word == word:
		return True

	return False

def palindrome2(word):
	reversed_word = word[::-1]

	if reversed_word == word:
		return True
	return False

	
def run():
	while True:
		word = str(input('Escriba un palabra: '))

		# result = palindrome(word)
		result = palindrome2(word)

		if result is True:
			print(f"{word} es palindrome")
		else:
			print(f"{word} NO es palindrome")

if __name__ == '__main__':
	run()
	