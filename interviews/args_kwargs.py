#Позиционные аргументы
def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
     
printScores("Jonathan",100, 95, 88, 92, 99)

#Именованные аргументы
def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   #print(pets)
   for name,pet in pets.items():
      print(f"{pet}: {name}")

printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
