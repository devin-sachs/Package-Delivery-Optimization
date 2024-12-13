class Truck:
    def __init__(self,truck_id,speed = 18):
        self.truck_id = truck_id
        self.packages = set() #packages in a truck are a set to help avoid any duplication
        self.speed = speed  # 18 miles per hour average speed of truck

    def load_package(self,package):
        self.packages.add(package)

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s" % (self.truck_id, self.packages)