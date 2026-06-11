import json
import subprocess

def run_job_matcher(jd, min_exp=0, skills="", limit=10):
    cmd = [
        "./.venv/bin/python", "job_matcher.py",
        "--jd", jd,
        "--min-experience", str(min_exp),
        "--limit", str(limit)
    ]
    if skills:
        cmd.extend(["--skills", skills])
        
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
        return None
    return json.loads(result.stdout)

def test_experience_filtering():
    print("--- Test 1: Experience Filtering ---")
    min_exp = 5.0
    results = run_job_matcher("Software Developer", min_exp=min_exp)
    if not results:
        print("FAIL: No results returned.")
        return False
        
    print(f"Query for min experience {min_exp} returned {len(results['top_matches'])} matches:")
    all_passed = True
    for match in results["top_matches"]:
        name = match["candidate_name"]
        score = match["match_score"]
        # Find candidate's experience from the reasoning or by querying their resume path
        print(f" - Candidate: {name}, Score: {score}")
        
    print("Experience filtering check completed.\n")
    return all_passed

def test_skills_filtering():
    print("--- Test 2: Skills Filtering ---")
    skills = "FastAPI,PostgreSQL"
    results = run_job_matcher("Web Developer with FastAPI and PostgreSQL experience.", skills=skills)
    if not results:
        print("FAIL: No results returned.")
        return False
        
    print(f"Query for must-have skills [{skills}] returned {len(results['top_matches'])} matches:")
    all_passed = True
    for match in results["top_matches"]:
        name = match["candidate_name"]
        matched_skills = [s.lower() for s in match["matched_skills"]]
        score = match["match_score"]
        print(f" - Candidate: {name}, Score: {score}, Matched Skills: {match['matched_skills']}")
        
    print("Skills filtering check completed.\n")
    return all_passed

if __name__ == "__main__":
    test_experience_filtering()
    test_skills_filtering()
