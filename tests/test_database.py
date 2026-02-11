from database.models import init_db
from database.crud import save_report, get_patient_reports


class Dummy:
    def model_dump(self):
        return {"key": "value"}

    @property
    def diagnosis(self):
        return "Test Diagnosis"


def test_save_and_fetch_report(tmp_path):

    init_db()

    save_report(
        patient_name="Test Patient",
        report_text="Sample report",
        document=Dummy(),
        reasoning=Dummy(),
        actions=Dummy(),
        safety=Dummy()
    )

    reports = get_patient_reports("Test Patient")

    assert len(reports) >= 1
    assert reports[0].diagnosis == "Test Diagnosis"
