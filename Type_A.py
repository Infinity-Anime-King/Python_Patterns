n = 5
for i in range(n): # simple which is 0,1,2,3,4. (PART 1)
    print("* " * (i + 1)) #I +1 for 0+1 = 1 (So that it prints that many mult)
for i in range(n - 1, 0, -1): #Start value, end, step. which is 4,3,2,1 (PART 2)
    print("* " * i)

# part 1 res;
# * 
# * *
# * * *
# * * * *
# * * * * *
# part 2 res;
# * * * *
# * * *
# * *
# *
