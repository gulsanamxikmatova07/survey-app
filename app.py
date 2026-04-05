import streamlit as st
import json

st.set_page_config(page_title="Academic Planning and Mental Clarity Survey")

st.title("Academic Planning and Mental Clarity Survey")
st.write("Please answer all questions below.")

# Questions faylini o'qish
with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]

# User details
name = st.text_input("Name")
surname = st.text_input("Surname")
student_id = st.text_input("Student ID")

st.write("---")

answers = []
total_score = 0

# Savollarni chiqarish
for i, q in enumerate(questions, start=1):
    st.subheader(f"Q{i}. {q['question']}")

    option = st.radio(
        "Choose one option:",
        list(q["options"].keys()),
        key=f"q_{i}"
    )

    score = q["options"][option]
    total_score += score

    answers.append({
        "question": q["question"],
        "selected_option": option,
        "score": score
    })

# Natija
if st.button("Submit"):
    if total_score <= 20:
        result = "Very Low Stress"
    elif total_score <= 40:
        result = "Low Stress"
    elif total_score <= 60:
        result = "Moderate Stress"
    elif total_score <= 80:
        result = "High Stress"
    else:
        result = "Very High Stress"

    st.success("Survey submitted successfully!")
    st.write(f"**Total Score:** {total_score}")
    st.write(f"**Result:** {result}")

    st.json({
        "name": name,
        "surname": surname,
        "student_id": student_id,
        "total_score": total_score,
        "result": result,
        "answers": answers
    })
