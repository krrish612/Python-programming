# How Python Code Gets Executed

## The Process
```
Your Code → Compiler/Interpreter → Machine Code → Output
```

## Python is Interpreted
Python reads your code line by line and executes it immediately.

## Steps:
1. **Write** - You write code in .py file
2. **Compile** - Python checks for errors (syntax)
3. **Interpret** - Converts each line to machine code
4. **Execute** - Runs the code
5. **Output** - Shows result

## How It's Different from Compiled Languages
| Compiled (C, C++) | Interpreted (Python) |
|-------------------|-------------------|
| All code compiles first | Code runs line by line |
| Errors shown at compile | Errors shown when running |
| Faster execution | Slower but easier |

## What Happens in Memory
```python
x = 10
y = 20
print(x + y)
```

1. Allocate memory for x
2. Store 10 in x's memory
3. Allocate memory for y
4. Store 20 in y's memory
5. Read values
6. Add them
7. Print result to screen

## IDEs and Interpreters
- **IDLE** - Python's built-in IDE
- **VS Code** - Popular editor
- **PyCharm** - Python-specific IDE
- **Jupyter** - For data science