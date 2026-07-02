#### Nested Models

```python

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class PatientData(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Kishor', 'gender': 'male', 'age': 40, 'address': address1}

patient1 = PatientData(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.city)
```
