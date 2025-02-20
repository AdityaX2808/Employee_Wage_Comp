import random

def calculate_wage(attendance : int):
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    WAGE_PER_HOUR = 20

    switch = {
        0: 0,                                   #absent
        1: FULL_TIME_HOUR * WAGE_PER_HOUR,      #full time
        2: PART_TIME_HOUR * WAGE_PER_HOUR       #part time
    }

    return switch.get(attendance)

def check_attendance():
    attendance = random.randint(0 , 2)
    switch = {
        0: "Employee is Absent",
        1: "Employee is Present (Full-Time)",
        2: "Employee is Present (Part-Time)"
    }
    print(switch.get(attendance))
    print(f"Daily Wages: ${calculate_wage(attendance)}")
    print(f"Monthly Wage: ${calculate_wage(attendance) * 2 * 10}")


if __name__ == "__main__":
    check_attendance()
    print("Welcome to Employee Wage Computation Program")
