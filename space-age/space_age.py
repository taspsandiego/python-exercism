class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_earth(self):
        T = 365.25*24*3600
        return round(self.seconds/T)

    def on_mars(self):
        T = 1.8808158*24*3600
        return round(self.seconds/T)
        
    def on_venus(self):
        T = 0.61519726*24*3600
        return round(self.seconds/T)
        
    def on_mercury(self):
        T = 0.2408467*24*3600
        return round(self.seconds/T)
    
    def on_jupiter(self):
        T = 11.862615*24*3600
        return round(self.seconds/T)   
        
    def on_uranus(self):
        T = 84.016846*24*3600
        return round(self.seconds/T)   
        
    def on_neptune(self):
        T = 164.79132*24*3600
        return round(self.seconds/T)   
    