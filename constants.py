import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = os.getenv("GITHUB_API_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

if not all([GITHUB_API_URL, GITHUB_TOKEN, GITHUB_USERNAME]):
    raise EnvironmentError("One or more required environment variables are missing.")
