import random

def check_attendance():
    attendance = random.randint(0 , 2)
    if attendance == 1:
        print("Employee is Present (Full-time)")
        calculate_wage(attendance)

    elif attendance == 2:
        print("Employee is Present (Part-time)")
        calculate_wage(attendance)
    else:
        print("Employeee is Absent")
        calculate_wage(attendance)

def calculate_wage(attendance : int):
    WAGE_PER_HOUR = 20
    ASSUME_FULL_DAY = 8

    if attendance == 1:
        daily_wage = ASSUME_FULL_DAY * WAGE_PER_HOUR

    elif attendance == 0:
        daily_wage = 0

    print(f"Daily Wage: ${daily_wage}")       

if __name__ == "__main__":
    check_attendance()
    print("Welcome to Employee Wage Computation Program")
