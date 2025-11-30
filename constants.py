import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = os.getenv("GITHUB_API_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")

if not all([GITHUB_API_URL, GITHUB_TOKEN, GITHUB_USERNAME, GEMINI_API_KEY, GEMINI_MODEL_NAME]):
    raise EnvironmentError("One or more required environment variables are missing.")
