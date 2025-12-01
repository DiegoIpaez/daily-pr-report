import os
import os.path
from datetime import datetime

BASE_LOGS_DIR = os.path.join(os.path.dirname(__file__), "../logs")


def save_log(filename, content, folder="app"):
    """
    Saves log content to a file with the current date in its name.
    For example, if filename is "app.log" and the date is 2024-11-30,
    the log will be saved to "app_2024-11-30.log" inside the specified folder.
    """
    root, ext = os.path.splitext(filename)
    date_str = datetime.now().strftime("%Y-%m-%d")
    dated_filename = f"{root}_{date_str}{ext}"

    folder_path = os.path.join(BASE_LOGS_DIR, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    path = os.path.join(folder_path, dated_filename)

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n--- {datetime.now().isoformat()} ---\n")
        f.write(content)
        f.write("\n")


def app_log(content):
    print(f"{content}\n")
    save_log("app.log", content)


def ai_log(response):
    content = ""
    usage = getattr(response, "usage_metadata", None)
    if usage:
        total_tokens = getattr(usage, "total_token_count", None)
        prompt_tokens = getattr(usage, "prompt_token_count", None)
        completion_tokens = getattr(usage, "candidates_token_count", None)
        content = f"Tokens usados: total={total_tokens}, prompt={prompt_tokens}, completion={completion_tokens}\n"

    save_log("ai.log", content, folder="ai")
