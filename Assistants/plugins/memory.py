import json
import os

PROFILE_PATH = "data/user_profile.json"

def load_profile():
    if not os.path.exists(PROFILE_PATH):
        return {"name" : None, "city" : None, "interests" : [], "tone" : "casual"}
    with open(PROFILE_PATH, "r") as file:
        profile = json.load(file)

        if profile.get("interests") is None:
            profile["interests"] = []
        if profile.get("tone") is None:
            profile["tone"] = "casual"
            
        return profile
    
def save_profile(profile):
    with open(PROFILE_PATH, "w") as file:
        json.dump(profile, file, indent=2)
    
def update_profile(field, value):
    profile = load_profile()
    if field == "interests":
        if not isinstance(profile["interests"], list):
            profile["interests"] = []
        if isinstance(value, str):
            profile["interests"] = list(set(profile["interests"] + value))

    else:
        profile[field] = value
        
    save_profile(profile)

def get_profile():
    p = load_profile()
    
    parts = []

    if p['name'] and p['city']:
        parts.append(f"You're {p['name']} from {p['city']}.")
    elif p['name']:
        parts.append(f"YOu're {p['name']}.")
    elif p['city']:
        parts.append(f"You are from {p['city']}.")
    
    if p['interests']:
        interests = ','.join(p['interests'])
        parts.append(f"You enjoy {interests}.")

    parts.append(f"I'm talking to you in a {p['tone']} tone.")

    return " ".join(parts) if parts else "I don't know anything about you yet."