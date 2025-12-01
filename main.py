import json
from services.gh_service import get_all_prs, get_pr_commits_by_pr_number
from services.ai_service import generate_professional_report
from utils.logger import app_log


def extract_commit(commit):
    return {"title": commit["commit"]["message"]}


def extract_pr(pull_request):
    repo_api = pull_request["repository_url"]
    repo_name = repo_api.split("/")[-1]

    commits_raw = get_pr_commits_by_pr_number(repo_api, pull_request["number"])
    commits = [extract_commit(commit) for commit in commits_raw]

    return {
        "repository": repo_name,
        "pull_request": {
            "number": pull_request["number"],
            "title": pull_request["title"],
        },
        "commits": commits,
    }


def main():
    try:
        app_log("📌 Buscando tus PRs actualizados hoy...")
        pull_request = get_all_prs()
        app_log(f"🔵 Encontrados {len(pull_request)} PRs actualizados hoy.")
        if not pull_request:
            exit("No hay PRs hoy.")

        report_json = [extract_pr(pull_request) for pull_request in pull_request]
        report_raw = json.dumps(report_json, ensure_ascii=False, separators=(",", ":"))

        app_log(report_raw)
        daily_report = generate_professional_report(report_raw)
        app_log(daily_report)

    except Exception as error:
        app_log(f"Error: {error}")
        return None


if __name__ == "__main__":
    main()
