# job_scraper.py
import requests

def fetch_jobs(keyword):
    url = f"https://remotive.com/api/remote-jobs?search={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("jobs", [])
    return []

# job_scraper.py
# import requests

# def fetch_jobs(keyword):
#     url = f"https://remotive.com/api/remote-jobs?search={keyword}"
#     print(f"🔗 Requesting: {url}")
#     response = requests.get(url)
    
#     print(f"✅ Status Code: {response.status_code}")
    
#     if response.status_code == 200:
#         data = response.json()
#         print(f"📦 Keys in response: {list(data.keys())}")
#         print(f"🔢 Total jobs returned: {len(data.get('jobs', []))}")
#         return data.get("jobs", [])
    
#     print("❌ Failed to fetch jobs")
#     return []

