import random
import os
deck = [6,7,8,9,10,2,3,4,11]
sum = [0,0]
random.shuffle(deck)
for i in [1,2]:
    print(f"\nPlayer {i}")
    aceNum = 0
    while True:
        choice = input("\nWanna draw a card?(y/n) ")
        if choice == 'y':
            drawedCard = deck.pop()
            if drawedCard == 11:
                aceNum += 1
                print("You drawed ace")
            else:
                print(f"You drawed {drawedCard}")
            sum[i-1] += drawedCard
            if aceNum > 0 and sum[i-1] > 21:
                aceNum -= 1
                sum[i-1] -= 10
            if sum[i-1] > 21:
                print("Your total score exceeded 21 ")
                sum[i-1] = -1
                break
            elif sum[i-1] == 21:
                print("Congratulations, 21!")
                break
            else:
                print(f"Your total score - {sum[i-1]} points")
        elif choice == 'n':
            print(f"Your final score {sum[i-1]}")
            break        
print()
if sum[0] > sum[1]:
    print("Player 1 won")
elif sum[1] > sum[0]:
    print("Player 2 won")
else:
    print("Tie")
