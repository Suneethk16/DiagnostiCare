from schemas.medical_schemas import DocumentExtraction


def test_document_schema_valid():
    data = {
        "diagnosis": "Diabetes",
        "medications": ["Metformin"],
        "lab_results": ["HbA1c 8.2%"],
        "doctor_instructions": ["Repeat test"]
    }

    doc = DocumentExtraction(**data)

    assert doc.diagnosis == "Diabetes"
    assert len(doc.medications) == 1
