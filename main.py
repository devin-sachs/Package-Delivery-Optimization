#Devin Sachs
#Student ID: 011292435
#C950 Performance Assesment - Data Structures & Algorithms II

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


def load_address_data():
    with open("WGUPS Address Table-cleaned.csv", encoding='utf-8-sig') as address_CSV_file:
        csv_reader = csv.reader(address_CSV_file, delimiter=',')
        for row in csv_reader:
            address_data.extend(row)  #using extend to only have a one-dimensional list


#returns x,y distance value from distance table
def distance_between(address1, address2):
    address1 = address_data.index(address1)
    address2 = address_data.index(address2)
    return distance_data[address1][address2]


#validate distance between function
#Print(distance_between("4001 South 700 East","177 W Price Ave"))
def print_packages(truck):
    for current_package in truck.packages:
        print(current_package)


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
    truck3.load_package(hash_table.search(2))

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

# This function sorts packages once loaded inside truck
def nearest_neighbor(truck):
    current_package = truck.packages[0]
    visited = [False] * len(truck.packages)
    visited[0] = True

    sorted_order = [current_package]

    for package in range(1,len(truck.packages)):
        nearest_package = None
        nearest_distance = float('inf')
        nearest_index = -1

        for next_package in range(len(truck.packages)):
            if not visited[next_package]:
                distance = distance_between(current_package.address, truck.packages[next_package].address)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_package = truck.packages[next_package]
                    nearest_index = next_package

        visited[nearest_index] = True
        sorted_order.append(nearest_package)
        current_package = nearest_package

    truck.packages = sorted_order

#Modifies truck package order based on delivery deadlines
def prioritize_delivery_time(truck):
    def parse_time(deadline):
        if deadline == 'inf':
            return (1,float('inf'))
        try:
            return (0,datetime.datetime.strptime(deadline, "%I:%M %p").time())
        except ValueError:
            return (1,float('inf'))
    truck.packages.sort(key=lambda package: parse_time(package.delivery_deadline))

#function delivers the packages given a truck and start time
def deliver_packages(truck, start_time):
    # print("Truck", truck.truck_id)
    # print(start_time)
    route_mileage = 0
    time = start_time
    for current_package in truck.packages:
        current_package.set_status("en route")
        route_mileage += distance_between(truck.current_address, current_package.address)
        package_time = distance_between(truck.current_address, current_package.address) / truck.speed
        time_to_add = datetime.timedelta(hours=package_time)
        time += time_to_add
        current_package.delivery_time = time
        truck.current_address = current_package.address
        current_package.set_status("delivered")
        # print(time)
    return route_mileage, time


load_package_data()

#validating hash table and that packages were inserted properly

# for i in range(len(hash_table.table) + 1):
#     print("Package: {}".format(hash_table.table[i - 1]))
#
# print(hash_table)

load_distance_data()

#validate distance data
# print(distance_data[5][2])
# print(distance_data[2][5])
# for i in range(27):
#     print(distance_data[i])


load_address_data()

# validate address data
# print(address_data)

#instantiate truck objects for truck1,2 and 3
truck1 = truck.Truck(1)
truck2 = truck.Truck(2)
truck3 = truck.Truck(3)

#load up the trucks
load_all_trucks()

#sort the trucks by nearest neigbhor "greedy" algorithm
nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)

#perform another sort, taking into account the delivery deadlines
prioritize_delivery_time(truck1)
prioritize_delivery_time(truck2)
prioritize_delivery_time(truck3)

first_leave_time = datetime.timedelta(hours=8, minutes=0, seconds=0)
second_leave_time = datetime.timedelta(hours=9, minutes=5, seconds=0)

#send truck 1 off for their route. tuple unpacking to define the mileage and return time. Repeat for other trucks
truck_1_mileage, truck1_return_time = deliver_packages(truck1,first_leave_time)

#Adding time to travel back to the hub and switch trucks
#Adding additional mileage to route
back_to_hub = distance_between(truck1.packages[len(truck1.packages) - 1].address, "4001 South 700 East") / truck1.speed
time_back_to_hub = datetime.timedelta(hours=back_to_hub)
truck1_return_time += time_back_to_hub
truck_1_mileage += back_to_hub

#Second driver heading out with a later start time to allow the late packages to be delivered on time
truck_3_mileage, truck3_return_time = deliver_packages(truck3,second_leave_time)

#Adding time to travel back to the hub
#Adding additional mileage to route
back_to_hub = distance_between(truck3.packages[len(truck3.packages) - 1].address, "4001 South 700 East") / truck3.speed
time_back_to_hub = datetime.timedelta(hours=back_to_hub)
truck3_return_time += time_back_to_hub

#First driver comes back and picks up truck 2 (final truck/trip) to deliver all the EOD packages
truck_2_mileage, truck2_return_time = deliver_packages(truck2,truck1_return_time)

#Adding time to travel back to the hub and switch trucks
#Adding additional mileage to route
back_to_hub = distance_between(truck2.packages[len(truck2.packages) - 1].address, "4001 South 700 East") / truck2.speed
time_back_to_hub = datetime.timedelta(hours=back_to_hub)
truck2_return_time += time_back_to_hub


print("truck 1: \n" , truck_1_mileage, truck1_return_time)
print("truck 2: \n" , truck_2_mileage, truck2_return_time)
print("truck 3: \n" , truck_3_mileage, truck3_return_time)

total_mileage = truck_1_mileage + truck_2_mileage + truck_3_mileage

print_packages(truck1)
print_packages(truck2)
print_packages(truck3)

print("total mileage: ", total_mileage)


# for i in range(len(hash_table.table) + 1):
#     print("Package: {}".format(hash_table.table[i - 1]))
#
# print(hash_table)
