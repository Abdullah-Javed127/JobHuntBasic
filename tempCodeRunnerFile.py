from job_scraper import fetch_jobs
from utils import match_jobs_live, get_user_input

def main():
    print("Welcome to Job Finder Agentic Bot 🔎\n")
    skills, experience, preference = get_user_input()

    # Fetch jobs based on each skill
    all_jobs = []
    for skill in skills:
        print(f"⏳ Searching jobs for: {skill}...")
        jobs = fetch_jobs(skill)
        print(f"✅ Found {len(jobs)} jobs for '{skill}'")
        all_jobs.extend(jobs)

    print(f"\n🔍 Total jobs fetched: {len(all_jobs)}")

    if not all_jobs:
        print("\n❌ No jobs found online. Try again later.")
        return

    matches = match_jobs_live(all_jobs, skills, preference)

    if not matches:
        print("\n😕 No matching jobs found. Try different skills or location preference.")
        return

    print("\n🎯 Top Matching Jobs:\n")
    for i, job in enumerate(matches, 1):
        print(f"{i}. {job['title']} at {job['company_name']}")
        print(f"   Location: {job['candidate_required_location']}")
        print(f"   Tags: {', '.join(job['tags'])}")
        print(f"   Apply here: {job['url']}\n")

if __name__ == "__main__":
    main()