import random
"""
Developer's Note :
 I have created a simple snake, water, gun game
 I've used a clear if/elif/else ladder below to check for the winner,
 as it's the most readable approach for this classic game's logic.
 I also explored a more mathematical approach using the modulo operator,
 where the winning condition can be simplified to `(player - computer) % 3 == 2`.
 While efficient, I chose the explicit ladder for better clarity in this project.

"""
choiceDict = {"s":-1, "w":0, "g":1}
reverseDict = {-1 : "Snake", 0 : "Water", 1 : "Gun"}
while True:
  youStr = input("\n Enter you choice (s,w,g or q for quit) : ")
  if youStr == "q":
   break
  if youStr not in choiceDict:
   print("Invalid choice, enter (s,w,g or q for quit) : ")
   continue
  you = choiceDict[youStr]
  computer = random.choice([-1,0,1])
  print(f"Your choice : {reverseDict[you]}\n Computer choice : {reverseDict[computer]}")
  if computer == you:
   print("Its a Draw!")
  else:
   if computer == -1 and you == 1:
    print("You win!")
   elif computer == -1 and you == 0:
    print("You Lose!")
   elif computer == 1 and you == -1:
    print("You Lose!")
   elif computer == 1 and you == 0:
    print("You Win!")
   elif computer == 0 and you == 1:
    print("You Lose!")
   elif computer == 0 and you == -1:
    print("You Win!")