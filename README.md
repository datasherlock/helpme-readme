# AI-Powered README Generator

This repository contains a Python script that automatically generates README.md files for GitHub repositories using Google AI. 

## Features

* Clones a given GitHub repository.
* Merges all code files into a single file for analysis.
* Sends the merged code to Google AI's Gemini Pro model.
* Uses a prompt engineered to generate human-like and informative README content.
* Writes the generated README back to the cloned repository.

## Dependencies

* Python 3.7+
* gitpython
* google-cloud-aiplatform
* vertexai

You can install the necessary packages using:

```bash
pip install -r requirements.txt 
```

## Usage

1.  **Set up Google Cloud Project and Vertex AI API:**
    *   Create a Google Cloud Project ([https://cloud.google.com/](https://cloud.google.com/)).
    *   Enable the Vertex AI API.
    *   Create a service account and download its JSON key file.
    *   Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your JSON key file:
        ```bash 
        export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/keyfile.json"
        ```

2. **Get Repository URL:**
    *   Get the repository URL from Github. This should be the complete path with the `.git` extension


3. **Run the script:**

   ```bash
   python helpme_readme.py --repo_url=<Github URL>
   ```

The script will generate or update the `README.md` file in the cloned repository directory.

## Disclaimer

* The quality of the generated README depends on the complexity and clarity of the codebase.
* This is an experimental tool and may require further refinement or customization.