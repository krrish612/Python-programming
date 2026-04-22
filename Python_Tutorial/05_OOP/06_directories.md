# Working with Directories

## OS Module
```python
import os
```

## Current Directory
```python
print(os.getcwd())  # Current working directory
```

## List Files
```python
# List all files in directory
print(os.listdir())

# List specific directory
print(os.listdir("C:/Users"))
```

## Create Directory
```python
os.mkdir("new_folder")           # Create one folder
os.makedirs("a/b/c")           # Create nested folders
```

## Remove Directory
```python
os.rmdir("empty_folder")        # Remove empty folder
os.rmdir("a/b/c")             # Remove nested (c only)
```

## Check if Exists
```python
print(os.path.exists("file.txt"))
print(os.path.isfile("file.txt"))
print(os.path.isdir("folder"))
```

## Path Operations
```python
# Join paths
path = os.path.join("folder", "file.txt")

# Get file name
print(os.path.basename(path))    # file.txt

# Get directory
print(os.path.dirname(path))    # folder

# Split extension
print(os.path.splitext("file.txt"))  # ('file', '.txt')
```

## Walk Through Directories
```python
for root, dirs, files in os.walk("."):
    print(f"Folder: {root}")
    print(f"Files: {files}")
```

## Practical Example
```python
import os

# Create project structure
os.makedirs("my_project/images")
os.makedirs("my_project/data")

# List all Python files
for file in os.listdir("."):
    if file.endswith(".py"):
        print(file)
```