#### Computed Fields

```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("BMI:", patient.bmi)
    print("Data added successfully to the database!")




patient_data = {"name": "bappy", "email": "bappy@hdfc.com", 
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/", 
                "age": "70", "weight": 70.5, 
                "height": 1.75,
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890", "emergency": "987-654-3210"}}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)
```
