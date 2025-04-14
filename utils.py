import json

def load_jobs(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def match_jobs(jobs, user_skills, preference):
    results = []
    for job in jobs:
        if preference in job['location'].lower():
            skill_overlap = set(user_skills) & set(job['skills'])
            if skill_overlap:
                job['score'] = len(skill_overlap)
                results.append(job)
    return sorted(results, key=lambda x: x['score'], reverse=True)[:3]

def match_jobs_live(jobs, user_skills, preference):
    results = []
    for job in jobs:
        location = job.get('candidate_required_location', '').lower()
        tags = [tag.lower() for tag in job.get('tags', [])]
        skill_overlap = set(user_skills) & set(tags)

        if (preference in location or preference == "any") and skill_overlap:
            job['score'] = len(skill_overlap)
            results.append(job)

    return sorted(results, key=lambda x: x['score'], reverse=True)[:5]

def get_user_input():
    skills = input("Enter your top skills (comma-separated): ").lower().split(",")
    skills = [skill.strip() for skill in skills]
    experience = input("Your experience level (e.g. junior, mid, senior): ").lower()
    preference = input("Remote or Onsite? (or type 'any'): ").lower()
    return skills, experience, preference

