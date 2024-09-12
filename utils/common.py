import argparse
import sys
import streamlit as st


# WARNING: Do not share code with you API key hard coded in it.
# Get your Gemini API key from: https://aistudio.google.com/app/apikey
#@st.fragment
def validate_apikey():
    # Prompt the user to enter the API key securely
    with st.sidebar:
        if 'GOOGLE_API_KEY' not in st.session_state:
            api_key_input = st.text_input("Enter your Google API Key from: https://aistudio.google.com/app/apikey", type="password")
            api_button = st.button("Save", key="apibutton")
            st.info("_Note: Your API key will not be saved anywhere and will be safe in your local session. Refreshing the page will wipe it from memory."
                    "Do not share your key with anyone_")

            if api_button:
                if len(api_key_input) > 0:
                    # Store the API key in session state
                    st.session_state['GOOGLE_API_KEY'] = api_key_input
                    # st.success("API key stored in session successfully! Please restart the app.")
                    # st.stop()  # Stop execution until the user restarts the app
                    #api_button.disabled = True
                else:
                    st.error("API key cannot be empty. Please try again.")

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo_url", help="Provide the GitHub Repo URL",
                        type=str, default='repo_url')
    parser.add_argument("--keep_merged_code", help="true/false. Set to false if you want to delete the merged code "
                                                   "file under temp/",type=str, default="true")
    args = parser.parse_args()
    return args


def write_to_file(filename, content):
    with open(filename, 'a+') as f:
        f.write(content)

@st.fragment
def download_readme(readme_file):
    with open(readme_file, "rb") as file:
        st.download_button(
            label="Download README",
            data=file,
            file_name="README.md",
            mime="text/csv",
        )

@st.fragment
def download_merged_code(output_file):
    with open(output_file, "rb") as file:
        st.download_button(
            label="Download Merged Codebase",
            data=file,
            file_name="merged.txt",
            mime="text/csv",
        )


def set_page_header_format():
    st.set_page_config(
        page_title="Google AI Powered README Generator",
        page_icon="🕵️",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    st.text("This application helps generate a README from a given Github repo")

    st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top=0, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )

    navbar = """
        <style>
            .navbar {
                background-color: #333;
                padding: 10px;
                color: white;
                text-align: center;
                top-margin: 0px;

            }
            .navbar a {
                color: white;
                text-decoration: none;
                padding: 10px;
            }
        </style>
        <div class="navbar">
            <a href="https://www.jeromerajan.com">About</a>
            <a href="https://linkedin.com/in/jeromerajan">LinkedIn</a>
            <a href="https://medium.com/@datasherlock">Medium</a>
            <a href="https://github.com/datasherlock">Github</a>
            <a href="https://buymeacoffee.com/datasherlock">Buy me a coffee</a>
        </div>
    """
    st.markdown("""<p />""", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; '>Google AI Powered README Generator</h1>", unsafe_allow_html=True)
    st.markdown(navbar, unsafe_allow_html=True)

    # columns = st.columns(8)

    # with columns[2]:
    #     st.write("""<div style="width:100%;text-align:center;"><a href="https://www.jeromerajan.com" style="float:center"><img src="https://cdn0.iconfinder.com/data/icons/england-13/504/sherlock-holmes-detective-inspector-man-512.png" width="22px"></img></a></div>""", unsafe_allow_html=True)

    # with columns[3]:
    #     st.write("""<div style="width:100%;text-align:center;"><a href="https://linkedin.com/in/jeromerajan" style="float:center"><img src="https://cdn2.iconfinder.com/data/icons/social-media-applications/64/social_media_applications_14-linkedin-512.png" width="22px"></img></a></div>""", unsafe_allow_html=True)

    # with columns[4]:
    #     st.write("""<div style="width:100%;text-align:center;"><a href="https://medium.com/@datasherlock" style="float:center"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Medium-512.png" width="22px"></img></a></div>""", unsafe_allow_html=True)

    # with columns[5]:
    #     st.write("""<div style="width:100%;text-align:center;"><a href="https://github.com/datasherlock" style="float:center"><img src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_github_2-512.png" width="22px"></img></a></div>""", unsafe_allow_html=True)

    st.markdown("""---""")
    # _, feedback, _ = st.columns(3)
    # feedback.markdown("""Share your feedback at [Github Repo Issues](https://github.com/datasherlock/spark-config-calculator/issues)""")

