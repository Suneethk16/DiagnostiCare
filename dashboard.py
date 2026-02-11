import streamlit as st
from dotenv import load_dotenv
from datetime import datetime

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# -----------------------------
# LangGraph
# -----------------------------
from graph_orchestrator import build_graph

# -----------------------------
# PDF OCR
# -----------------------------
from utils.pdf_ocr import extract_text_from_pdf

# -----------------------------
# Database
# -----------------------------
from database.models import init_db
from database.crud import save_report, get_patient_reports

# Initialize DB
init_db()

# Build LangGraph once
graph = build_graph()

# ==========================================================
# Streamlit Config
# ==========================================================

st.set_page_config(
    page_title="Agentic Medical Decision Support",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Agentic Medical Decision Support System")

st.markdown(
    """
    Multi-agent clinical decision support powered by:
    - LangGraph orchestration
    - OCR-enabled PDF ingestion
    - Schema-validated structured outputs
    - Persistent patient timeline storage
    """
)

# ==========================================================
# PATIENT SECTION
# ==========================================================

st.header("👤 Patient Information")

patient_name = st.text_input("Patient Name")

# ==========================================================
# INPUT SECTION
# ==========================================================

st.header("📄 Medical Report Input")

uploaded_file = st.file_uploader(
    "Upload medical report (PDF)",
    type=["pdf"]
)

report_text = st.text_area(
    "Or paste medical report text:",
    height=200,
    placeholder="Enter doctor's notes, discharge summary, lab results..."
)

analyze_button = st.button("🔍 Analyze Report")

# ==========================================================
# ANALYSIS
# ==========================================================

if analyze_button:

    if not patient_name.strip():
        st.warning("Please enter a patient name.")
        st.stop()

    # -------- Extract from PDF if provided --------
    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            pdf_bytes = uploaded_file.read()
            report_text = extract_text_from_pdf(pdf_bytes)

        st.subheader("📄 Extracted Text Preview")
        st.text(report_text[:1500])

    if not report_text.strip():
        st.warning("Please upload a PDF or paste medical text.")
        st.stop()

    # -------- Run LangGraph --------
    with st.spinner("Running multi-agent clinical reasoning..."):
        result = graph.invoke({
            "report_text": report_text,
            "document": None,
            "reasoning": None,
            "actions": None,
            "safety": None
        })

    st.success("✅ Analysis complete!")

    # -------- Save to database --------
    save_report(
        patient_name=patient_name,
        report_text=report_text,
        document=result["document"],
        reasoning=result["reasoning"],
        actions=result["actions"],
        safety=result["safety"]
    )

    # ==========================================================
    # OUTPUT SECTION
    # ==========================================================

    st.header("🧠 Agent Outputs")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📑 Document Extraction")
        st.json(result["document"].model_dump())

        st.subheader("🧠 Clinical Reasoning")
        st.json(result["reasoning"].model_dump())

    with col2:
        st.subheader("📝 Action Plan")
        st.json(result["actions"].model_dump())

        st.subheader("🛡️ Safety Review")
        st.json(result["safety"].model_dump())

    # ==========================================================
    # QUICK SUMMARY
    # ==========================================================

    st.header("🧾 Quick Clinical Summary")

    diagnosis = result["document"].diagnosis
    critical_findings = result["reasoning"].critical_findings

    summary = f"""
    Patient: {patient_name}  
    Diagnosis: {diagnosis}  
    Key Concern: {critical_findings[0] if critical_findings else "No major concerns detected."}  
    Structured action plan and safety validation generated.
    """

    st.info(summary)

# ==========================================================
# PATIENT TIMELINE
# ==========================================================

st.header("📅 Patient Timeline")

if patient_name:
    reports = get_patient_reports(patient_name)

    if reports:
        for r in reports:
            with st.expander(
                f"Report on {r.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
            ):
                st.write("Diagnosis:", r.diagnosis)
                st.write("Created At:", r.created_at)

                st.subheader("Original Report")
                st.text(r.report_text[:800])

    else:
        st.info("No previous reports found for this patient.")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")
st.markdown(
    "Built with ❤️ using LangGraph, OCR, Pydantic, SQLAlchemy, and Agentic AI architecture."
)
