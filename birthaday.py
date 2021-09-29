def birthday(inp):
    if inp=="Albert Einstein":
        print(inp,"birthday is",data["Albert Einstein"])
    elif inp=="Benjamin Franklin":
         print( inp,"birthday is",data["Benjamin Franklin"])
    elif inp=="Ada Lovelace":
         print( inp,"birthday is",data["Ada Lovelace"])
    else:
       print("the input you gave is not in our directory please recheck")
data= {"Albert Einstein":"14/03/1979","Benjamin Franklin":"01/17/1706","Ada Lovelace":"10/12/1815"}
print("welcome to the birthday dictionary.we know the birthdays of: \nAlbert Einstein \nBenjamin Franklin \n AdaLoveLace")
inp=input("who's birthday want to look?")
birthday(inp)
