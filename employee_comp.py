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
    ASSUME_FULL_TIME = 8
    ASSUME_PART_TIME = 4

    if attendance == 1:
        daily_wage = ASSUME_FULL_TIME * WAGE_PER_HOUR

    elif attendance == 0:
        daily_wage = 0
    
    else:
        daily_wage = ASSUME_PART_TIME * WAGE_PER_HOUR    

    print(f"Daily Wage: ${daily_wage}")       

if __name__ == "__main__":
    check_attendance()
    print("Welcome to Employee Wage Computation Program")
