import os
import pathlib
import sys
from pathlib import Path
import git
import shutil

from utils.common import parse_args, write_to_file


class GITREPO:
    def __init__(self, repo_url, extension=('py', 'txt')):
        self.repo_url = repo_url
        self.extension = extension
        self.repo_name = repo_url.split('/')[-1]
        self.clone_dir = os.path.join(os.getcwd(), "temp", self.repo_name)
        self.output_file = os.path.join(os.getcwd(), "temp", 'merged.txt')
        self.readme_file = os.path.join(self.clone_dir, "README.md")

    def _clone_repo(self):
        """Clone the given GitHub repository to a local directory."""

        print(f"Cloning the repository from {self.repo_url} to {self.clone_dir}...")
        if os.path.exists(self.clone_dir):
            shutil.rmtree(self.clone_dir)
        git.Repo.clone_from(self.repo_url, self.clone_dir)

    def _merge_files(self):
        """Merge all files in the repository into a single file with annotations."""

        print(f"Merging files into {self.output_file}...")
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

        with open(self.output_file, 'w'):
            pass

        with open(self.output_file, 'w') as merged_file:
            for root, _, files in os.walk(self.clone_dir):
                for file in files:
                    if file.endswith(self.extension):
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, self.clone_dir)
                        merged_file.write(f"\n\n# --- Start of {relative_path} ---\n\n")
                        with open(file_path, 'r') as source_file:
                            merged_file.write(source_file.read())
                        merged_file.write(f"\n\n# --- End of {relative_path} ---\n\n")

        print(f"Files have been merged into {self.output_file}")

    def _delete_repo(self):
        shutil.rmtree(self.clone_dir)

    def cleanup(self):

        merged_file = pathlib.Path(self.output_file)
        merged_file.unlink()

    def write_repo_readme(self, text):
        Path(self.clone_dir).mkdir(parents=True, exist_ok=True)
        with open(self.readme_file, 'a+') as f:
            f.write(text)


    def merge_repo(self):

        self._clone_repo()
        self._merge_files()
        self._delete_repo()
        return self.output_file
