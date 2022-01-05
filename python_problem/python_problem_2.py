data = {}

def Menu1(name="", mid_score=0, final_score=0):
    global data
    data[name] = [mid_score, final_score]

def Menu2(person=""):
    global data
    avg = (data[person][0] + data[person][1]) / 2

    if avg < 70:
        data[person].append("D")
    elif avg < 80:
        data[person].append("C")
    elif avg < 90:
        data[person].append("B")
    else:
        data[person].append("A")

def Menu3():
    print('''
------------------------------------
name      mid       final     grade
------------------------------------'''
)
    for person in data:
        print(person, end=" "*(10-len(person)))
        print(data[person][0], end=" "*(10-len(str(data[person][0])))) # table 정렬 위해 점수를 잠시 string화
        print(data[person][1], end=" "*(10-len(str(data[person][1]))))
        print(data[person][2])

def Menu4(del_name=""):
    global data
    del data[del_name]

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        info = input("Enter name mid-score final-score : ").split()

        if len(info) != 3: # 입력된 데이터 갯수가 3이 아닐 때
            print("Num of data is not 3!")

        else:
            name, mid_score, final_score = info

            if name in data: # 이미 존재하는 이름일 때
                print("Already exist name!")
            elif not(mid_score.isdigit() and int(mid_score) != 0) or \
                not(final_score.isdigit() and int(final_score) != 0): # 점수 값이 양의 정수가 아닐 때
                print("Score is not positive integer!")
            else:
                Menu1(name, int(mid_score), int(final_score))

    elif choice == "2":
        if not data:
            print("No student data!")

        else:
            print("Grading to all students.")
            for person in data:
                if len(data[person]) != 3: # 학점이 부여되지 않은 학생에 대해
                    Menu2(person)

    elif choice == "3":
        if not data:
            print("No student data!")

        else:
            for person in data:
                if len(data[person]) != 3: # 학점이 부여되지 않은 학생이 있을 때
                    print("There is a student who didn't get grade.")
                    break
            else: # 모든 학생들의 학점이 부여됐을 때
                Menu3()

    elif choice == "4":
        if not data:
            print("No student data!")

        else:
            del_name = input("Enter the name to delete : ")

            if del_name in data:
                Menu4(del_name)
                print(f"{del_name} student information is deleted.")
            else:
                print("Not exist name!")

        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5":
        print("Exit Program!")
        break

    else:
        print("Wrong number. Choose again.")