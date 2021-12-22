# Chapter 2: Objects in Python # 

## 1. The usage of mypy package ##

- The [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) package helps us to detect static errors in our python code where [mypy_usage.py](https://github.com/dukele35/python-oop-practices/blob/main/chap2-objects-in-python/mypy_usage.py) is an example.
- the usage: using `mypy --strict <python_file.py>` in the terminal.
- [Example](http://mypy-lang.org/).

## 2. Doctest for Python Class ##

- For this, please refer to [points.py](https://github.com/dukele35/python-oop-practices/blob/main/chap2-objects-in-python/points.py).
- Docstring is essential for writing python classes, methods, functions, etc. Please refer to the python file above as the blue-print or conventions for writing python doctring. 
- To enter the interactive shell with one particular python file, please use `python -i <python_file.py>` in the terminal. You are then able to get the information of the class by typing `help(<Class_Name>)` in the interactive environment. You can also get the information of the class or an instance with `<Instance>.__doc__`. 
- It is advisable to include example in the docstring with the following format:
```
>>> <something_1>
>>> <something_2>
result 
```
- Such examples could be validated by `python -m doctest -v <python_file.py>` in the terminal.
- [Example1](https://realpython.com/documenting-python-code/) & [Example2](https://www.programiz.com/python-programming/docstrings) for docstring documentation.

## 3. Useful hints from Python Typing ##

- Please refer to [typing_usage.py](https://github.com/dukele35/python-oop-practices/blob/main/chap2-objects-in-python/typing_usage.py).
- There are `#valid` as well as `#invalid` in the file as demonstrated for correct/incorrect examples of using [typing](https://docs.python.org/3/library/typing.html) to provide hints for variables, functions as well as functions' parameters. 
- To check the validity of the typing usage, please run `mypy --strict <python_file.py>`.