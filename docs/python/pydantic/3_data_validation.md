#### Data Validation

```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class PatientData(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=100)
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_info: Dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")




patient_data = {"name": "Bappy", "email": "bappy@gmail.com",
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/",
                "age": "25", "weight": "70.5",
                "allergies": ["peanuts", "shellfish"],
                "contact_info": {"phone": "123-456-7890"}}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)
```
