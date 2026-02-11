import json
from database.models import SessionLocal, PatientReport


def save_report(patient_name, report_text, document, reasoning, actions, safety):
    db = SessionLocal()

    new_record = PatientReport(
        patient_name=patient_name,
        diagnosis=document.diagnosis,
        report_text=report_text,
        document_json=json.dumps(document.model_dump()),
        reasoning_json=json.dumps(reasoning.model_dump()),
        action_json=json.dumps(actions.model_dump()),
        safety_json=json.dumps(safety.model_dump()),
    )

    db.add(new_record)
    db.commit()
    db.close()


def get_patient_reports(patient_name):
    db = SessionLocal()
    reports = db.query(PatientReport).filter(
        PatientReport.patient_name == patient_name
    ).order_by(PatientReport.created_at.desc()).all()
    db.close()
    return reports
