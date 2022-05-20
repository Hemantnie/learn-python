
def allCaps(f):
    
    def wrap(*args,**kwargs):
        
        x = f(*args,**kwargs)
        x = x.upper()
        return x
    return wrap

@allCaps
def foo():
    return "love is blinking"

class CallCount:
    def __init__(self,f):
        self.count = 0
        self.f = f
    
    def __call__(self,*args, **kwargs):
        self.count += 1
        return self.f(*args,**kwargs)

class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args,**kwargs)
        return wrap
            

@CallCount    
def hello(name):
    print(name)    




