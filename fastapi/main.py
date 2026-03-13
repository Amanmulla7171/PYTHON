from fastapi import FastAPI,HTTPException,Path,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Literal
from pathlib import Path
app=FastAPI()

import json


class Patient(BaseModel):
    patient_id:Annotated[str,Field(...,description="The ID of the patient" ,examples={"P1001"})] 
    name: Annotated[str,Field(...,description="The name of the patient" )]
    age: Annotated[float,Field(...,gt=0,lt=120,description="The BMI of the patient" )]
    diagnosis: Annotated[str,Field(...,description="The diagnosis of the patient" )]
    gender: Annotated[Literal["Male", "Female"],Field(...,description="The gender of the patient" )]
    weight: Annotated[float,Field(...,gt=0,description="The weight of the patient" )]
    height: Annotated[float,Field(...,gt=0,description="The height of the patient" )]

    @computed_field
    @property
    def bmi(self) -> float:
        if self.height > 0:
            return round(self.weight / (self.height ** 2), 2)
        return 0
    


def load_data():
   
    try:
        file_path = Path(__file__).parent / "patient.json"
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        
        return {"error": str(e)}
    
def save_data(data):
    try:
        file_path = Path(__file__).parent / "patient.json"
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

@app.get("/")
def hello():
    return {'message':'hello world'}


@app.get("/about")
def about():
    return {'message':'This is the about page'}

@app.get("/view")
def view():
        data=load_data()


        return data


@app.get("/patients/{patient_id}" )
def view_by_id(patient_id: str ):
        data=load_data()
        if "patients" in data:
            for patient in data["patients"]:
                if patient["patient_id"] == patient_id:
                    return patient
        return {"message":"patient not found"}


@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.patient_id in data:
         raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.patient_id] = patient.model_dump(exclude={'patient_id'})

    save_data(data)

    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)



@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()

    if "patients" not in data:
        raise HTTPException(status_code=404, detail="No patients found")

    for i, patient in enumerate(data["patients"]):
        if patient["patient_id"] == patient_id:
            del data["patients"][i]
            save_data(data)
            return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)

    raise HTTPException(status_code=404, detail="Patient not found")
