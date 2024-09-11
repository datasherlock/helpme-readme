import base64
import vertexai
import google.generativeai as genai
# from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
# import vertexai.preview.generative_models as generative_models
# from google.cloud import aiplatform
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file




class GOOGLE_AI:
    def __init__(self):
        # load_dotenv()
        if 'GOOGLE_API_KEY' in st.session_state:
            self.api_key = st.session_state['GOOGLE_API_KEY']
        else:
            self.api_key = None
            exit(1)

        genai.configure(api_key=self.api_key)
        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }


        self.model = genai.GenerativeModel(
            "gemini-1.5-pro-001",
            generation_config=self.generation_config
        )




        self.context = """
        You are the world\'s leading developer relations consultant. You write thorough, understandable and human-like documentation.
        You will be given a code base which has been merged from multiple files into a single file.
        This code will be enclosed within ~```~.
        You have to generate a README.md that will be hosted in Github. Provide the output in markdown language that can be copy pasted
        """

    def generate_readme(self, text):
        input = self.context + '~```~' + text + '~```~'
        responses = self.model.generate_content(
            [input],
            generation_config=self.generation_config,
           # safety_settings=self.safety_settings,
            stream=True,
        )
        return responses

