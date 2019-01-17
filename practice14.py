#1
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
fo.close()

#2
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

#3
for letter in 'Python':
   if letter == 'h':
      break
   print ('Current Letter :', letter)
var = 10
while var > 0:
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break
print ("Good bye!")

#4
for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")

#5
import math
print ("math.exp(-45.17) : ", math.exp(-45.17))
print ("math.exp(100.12) : ", math.exp(100.12))
print ("math.exp(100.72) : ", math.exp(100.72))
print ("math.exp(math.pi) : ", math.exp(math.pi))