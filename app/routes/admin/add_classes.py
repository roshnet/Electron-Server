import pandas as pd

from app import app
from app.database import db
from app.database import engine
from app.database.models.classes import Classes
from fastapi import Response, UploadFile, File
from pydantic import BaseModel, validator


@app.post("/admin/add_classes")
async def add_classes(file: bytes = File(...)):
    try:
        data = pd.read_excel(file, index_col=None)
        classes = data.values.tolist()

        for classDetail in classes:
            classInstance = Classes()
            classInstance.name = classDetail[0]
            classInstance.year = classDetail[1]
            classInstance.department_name = classDetail[2]

            try:
                db.add(classInstance)
                db.commit()
            except Exception as e:
                print(e)
                pass

        return {"result": "Pass"}
    except Exception as e:
        print(e)
        return {"result": e}
