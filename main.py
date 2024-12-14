import csv
import hash
import package
import truck
import datetime

distance_data = []
address_data  = []


hash_table = hash.ChainingHashTable()

def load_package_data():
    with open("WGUPS Package File-cleanup.csv") as packageCSV:
        package_rows = csv.reader(packageCSV, delimiter=',')
        next(package_rows)  # skip header
        for package_csv in package_rows:
            package_id = package_csv[0]
            address = package_csv[1]
            city = package_csv[2]
            state = package_csv[3]
            zip_code = package_csv[4]
            delivery_deadline = package_csv[5]
            weight = package_csv[6]
            special_notes = package_csv[7]

            #create package object
            all_packages = package.Package(package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes)
            # print(all_packages)

            #insert into hash table

            hash_table.insert(package_id,all_packages)


load_package_data()

#validating hash table and that packages were inserted properly

# for i in range(len(hash_table.table) + 1):
#     print("Package: {}".format(hash_table.table[i - 1]))
#
# print(hash_table)

def load_distance_data():
    with open("WGUPS Distance Table-cleaned.csv") as distance_CSV_file:
        csv_reader = csv.reader(distance_CSV_file, delimiter=',')
        next(csv_reader)  # skip header
        for row in csv_reader:
            for num in range(len(row)):
                try:
                    row[num] = float(row[num])
                except ValueError:
                    pass

            distance_data.append(row)


            #insert into hash table

load_distance_data()

#validate distance data
# print(distance_data[5][2])
# print(distance_data[2][5])
#
# for i in range(27):
#     print(distance_data[i])


def load_address_data():
    with open("WGUPS Address Table-cleaned.csv" , encoding='utf-8-sig') as address_CSV_file:
        csv_reader = csv.reader(address_CSV_file, delimiter=',')
        for row in csv_reader:
            address_data.extend(row) #using extend to only have a one-dimensional list

load_address_data()

# validate address data
# print(address_data)

#returns x,y distance value from distance table
def distance_between(address1,address2):
    address1 = address_data.index(address1)
    address2 = address_data.index(address2)
    return distance_data[address1][address2]

#validate distance between function
# print(distance_between("4001 South 700 East","177 W Price Ave"))

def min_distance(from_address,truck_packages):
    for truck_package in truck_packages:
        return distance_between(from_address, truck_packages.packages[truck_package.address])

# min_distance()
# TO DO - COME BACK TO WORK ON THIS FUNCTION

truck1 = truck.Truck(1)
truck2 = truck.Truck(2)
truck3 = truck.Truck(3)

# Manually loading packages in trucks

def load_all_trucks():
    # Loading truck 3 with certain special notes packages
    truck3.load_package(hash_table.search("9"))  # package has wrong address
    truck3.load_package(hash_table.search("6"))  # some don't arrive until 9:05am
    truck3.load_package(hash_table.search("25"))  # the rest don't fit with the rest of the trucks
    truck3.load_package(hash_table.search("28"))
    truck3.load_package(hash_table.search("32"))

    truck3.load_package(hash_table.search("27"))
    truck3.load_package(hash_table.search("33"))
    truck3.load_package(hash_table.search("35"))
    truck3.load_package(hash_table.search("39"))

    truck3.load_package(hash_table.search("2"))
    truck3.load_package(hash_table.search("4"))

    # Loading truck 2
    truck2.load_package(hash_table.search("3"))  # packages must be on truck 2 or delivered together

    truck2.load_package(hash_table.search("1"))
    truck2.load_package(hash_table.search("18"))
    truck2.load_package(hash_table.search("36"))
    truck2.load_package(hash_table.search("38"))

    truck2.load_package(hash_table.search("13"))
    truck2.load_package(hash_table.search("14"))
    truck2.load_package(hash_table.search("15"))
    truck2.load_package(hash_table.search("16"))

    truck2.load_package(hash_table.search("19"))
    truck2.load_package(hash_table.search("20"))
    truck2.load_package(hash_table.search("29"))
    truck2.load_package(hash_table.search("30"))

    # Loading truck 1
    truck1.load_package(hash_table.search("31"))
    truck1.load_package(hash_table.search("34"))
    truck1.load_package(hash_table.search("37"))
    truck1.load_package(hash_table.search("40"))

    truck1.load_package(hash_table.search("5"))
    truck1.load_package(hash_table.search("7"))
    truck1.load_package(hash_table.search("8"))
    truck1.load_package(hash_table.search("10"))

    truck1.load_package(hash_table.search("11"))
    truck1.load_package(hash_table.search("12"))
    truck1.load_package(hash_table.search("17"))
    truck1.load_package(hash_table.search("21"))

    truck1.load_package(hash_table.search("22"))
    truck1.load_package(hash_table.search("23"))
    truck1.load_package(hash_table.search("24"))
    truck1.load_package(hash_table.search("26"))

load_all_trucks()

#Validate the packages for a given truck
# for current_package in truck1.packages:
#     print(current_package)

#The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
# WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the
# correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

# def truck_deliver_packages(truck):
#     miles_traveled = 0
#     time = 0
#     for address in truck.packages.address:
#         min_distance(address)

def deliver_packages(truck):
    route_mileage = 0
    for current_package in truck.packages:
        current_package.set_status("en route")
        if current_package.delivery_deadline == "9:00 AM":
            route_mileage += distance_between(truck.current_address,current_package.address)
            truck.current_address = current_package.address
            current_package.set_status("delivered")

        elif current_package.delivery_deadline == "10:30 AM":
            route_mileage += distance_between(truck.current_address,current_package.address)
            truck.current_address = current_package.address
            current_package.set_status("delivered")

        elif current_package.delivery_deadline == "EOD":
            route_mileage += distance_between(truck.current_address,current_package.address)
            truck.current_address = current_package.address
            current_package.set_status("delivered")

    return route_mileage

print(deliver_packages(truck1))
print(deliver_packages(truck2))
print(deliver_packages(truck3))

# for current_package in truck2.packages:
#     print(distance_between(current_package.address,truck2.current_address))
#
# for current_package in truck3.packages:
#     print(distance_between(current_package.address,truck3.current_address))

# hours = distance / speed