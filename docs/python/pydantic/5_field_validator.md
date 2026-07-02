#### Field Validator

```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()



def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")




patient_data = {"name": "bappy", "email": "bappy@hdfc.com", 
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/", 
                "age": "25", "weight": 70.5, 
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890"}}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)
```
