print("***ANIMAL SOUND GAME!***")
exit_game = " "
while exit_game != "y":
  animal = input("What animal do you want?: ")
  if animal == "snake":
    print("Sssssssss")
  elif animal == "cat":
    print("Meow")
  elif animal == "cow":
    print("Mooooo")
  elif animal == "dog":
    print("Woof woof")
  elif animal == "owl":
    print("Hoo Hoo!")
  else: 
    print("Try again")
exit_game = input("Exit game? ")