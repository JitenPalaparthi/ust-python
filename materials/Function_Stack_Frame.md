
# 🧠 Function Stack Frame in Python – Simple Explanation

A **stack frame** is a block of memory used to **store information about a function call**, including:

- Local variables
- Function arguments
- Return address (where to resume after the function ends)
- Intermediate data

Python uses a **call stack** to manage function calls. Each time a function is called, a **new stack frame** is created and pushed onto the stack. When the function returns, its frame is **popped** off.

---

## 📦 What’s Inside a Stack Frame?

When a function is called, Python creates a stack frame that contains:

| Element            | Description                                         |
|--------------------|-----------------------------------------------------|
| Arguments          | Values passed to the function                       |
| Local variables    | Variables declared inside the function              |
| Return address     | Where to return control after function execution    |
| Function context   | Includes the scope and temporary values             |

---

## 🧪 Example

```python
def multiply(a, b):
    result = a * b
    return result

def main():
    x = 5
    y = 10
    z = multiply(x, y)
    print(z)

main()
```

### Stack Frame Order:

1. `main()` stack frame is pushed  
2. Inside `main()`, `multiply(x, y)` is called → `multiply()` stack frame is pushed  
3. `multiply()` computes result and returns → `multiply()` frame is popped  
4. `main()` prints the result → then `main()` frame is popped

---

## 🔁 Visual Representation

```
[Top of Stack]
-------------------
| multiply(a=5, b=10) | <- Active
-------------------
| main()             |
-------------------
[Bottom of Stack]
```

When `multiply()` finishes, its frame is removed:

```
[Top of Stack]
-------------------
| main()             | <- Active
-------------------
[Bottom of Stack]
```

---

## 🛠 Under the Hood

In CPython (the main Python interpreter), this is implemented using **C structures**. Each function call creates a `PyFrameObject` internally.

---

## 🔄 Recursion and Stack

Each recursive call creates **a new stack frame**. Too many calls can lead to a **stack overflow**.

```python
def recurse(n):
    if n == 0:
        return
    recurse(n - 1)

recurse(1000)  # works
recurse(100000)  # may hit RecursionError
```
