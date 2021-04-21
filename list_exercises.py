#a list of ages
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

#write a function that consumes a list and outputs the first item
def firstAge(ages):
    return ages[0]

#write a function that consumes a list and outputs the last item
def lastAge(ages):
    return ages[-1]
#write a function that consumes a list and outputs the length of the list
def lengthOfList(ages):
    return len(ages)
#write a function that consumes a list and removes the last item of the List
def removeLastItem(ages):
    ages.pop()
    print(ages)

#write a function that consumes a list and a new age as an integer and outputs the list with the age added to the end of the list
def addToEnd(ages):
    ages.append(107)
    print(ages)
#write a function that consumes a list and prints each element on a separate line. (No return)
def separate(ages):
    ageIndex=0
    while ageIndex<len(ages):
        print(ages[ageIndex])
        ageIndex+=1
#write a function that consumes a list and outputs the sum
def sumAge(ages):
    sum=0
    # ageIndex=0
    for x in ages:
        sum += x
        # ageIndex+=1
    print(sum)
    # sum= age[0]+age[1]+age[2]+age[3]+age[4]+age[5]+age

#write a function that consumes a list and outputs the average
def averageAge(ages):
    sum=0
    for x in ages:
        sum += x
    avg = sum/len(ages)
    print(avg)
#write a function that consumes a list and outputs all ages less than 18
def lessThan18(ages):
    for x in ages:
        if x<18:
            print(x)

#try the same but output a list of all the ages less than 18 (if you are not yet 18 you are considered a minor)
def listOfMinors(ages):
    ages.sort()
    minors=[]
    for x in ages:
        if x<18:
            minors.append(x)
    # for x in ages:
    #     if x>18:
    #         ages.pop()

    print(minors)
    # for x in ages:
    #     if x<18:
    #         ages.pop(x)
    #         print(ages)
#write a function that consumes a list and outputs the max age
def maxAge(ages):
    ages.sort()
    print(ages[-1])

#write a function the consumes a list and outputs the min age
def minAge(ages):
    ages.sort()
    print(ages[0])







### CALL YOUR FUNCTIONS HERE
# print(firstAge(ages))
#print(lastAge(ages))
#print(lengthOfList(ages))
#print(removeLastItem(ages))
#print(addToEnd(ages))
#separate(ages)
#sumAge(ages)
#averageAge(ages)
#lessThan18(ages)
#maxAge(ages)
#listOfMinors(ages)
minAge(ages)
#Done already? Go to  http://codingbat.com/python/List-
