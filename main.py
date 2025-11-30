from services.gh_service import get_all_prs, get_pr_commits_by_pr_number
from services.ai_service import generate_professional_report


def show_commit(commit):
    sha = commit["sha"]
    mensaje = commit["commit"]["message"]
    autor = commit["commit"]["author"]["name"]
    fecha = commit["commit"]["author"]["date"]
    return f"    - {sha}: {mensaje} by {autor} on {fecha}\n"


def show_pr(pr):
    state = pr["state"]
    titulo = pr["title"]
    url = pr["html_url"]
    numero = pr["number"]
    user = pr["user"]["login"]
    repo_api = pr["repository_url"]
    association = pr["author_association"]
    closed = pr.get("closed_at", "N/A")
    labels = [label["name"] for label in pr["labels"]]
    repo_owner = repo_api.split("/")[-2]
    repo_name = repo_api.split("/")[-1]

    pr_str = f"\n🔵 PR #{numero} — {repo_owner}/{repo_name}\n"
    pr_str += f"    Título: {titulo}\n"
    pr_str += f"    URL: {url}\n"
    pr_str += f"    Repositorio: {repo_name}\n"
    pr_str += f"    Autor: {user} ({association})\n"
    pr_str += f"    Estado: {state}\n"
    pr_str += f"    Labels: {', '.join(labels) if labels else 'Ninguna'}\n"
    pr_str += f"    Cerrado: {closed}\n"

    commits = get_pr_commits_by_pr_number(repo_api, numero)
    pr_str += "    Commits:\n"
    for commit in commits:
        pr_str += show_commit(commit)
    return pr_str


def main():
    try:
        print("📌 Buscando tus PRs actualizados hoy...\n")
        prs = get_all_prs()

        print(f"🔵 Encontrados {len(prs)} PRs actualizados hoy.\n")
        if not prs:
            exit("No hay PRs hoy.")

        reporte_str = ""
        for pr in prs:
            reporte_str += show_pr(pr)

        dr = generate_professional_report(reporte_str)
        print("\n\n--- DAILY REPORT ---\n")
        print(dr)

    except Exception as error:
        print(f"Error: {error}")
        return None


if __name__ == "__main__":
    main()
