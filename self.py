
import time
class Person:
    
    def __init__(self,id,name):
        self.id = id
        self.name = name

    @staticmethod
    def printMe():
        print("Hello")
        
    @classmethod
    def classMethodExample(cls,val):
        print(cls.printMe())
        print('Class method -> '  + str(val)) 
        
    def __call__(self):
        print("I am a person")


def tryMe():
    
    a = "I am a global"
    def foo():
        # print(a)
        print('Good That You tried me')
    
    return foo
    #from self import Person
    
def make_timer():
    last_called = None
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed
    
