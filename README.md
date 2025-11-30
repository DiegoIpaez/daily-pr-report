# Daily PRs Report

lightweight CLI tool that fetches all your GitHub pull requests updated today and generates a clear, terminal-friendly daily report. It helps developers quickly review their activity, track progress, and stay organized without needing to open the GitHub UI.


## Requirements
- Python 3.11+
- GitHub personal access token

## Installation
1. Clone the repository and enter the project directory.
2. Install the dependencies:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy the `.env.example` file to `.env` and fill in your GitHub credentials:
   ```sh
   cp .env.example .env
   # Edit .env and add your token and username
   ```

## Usage
Run the main script:
```sh
python main.py
```
The script will search for your PRs updated today and display details and commits for each one.

## Structure
- `main.py`: Main script.
- `constants.py`: Loads environment variables.
- `services/gh_service.py`: Functions to interact with the GitHub API.
- `.env`: Environment variables (do not version).

## Notes
- The token must have permissions to read PRs.
- Results depend on the recent activity of the configured user.
