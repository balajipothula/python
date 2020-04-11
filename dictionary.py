emp = {101: {'name': 'Ram', 'sal': 22000}, 102: {'name': 'Sam', 'sal': 19000} }

emp_no_set = sorted(emp.keys())

for no in emp_no_set: print(no, emp.get(no)['name'], emp.get(no)['sal'])
