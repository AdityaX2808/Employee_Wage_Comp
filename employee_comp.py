import random 

class Employee_wage:
    def __init__(self):
        # Class attributes (global constants)
        self.FULL_TIME_HOUR = 8
        self.PART_TIME_HOUR = 4
        self.WAGE_PER_HOUR = 20
        self.TOTAL_WORKING_LIMIT = 20
        self.TOTAL_WORKING_HOURS = 100

        # Tracking employee details
        self.total_wage = 0
        self.total_working_hours = 0
        self.total_working_days = 0

    def get_attendance(self):
        return random.randint(0, 2)  # 0 = Absent, 1 = Full-time, 2 = Part-time

    def calculate_daily_wage(self, attendance):
        work_hours = {
            0: 0,
            1: self.FULL_TIME_HOUR,
            2: self.PART_TIME_HOUR
        }
        return work_hours.get(attendance)  

    def calculate_monthly_wage(self):
        while self.total_working_hours < self.TOTAL_WORKING_HOURS and self.total_working_days < self.TOTAL_WORKING_LIMIT:
            attendance = self.get_attendance()
            hours_worked = self.calculate_daily_wage(attendance)
            
            daily_wage = hours_worked * self.WAGE_PER_HOUR
            self.total_wage += daily_wage
            self.total_working_hours += hours_worked
            self.total_working_days += 1 if hours_worked > 0 else 0  

            print(f"Day {self.total_working_days}: Attendance {attendance}, Worked {hours_worked} hours, Earned ${daily_wage}")

        print("\nFinal Summary:")
        print(f"Total Working Days: {self.total_working_days}")
        print(f"Total Working Hours: {self.total_working_hours}")
        print(f"Total Monthly Wage: ${self.total_wage}")

    def start_wage_computation(self):
        print("Welcome to Employee Wage Computation Program\n")
        self.calculate_monthly_wage()

if __name__ == "__main__":
    employee = Employee_wage()  
    employee.start_wage_computation() 