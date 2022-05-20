import socket

# def resolve(host):
#     return socket.gethostbyname(host)

class Resolver:
    
    def __init__(self):
        self._cache = {}
    
    def __call__(self,host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()
        
    def has_host(self,host):
        return host in self._cache
    
def sequence_class(immutable):
    
    print(callable(sequence_class))
    if immutable:
        return tuple
    else:
        return list
    
def sequence_class_1(immutable):
    return tuple if immutable else list

def hypervolume_1(length,*lengths):
    v = length
    for item in lengths:
        v *= item
    return v

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v
    
 
 