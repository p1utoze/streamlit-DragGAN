import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline

@st.cache_resource
def image_to_text(image):
    st.write("Converting image to text...")
    st.write("This may take a while")
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    output = image_to_text(image)
    st.write(output)