class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.manager = None
        self.subordinates = []
        
    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)
        subordinate.manager = self

class FactoryHierarchy:
    def __init__(self):
        self.employees = {}
        
    def add_employee(self, name, position):
        if name not in self.employees:
            self.employees[name] = Employee(name, position)
            
    def set_manager(self, employee_name, manager_name):
        employee = self.employees.get(employee_name)
        manager = self.employees.get(manager_name)
        if employee and manager:
            manager.add_subordinate(employee)
    
    def find_colleagues(self, name):
        employee = self.employees.get(name)
        if not employee or not employee.manager:
            return []
        
        manager = employee.manager
        colleagues = [sub.name for sub in manager.subordinates if sub.name != name]
        return colleagues
    
    def find_subordinates(self, name):
        employee = self.employees.get(name)
        if not employee:
            return []
        
        subordinates = [sub.name for sub in employee.subordinates]
        return subordinates

    def find_hierarchy_level(self, name):
        employee = self.employees.get(name)
        level = 1
        while employee and employee.manager:
            level += 1
            employee = employee.manager
        return level


factory_hierarchy = FactoryHierarchy()
factory_hierarchy.add_employee('Stas', 'Dev')
factory_hierarchy.add_employee('Liza', 'Research')
factory_hierarchy.add_employee('Maks', 'Dev')
factory_hierarchy.add_employee('Kate', 'Dev')
factory_hierarchy.add_employee('Vyavheslav', 'Team lead')
factory_hierarchy.add_employee('Andry', 'CEO')

factory_hierarchy.set_manager('Maks', 'Stas')
factory_hierarchy.set_manager('Liza', 'Stas')
factory_hierarchy.set_manager('Stas', 'Vyavheslav')
factory_hierarchy.set_manager('Vyavheslav', 'Andry')

resutls = factory_hierarchy.find_subordinates('Stas')
print(resutls)
