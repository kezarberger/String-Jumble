"""
stringjumble.py
Author: kezar
Credit: kotz

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

stringjumble.py
Author: kezar
Credit: kotz
Assignment:
The purpose of this challenge is to gain proficiency with 
manipulating lists.
Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:
* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.
Output of your program should look like this:
Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string = input("Please enter a string of text (the bigger the better): ")
print ('You entered "' + string + '". Now jumble it:')
lies = list(string)
length = len(string)


leng = length
back = ""
leng = leng -1
while leng >= 0:
    x = lies[leng]
    back = back + str(x)
    leng = leng -1
print (back)



lies = string.split()
backs = ""
lend = len(lies)-1
while lend >= 0:
    y = lies[lend]
    backs = backs + y + " "
    lend = lend -1
print (backs)



kotz = string.split()
backer = ""
backed = ""
lent = len(kotz)-1
for z in kotz:
    backed = ""
    lent = len(z) -1
    z = list(z)
    while lent >= 0:
        now = z[lent]
        backed = backed + now
        lent = lent-1
    backer = backer + backed + " "
print (backer)