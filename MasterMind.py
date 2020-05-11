import random

def getSolution(len, min, max):
	solution = []
	for i in range(len):
		solution.append(random.randint(min,max))
	return solution

solution = getSolution(3,1,5)

print(f"Solution: {solution}")


def testGuess(guess):
	if guess == solution:
		return True
		print(f"Guess: {guess}")
		print(f"Answer: {solution}")
	for i in range(len(guess)):
		try:
			solution.index(guess[i])
			print(guess[i])
		except:
			continue
	return False

guesses = 0
answered = False
while(not answered):
	guesses += 1
	guess = list(map(int, (input("Guess... ").split())))
	if(len(guess) == len(solution)):
		if(testGuess(guess)):
			print("You Win!")
			print(f"Guesses used: {guesses}")
			answered = True
	else:
		print("Not correct length")


"""
Responses:
No values correct
x amount correct but wrong position
x amount fully correct
"""