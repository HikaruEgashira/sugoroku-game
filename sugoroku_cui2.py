import random
import numpy as np
total = np.array([0,0])
n = 0
game = False
turn_num = np.array([1,1,1])
print('---すごろくゲーム---')
n = input('マスの数を入力してください :')
# 参考: https://teratail.com/questions/60174
for x in range(20,41): 
    if n == str(x):
        n = int(n)
        game = True
if game == False:
    print('Not Accept')
if game == True:
    print('Game Start!!')
while game == True:
    print(f'{turn_num[0]}ターン目')
    print('1Pのターンです')
    while turn_num[1] == turn_num[0]:
        turn1 = input('\'w\'でサイコロを振ります: ')
        if turn1 == 'w':
            num = random.randint(1,6)
            total[0] += num
            if total[0] > n:
                total[0] = 2 * n - total[0]
            print(f'{num}でした')
            turn_num[1] += 1
            print(f'現在{turn_num[0]}ターンで{total[0]}')
        else:
            print('Not Accept')
        if total[0] == n:
            print(f'{total[0]}! Game Clear!!')
            print(f'{turn_num[1]}ターン目でクリアしました')
            game = False
    print('2Pのターンです')
    while turn_num[2] == turn_num[0]:
        turn2 = input('\'w\'でサイコロを振ります: ')
        if turn2 == 'w':
            num = random.randint(1,6)
            total[1] += num
            if total[1] > n:
                total[1] = 2 * n - total[1]
            print(f'{num}でした')
            turn_num[2] += 1
            print(f'現在{turn_num[1]}ターンで{total[1]}')
        else:
            print('Not Accept')
        if total[1] == n:
            print(f'{total[1]}! Game Clear!!')
            print(f'{turn_num[0] + 1}ターンでクリアしました')
            game = False
    print(f'{total}{turn_num[0]}ターン目で終了')
    turn_num[0] += 1
