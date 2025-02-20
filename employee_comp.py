import random

def check_attendance():
    attendance = random.randint(0 , 1 , 2)
    if attendance == 1:
        print("Employee is Present Full time")
    elif attendance == 2:
        print("Employee is Present Part time")
    else:
        print("Employeee is Absent")


if __name__ == "__main__":
    check_attendance()
    print("Welcome to Employee Wage Computation Program")
