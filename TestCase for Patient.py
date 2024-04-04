from PatientSystem import PatientSystem
from PatientSystem import Patient
from PatientSystem import Doctor
from PatientSystem import Prescription
from PatientSystem import Specialization
hospital = PatientSystem()

def test_add_patient():
    print("Test Case 1: Adding a New Patient")
    patientID = "Patient12"  # Corrected to use for both adding and checking
    hospital.addPatient(patientID, "Ahmad", "Alzaabi", "No significant medical history", "Cold", 30, "2024-01-01", "ahmad.alzaabi@example.com", "555-0123", "123 Main St", "Sara Alzaabi")
    if patientID in hospital._patients:
        print(f"Passed: {patientID} (Ahmad Alzaabi) successfully added.")
    else:
        print(f"Failed: {patientID} (Ahmad Alzaabi) was not added.")

test_add_patient()


def test_update_patient():
    #In this test, we will be updating an existing patient's record
    print("Test Case 2: Updating a Patient Record")
    hospital.updatePatient("Patient12", "Updated medical history", "Improved Condition", 31)
    if hospital._patients["Patient12"]._familyHistory == "Updated medical history":
        print("Passed: Patient12 (Ahmad Alzaabi) record successfully updated.\n")
    else:
        print("Failed: Patient12 (Ahmad Alzaabi) record was not updated.\n")

test_update_patient()

def test_issue_prescription():
    #This test case we will be issuing a prescription to a patient
    print("Test Case 3: Issuing and Retrieving a Prescription")
    hospital.issuePrescription("Patient12", "RX100", "Ibuprofen", "200mg", "Every 8 hours", "Pharmacy A", "10 days")
    if hospital._patients["Patient12"]._prescription[0]._prescriptionNum == "RX100":
        print("Passed: Prescription RX100 successfully issued to Patient P001 (Ahmad Alzaabi).\n")
    else:
        print("Failed: Prescription RX100 was not issued to Patient P001 (Ahmad Alkhalidi).\n")

test_issue_prescription()

def test_sort_by_condition():
    #If we assume getSortedPatients function exists and sorts by condition
    print("Test Case 4: Sorting Patient Records by Condition")
    #Then we add another patient with a different condition for sorting
    hospital.addPatient("P002", "Mariam", "Alshamsi", "Asthma", "Asthma", 28)
    sortedPatients = hospital.getSortedPatients(sortBy="condition")
    if sortedPatients[0]._condition <= sortedPatients[1]._condition:
        print("Patients successfully sorted by condition.\n")
    else:
        print("Patients were not sorted by condition.\n")

test_sort_by_condition()

def test_remove_patient():
    #In this test we will be removing an existing patient
    print("Test Case 5: Removing a Patient")
    #Then we will ensure there is a patient to remove
    hospital.addPatient("P003", "Laila", "Aldhaheri", "No significant medical history", "Flu", 29)
    hospital.removePatient("P003")
    #Then we attempt to remove the same patient again to test handling non-existent patient
    try:
        hospital.removePatient("P003")
        print("Patient P003 (Laila Aldhaheri) was successfully removed and system handled non-existent patient gracefully.\n")
    except Exception as e:
        print(f"An error occurred - {e}\n")

test_remove_patient()

def test_dequeue_consultation():
    #In this test dequeuing a patient from the consultation queue
    print("Test Case 6: Dequeuing a Patient from Consultation")
    #Then we add two patients and enqueue them for consultation
    hospital.addPatient("P004", "Sami", "Ahmed", "No significant medical history", "Headache", 33)
    hospital.addPatient("P005", "Noura", "Alfalasi", "No significant medical history", "Back Pain", 27)
    hospital.createEnqueueConsultation("P004")
    hospital.createEnqueueConsultation("P005")
    #After that we use Dequeue for the first patient and check if it was P004
    hospital.createDequeueConsultation()
    if "P004" not in hospital.consultationQueue:
        print("Patient P004 (Sami Ahmed) was successfully dequeued from the consultation queue.\n")
    else:
        print("Patient P004 (Sami Ahmed) was not dequeued from the consultation queue.\n")

test_dequeue_consultation()

#First, we initialize and test operations
#Then, we ssume Specialization, Doctor, and Patient classes are defined correctly as well
hospital._doctors[1] = Doctor("1", "Dr. Ahmad", Specialization.GENERALDOCTOR)
hospital._doctors[2] = Doctor("2", "Dr. Sarah", Specialization.PEDIATRICS)

#This function will be used for Adding patients
hospital.addPatient("100", "Mohammad", "Al-Ali", "No significant medical history", "Cough and cold", 30)
hospital.addPatient("101", "Fatima", "Alzaabi", "Asthma", "Shortness of breath", 28)

#This function will be used for Updating a patient record
hospital.updatePatient("100", None, "Improved after medication")

#This function will be used for Correcting the enqueue and dequeue method calls
hospital.createEnqueueConsultation("100")
hospital.createEnqueueConsultation("101")

#This function will be used for Dequeue a patient after consultation
hospital.createDequeueConsultation()

#This function will be used for Issue a prescription
hospital.issuePrescription("100", "RX100", "Amoxicillin", "500mg", "Three times a day for 7 days", "Happy Pharmacy", "5", "Dr Ahmed")

#This function will be used for Search for a patient
hospital.searchPatient("100")