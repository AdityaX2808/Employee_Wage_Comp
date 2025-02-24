import random 

class EmployeeWage:
    def __init__(self, company_name, wage_per_hour, max_working_days, max_working_hours):
        
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def get_attendance(self):
        return random.randint(0, 2) #checking attendance

    def calculate_daily_wage(self, attendance): # total wages 
        work_hours = {
            0: 0,   # Absent
            1: 8,   # Full-time
            2: 4    # Part-time
        }
        return work_hours.get(attendance, 0)

    def compute_employee_wage(self):
        #calculate total wage 
        total_wage = 0
        total_working_hours = 0
        total_working_days = 0

        print(f"\nCalculating Wages for {self.company_name}...")

        while total_working_hours < self.max_working_hours and total_working_days < self.max_working_days:
            attendance = self.get_attendance()
            hours_worked = self.calculate_daily_wage(attendance)

            # Ensure we do not exceed max hours
            if total_working_hours + hours_worked > self.max_working_hours:
                hours_worked = self.max_working_hours - total_working_hours

            daily_wage = hours_worked * self.wage_per_hour
            total_wage += daily_wage
            total_working_hours += hours_worked
            total_working_days += 1 if hours_worked > 0 else 0  

            print(f"Day {total_working_days}: Attendance {attendance}, Worked {hours_worked} hours, Earned ${daily_wage}")

        print("\nFinal Summary for", self.company_name)
        print(f"Total Working Days: {total_working_days}")
        print(f"Total Working Hours: {total_working_hours}")
        print(f"Total Monthly Wage: ${total_wage}")

if __name__ == "__main__":
    # Creating instances for multiple companies
    company1 = EmployeeWage("Company A", wage_per_hour=20, max_working_days=20, max_working_hours=100)
    company2 = EmployeeWage("Company B", wage_per_hour=25, max_working_days=22, max_working_hours=110)

    # Compute wages for both companies
    company1.compute_employee_wage()
    company2.compute_employee_wage()
