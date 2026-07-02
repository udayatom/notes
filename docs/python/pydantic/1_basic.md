```python

from pydantic import BaseModel

class PatientData(BaseModel):
    name: str
    age: int
    weight: float


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Data added successfully to the database!")


def update_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Data updated successfully in the database!")

patient_data = {"name": "Bappy", "age": "25", "weight": "70.5"}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)

```
