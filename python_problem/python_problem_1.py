from random import *
players = ["computer", "player"] # player 목록


def play_br_game(players):
    print("computer, player 순으로 번갈아 가며 게임이 진행됩니다.")

    main_player = None # 숫자를 부를 차례인 player
    last_num = 0 # 현재까지 불러진 수
    current_turn = 0 # 현재 몇번째 turn이 진행 중인지

    while last_num < 31:
        current_turn += 1

        if current_turn % 2: # 홀수번째 turn엔
            main_player = players[0] # computer가 랜덤으로 숫자 부름
            shouted_num = randint(1, 3)

        else: # 짝수번째 turn엔
            main_player = players[1] # player로부터 숫자를 입력 받음

            while True:
                try:
                    shouted_num = float(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
                
                    if shouted_num % 1:
                        raise

                    if 1 <= int(shouted_num) <= 3: # 1 이상 3 이하 정수일 때
                        shouted_num = int(shouted_num)
                        break
                    else: # 그 외 정수를 입력받았을 때
                        print("1,2,3 중 하나를 입력하세요")
                        
                except: # 소수, 문자를 입력받았을 때
                    print("정수를 입력하세요")


        for count in range(shouted_num):
            last_num += 1
            print(f"{main_player} : {last_num}")

            if last_num == 31:
                players.remove(main_player)
                break

    print(f"{players[0]} won!")


play_br_game(players)