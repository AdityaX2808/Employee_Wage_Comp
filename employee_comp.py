import random

#global variables
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WAGE_PER_HOUR = 20
TOTAL_WORKING_LIMIT  = 20
TOTAL_WORKING_HOURS = 100

def calculate_monthly_wage():
    total_wage = 0 
    total_working_hours = 0
    total_working_days = 0

    while total_working_hours < TOTAL_WORKING_HOURS and total_working_days < TOTAL_WORKING_LIMIT:
        attendance = random.randint(0 , 2)
        work_hours = {
            0: 0, 
            1: FULL_TIME_HOUR,
            2: PART_TIME_HOUR
        }

        hours_worked = work_hours.get(attendance)

        daily_wage = hours_worked * WAGE_PER_HOUR
        total_wage += daily_wage
        total_working_hours += hours_worked
        total_working_days += 1 if hours_worked > 0 else 0

        print(f"Day {total_working_days}: Attendance {attendance}, Worked {hours_worked} hours, Earned ${daily_wage}")

    print("\nFinal Summary:")
    print(f"Total Working Days: {total_working_days}")
    print(f"Total Working Hours: {total_working_hours}")
    print(f"Total Monthly Wage: ${total_wage}")



if __name__ == "__main__":
    calculate_monthly_wage()
    print("Welcome to Employee Wage Computation Program")
