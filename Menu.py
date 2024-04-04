from PatientSystem import PatientSystem
from PatientSystem import Patient
from PatientSystem import Doctor
from PatientSystem import Prescription
from PatientSystem import Specialization
def main_menu():
    while True:
        # Display the main menu options to the user
        print("\n--- WELCOME TO ABC HOSPITAL - PATIENTS ARE OUR MAIN PRIORITY ---")
        print("\n--- Hospital Patient Record Management System ---")
        print("1. Add a New Patient")
        print("2. Update Patient Record")
        print("3. Remove a Patient")
        print("4. Enqueue Patient for Consultation")
        print("5. Dequeue Patient after Consultation")
        print("6. Issue a Prescription")
        print("7. Search for a Patient")
        print("8. Exit")
        choice = input("Enter your choice: ")

        # Process user input and call the corresponding function
        if choice == "1":
            addPatient()
        elif choice == "2":
            updatePatient()
        elif choice == "3":
            removePatient()
        elif choice == "4":
            enqueue_patient()
        elif choice == "5":
            dequeue_patient()
        elif choice == "6":
            issue_prescription()
        elif choice == "7":
            search_patient()
        elif choice == "8":
            # Exit the program
            print("Thank you for using the system, Stay Safe <3")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1-8.")

def addPatient():
    # Collects new patient data from the user and adds the patient to the system
    patientId = input("Enter patient ID: ")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    familyHistory = input("Enter medical history: ")
    condition = input("Enter current condition: ")
    age = input("Enter age: ")
    hospital.addPatient(patientId, firstName, lastName, familyHistory, condition, int(age))
    print("Patient added successfully.")

def updatePatient():
    # Collects patient ID and updates the specified patient's record with new information
    patientId = input("Enter patient ID to update: ")
    familyHistory = input("Update medical history (leave blank to skip): ")
    condition = input("Update current condition (leave blank to skip): ")
    age = input("Update age (leave blank to skip): ")
    age = int(age) if age else None
    hospital.updatePatient(patientId, familyHistory if familyHistory else None, condition if condition else None, age)

def removePatient():
    # Removes a patient from the system based on the provided patient ID
    patientId = input("Enter patient ID to remove: ")
    hospital.removePatient(patientId)

def enqueue_patient():
    # Enqueues a patient for a consultation based on the provided patient ID
    patientId = input("Enter patient ID to enqueue for consultation: ")
    hospital.createEnqueueConsultation(patientId)

def dequeue_patient():
    # Dequeues the next patient from the consultation queue
    hospital.createDequeueConsultation()

def issue_prescription():
    # Issues a new prescription to a patient based on the provided details
    patientId = input("Enter patient ID to issue prescription: ")
    prescriptionNum = input("Enter prescription number: ")
    medicationType = input("Enter medication type: ")
    dosage = input("Enter dosage: ")
    instructions = input("Enter instructions: ")
    pharmacy = input("Enter pharmacy: ")
    daysUsed = input("Enter days used: ")
    prescribedBy = input("Enter prescribed by: ")
    prescriptionDate = input("Enter prescription date: ")
    refillInformation = input("Enter refill information: ")
    sideEffects = input("Enter side effects: ")
    hospital.issuePrescription(patientId, prescriptionNum, medicationType, dosage, instructions, pharmacy, daysUsed, prescribedBy, prescriptionDate, refillInformation, sideEffects)
    print("Prescription issued successfully.")

def search_patient():
    # Searches for a patient by ID and displays their details
    patientId = input("Enter patient ID to search: ")
    hospital.searchPatient(patientId)

if __name__ == "__main__":
    # Creates an instance of the PatientSystem and starts the main menu
    hospital = PatientSystem()  # Ensure you have an instance of your system
    main_menu()