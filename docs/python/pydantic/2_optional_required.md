#### Optional 

```python

from pydantic import BaseModel
from typing import List, Dict, Optional

class PatientData(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")




patient_data = {"name": "Bappy", "age": "25", "weight": "70.5", "contact_info": {"email": "bappy@example.com", "phone": "123-456-7890"}}

patient_1 = PatientData(**patient_data)


add_patient_data(patient_1)
```
 
