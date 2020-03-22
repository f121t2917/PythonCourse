import one

print("top-level in two.py")

one.func()

if __name__ == "__main__": # python two.py
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

    
'''
# python two.py 

top-level print inside of one.py
one.py is being imported into another module
top-level in two.py
func() ran in one.py
two.py is being run directly
'''