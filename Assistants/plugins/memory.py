import json
import os

PROFILE_PATH = "data/user_profile.json"

def load_profile():
    if not os.path.exists(PROFILE_PATH):
        return {"name" : None, "city" : None, "interests" : [], "tone" : "casual"}
    with open(PROFILE_PATH, "r") as file:
        return json.load(file)
    
def save_profile(profile):
    with open(PROFILE_PATH, "w") as file:
        json.dump(profile, file, indent=2)
    
def update_profile(field, value):
    profile = load_profile()
    if field == "interests" and isinstance(value, list):
        profile["interests"] = list(set(profile["interests"] + value))
    else:
        profile[field] = value
    save_profile(profile)

def get_profile():
    p = load_profile()
    return(
        f"Name: {p['name'] or 'Unknown'}\n"
        f"City: {p['city'] or 'Unkonwn'}\n"
        f"Interests: {','.join(p['interests']) or 'None'}\n"
        f"Tone: {p['tone']}"
    )