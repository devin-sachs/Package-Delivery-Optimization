import csv
import hash
import package

hash_table = hash.ChainingHashTable()


def loadPackageData():
    with open("WGUPS Package File-cleanup.csv") as packageCSV:
        packageRows = csv.reader(packageCSV, delimiter=',')
        next(packageRows)  # skip header
        for package_csv in packageRows:
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
            print(all_packages)

loadPackageData()

