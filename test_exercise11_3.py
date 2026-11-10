from exercise11_3 import Employee

def test_give_default_raise():
    employee = Employee("Khairul", "Ahmad", 50000)

    employee.give_raise()

    assert employee.annual_salary == 55000


def test_give_custom_raise():
    employee = Employee("Khairul", "Ahmad", 50000)

    employee.give_raise(10000)

    assert employee.annual_salary == 60000