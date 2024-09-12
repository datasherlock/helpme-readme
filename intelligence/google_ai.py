import base64
from logging import exception

import vertexai
import google.generativeai as genai
# from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
# import vertexai.preview.generative_models as generative_models
# from google.cloud import aiplatform
import os
from dotenv import load_dotenv
import streamlit as st
from google.api_core.exceptions import InvalidArgument
from utils.common import validate_apikey


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
        Write a detailed and professional README for a software project. 
        The README should include the following sections: Project Title, Project Description, Features, Installation Instructions, 
        Usage Guide, Example Code Snippet, Contributing Guidelines, 
        License Information, and Contact Details. The README should be clear, easy to follow, and written in markdown format. 
        Ensure that the tone is friendly and helpful, providing necessary details for users and developers. Also generate a project banner
        in the README. The README must follow all the recommended best practices
        """

    def generate_readme(self, text):
        input = self.context + '~```~' + text + '~```~'
        try:
            with st.status("Asking Google AI to generate the README..."):
                responses = self.model.generate_content(
                    [input],
                    generation_config=self.generation_config,
                   # safety_settings=self.safety_settings,
                    stream=True,
                )
        except InvalidArgument as e:
            st.warning("Invalid API Key Provided. Please get the correct one from https://aistudio.google.com/app/apikey")
            validate_apikey()
            exit(-1)

            # st.rerun()
        return responses

