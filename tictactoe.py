count=0
flag=0
def game():
    global count
    global flag
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    gap = "------------------------"
    while not win(grid):
        print(f"\t{grid[0][0]}\t|\t{grid[0][1]}\t|\t{grid[0][2]}\t\n {gap}\n \t{grid[1][0]}\t|\t{grid[1][1]}\t|\t{grid[1][2]}\t\n {gap}\n \t{grid[2][0]}\t|\t{grid[2][1]}\t|\t{grid[2][2]}\t")

        if flag==0:
            move=int(input("\nPlayer 1, Enter your move position (1-9): "))
            if move==1:
                grid[0][0] = "X"
            elif move==2:
                grid[0][1] = "X"
            elif move==3:
                grid[0][2] = "X"
            elif move==4:
                grid[1][0] = "X"
            elif move==5:
                grid[1][1] = "X"
            elif move==6:
                grid[1][2] = "X"
            elif move==7:
                grid[2][0] = "X"
            elif move==8:
                grid[2][1] = "X"
            elif move==9:
                grid[2][2] = "X"
            count += 1
            result = win(grid)
            if result:
                print(
                    f"\t{grid[0][0]}\t|\t{grid[0][1]}\t|\t{grid[0][2]}\t\n {gap}\n \t{grid[1][0]}\t|\t{grid[1][1]}\t|\t{grid[1][2]}\t\n {gap}\n \t{grid[2][0]}\t|\t{grid[2][1]}\t|\t{grid[2][2]}\t")
                print(result)
                break
            flag=1


        if flag==1:
            move = int(input("\nPlayer 2, Enter your move position (1-9): "))
            if move == 1:
                grid[0][0] = "O"
            elif move == 2:
                grid[0][1] = "O"
            elif move == 3:
                grid[0][2] = "O"
            elif move == 4:
                grid[1][0] = "O"
            elif move == 5:
                grid[1][1] = "O"
            elif move == 6:
                grid[1][2] = "O"
            elif move == 7:
                grid[2][0] = "O"
            elif move == 8:
                grid[2][1] = "O"
            elif move == 9:
                grid[2][2] = "O"
            count+= 1
            result = win(grid)
            if result:
                print(
                    f"\t{grid[0][0]}\t|\t{grid[0][1]}\t|\t{grid[0][2]}\t\n {gap}\n \t{grid[1][0]}\t|\t{grid[1][1]}\t|\t{grid[1][2]}\t\n {gap}\n \t{grid[2][0]}\t|\t{grid[2][1]}\t|\t{grid[2][2]}\t")
                print(result)
                break
            flag=0


    return win(grid)

def win(grid):
    global count
    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        return "X is the winner"
    elif grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        return "O is the winner"
    elif grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        return "X is the winner"
    elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        return "O is the winner"
    elif grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        return "X is the winner"
    elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        return "O is the winner"
    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        return "X is the winner"
    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        return "O is the winner"
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        return "X is the winner"
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        return "O is the winner"
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        return "X is the winner"
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        return "O is the winner"
    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        return "X is the winner"
    elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        return "O is the winner"
    elif grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        return "X is the winner"
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        return "O is the winner"
    elif count == 9:
        return "It's a draw"
    return False


print("Welcome to Tic Tac Toe!")
variable=input("Do you want to be X or O: ").upper()
if variable=="X":
    print("You are player 1")
else:
    print("You are player 2")
    flag=1
game()