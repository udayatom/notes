#### Decorator

A decorator lets you add reusable behavior to functions or methods without changing their core implementation. This is useful for concerns like validation, logging, timing, authentication, caching, and more, allowing you to write that logic once and apply it wherever it's needed.

# Python Decorators - Complete Reference Notes

# 1. What is a Decorator?

A **decorator** is a function that takes another function (or method) as input, adds some extra functionality, and returns a new function.

In simple words:

> A decorator allows you to modify or extend the behavior of a function without changing its original source code.

Think of it as wrapping a gift.

- Original function = Gift
- Decorator = Gift wrapper

The gift remains the same, but the wrapper adds something extra.

---

# 2. Why Do We Need Decorators?

Suppose you have many functions.

```python
def login():
    print("Logging in...")

def logout():
    print("Logging out...")

def profile():
    print("Showing profile...")
```

Now suppose before every function you want to:

- Check login
- Print logs
- Measure execution time
- Handle exceptions

Without decorators:

```python
print("Starting...")
login()
print("Finished")

print("Starting...")
logout()
print("Finished")

print("Starting...")
profile()
print("Finished")
```

Notice how the same code is repeated.

Decorators solve this repetition.

---

# 3. Functions are First-Class Objects

Python treats functions like variables.

Example:

```python
def greet():
    print("Hello")

message = greet

message()
```

Output

```
Hello
```

A function can also be passed to another function.

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

Output

```
Hello
```

Since functions can be passed around, decorators become possible.

---

# 4. Building Our First Decorator

```python
def my_decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper
```

Let's understand it.

The decorator receives

```
func
```

which is the original function.

Inside it creates another function

```
wrapper()
```

This wrapper

1. Executes code before
2. Calls original function
3. Executes code after

Finally

```python
return wrapper
```

returns the new function.

---

# 5. Applying the Decorator Manually

Original function

```python
def greet():
    print("Hello")
```

Decorate it

```python
greet = my_decorator(greet)
```

Now call

```python
greet()
```

Output

```
Before function
Hello
After function
```

Notice

The original function never changed.

The decorator changed its behavior.

---

# 6. The @ Syntax

Instead of writing

```python
greet = my_decorator(greet)
```

Python provides shorthand syntax.

```python
@my_decorator
def greet():
    print("Hello")
```

Python internally converts it into

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

These two are exactly the same.

---

# 7. Understanding the Flow

Suppose we have

```python
@my_decorator
def greet():
    print("Hello")
```

Execution flow

```
Python reads greet()

↓

Python passes greet to my_decorator()

↓

my_decorator creates wrapper()

↓

wrapper is returned

↓

greet now points to wrapper()

↓

Calling greet()

↓

Actually executes wrapper()

↓

wrapper executes original greet()
```

Visual representation

```
greet()

↓

wrapper()

↓

Before

↓

Original greet()

↓

After
```

---

# 8. Example: Execution Timer

```python
import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print(f"Execution Time: {end-start:.2f}")

    return wrapper
```

Usage

```python
@timer
def task():

    time.sleep(2)

    print("Task completed")

task()
```

Output

```
Task completed
Execution Time: 2.00
```

---

# 9. Example: Logging

```python
def logger(func):

    def wrapper():

        print(f"Calling {func.__name__}")

        func()

        print("Finished")

    return wrapper
```

Usage

```python
@logger
def save():

    print("Saving data")

save()
```

Output

```
Calling save
Saving data
Finished
```

---

# 10. Example: Login Required

```python
logged_in = False

def login_required(func):

    def wrapper():

        if logged_in:
            func()
        else:
            print("Please login first")

    return wrapper
```

Usage

```python
@login_required
def dashboard():

    print("Dashboard")

dashboard()
```

Output

```
Please login first
```

---

# 11. Decorators with Arguments

Most functions have arguments.

Without handling arguments

```python
def greet(name):
    print(name)
```

This won't work.

Instead use

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper
```

Now

```python
@decorator
def greet(name):

    print(name)

greet("Alice")
```

Output

```
Before
Alice
After
```

`*args` handles positional arguments.

`**kwargs` handles keyword arguments.

---

# 12. Returning Values

Suppose

```python
def add(a, b):
    return a + b
```

Decorator

```python
def logger(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        print("Executed")

        return result

    return wrapper
```

Usage

```python
@logger
def add(a, b):
    return a+b

print(add(3,4))
```

Output

```
Executed
7
```

---

# 13. Decorators in Classes

Python has many built-in decorators.

## @staticmethod

```python
class Math:

    @staticmethod
    def add(a, b):
        return a+b
```

No self.

No cls.

Acts like a normal function inside the class.

---

## @classmethod

```python
class Student:

    school = "ABC School"

    @classmethod
    def get_school(cls):
        return cls.school
```

Receives

```
cls
```

instead of

```
self
```

---

## @property

Turns a method into an attribute.

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2
```

Usage

```python
c = Circle(5)

print(c.area)
```

Notice

No parentheses.

---

# 14. Decorators in Pydantic

Example

```python
from pydantic import BaseModel, field_validator

class Patient(BaseModel):

    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        return value.upper()
```

Creating object

```python
patient = Patient(name="john")
```

Flow

```
Input

↓

Pydantic validates type

↓

Runs field_validator()

↓

Converts to uppercase

↓

Stores value
```

Result

```
patient.name

JOHN
```

---

# 15. Email Validator Example

```python
class Patient(BaseModel):

    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        allowed = ["company.com"]

        domain = value.split("@")[-1]

        if domain not in allowed:

            raise ValueError("Invalid Domain")

        return value
```

Input

```
abc@gmail.com
```

Output

```
ValidationError
```

Input

```
abc@company.com
```

Accepted.

---

# 16. Real-World Uses of Decorators

Decorators are commonly used for:

- Authentication
- Authorization
- Logging
- Execution timing
- Input validation
- Rate limiting
- Database transactions
- Exception handling
- Caching
- API routing (Flask/FastAPI)
- Retry logic
- Monitoring
- Permissions

---

# 17. Popular Framework Examples

Flask

```python
@app.route("/")
def home():
    return "Hello"
```

The `@app.route` decorator registers `home()` as the handler for the `/` URL.

FastAPI

```python
@app.get("/users")
def get_users():
    return []
```

The `@app.get` decorator registers `get_users()` as the endpoint for `GET /users`.

Pydantic

```python
@field_validator("email")
```

Registers a method that validates the `email` field whenever a model instance is created.

---

# 18. Advantages

- Reuse common code
- Avoid duplication
- Keep business logic clean
- Easy to maintain
- Easy to test
- Improve readability
- Follow the DRY (Don't Repeat Yourself) principle

---

# 19. Summary

A decorator:

- Is a function.
- Takes another function as input.
- Adds extra behavior.
- Returns a new function.
- Does not modify the original function's source code.
- Is applied using the `@decorator_name` syntax.

General flow:

```
Original Function
        │
        ▼
Decorator Receives Function
        │
        ▼
Creates Wrapper Function
        │
        ▼
Adds Extra Logic
        │
        ▼
Calls Original Function
        │
        ▼
Returns Wrapper
        │
        ▼
Calling the Original Name Actually Calls the Wrapper
```

Remember this mental model:

> **A decorator wraps a function to add reusable behavior before, after, or around the function's execution without changing the function's original implementation.**
