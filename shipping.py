import iso6346
class ShippingContainer:
    
    #This is defined at the Class level
    #For the LEGB Rule this is not treated as a varibale at globla level, because in Python class Don't create a scope.
    next_serial = 1337
    
    @classmethod
    def __class_generate_serial(cls):
        
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    @classmethod
    def create_empty(cls,owner_code, **kwargs):
        return cls(owner_code=owner_code, contents=[],**kwargs)
    
    @staticmethod
    def play():
        print("Ohhhhhhhhhhhhh Tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    
    @staticmethod
    def __generate_serial():
        result  = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6)
        )
         
    
    def __init__(self,owner_code,contents,**kwargs):
        self.owner_code = owner_code
        self.contents = contents
        # self.serial = ShippingContainer.__generate_serial()
        # self.serial = self.next_serial
        # ShippingContainer.next_serial += 1
        #Think what will happen here self.next_serial = self.next_serial + 1
        # self.next_serial += 1
        self.bic = self._make_bic_code(
            owner_code, 
            serial= ShippingContainer.__generate_serial()
            )

class RefrigeratedShippingContainer(ShippingContainer):
    
    MAX_CELSIUS = 4.0
    
    def __init__(self, owner_code,contents,*,celsius,**kwargs):
        super().__init__(owner_code=owner_code,contents=contents)
        self.celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS :
            raise ValueError("Temparature too hot")
        self._celsius = celsius
    
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code= owner_code, 
            serial = str(serial).zfill(6),
            category = "R"
            )     