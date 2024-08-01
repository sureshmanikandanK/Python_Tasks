class Salary:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_salary(self):
        return self.basic_salary


class Allowances(Salary):
    def __init__(self, basic_salary):
        super().__init__(basic_salary) 
        self.hra = 0.2 * self.basic_salary
        self.da = 0.4 * self.basic_salary
        self.ta = 0.25 * self.basic_salary

    def get_allowances(self):
        return {
            "HRA": self.hra,
            "DA": self.da,
            "TA": self.ta
        }

    def get_gross_salary(self):
        allowances_total = self.hra + self.da + self.ta
        return self.basic_salary + allowances_total


class Deductions(Allowances):
    def __init__(self, basic_salary):
        super().__init__(basic_salary) 
        self.insurance = 5000
        self.pf = 0.12 * self.basic_salary
        self.gratuity = 0.05 * self.basic_salary

    def get_deductions(self):
        return {
            "Insurance": self.insurance,
            "PF": self.pf,
            "Gratuity": self.gratuity
        }

    def get_net_salary(self):
        deductions_total = self.insurance + self.pf + self.gratuity
        return self.get_gross_salary() - deductions_total

    def get_salary_slip(self):
        slip = {
            "Basic Salary": self.get_salary(),
            "Gross Salary": self.get_gross_salary(),
            "Net Salary": self.get_net_salary(),
            "Allowances": self.get_allowances(),
            "Deductions": self.get_deductions()
        }
        return slip


def calculate_salary(basic_salary):
    return Deductions(basic_salary)

# Example usage:
cs = calculate_salary(10000)
salary_slip = cs.get_salary_slip()

print("Salary Slip:")
print(f"Basic Salary: {salary_slip['Basic Salary']}")
print(f"Gross Salary: {salary_slip['Gross Salary']}")
print(f"Net Salary: {salary_slip['Net Salary']}")
print("Allowances:")
for key, value in salary_slip['Allowances'].items():
    print(f"  {key}: {value}")
print("Deductions:")
for key, value in salary_slip['Deductions'].items():
    print(f"  {key}: {value}")
