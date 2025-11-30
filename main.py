from services.gh_service import get_all_prs, get_pr_commits_by_pr_number


def show_commit(commit):
    sha = commit["sha"]
    mensaje = commit["commit"]["message"]
    autor = commit["commit"]["author"]["name"]
    fecha = commit["commit"]["author"]["date"]

    print(f"    - {sha}: {mensaje} by {autor} on {fecha}\n")


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

    print(f"\n🔵 PR #{numero} — {repo_owner}/{repo_name}")
    print(f"    Título: {titulo}")
    print(f"    URL: {url}")
    print(f"    Repositorio: {repo_name}")
    print(f"    Autor: {user} ({association})")
    print(f"    Estado: {state}")
    print(f"    Labels: {', '.join(labels) if labels else 'Ninguna'}")
    print(f"    Cerrado: {closed}")

    commits = get_pr_commits_by_pr_number(repo_api, numero)
    print("    Commits:")
    for commit in commits:
        show_commit(commit)


def main():
    try:
        print("📌 Buscando tus PRs actualizados hoy...\n")

        prs = get_all_prs()

        print(f"Encontrados {len(prs)} PRs actualizados hoy.\n")
        if not prs:
            exit("No hay PRs hoy.")

        print("🔵 PRs encontrados:")
        for pr in prs:
            show_pr(pr)

    except Exception as error:
        print(f"Error: {error}")


main()
