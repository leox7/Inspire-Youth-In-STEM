#listsofsports
#listoffavmusicians
#listofemptylistoffavmusicians
#addusingforloopaddfivemusicians
#copylisttoanewlists


fav_musician = []

#for loop add five musicians

for musician in range (0,5):
      musician = input("enter name:")
      fav_musician.append(musician)
      print(musician)
      print(fav_musician)


celebs = fav_musician.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()
print(len(celebs))




