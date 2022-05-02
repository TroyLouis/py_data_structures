# Last-In First-Out, all push and pop are to/from the top

class Stack():
    #initalize
    def __init__(self):
        self.stack = list()

    def push(self,item):
        ''' Adds an item to the stack returns None '''
        self.stack.append(item)

    def pop(self,item):
        ''' Removes item from top of stack if stack isn't empty '''
        if len(self.stack) > 0:
            self.stack.pop(item)
            return self.stack
        else:
            return None

    def peek(self):
        ''' Returns top of stack if the stack is not empty '''
        last_item = len(self.stack) - 1
        if len(self.stack) > 0:
            return self.stack[last_item]
        else:
            return None

    # returns a string representation of the list
    def __str__(self):
        return str(self.stack)
