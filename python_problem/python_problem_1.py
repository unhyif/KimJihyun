from random import *
players = ["computer", "player"] # player 목록

def brGame(players_list):
    global players # 마지막에 승자 결정 시 players를 수정하기 위해

    main_player = "" # 숫자를 부를 차례인 player
    num = 0 # 현재까지 불러진 수
    current_turn = 0 # 현재 몇번째 turn이 진행 중인지

    while num < 31:

        current_turn += 1
        if current_turn % 2 == 1: # 홀수번째 turn이면
            main_player = players[0] # computer 차례
        else: # 짝수번째 turn이면
            main_player = players[1] # player 차례

        if main_player == players[1]: # player 차례면 숫자를 입력 받음
            while True: # 1 이상 3 이하의 정수를 입력받는 과정
                called_num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

                if called_num.isdigit(): # 0 이상의 정수를 입력받았을 때
                    if 1 <= int(called_num) <= 3: # 1 이상 3 이하 정수일 때
                        called_num = int(called_num)
                        break
                    else: # 0 또는 3 초과인 정수일 때
                        print("1,2,3 중 하나를 입력하세요")
                else: # 음수, 소수, 문자를 입력받았을 때
                    print("정수를 입력하세요")

        else: # computer 차례면 랜덤으로 숫자 부름
            called_num = randint(1, 3)

        for _ in range(called_num):
            num += 1
            print(f"{main_player} :", num)
            if num == 31:
                players.remove(main_player) # 승자만 players에 남겨 놓기 위해
                break

    print(f"{players[0]} win!")


brGame(players)