#課題内容 https://github.com/brains-tsukuba/Info-and-Rules/blob/master/sugoroku/sugoroku3.md
import random
import numpy as np
flag_player = False #プレイヤー数決めるときに使う
flag = False #設定が完了したか＋ゲーム終了
m = 1
print('---すごろくゲーム---')
while flag_player == False:
    player = input('プレイヤー数を入力してください(2~5): ')
    for x in range(2,6):
        if player == str(x):
            player = int(x)
            n = player + 1 #配列の[0]を全体を判定するのに使った
            flag_player = True
turn_num = np.ones(n) #ターン数
total = np.zeros(n) #現在のマス目
player_pt = np.zeros(n) #現在のポイント
player_rank = np.zeros(n)
while flag == False: #20 ~ 40のみを受け付けてint式に
    masu = input('マスの数を入力してください(20~40): ')
    for x in range(20,41): 
        if masu == str(x):
            masu = int(x)
            flag = True
            _pt = np.random.randint(1,11,41) #40マス目までポイントを割り振った。[0]を使ってないがプログラムとしてやっていいのか
            print(_pt) #デバック用。使うマスだけ表現したいが見当たらない
    # if flag == False:
    #     print('Not Accept')
print('Game Start!!')
# 参考　https://www.sejuku.net/blog/28182
while flag == True:
    for x in range(player):
        _list = x + 1
        if total[_list] != masu:#クリアしたらスキップするように追加した
            print('--------------------')
            print(f'{turn_num[0]}ターン目')
            print(f'現在位置{total}')
            print(f'得点{player_pt}')
            # print(turn_num)
            while turn_num[_list] == turn_num[0]:
                print(f'{_list}Pのターンです')
                turn = True#input('\'w\'でサイコロを振ります: ')
                if turn == True:
                    dice = random.randint(1,8)
                    print(f'{dice}でした')
                    if dice % 2 == 0:
                        total[_list] += dice
                        if total[_list] > masu:
                            total[_list] = 0
                        tt = np.fix(total)##wakaran
                        print(tt)
                        print(f'{_pt[int(tt[_list])]}ポイント手に入れた!')
                        player_pt[_list] += int(tt[_list])
                        print(f'{player}P : {player_pt[_list]}Pt')
                    else:
                        print('奇数なので減点')
                        total[_list] -= dice
                        if total[_list] < 0:
                            total[_list] = 0
                    turn_num[_list] += 1
                else:
                    print('Not Accept')
                if total[_list] == masu:
                    print(f'{total[_list]}! Game Clear!!')
                    player_pt[_list] += player / m
                    player_rank[_list] += m
                    m += 1
                    flag = False
                    clear_turn = np.zeros(n)
                    clear_turn[_list] = turn_num[_list] #クリアターンを保存
                    for x in range(1,player + 1):
                        if total[x] != masu:
                            flag = True
                else:
                    print(f'あと{masu - total[_list]}')
        else:
            player_pt[_list] += int(_pt[masu])
    turn_num[0] += 1
print(f'ターン数：{turn_num[0]}')
# clear_turn[0] = np.argmax(clear_turn) + 1
# print(f'{np.argmin(clear_turn)}Pの勝利')
print(f'得点：{player_pt}')
print(f'順位{player_rank}')
print(f'{np.argmax(player_pt)}Pの勝利')