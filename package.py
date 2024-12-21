#Devin Sachs
#Student ID: 011292435
#C950 Performance Assesment - Data Structures & Algorithms II

class Package:
    def __init__(self, package_id, address, city, state,zip_code, delivery_deadline,weight,delivery_time = "not yet delivered", delivery_status = "at the hub",special_notes=""):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes


    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zip_code, self.delivery_deadline, self.weight, self.delivery_status, self.delivery_time, self.special_notes)


    def set_status(self, input_status):
        if input_status == "at the hub":
            self.delivery_status = "at the hub"
        elif input_status == "en route":
            self.delivery_status = "en route "
        elif input_status == "delivered":
            self.delivery_status = "delivered"
