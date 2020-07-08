import sqlite3
from employee import Employee


conn = sqlite3.connect(':employee.db')
c = conn.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")





##def printi(emps):
##    print(emps)
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
   

##def get_emps_by_id(id):
##    c.execute("SELECT last FROM employees WHERE pay=:pay", {'pay': id})
##  
##    for row in c.fetchall():
##        print(row[0])
##    return (row[0])




def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('moin', 'moinuddin.ub@somaiya.edu', 1)
emp_2 = Employee('Jimit', 'jimit.ks@somaiya.edu', 2)
emp_3 = Employee('srijan', 'srijan.das@somaiya.edu', 3)
emp_4 = Employee('neha', 'mishra.na@somaiya.edu', 4)
emp_5 = Employee('anuya', 'anuya.padte@somaiya.edu', 5)
emp_6 = Employee('sanjali', 'sanjali@somaiya.edu', 6)
emp_7 = Employee('moin', 'skyasky1@gmail.com', 7)
emp_8 = Employee('moin', 'skyasky1@gmail.com', 8)
emp_9 = Employee('moin', 'skyasky1@gmail.com', 9)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)
insert_emp(emp_5)
insert_emp(emp_6)
insert_emp(emp_7)
insert_emp(emp_8)
insert_emp(emp_9)

##emps = get_emps_by_name('Doe')
##print(emps)






conn.close()