import streamlit as st
from assistent import recommend, parse_skills

st.set_page_config(page_title="Virtual Career Counsellor", layout="centered")

st.title("🎯 Virtual Career Counsellor")
st.write("Enter your skills and choose interests to get career suggestions.")

with st.form("user_form"):
    skills_input = st.text_area(
        "Your skills (comma separated)",
        placeholder="Python, SQL, Excel, Figma,Financial Knowledge"
    )
    education = st.selectbox(
        "Education level",
        ["High School", "BSC/BTech", "Masters","FRM (Financial Risk Manager)", "Other"]
    )
    interests = st.multiselect(
        "Interests (choose any)",
        ["Data", "Design", "AI", "Software", "Marketing","finance & money management"]
    )
    submit = st.form_submit_button("Get recommendations")

if submit:
    if not skills_input.strip():
        st.warning("⚠️ Please write at least one skill (e.g., Python).")
    else:
        with st.spinner("Analyzing..."):
            recs = recommend(skills_input, education, interests)

        st.success("✅ Career Recommendations:")
        for r in recs:
            st.write(f"- {r}")
