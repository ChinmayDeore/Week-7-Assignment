## Chinmay D. 10/19/2022 Hg5590
def makeDictionary(x,y):
# Naming and starting the function with multiple parameters
    john = {x[i]: y[i] for i in range(len(x))}
    john["John"]= 19 
    return john
# [3] ^Adds another key and value pair to the dictionary
x = ['joe','tom','barb','sue','sally']
y = [10, 23, 13, 18, 12]
scoreDict = makeDictionary(x,y)
# [1] ^Turns both of the lists into a dictionary^
find = input("Who's score would you like to search? -> ")
# ↓Adds an else/if parameter to inform the user of non eligible inputs↓
if find in x:
    print(find," had a score of ",scoreDict[find])
else:
    print("The student",find,"does not exist")
# [2] ^Adds an input promt then prints out the score^
sortedList = {key: value for key, value in sorted(scoreDict.items(), key=lambda item: item[1])}
# [4] ^Creates a sorted list of all the values from scoreDict^
print(sortedList)
# [5] ^End of the function and completes all the criteria by printing all students and scores^
# AlphaBeta, Sam Loomis, Robert Burke, project #: LE9000