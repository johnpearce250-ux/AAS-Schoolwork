# Salary Tracker - Employee Management System

A Python-based employee management system built with Object-Oriented Programming (OOP) principles. This system manages employee information including names, job levels, and salaries with built-in validation.

## Overview

The `Employee` class represents an employee with their name, job level, and salary. It enforces business rules through property validation and prevents invalid state changes.

## Features

### Base Salaries by Level
The system defines predefined base salaries for each job level:

| Level | Base Salary |
|-------|------------|
| trainee | $1,000 |
| junior | $2,000 |
| mid-level | $3,000 |
| senior | $4,000 |

## Class: Employee

### Constructor: `__init__(name, level)`

Initializes a new employee with validation.

**Parameters:**
- `name` (str): Employee's name
- `level` (str): Job level (trainee, junior, mid-level, or senior)

**Raises:**
- `TypeError`: If name or level is not a string
- `ValueError`: If level is not a valid job level

**Example:**
```python
charlie_brown = Employee('Charlie Brown', 'trainee')
```

### String Representations

#### `__str__()`
Returns a user-friendly string representation of the employee.

**Example Output:**
```
Charlie Brown: trainee
```

#### `__repr__()`
Returns a developer-friendly string representation that can be used to recreate the object.

**Example Output:**
```
Employee('Charlie Brown', 'trainee')
```

### Properties

#### `name` Property
Gets or sets the employee's name.

**Getter:** Returns the employee's name
**Setter:** 
- Validates that the input is a string
- Raises `TypeError` if not a string
- Prints confirmation message on successful update

**Example:**
```python
print(charlie_brown.name)  # Charlie Brown
charlie_brown.name = 'Charles Brown'  # 'name' updated to 'Charles Brown'.
```

#### `level` Property
Gets or sets the employee's job level (promotion management).

**Getter:** Returns the employee's current job level
**Setter:**
- Validates that the new level exists
- Prevents demotion (level can only stay same or go up)
- Prevents unnecessary updates (can't set to current level)
- Updates salary automatically on promotion
- Raises `ValueError` if attempting demotion, invalid level, or same level
- Prints confirmation message on successful promotion

**Example:**
```python
charlie_brown.level = 'junior'  # 'Charlie Brown' promoted to 'junior'.
```

#### `salary` Property
Gets or sets the employee's salary.

**Getter:** Returns the employee's current salary
**Setter:**
- Validates that input is a number (int or float)
- Ensures salary doesn't go below the minimum for the current level
- Raises `TypeError` if not a number
- Raises `ValueError` if salary is below minimum
- Prints confirmation message on successful update

**Example:**
```python
print(charlie_brown.salary)  # 1000
charlie_brown.salary = 1500  # Salary updated to $1500.
```

## Usage Example

```python
# Create a new employee
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)  # Charlie Brown: trainee
print(f'Base salary: ${charlie_brown.salary}')  # Base salary: $1000

# Promote employee to next level
charlie_brown.level = 'junior'  # 'Charlie Brown' promoted to 'junior'.
```

## Validation Rules

1. **Name & Level**: Must be strings
2. **Level**: Must be one of: trainee, junior, mid-level, senior
3. **Promotions Only**: Level can only increase or stay the same, never decrease
4. **Salary Floor**: Salary cannot fall below the minimum for the employee's level
5. **No Redundant Changes**: Cannot set level to its current value

## Error Handling

The class raises specific exceptions to handle invalid operations:

- `TypeError`: For invalid data types (non-string names/levels, non-numeric salaries)
- `ValueError`: For invalid values (invalid levels, demotion attempts, salary too low)

## Class Design Notes

- Uses private attributes (`_name`, `_level`, `_salary`) for encapsulation
- Uses properties with getters and setters for controlled access
- Class variable `_base_salaries` stores configuration data
- Immutable class variable prevents accidental modification
