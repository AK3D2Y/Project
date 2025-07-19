import random
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