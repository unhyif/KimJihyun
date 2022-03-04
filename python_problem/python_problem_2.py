data = {}

def Menu1(name="", mid_score=0, final_score=0):
    data[name] = {"mid": mid_score, "final": final_score}


def Menu2(name=""):
    avg = (data[name].get("mid") + data[name].get("final")) / 2

    if avg < 70:
        data[name]["grade"] = "D"
    elif avg < 80:
        data[name]["grade"] = "C"
    elif avg < 90:
        data[name]["grade"] = "B"
    else:
        data[name]["grade"] = "A"


def Menu3():
    print('''
------------------------------------
name      mid       final     grade
------------------------------------'''
)
    for name in data:
        print(name.ljust(10) + str(data[name].get("mid")).ljust(10) + str(data[name].get("final")).ljust(10) + data[name].get("grade"))


def Menu4(del_name=""):
    del data[del_name]

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        info = input("Enter name mid-score final-score : ").split()

        try:
            if len(info) != 3:
                raise Exception("Num of data is not 3!")

            name, mid_score, final_score = info

            if name in data: # 이미 존재하는 이름일 때
                raise Exception("This name already exists!")

            if not((mid_score.isdigit() and int(mid_score) != 0) and \
                (final_score.isdigit() and int(final_score) != 0)): # 점수 값이 양의 정수가 아닐 때
                raise Exception("Score is not positive integer!")

            Menu1(name, int(mid_score), int(final_score))

        except Exception as e:
            print(e)


    elif choice == "2":
        try:
            if not data:
                raise Exception("No student data!")

            print("Grading to all students.")
            for name in data:
                if len(data[name]) != 3: # 학점이 부여되지 않은 학생에 대해
                    Menu2(name)

        except Exception as e:
            print(e)


    elif choice == "3":
        try:
            if not data:
                raise Exception("No student data!")

            for name in data:
                if len(data[name]) != 3: # 학점이 부여되지 않은 학생이 있을 때
                    raise Exception("There is a student who didn't get grade.")

            Menu3()
        
        except Exception as e:
            print(e)


    elif choice == "4":
        try:
            if not data:
                raise Exception("No student data!")

            del_name = input("Enter the name to delete : ")

            if del_name not in data:
                raise Exception("This name doesn't exist!")
            
            print(f"{del_name} student information is deleted.")
            Menu4(del_name)

        except Exception as e:
            print(e)


    elif choice == "5":
        print("Exit Program!")
        break

    else:
        print("Wrong number. Choose again.")