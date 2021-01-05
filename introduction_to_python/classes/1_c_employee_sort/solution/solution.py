from operator import itemgetter, attrgetter, itemgetter

class Employee:
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

    def __repr__(self):
            return '({})'.format(self.name)

#employee_list = [emp1, emp2, emp3, emp4]
def sort_employees(employee_lst):
    employees = sorted(employee_lst, key=attrgetter('name'))
    return [employee.name for employee in employees]
