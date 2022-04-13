# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

class Stack(object):
    def _init_(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        ''' Pushes a element to top of the stack '''
        if (self.isFull() != True):
            self.index.append(data)
        else:
            print('Stack overflow')

    def pop(self):
        ''' Pops the top element '''
        if (self.isEmpty() != True):
            return self.index.pop()
        else:
            print('Stack is already empty!')

    def isEmpty(self):
        ''' Checks whether the stack is empty '''
        return len(self.index) == []

    def isFull(self):
        ''' Checks whether the stack if full '''
        return len(self.index) == self.size

    def peek(self):
        ''' Returns the top element of the stack '''
        if (self.isEmpty() != True):
            return self.index[-1]
        else:
            print('Stack is already empty!')

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.index)

    def _str_(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

if __name__ == '_main_':
       myStack = Stack(10)
       for i in range(0, 10):
          myStack.push(i)
       print(myStack.isEmpty())
       print(myStack.isFull())
       print(myStack)
       print(myStack.stackSize())
       print(myStack.pop())
       print(myStack)
       print(myStack.peek())

       
 # 20CS097
# Vaibhav thummar