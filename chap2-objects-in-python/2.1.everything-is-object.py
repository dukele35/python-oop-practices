# these will show <'class string'> or <'class interger'>
# print(type("Hello, world!"))
# print(type(42))

def odd(n:int) -> bool:
    return n%2 != 0

def main():
    print(odd("Hello, world!"))

if __name__=="__main__":
    main()