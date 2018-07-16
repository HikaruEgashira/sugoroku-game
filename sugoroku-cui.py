import random
total = 0
n = 0
game = False
turn_num = 0
print('---すごろくゲーム---')
mode = input('ゲームを始めるときは\'s\'を押してください :')
if mode == 's':
    level = input('レベルを選択してください =>  normal : hard >> ')
    if level == 'normal':
        n = 20
        print('マス目は「20」です')
        game = True
    elif level == 'hard':
        n = 50
        print('マス目は「50」です')
        game = True
    else:
        print('誤った入力です')
if game == True:
    print('Game Start!!')
    print(game)
    print(n)
while game == True:
    turn = input('\'w\'でサイコロを振ります: ')
    if turn == 'w':
        num = random.randint(1,6)
        total += num
        if total > n:
            total = n
        turn_num += 1
        print(f'{num}でした')
    else:
        print('error')
    if total == n:
        print('Game Clear!!')
        print(f'{turn_num}ターンでクリアしました')
        game = False
    else:
        print(f'現在{turn_num}ターンで{total}')