class Veterinarian:
    def __init__(self, vet_id, name, pet_id, pet_name, pet_type, birth_year, weight):
        self.vet_id = vet_id
        self.name = name
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.birth_year = birth_year
        self.weight = weight
        self.next_pet = None

class VeterinarianLinkedList:
    def __init__(self):
        self.head = None

    def add_pet_record(self, vet_id, name, pet_id, pet_name, pet_type, birth_year, weight):
        new_pet_record = Veterinarian(vet_id, name, pet_id, pet_name, pet_type, birth_year, weight)
        
        if not self.head or pet_id < self.head.pet_id:
            new_pet_record.next_pet = self.head
            self.head = new_pet_record
        else:
            current_pet = self.head
            while current_pet.next_pet and current_pet.next_pet.pet_id < pet_id:
                current_pet = current_pet.next_pet
            new_pet_record.next_pet = current_pet.next_pet
            current_pet.next_pet = new_pet_record

    def remove_pet_record(self, pet_id):
        if not self.head:
            print("List is empty.")
            return

        if self.head.pet_id == pet_id:
            self.head = self.head.next_pet
            return

        current_pet = self.head
        while current_pet.next_pet and current_pet.next_pet.pet_id != pet_id:
            current_pet = current_pet.next_pet

        if current_pet.next_pet and current_pet.next_pet.pet_id == pet_id:
            current_pet.next_pet = current_pet.next_pet.next_pet
        else:
            print("Pet not found.")

    def print_all_pet_records(self):
        current_pet = self.head
        while current_pet:
            print(f"Vet ID: {current_pet.vet_id}, Vet Name: {current_pet.name}, "
                  f"Pet ID: {current_pet.pet_id}, Pet Name: {current_pet.pet_name}, "
                  f"Pet Type: {current_pet.pet_type}, Birth Year: {current_pet.birth_year}, "
                  f"Weight: {current_pet.weight}")
            current_pet = current_pet.next_pet


def main_menu():
    vet_list = VeterinarianLinkedList()

    while True:
        print("\nMain Menu:")
        print("1. Add a new pet record")
        print("2. Remove a pet")
        print("3. Print all pet records")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            vet_id = int(input("Enter Vet ID: "))
            name = input("Enter Vet Name: ")
            pet_id = int(input("Enter Pet ID: "))

            
            pet_name = input("Enter Pet Name: ")
            pet_type = input("Enter Pet Type: ")
            birth_year = int(input("Enter Birth Year: "))
            weight = float(input("Enter Weight: "))
            
            vet_list.add_pet_record(vet_id, name, pet_id, pet_name, pet_type, birth_year, weight)

        elif choice == "2":
            pet_id = int(input("Enter the ID of the pet to remove: "))
            vet_list.remove_pet_record(pet_id)

        elif choice == "3":
            vet_list.print_all_pet_records()

        elif choice == "4":
            print("Program is closing..")
            break

        else:
            print(" Try again.. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()

