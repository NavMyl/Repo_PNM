class Employee(object):

    raise_amt = 1.05
    num_of_emp = 0

    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay=pay
        self.email = firstname+lastname+'@Comp.com'

        Employee.num_of_emp +=1

    def full_name(self):
        return '{} {}'.format(self.firstname,self.lastname)


    def pay_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod
    def from_String_split(cls,emp_str):
        firstname, lastname, (pay) = emp_str.split('-')
        return cls(firstname,lastname, int(pay))

class Developer(Employee):
    raise_amt =1.10

    def __init__(self, firstname, lastname, pay, coding_lang):
        Employee.__init__(self,firstname, lastname, pay)
        self.coding_lang = coding_lang


class Manager(Employee):

    def __init__(self, firstname, lastname, pay, Employees=None):
        Employee.__init__(self,firstname, lastname, pay)

        if Employees == None:
            self.Employees = []
        else:
            self.Employees = Employees

    def add_emp(self,emp):
        if emp not in self.Employees:
            self.Employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.Employees:
            self.Employees.remove(emp)

    def print_emp(self):
        for emp in self.Employees:
            print('Employees are',emp.full_name())



#emp3_str= 'testfname-testlname-90000-C'
#emp4_str = 'test2fname-test2lname-95000'
#fname,lname,pay=emp3_str.split('-')



emp1=Developer('Naveen','Kumar',60000,'C')
emp2=Employee('Na','Kum',60001)
#emp3=Employee(fname,lname,pay)
#emp3= Developer.from_String_split(emp3_str)
mgr1=Manager('A','BC',68000,[emp1])

#print(help(Developer))
print emp1.email
print emp1.coding_lang

emp1.pay_raise()

print Developer.raise_amt

print emp1.pay
print mgr1.email
#print mgr1.Employees
mgr1.print_emp()
mgr1.add_emp(emp2)
mgr1.print_emp()