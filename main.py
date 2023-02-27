def sum(a,b,c,):
    return a+b+c


xstate = [0,0,0,0,0,0,0,0,0]
ystate = [0,0,0,0,0,0,0,0,0]
def printboard(xstate, ystate):
    zero = 'x' if xstate[0] else  ('o' if ystate[0] else 0)
    one = 'x' if xstate[1] else  ('o' if ystate[1] else 1)
    two = 'x' if xstate[2] else  ('o' if ystate[2] else 2)
    three = 'x' if xstate[3] else  ('o' if ystate[3] else 3)
    four = 'x' if xstate[4] else  ('o' if ystate[4] else 4)
    five = 'x' if xstate[5] else  ('o' if ystate[5] else 5)
    six = 'x' if xstate[6] else  ('o' if ystate[6] else 6)
    seven = 'x' if xstate[7] else  ('o' if ystate[7] else 7)
    eight = 'x' if xstate[8] else  ('o' if ystate[8] else 8)
    print(f"   {zero}   |   {one}   |   {two}   ")
    print(f"-------|-------|-------")
    print(f"   {three}   |   {four}   |   {five}   ")
    print(f"-------|-------|-------")
    print(f"   {six}   |   {seven}   |   {eight}   ")

def checkwin(xstate,ystate):

    wins = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

    for win in wins:
        if sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3:
            print("X' win the mach")

            return 1
        else:
            print("Game Over")
            break
    for win in wins:
        if sum(ystate[win[0]],ystate[win[1]],ystate[win[2]]) == 3:
            print("O win the mach")
            return 0
        else:
            print("Game Over")
            break
    return -1
if __name__ == "__main__":

    turn = 1 # 1 for x chance and o for 0 chance
    print("****Welcome to Tic tack to****")
    while True:
        printboard(xstate, ystate)
        if turn == 1:
                
            print("X' turn")
            value = int(input("enter te value: "))
            xstate[value] = 1
        else:
            print("0' turn")
            value = int(input("enter te value: "))
            ystate[value] = 1            
        

        cwin = checkwin(xstate,ystate)

        if(cwin!= -1):
            break

        turn = 1 - turn
        