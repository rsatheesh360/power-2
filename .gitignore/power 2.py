terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result

print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
   print("2 raised to power",i,"is",result[i])
