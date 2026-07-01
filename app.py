import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Exam Performance Indicator")
st.write("Enter the details below to predict the Maths Score.")

# Categorical Features
gender = st.selectbox(
    "Gender",
    ["Select Gender", "male", "female"]
)

ethnicity = st.selectbox(
    "Race or Ethnicity",
    ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "Select Parent Education",
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["Select Lunch Type", "free/reduced", "standard"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["Select Test Preparation Course", "none", "completed"]
)

# Numerical Features
reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    step=1
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("Predict Maths Score"):

    if (
        gender == "Select Gender"
        or ethnicity == "Select Ethnicity"
        or parental_level_of_education == "Select Parent Education"
        or lunch == "Select Lunch Type"
        or test_preparation_course == "Select Test Preparation Course"
    ):
        st.error("Please fill all the fields.")
    else:
        try:
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()

            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)

            st.success(
                f"Predicted Maths Score: {result[0]:.2f}"
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")