a = int (input ("Enter marks for subject 1: "))
b = int (input ("Enter marks for subject 2: "))
c = int (input ("Enter marks for subject 3: "))
d = int (input ("Enter marks for subject 4: "))
e = int (input ("Enter marks for subject 5: "))

avg = a + b + c + d + e / 5

print ("Average of 5 subjects: ", avg)

if (avg > 80):
  print ("Grade: A")
elif (avg > 60 or avg < 80):
  print ("Grade: B")
elif (avg > 40 or avg < 60):
  print ("Grade: C")
else:
  print ("You Failed.")
