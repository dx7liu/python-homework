#1
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")
if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")
c=b/a
if ( c in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")

#2
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#3
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

#4
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total
total = sum( 10, 20 )
print ("Outside the function : ", total )

#5
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()

