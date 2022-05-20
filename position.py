class Position:
    
    def __init__(self,latitude,longitude):        
        self.latitude = latitude
        self.longitude = longitude
        
    def __repr__(self):
        return f"{type(self).__name__} is { self.latitude } and longitude is { self.longitude}"
        
    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude
    
    @latitude.setter
    def latitude(self,val):
        if not (-90 <= val <= +90):
            raise ValueError(f"Latitude {val} out of range")
        self._latitude = val
    
    @longitude.setter
    def longitude(self,val):
        if not (-180 <= val <= +180):
            raise ValueError(f"Longitude {val} out of range")
        self._longitude = val