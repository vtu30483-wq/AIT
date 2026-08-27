b = [" "] * 9

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
         (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i] == p for i in x) for x in w)

def minimax(ai):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in b: return 0

    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if ai else "X"
            scores.append(minimax(not ai))
            b[i] = " "
    return max(scores) if ai else min(scores)

def show():
    for i in range(0,9,3):
        print("|".join(b[i:i+3]))
        print("-"*5)

while True:
    show()
    p = int(input("Enter position (1-9): ")) - 1
    if b[p] != " ": continue
    b[p] = "X"

    if win("X"):
        show(); print("You Win!"); break
    if " " not in b:
        print("Draw!"); break

    best, move = -99, 0
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            s = minimax(False)
            b[i] = " "
            if s > best: best, move = s, i
    b[move] = "O"

    if win("O"):
        show(); print("Computer Wins!"); break
    if " " not in b:
        show(); print("Draw!"); break
