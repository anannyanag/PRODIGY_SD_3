import csv
import os

def create_csv():
    fields = ["Name", "Phone", "Email"]
    if not os.path.exists("employees.csv"):
        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fields)

def add_record():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email ID: ")

    with open("employees.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Record added successfully!")

def view_records():
    with open("employees.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

def edit_record():
    name_to_edit = input("Enter the name of the record you want to edit: ")
    updated_records = []
    with open("employees.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name_to_edit:
                row[1] = input(f"Enter new phone number for {row[0]}: ")
                row[2] = input(f"Enter new email ID for {row[0]}: ")
            updated_records.append(row)

    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_records)
    print("Record updated successfully!")

def delete_record():
    name_to_delete = input("Enter the name of the record you want to delete: ")
    records_to_keep = []
    with open("employees.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name_to_delete:
                records_to_keep.append(row)

    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(records_to_keep)
    print("Record deleted successfully!")

def main():
    create_csv()

    while True:
        print("\nEmployee Records Menu:")
        print("1. Add Record")
        print("2. View Records")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            edit_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
