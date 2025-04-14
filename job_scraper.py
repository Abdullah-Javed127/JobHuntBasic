# job_scraper.py
import requests

def fetch_jobs(keyword):
    url = f"https://remotive.io/api/remote-jobs?search={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("jobs", [])
    return []
