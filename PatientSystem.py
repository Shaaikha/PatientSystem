from collections import deque
from datetime import datetime


#Creating a class with protected attributes to better manage the data of the patients and ensure privacy
class Patient:
  """ Creating Class for patient to store important data for the patient information"""
  def __init__(self, patientId="", firstName="", lastName="", familyHistory="", condition="", age= 0, admissionDate="", emailAddress="", phoneNumber="", address="", emergencyContact=""):
        self._patientId = patientId
        self._firstName = firstName
        self._lastName= lastName
        self._familyHistory = familyHistory
        self._condition = condition
        self._age= age
        self._appointment = []  # Creating a list to store the data of the appointments including the date of the appointement
        self._prescription = []  # Adding a stack for LIFO, better usage when it comes to retrival of the prescriptions
        self.admissionDate = admissionDate
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.address = address
        self.emergencyContact = emergencyContact

from enum import Enum
#adding import enum library to store options for the specialization of the doctor
class Specialization(Enum):
  EAR= "Ear Doctor"
  EYE= "Eye Doctor"
  NERVES= "Nerves Doctor"
  GENERALDOCTOR= "GENERAL DOCTOR"
  PEDIATRICS= "PEDIATRICS"

#Creating a class with protected attributes to better manage the data of the doctor and ensure privacy
class Doctor:
   """ Creating Class for Doctor to store important data for the doctor's data"""
   def __init__(self, doctorId="", name="", specialization= Specialization.EYE, phoneNumber="", emailAddress="", yearsOfExperience=0, clinicAddress="", consultationFee=0, workingHours=""):
        self._doctorId = doctorId
        self._name = name
        self._specialization = specialization
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.yearsOfExperience = yearsOfExperience
        self.clinicAddress = clinicAddress
        self.consultationFee = consultationFee
        self.workingHours = workingHours


#Creating a class with protected attributes to better manage the data of the prescriptions
class Prescription:
  """ Creating Class for Prescription to store important data for the patient's prescription data"""
  def __init__(self, prescriptionNum="", medicationType= "", dosage="", instructions="", pharmacy= "", daysUsed="", prescribedBy="", prescriptionDate="", refillInformation="", sideEffects=""):
        self._prescriptionNum = prescriptionNum
        self._medicationType = medicationType
        self._dosage = dosage
        self._instructions = instructions
        self._pharmacy= pharmacy
        self._daysUsed= daysUsed
        self.prescribedBy = prescribedBy
        self.prescriptionDate = prescriptionDate
        self.refillInformation = refillInformation
        self.sideEffects = sideEffects

# Assuming Patient, Doctor, Prescription, and Specialization classes are defined as previously described

class PatientSystem:
    """Creating Class for PatientSystem to store and manage patient and doctor data"""
    def __init__(self):
        self._patients = {}  # Dictionary to store patient data
        self._doctors = {}  # Dictionary to store doctor data
        self.consultationQueue = deque()  # Queue for managing patient consultations

    def addPatient(self, patientId, firstName, lastName, familyHistory, condition, age, admissionDate="", emailAddress="", phoneNumber="", address="", emergencyContact=""):
        #Add a new patient to the system"""
        if patientId not in self._patients:
            newPatient = Patient(patientId, firstName, lastName, familyHistory, condition, age, admissionDate, emailAddress, phoneNumber, address, emergencyContact)
            self._patients[patientId] = newPatient
            print(f"A new patient named: {firstName} {lastName} has been added to the hospital's records.")
        else:
            print(f"The patient with Patient ID {patientId} is already registered.")

    def updatePatient(self, patientId, familyHistory=None, condition=None, age=None, emailAddress=None, phoneNumber=None, address=None, emergencyContact=None):
        #Update an existing patient's record
        if patientId in self._patients:
            patient = self._patients[patientId]
            if familyHistory is not None:
                patient._familyHistory = familyHistory
            if condition is not None:
                patient._condition = condition
            if age is not None:
                patient._age = age
            if emailAddress is not None:
                patient.emailAddress = emailAddress
            if phoneNumber is not None:
                patient.phoneNumber = phoneNumber
            if address is not None:
                patient.address = address
            if emergencyContact is not None:
                patient.emergencyContact = emergencyContact
            print(f"Patient ID {patientId}'s record updated.")
        else:
            print(f"Patient ID {patientId} not found.")

    def removePatient(self, patientId):
        #Remove a patient from the system
        if patientId in self._patients:
            del self._patients[patientId]
            print(f"Patient ID {patientId} removed from the system.")
        else:
            print(f"Patient ID {patientId} not found.")

    def createEnqueueConsultation(self, patientId):
        #Enqueue a patient for a consultation
        if patientId in self._patients and patientId not in self.consultationQueue:
            self.consultationQueue.append(patientId)
            print(f"Patient ID {patientId} added to the consultation queue.")
        else:
            print(f"Patient ID {patientId} not found or already in queue.")

    def createDequeueConsultation(self):
        #Dequeue a patient after consultation
        if self.consultationQueue:
            patientId = self.consultationQueue.popleft()
            print(f"Patient ID {patientId} has been consulted and removed from the queue.")
        else:
            print("Consultation queue is empty.")

    def issuePrescription(self, patientId, prescriptionNum, medicationType, dosage, instructions, pharmacy, daysUsed, prescribedBy="", prescriptionDate="", refillInformation="", sideEffects=""):
        #Issue a prescription to a patient"""
        if patientId in self._patients:
            newPrescription = Prescription(prescriptionNum, medicationType, dosage, instructions, pharmacy, daysUsed, prescribedBy, prescriptionDate, refillInformation, sideEffects)
            self._patients[patientId]._prescription.append(newPrescription)
            print(f"Prescription {prescriptionNum} issued to Patient ID {patientId}.")
        else:
            print(f"Patient ID {patientId} not found.")

    def searchPatient(self, patientId):
        #Search for a patient by ID and display their details"""
        if patientId in self._patients:
            patient = self._patients[patientId]
            print(f"Patient ID: {patient._patientId}, Name: {patient._firstName} {patient._lastName}")
            print(f"Medical History: {patient._familyHistory}, Current Condition: {patient._condition}, Age: {patient._age}, Admission Date: {patient.admissionDate}")
            print("Prescriptions:")
            for prescription in patient._prescription:
                print(f"- {prescription._medicationType}: {prescription._dosage} ({prescription._instructions}), Pharmacy: {prescription._pharmacy}, Days Used: {prescription._daysUsed}, Prescribed By: {prescription.prescribedBy}")
        else:
            print(f"Patient ID {patientId} not found.")

    def getSortedPatients(self, sortBy="condition"):
        patientList = list(self._patients.values())
        sortedPatients = patientList  # Default assignment, in case sortBy doesn't match any condition

        if sortBy == "condition":
            sortedPatients = sorted(patientList, key=lambda x: (x._condition, x.admissionDate))
        elif sortBy == "admissionDate":
            sortedPatients = sorted(patientList,
                                    key=lambda x: datetime.strptime(x.admissionDate, '%Y-%m-%d') if isinstance(
                                        x.admissionDate, str) else x.admissionDate)
        else:
            print(f"Warning: sortBy parameter '{sortBy}' not recognized. Returning unsorted list.")

        return sortedPatients