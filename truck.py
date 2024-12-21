#Devin Sachs
#Student ID: 011292435
#C950 Performance Assessment - Data Structures & Algorithms II

class Truck:
    def __init__(self,truck_id,current_address = "4001 South 700 East", speed = 18):
        self.truck_id = truck_id
        self.packages = [] #packages in a truck are a set to help avoid any duplication
        self.current_address = current_address
        self.speed = speed  # 18 miles per hour average speed of truck

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s" % (self.truck_id, self.packages)

    def load_package(self,package):
        self.packages.append(package)

    def set_address(self,address):
        self.current_address = address

