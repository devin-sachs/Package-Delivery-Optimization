import csv
import hash
import package
import truck
import datetime

distance_data = []
address_data = []

hash_table = hash.ChainingHashTable()


def load_package_data():
    with open("WGUPS Package File-cleanup.csv") as packageCSV:
        package_rows = csv.reader(packageCSV, delimiter=',')
        next(package_rows)  # skip header
        for package_csv in package_rows:
            package_id = int(package_csv[0])
            address = package_csv[1]
            city = package_csv[2]
            state = package_csv[3]
            zip_code = package_csv[4]
            delivery_deadline = package_csv[5]
            weight = package_csv[6]
            special_notes = package_csv[7]

            #create package object
            all_packages = package.Package(package_id, address, city, state, zip_code, delivery_deadline, weight, special_notes=special_notes)
            # print(all_packages)

            #insert into hash table

            hash_table.insert(package_id, all_packages)


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
    with open("WGUPS Address Table-cleaned.csv", encoding='utf-8-sig') as address_CSV_file:
        csv_reader = csv.reader(address_CSV_file, delimiter=',')
        for row in csv_reader:
            address_data.extend(row)  #using extend to only have a one-dimensional list


load_address_data()


# validate address data
# print(address_data)

#returns x,y distance value from distance table
def distance_between(address1, address2):
    address1 = address_data.index(address1)
    address2 = address_data.index(address2)
    return distance_data[address1][address2]


#validate distance between function
# print(distance_between("4001 South 700 East","177 W Price Ave"))


truck1 = truck.Truck(1)
truck2 = truck.Truck(2)
truck3 = truck.Truck(3)

# TO DO: More work to do here, see if this logic is feasible to continue.
#try to sort packages by deadlines, notes and priority first then load them into the trucks create seperate lists????
# package_set_truck_one = set()
# package_set_truck_two = set()
# package_set_truck_three = set()
# package_set_truck_anywhere = set()
#
# for package in range(1, 41):
#     package_object = hash_table.search(package)
#     if "Delayed" in package_object.special_notes:
#         package_set_truck_three.add(package_object)
#     elif package_object.delivery_deadline == "9:00 AM":
#         package_set_truck_two.add(package_object)
#     elif package_object.delivery_deadline == "10:30 AM":
#         package_set_truck_two.add(package_object)
#     elif "truck 2" in package_object.special_notes:
#         package_set_truck_two.add(package_object)
#     else:
#         package_set_truck_anywhere.add(package_object)
#
#
# print("Truck 1: ")
# for package in package_set_truck_one:
#     truck1.load_package(package)
#     print(package)
#
# print("\nTruck 2: ")
# for package in package_set_truck_two:
#     truck2.load_package(package)
#     print(package)
#
# print("\nTruck 3: ")
# for package in package_set_truck_three:
#     truck3.load_package(package)
#     print(package)
#
# print("\nTruck needed: ")
# for package in package_set_truck_anywhere:
#     print(package)

# Manually loading packages in trucks

