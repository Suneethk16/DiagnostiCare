from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///medical_ai.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class PatientReport(Base):
    __tablename__ = "patient_reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, index=True)
    diagnosis = Column(String)
    report_text = Column(Text)

    document_json = Column(Text)
    reasoning_json = Column(Text)
    action_json = Column(Text)
    safety_json = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)
