import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Missing GOOGLE_API_KEY in the .env file.")
    st.stop()

genai.configure(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI Agricultural Assistant.
Help farmers identify crop diseases and provide practical farming advice.
Always answer in simple, farmer-friendly language.
"""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT,
)

st.set_page_config(page_title="AI Agriculture Assistant", page_icon="🌱", layout="wide")
st.title("🌱 AI Agriculture Assistant")
st.markdown("### Smart Crop Care Powered by AI")
#input fields
crop=st.text_input("Enter Crop Name")
symptoms=st.text_area("Describe Symptoms")
if st.button("Analyze Crop"):
    if crop and symptoms:
        prompt = f"""
You are an expert agricultural scientist.
Analyze the following crop issue.
Crop Name: {crop}
Symptoms: {symptoms}
Provide the output in the following format:
1. Possible Disease or Problem
2. Likely Causes
3. Prevention Methods
4. Treatment Suggestions
5. Farmer-Friendly Explanation
Keep the language simple and practical for farmers.
"""
        with st.spinner("Analyzing..."):
            response = model.generate_content(prompt)
            st.success("Analysis Complete")
            st.markdown(response.text)
    else:
        st.warning("Please enter the crop name and symptoms.")

st.subheader("Ask a follow-up question")
user_question = st.text_input("Ask a question", key="ask_question")

if st.button("Ask AI", key="ask_ai"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=user_question,
                )
                text = getattr(response, "text", None) or "No response returned."
                st.markdown(text)
            except Exception as exc:
                st.error(f"AI response failed: {exc}")
    else:
        st.warning("Please enter your question first.")