def load_all_trucks():
    # Loading truck 3 with certain special notes packages
    truck3.load_package(hash_table.search(21))  # package has wrong address
    truck3.load_package(hash_table.search(28))  # some don't arrive until 9:05am
    truck3.load_package(hash_table.search(7))  # the rest don't fit with the rest of the trucks
    truck3.load_package(hash_table.search(33))
    truck3.load_package(hash_table.search(9))

    truck3.load_package(hash_table.search(6))
    truck3.load_package(hash_table.search(32))
    truck3.load_package(hash_table.search(25))
    truck3.load_package(hash_table.search(26))

    # truck3.load_package(hash_table.search("2"))
    # truck3.load_package(hash_table.search("4"))

    # Loading truck 2
    truck2.load_package(hash_table.search(3))  # packages must be on truck 2 or delivered together

    truck2.load_package(hash_table.search(5))
    truck2.load_package(hash_table.search(38))
    truck2.load_package(hash_table.search(24))
    truck2.load_package(hash_table.search(22))

    truck2.load_package(hash_table.search(36))
    truck2.load_package(hash_table.search(12))
    truck2.load_package(hash_table.search(17))
    truck2.load_package(hash_table.search(11))

    truck2.load_package(hash_table.search(23))
    truck2.load_package(hash_table.search(27))
    truck2.load_package(hash_table.search(35))
    truck2.load_package(hash_table.search(18))

    truck2.load_package(hash_table.search(10))

    # Loading truck 1
    truck1.load_package(hash_table.search(1))
    truck1.load_package(hash_table.search(40))
    truck1.load_package(hash_table.search(4))
    truck1.load_package(hash_table.search(19))

    truck1.load_package(hash_table.search(20))
    truck1.load_package(hash_table.search(29))
    truck1.load_package(hash_table.search(30))
    truck1.load_package(hash_table.search(8))

    truck1.load_package(hash_table.search(37))
    truck1.load_package(hash_table.search(31))
    truck1.load_package(hash_table.search(39))
    truck1.load_package(hash_table.search(13))

    truck1.load_package(hash_table.search(14))
    truck1.load_package(hash_table.search(15))
    truck1.load_package(hash_table.search(16))
    truck1.load_package(hash_table.search(34))

#
load_all_trucks()


#Validate the packages for a given truck
# for current_package in truck1.packages:
#     print(current_package)

#The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
# WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the
# correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.


#Flush this part out afterward when packages are sorted slightly better

#Sort packages once loaded inside truck
def nearest_neighbor(truck_packages):
    for truck_package in truck_packages:
        return distance_between(truck_packages.packages[truck_package.address])

def deliver_packages(truck):
    route_mileage = 0
    time = datetime.timedelta(hours=8, minutes=0, seconds=0)
    print(time)
    for current_package in truck.packages:
        current_package.set_status("en route")
        route_mileage += distance_between(truck.current_address, current_package.address)
        package_time = distance_between(truck.current_address, current_package.address) / truck.speed
        time_to_add = datetime.timedelta(hours=package_time)
        time += time_to_add
        current_package.delivery_time = time
        truck.current_address = current_package.address
        current_package.set_status("delivered")
        print(time)

        # if current_package.delivery_deadline == "9:00 AM":
        #     route_mileage += distance_between(truck.current_address, current_package.address)
        #     package_time = distance_between(truck.current_address, current_package.address) / truck.speed
        #     time_to_add = datetime.timedelta(hours=package_time)
        #     time += time_to_add
        #     current_package.delivery_time = time
        #     truck.current_address = current_package.address
        #     current_package.set_status("delivered")
        #     print(time)
        #
        # elif current_package.delivery_deadline == "10:30 AM":
        #     route_mileage += distance_between(truck.current_address, current_package.address)
        #     package_time = distance_between(truck.current_address, current_package.address) / truck.speed
        #     time_to_add = datetime.timedelta(hours=package_time)
        #     time += time_to_add
        #     current_package.delivery_time = time
        #     truck.current_address = current_package.address
        #     current_package.set_status("delivered")
        #
        # elif current_package.delivery_deadline == "EOD":
        #     route_mileage += distance_between(truck.current_address, current_package.address)
        #     package_time = distance_between(truck.current_address, current_package.address) / truck.speed
        #     time_to_add = datetime.timedelta(hours=package_time)
        #     time += time_to_add
        #     current_package.delivery_time = time
        #     truck.current_address = current_package.address
        #     current_package.set_status("delivered")

    return route_mileage


print(deliver_packages(truck1))
print(deliver_packages(truck2))
print(deliver_packages(truck3))


# for current_package in truck2.packages:
#     print(distance_between(current_package.address,truck2.current_address))
#
# for current_package in truck3.packages:
#     current_package.set_status("en route")
#     print(current_package)
#
# for current_package in truck2.packages:
#     current_package.set_status("en route")
#     print(current_package)
#
# for current_package in truck1.packages:
#     current_package.set_status("en route")
#     print(current_package)

# hours = distance / speed

# for i in range(len(hash_table.table) + 1):
#     print("Package: {}".format(hash_table.table[i - 1]))
#
# print(hash_table)
