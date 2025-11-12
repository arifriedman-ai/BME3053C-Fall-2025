class PatientRecords:
    """
    A class to manage patient records, including methods for adding, updating, and retrieving records.
    It also implements data validation and basic statistical analysis methods.

    Attributes:
        records (dict): A dictionary to store patient records with patient ID as the key.
    """

    def __init__(self):
        """Initialize the PatientRecords class with an empty records dictionary."""
        self.records = {}

    def add_record(self, patient_id: str, name: str, age: int, weight: float, height: float):
        """
        Add a new patient record.

        Args:
            patient_id (str): Unique identifier for the patient.
            name (str): Name of the patient.
            age (int): Age of the patient.
            weight (float): Weight of the patient in kilograms.
            height (float): Height of the patient in meters.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        self.validate_patient_data(patient_id, name, age, weight, height)
        self.records[patient_id] = {
            'name': name,
            'age': age,
            'weight': weight,
            'height': height
        }

    def update_record(self, patient_id: str, name: str = None, age: int = None, weight: float = None, height: float = None):
        """
        Update an existing patient record.

        Args:
            patient_id (str): Unique identifier for the patient.
            name (str, optional): New name of the patient.
            age (int, optional): New age of the patient.
            weight (float, optional): New weight of the patient in kilograms.
            height (float, optional): New height of the patient in meters.

        Raises:
            ValueError: If the patient ID does not exist or if any of the input values are invalid.
        """
        if patient_id not in self.records:
            raise ValueError("Patient ID does not exist.")
        
        if name is not None:
            self.records[patient_id]['name'] = name
        if age is not None:
            self.records[patient_id]['age'] = age
        if weight is not None:
            self.records[patient_id]['weight'] = weight
        if height is not None:
            self.records[patient_id]['height'] = height

    def get_record(self, patient_id: str):
        """
        Retrieve a patient record by patient ID.

        Args:
            patient_id (str): Unique identifier for the patient.

        Returns:
            dict: The patient's record.

        Raises:
            ValueError: If the patient ID does not exist.
        """
        if patient_id not in self.records:
            raise ValueError("Patient ID does not exist.")
        return self.records[patient_id]

    def validate_patient_data(self, patient_id: str, name: str, age: int, weight: float, height: float):
        """
        Validate patient data before adding or updating records.

        Args:
            patient_id (str): Unique identifier for the patient.
            name (str): Name of the patient.
            age (int): Age of the patient.
            weight (float): Weight of the patient in kilograms.
            height (float): Height of the patient in meters.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        if not isinstance(patient_id, str) or not patient_id:
            raise ValueError("Patient ID must be a non-empty string.")
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")

    def calculate_average_age(self):
        """
        Calculate the average age of all patients.

        Returns:
            float: The average age of patients, or None if there are no records.
        """
        if not self.records:
            return None
        total_age = sum(record['age'] for record in self.records.values())
        return total_age / len(self.records)

    def calculate_average_bmi(self):
        """
        Calculate the average Body Mass Index (BMI) of all patients.

        Returns:
            float: The average BMI of patients, or None if there are no records.
        """
        if not self.records:
            return None
        total_bmi = sum(record['weight'] / (record['height'] ** 2) for record in self.records.values())
        return total_bmi / len(self.records)