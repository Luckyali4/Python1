#Q1.  Write a python program to describe local and global variable with same name?
name="Global Name"
def demonstrate_scope():
    name="Local Name"
    print("Inside the function,name is:",name)
    demonstrate_scope()
    print("Outside the function, name is:"name)