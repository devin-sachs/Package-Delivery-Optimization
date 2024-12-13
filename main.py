import csv
import hash
import package

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
#print(distance_between("4001 South 700 East","177 W Price Ave"))
