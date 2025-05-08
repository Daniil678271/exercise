from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    @abstractmethod
    def get_info(self) -> str:
        pass
    
class Worker(Employee):
    def get_info(self) -> str:
        return f" Работник :{self.name},  Возраст     :{self.age}, Зарплата      :{self.salary}"

class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, bonus: float):
        super().__init__(name, age, salary)
        self.bonus = bonus
    def get_info(self) -> str:
        return f" Работник :{self.name},  Возраст     :{self.age}, Зарплата      :{self.salary}, Бонус :{self.bonus}"
     
        
def print_employee_info(employee:Employee):
    print(employee.get_info())
    
if __name__ == "__main__":
    worker = Worker("Danya", 14, 50000)
    manager = Manager("Nastya", 55, 200000, 250)
    
    print_employee_info(worker)
    print_employee_info(manager)
    
    