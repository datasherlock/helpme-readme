import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
import vertexai.preview.generative_models as generative_models


class GOOGLE_AI:
    def __init__(self):
        vertexai.init(project="datasherlock", location="us-central1")
        self.model = GenerativeModel(
            "gemini-1.5-pro-001",
        )
        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }

        self.safety_settings = [
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
        ]

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
            safety_settings=self.safety_settings,
            stream=True,
        )
        return responses




