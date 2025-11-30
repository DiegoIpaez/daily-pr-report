import requests
import datetime
from utils.constants import GITHUB_TOKEN, GITHUB_API_URL, GITHUB_USERNAME

DEFAULT_GH_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_all_prs():
    """Get all PRs involving the authenticated user updated today."""
    try:
        endpoint = f"{GITHUB_API_URL}/search/issues"
        currentDate = datetime.datetime.now(datetime.UTC).date()

        query = f"is:pr involves:{GITHUB_USERNAME} updated:>={currentDate}"
        params = {"q": query}

        responseRaw = requests.get(
            endpoint, headers=DEFAULT_GH_HEADERS, params=params
        ).json()

        pullRequest = responseRaw.get("items", [])
        return pullRequest
    except Exception as error:
        raise Exception(f"Error al buscar PRs: {error}")


def get_pr_commits_by_pr_number(repo_api, pr_number):
    """Get commits for a specific PR by its number."""
    try:
        endpoint = f"{repo_api}/pulls/{pr_number}/commits"
        commits = requests.get(endpoint, headers=DEFAULT_GH_HEADERS).json()
        return commits
    except Exception as error:
        raise Exception(f"Error al buscar commits del PR #{pr_number}: {error}")
