
# 🌟 Object-Oriented Programming (OOP) Principles

Object-Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data and methods.

Objects are classified as classes

## 🧱 1. Encapsulation

> Wrapping data (variables) and code (methods) together into a single unit (class), and restricting direct access to some of the object’s components.

- ✅ Helps with data hiding.
- ✅ Prevents accidental modification.
- ✅ Achieved via private, public, and protected members.

**Example (Python):**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

## 🧬 2. Inheritance

> One class can inherit properties and methods from another class.

- ✅ Promotes code reuse.
- ✅ Enables a natural hierarchy.

**Example:**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

---

## 🧠 3. Polymorphism

> Same interface, different behavior. It allows methods to do different things based on the object calling them.

- ✅ Makes code flexible and extensible.
- ✅ Can be achieved via method overriding or overloading (Python supports overriding, not true overloading).

**Example:**
```python
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def take_off(flier):
    flier.fly()

take_off(Bird())       # Bird flies
take_off(Airplane())   # Airplane flies
```

---

## 🧰 4. Abstraction

> Hiding the complex implementation and showing only the essential features.

- ✅ Helps manage complexity.
- ✅ Achieved using abstract classes or interfaces.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

---

## 📌 Summary Table

| Principle      | Purpose                          | Key Feature                     |
|----------------|----------------------------------|----------------------------------|
| Encapsulation  | Data hiding and access control   | Private/public attributes        |
| Inheritance    | Reuse and hierarchy              | `class Subclass(Superclass)`    |
| Polymorphism   | Same method, different behavior  | Method overriding                |
| Abstraction    | Simplify complex systems         | Abstract base classes            |

---
