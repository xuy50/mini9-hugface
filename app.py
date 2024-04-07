import streamlit as st
from transformers import pipeline

# Set up title and user input
st.title('Text Generation with Hugging Face')
user_input = st.text_input("Enter your text:", "Type here")

if st.button('Generate Text'):
    # Load the model
    generator = pipeline('text-generation', model='gpt2')
    # Generate text
    generated = generator(user_input, max_length=50, num_return_sequences=1)
    # Display generated text
    st.write(generated[0]['generated_text'])
