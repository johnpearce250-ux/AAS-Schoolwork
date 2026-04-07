class Employee:
    _base_salaries = {
            'trainee': 1000,
            'junior': 2000,
            'mid-level': 3000,
            'senior': 4000
        }
    def __init__ (self, name, level):
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attribute must be of type 'str'."))
        
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        
        self._name = name
        self._level = level

        self._salary = Employee._base_salaries[level]
    
    def __str__(self):
        return f'{self.name}: {self.level}'
    
    def __repr__(self):
        return f'Employee({repr(self.name)}, {repr(self.level)})'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{new_name}'.")
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, new_level):
        if not new_level in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.") 
        current_salary = Employee._base_salaries[self.level]
        new_salary = Employee._base_salaries[new_level]
        if new_salary < current_salary:
            raise ValueError(f"Cannot change to lower level.")
        self.salary= Employee._base_salaries[new_level]
        self._level = new_level
        print(f"'{self.name}' promoted to '{new_level}'.")
     
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f"Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.")
        self._salary = new_salary
        print(f"Salary updated to ${new_salary}.")

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'


    