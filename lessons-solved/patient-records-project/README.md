# Patient Records Project

## Overview
The Patient Records Project is a Python application designed to manage patient records efficiently. It provides functionalities for adding, updating, and retrieving patient information while ensuring data integrity through validation. Additionally, the project includes methods for basic statistical analysis of patient data.

## Features
- **Add Patient Records**: Easily add new patient records with necessary details.
- **Update Patient Records**: Modify existing records to keep information up-to-date.
- **Retrieve Patient Records**: Access patient information quickly and efficiently.
- **Data Validation**: Ensure that all patient data entered meets specified criteria.
- **Statistical Analysis**: Perform basic statistical operations on patient data for insights.

## Project Structure
```
patient-records-project
├── src
│   ├── patient_records.py       # Implementation of the PatientRecords class
│   └── __init__.py              # Marks the src directory as a Python package
├── notebooks
│   └── 08_Copilot_Introduction_11_12_2025.ipynb  # Jupyter notebook with exercises
├── tests
│   └── test_patient_records.py   # Unit tests for the PatientRecords class
├── .gitignore                    # Files and directories to ignore by Git
├── pyproject.toml                # Project configuration and dependencies
└── requirements.txt              # List of required Python packages
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd patient-records-project
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the `PatientRecords` class, import it from the `src` package and create an instance. You can then call its methods to manage patient records.

### Example
```python
from src.patient_records import PatientRecords

# Create an instance of PatientRecords
records = PatientRecords()

# Add a new patient record
records.add_patient(name="John Doe", age=30, condition="Healthy")

# Retrieve patient information
patient_info = records.get_patient(name="John Doe")
print(patient_info)
```

## Testing
To run the unit tests for the `PatientRecords` class, navigate to the `tests` directory and execute:
```
pytest test_patient_records.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.