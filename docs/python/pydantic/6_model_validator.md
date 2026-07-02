#### Model Validator

```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")




patient_data = {"name": "bappy", "email": "bappy@hdfc.com", 
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/", 
                "age": "70", "weight": 70.5, 
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890", "emergency": "987-654-3210"}}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)
```
