from models.patient import Patient
from services.patient_services import insert_patient_data

patient_info={
    'name':'Divya',
    'age':'21',
    'contact_details':{'phone':'1234567890',
                       'emergency':'9876544563'},
    'email':'divyaparmar@gmail.com',
    'address':{
      "city":"Mumbai",
      "state":'Maharastra',
      "pin":'123456',
      "country":'India',

    },
    'gender':'Female',
    'weight':65.5,
    'height':1.75,
    'married':False
}

try:
    patient=Patient(**patient_info)
    insert_patient_data(patient)
    print("\n Dictionary Model Dump")
    print(patient.model_dump())
    print("\nJSON Dump")
    print(patient.model_dump_json())

except Exception as e:
    print(f'validation error:{e}')    

