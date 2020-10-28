print("Title of program: Percy Jackson Series Quiz")
print()

counter = 0
score = 0
total_num_of_qn = 4


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who is the father of the olympians?")
  print("   a) Kronos")
  print("   b) Mercury")
  print("   c) Jesu1s")
  print("   d) Uranus")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes!"
    score +=1
  elif answer == "b":
    output = "Try again"
    score -=1
  elif answer == "c":
    output = "Read carefully"
    tracker =1
    score -=1
  elif answer == "d":
    output = "Nope, try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who is the god of the sky and leader of the olympians?")
  print("   a) Zeus")
  print("   b) Poseidon")
  print("   c) Hades")
  print("   d) Apollo")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "yes congratulations you have passed your mathematics and eyesight test"
    tracker =1
    score +=1
  elif answer == "b":
    output = "nope"
    score -=1
  elif answer == "c":
    output = "sorry but no"
    score -=1
    
  elif answer == "d":
    output = "try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who is the wife of Zeus?")
  print("   a) Amphrodite")
  print("   b) Athena")
  print("   c) Demeter")
  print("   d) Hera")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "that's not quite right"
    score -=1
  elif answer == "b":
    output = "are you really sure?"
    score -=1
  elif answer == "c":
    output = "check"
    score -=1
    
  elif answer == "d":
    output = "congratulations"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

    
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who is the godly parent of Percy and Jason respectively?")
  print("   a) Neptune, Zeus")
  print("   b) Pluto, Poseidon")
  print("   c) Poseidon, Jupiter")
  print("   d) Neptune, Apollo")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "that's not quite right"
    score -=1
  elif answer == "b":
    output = "are you really sure?"
    score -=1
  elif answer == "c":
    output = "yes!!!"
    score -=1
    
  elif answer == "d":
    output = "try again"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."
    
  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
