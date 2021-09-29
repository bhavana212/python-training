p1 = input("enter  ")
p2 = input("enter ")
def compare(p1,p2):
    if(p1 == p2):
        print("draw")
    elif p1 == "rock":
        if p2 == "scissor":
            return("p1 wins")
        else:
            return ("p2 wins")
    elif p1 == "scissor":
        if p2 == "paper":
            return("p1 wins")
        else:
            return ("p2 wins")
    elif p1 == "paper":
        if p2 == "rock":
            return("p1 wins")
        else:
            return ("p2 wins")

    else:
        return ("invalid syntax")

print((compare(p1,p2)))
