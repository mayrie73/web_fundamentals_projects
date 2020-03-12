class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand= brand
        self.status="for sale"
    def Display_info(self):
        print "Price: ${}".format(self.price)
        print "item_name: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status) 
        print "  "
        return self 
    def Sell(self):
        self.status= "sold"
        return self
    def Add_tax(self):
        tax = 0.12 * self.price
        self.price = self.price + tax 
        return self
    def Return(self,reason):
        if reason == "defective":
            self.status="defective"
            self.price=0
        elif reason== "closed box":
            self.status="for sale"    
        elif reason== "opened box":
            self.status="used"
            self.price = self.price * .8
        return self    
coffee_maker= Product(100, "Coffee Maker", "2 lbs", "Keurig" )
blender= Product(100, "blender", "1 lbs", "Ninja")
blender1= Product(100, "blender", "1 lbs", "Ninja")
blender2= Product(100, "blender", "1 lbs", "Ninja")
coffee_maker.Add_tax().Display_info()
blender.Add_tax().Return("defective").Display_info()
blender1.Add_tax().Return("closed box").Display_info()
blender2.Add_tax().Return("opened box").Display_info()