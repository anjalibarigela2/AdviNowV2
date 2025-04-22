from fastapi import APIRouter, UploadFile, File, Depends, Query
from sqlalchemy.orm import Session
import csv
from io import StringIO

from app.models import Business, Symptom, BusinessSymptom
from app.database import get_db

router = APIRouter()


# ✅ Existing health check endpoint
@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}
    except Exception as e:
        return {'Error: ' + str(e)}


# ✅ Existing import CSV endpoint
@router.post("/import-csv/")
async def import_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        content = await file.read()
        csv_data = StringIO(content.decode("utf-8"))
        reader = csv.DictReader(csv_data)

        for row in reader:
            business = db.query(Business).filter_by(name=row["Business Name"]).first()
            if not business:
                business = Business(name=row["Business Name"])
                db.add(business)
                db.commit()
                db.refresh(business)

            symptom = db.query(Symptom).filter_by(code=row["Symptom Code"]).first()
            if not symptom:
                symptom = Symptom(
                    code=row["Symptom Code"],
                    name=row["Symptom Name"]
                )
                db.add(symptom)
                db.commit()
                db.refresh(symptom)

            existing_relation = db.query(BusinessSymptom).filter_by(
                business_id=business.id,
                symptom_id=symptom.id
            ).first()

            if not existing_relation:
                relation = BusinessSymptom(
                    business_id=business.id,
                    symptom_id=symptom.id,
                    diagnostic=row["Symptom Diagnostic"]
                )
                db.add(relation)

        db.commit()
        return {"message": "CSV data imported successfully!"}
    except Exception as e:
        return {"error": str(e)}


# ✅ 🔥 NEW: Symptom Data Query API
@router.get("/symptoms/")
def get_symptom_data(
    business_id: int = Query(None),
    diagnostic: str = Query(None),
    db: Session = Depends(get_db)
):
    try:
        query = db.query(
            Business.id.label("business_id"),
            Business.name.label("business_name"),
            Symptom.code.label("symptom_code"),
            Symptom.name.label("symptom_name"),
            BusinessSymptom.diagnostic.label("diagnostic")
        ).join(BusinessSymptom, Business.id == BusinessSymptom.business_id
        ).join(Symptom, Symptom.id == BusinessSymptom.symptom_id)

        if business_id:
            query = query.filter(Business.id == business_id)
        if diagnostic:
            query = query.filter(BusinessSymptom.diagnostic.ilike(f"%{diagnostic}%"))

        results = query.all()

        data = [
            {
                "business_id": r.business_id,
                "business_name": r.business_name,
                "symptom_code": r.symptom_code,
                "symptom_name": r.symptom_name,
                "diagnostic": r.diagnostic,
            }
            for r in results
        ]

        return data
    except Exception as e:
        return {"error": str(e)}

"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/status')
async def get_status():
    try:
        return {"Health OK"}

    except Exception as e:
        return {'Error: ' + str(e)}
"""
