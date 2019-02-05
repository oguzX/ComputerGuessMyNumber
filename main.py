import Computer

comp = Computer.Computer(input("Down limit"),input("Up limit"))
GAMEOVER = 0

while GAMEOVER == 0 and comp.err==0:
    print "I guess, number is >> " + str(comp.guessnumber())
    print "is it right?"
    if(int(input("YES = 1, NO = 0"))==1):
        GAMEOVER = 1
    else:
        inp = input("[1]Up-[2]Down?")
        if int(inp) == 1:
            comp.upp()
        else :
            comp.downn()

print "I found it in " + str(comp.getcount())
print "Thanks for play with me"
