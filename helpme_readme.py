import sys

from utils.common import parse_args
from utils.repo import GITREPO
from intelligence.google_ai import GOOGLE_AI


def main():
    args = parse_args(sys.argv)
    repo_url = args.repo_url
    repo = GITREPO(repo_url)

    merged = repo.merge_repo()

    with open(merged) as text:
        from_code = text.read()

    ask_google_ai = GOOGLE_AI()

    responses = ask_google_ai.generate_readme(from_code)

    for response in responses:
        repo.write_repo_readme(response.text)

    repo.cleanup()


if __name__ == '__main__':
    main()
