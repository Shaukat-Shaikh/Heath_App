from dotenv import load_dotenv  # For loading environment variables
import streamlit as st  # Streamlit for UI
import os  # For accessing environment variables
from PIL import Image  # For image processing
import requests  # For making API requests
import base64  # For encoding image to base64
import tempfile  # For creating temporary image file
import re  # For cleaning up the output
import os

# Load environment variables

# api_key = os.getenv("api_key")
# load_dotenv()
# os.environ["api_key"]=os.getenv("api_key")
# api_key = os.environ["api_key"]

api_key  ="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"


# Function to encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to analyze the uploaded image
def analyze_image(img):
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
        img.save(temp.name)
        image_path = temp.name

    encoded_image = encode_image(image_path)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "moonshotai/kimi-vl-a3b-thinking:free",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a healthcare professional. Look at the report verry cearfully and explain briefly and in simple language whether the patient is normal or not. Keep it clean, precise, and short."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
                    }
                ]
            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    raw_text = response.json()["choices"][0]["message"]["content"]

    cleaned_text = re.sub(r"◁think▷.*?◁/think▷", "", raw_text, flags=re.DOTALL).strip()
    return cleaned_text

# Streamlit page config
st.set_page_config(page_title="Medical Report Summary")

st.header("Get a Summary of Your Medical Report")
st.write("Upload a medical report image (JPG/PNG) and get a quick summary with an assessment.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width =True)

    if st.button("Tell me about the Report"):
        response = analyze_image(image)
        st.subheader("Summary:")
        st.write(response)

# # # Error: 401, {"error":{"message":"No auth credentials found","code":401}}
# print(api_key)
