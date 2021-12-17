# these will show <'class string'> or <'class interger'>
# print(type("Hello, world!"))
# print(type(42))

def odd(n:int) -> bool:
    return n%2 != 0

def main():
    print(odd("Hello, world!"))

if __name__=="__main__":
    main()

# RUNNING mypy
# doc: https://mypy.readthedocs.io/en/stable/getting_started.html
# mypy --strict chap2-objects-in-python/2.1.mypy-package-usage.py 
# chap2-objects-in-python/2.1.mypy-package-usage.py:8: error: Function is missing a return type annotation
# chap2-objects-in-python/2.1.mypy-package-usage.py:8: note: Use "-> None" if function does not return a value
# chap2-objects-in-python/2.1.mypy-package-usage.py:9: error: Argument 1 to "odd" has incompatible type "str"; expected "int"
# chap2-objects-in-python/2.1.mypy-package-usage.py:12: error: Call to untyped function "main" in typed context
# Found 3 errors in 1 file (checked 1 source file)