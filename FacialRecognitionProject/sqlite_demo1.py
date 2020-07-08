import sqlite3
from employee import Employee

conn = sqlite3.connect(':employee.db')

c = conn.cursor()



def printi(emps):
    print(emps)



def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def get_emps_by_id(id):
    c.execute("SELECT last FROM employees WHERE pay=:pay", {'pay': id})
  
    for row in c.fetchall():
        print(row[0])
    return (row[0])









##emps = get_emps_by_name('Doe')
##print(emps)



emps = get_emps_by_id('6')
print(emps)
printi(emps)

conn.close()