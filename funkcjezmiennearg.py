def foo(a, b, c, *d):
    return len(d)

def bar(a, b, c, **de):
    return de["magicnumber"] == 7


if foo(1,2,3,4) == 1:
    print ("Dobrze.")
if foo(1,2,3,4,5) == 2:
    print ("Lepiej.")
if bar(1,2,3,magicnumber = 6) == False:
    print ("Bardzo dobrze.")
if bar(1,2,3,magicnumber = 7) == True:
    print ("Doskonale!")

