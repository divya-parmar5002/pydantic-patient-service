from pydantic import BaseModel,EmailStr,Field,field_validator,model_validator,computed_field
from typing import Dict,List,Annotated,Optional
from models.address import Address

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patient",description="Give the name of the patient that must be less than 50 character",examples=["Divya","Gungun"])]
    age:int=Field(gt=0,lt=100)
    contact_details:Dict[str,str]
    email:EmailStr
    address:Address
    gender:str="Other"
    weight:float
    height:float
    married:Annotated[bool,Field(default=None,description='Is patient married or not',examples=['True','False'])]
    allergies_details:Optional[List[str]]=None

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
      valid_domain=['gmail.com']
      domain_name=value.split('@')[-1]
      if domain_name not in valid_domain:
        raise ValueError('Not a valid domain')
      return value

    @model_validator(mode='after')
    def emergency_contact_validator(cls,model):
      if model.age>60 and 'emergency' not in model.contact_details:
        raise ValueError('Patient older than 60 must have an emergency contact')
      return model

    @computed_field
    @property
    def calculate_bmi(self)->float:
      bmi=round(self.weight/(self.height**2),2)
      return bmi

