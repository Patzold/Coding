# We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as:  ((32+8)∗(5/2))/(2+6).
# In real life this extend to many things such as text editor plugins and interactive development environments for all sorts of bracket completion checks.
# Takes a string as an input and return True if it's parentheses are balanced or False if it is not.

# The stack class imported from basics part

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
        equation(string): String form of equation
    Returns:
        bool: Return if parentheses are balanced or not
    """
    
    # TODO: Intiate stack object
    stack = Stack()    
    # TODO: Interate through equation checking parentheses
    for letter in equation:
        if letter == "(": stack.push(True)
        if letter == ")":
            if stack.pop() == None: return False
    
    # TODO: Return True if balanced and False if not
    
    if stack.size() == 0: return True
    return False

# -- TEST CASES ---
print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")