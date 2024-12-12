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

for i in range(len(hash_table.table) + 1):
    print("Package: {}".format(hash_table.table[i - 1]))

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

