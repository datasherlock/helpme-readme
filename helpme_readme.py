import sys
from utils.common import parse_args, download_readme, download_merged_code, set_page_header_format, validate_apikey
from utils.repo import GITREPO
from intelligence.google_ai import GOOGLE_AI
import streamlit as st


def main():
    set_page_header_format()
    repo_url = st.text_input("__Github Repo URL__", value="https://github.com/google-gemini/gemini-api-quickstart.git")
    validate_apikey()
    repo = GITREPO(repo_url)
    submit = False
    if 'GOOGLE_API_KEY' in st.session_state:
        submit = st.button("Submit", key="submit")
    else:
        st.warning("Enter your Google API Key from: https://aistudio.google.com/app/apikey")

    if submit:

        with st.status("Merging Repo..."):
            merged = repo.merge_repo()

        with st.status("Analyzing the codebase..."):
            with open(merged) as text:
                from_code = text.read()

        try:
            ask_google_ai = GOOGLE_AI()
        except Exception as e:
            print(str(e))

        responses = ask_google_ai.generate_readme(from_code)
        with st.status("Receiving Response..."):
            for response in responses:
                repo.write_repo_readme(response.text)
            #download_readme = st.button("Download README", key = "download_readme")

        readme, output = st.columns(2)
        with readme:
            download_readme(repo.readme_file)
        with output:
            download_merged_code(repo.output_file)

        st.info("All done!!")



if __name__ == '__main__':
    main()
