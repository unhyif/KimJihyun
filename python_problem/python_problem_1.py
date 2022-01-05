players = ["playerA", "playerB"] # player 목록
num = 0 # 현재까지 불러진 수

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

for _ in range(called_num):
    num += 1
    print(f"{players[0]} :", num)