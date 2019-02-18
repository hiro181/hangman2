# hangman(word : zen 2.txt)


def hangman(word):
    wrong = 0
    stages = ["",
              "______________         ",
              "|           |          ",
              "|           |          ",
              "|         (+_+)        ",
              "|           |          ",
              "|          /|\         ",
              "|           |          ",
              "|          / \         ",
              "|                      "
              ]
    
    rletters = list(word)
    board = ["_"]* len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) -1:
        print("\n")
        char = input("1文字を予想してね ?:")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print("正解："," ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は　{}.".format(word))



with open("zen 2.txt","r") as f:
    st = f.read()
    w = st.split(" ")

print(w)

import random

l = len(w)
n = random.randint(0,l)
wx = w[n]

#print(wx)

hangman(wx)

