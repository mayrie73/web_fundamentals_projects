class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        print "creating a bike"
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def display_info(self):
        print "Price: ${}".format(self.price),"Max_Speed: {}".format(self.max_speed), "Miles: {}".format(self.miles)
        return self
    def ride(self):
        self.miles=self.miles+10
        print "Riding:{}".format(self.miles)
        return self
    def reverse(self):
        if self.miles < 5:
            print "Cannot reverse. We only have:", self.miles, "miles left"
        if self.miles > 5:
            self.miles= self.miles-5
            print "Reversing:{}".format(self.miles)  
        return self
bike1=Bike(200, "25mph")
bike2=Bike(300, "40mph")
bike3=Bike(400, "60mph")

print bike1.ride().ride().ride().reverse().display_info()
print bike2.ride().ride().reverse().reverse().display_info()
print bike3.reverse().reverse().reverse().display_info()