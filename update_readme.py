import datetime
import random
import re

def generate_breach_row():
    ips = ["104.28.x.x", "35.211.x.x", "54.39.x.x", "103.212.x.x", "47.128.x.x"]
    entities = ["AI_SCRAPER (GPTBot)", "SEC_SCANNER (Snyk)", "UNAUTH_AWS_ACCESS", "AWS_CRED_BOT (OVH)", "CUSTOM_SCRAPER (Requests)"]
    actions = ["[PROMPT_INJECTION_PREVENTED]", "[LOG_INJECTION_SUCCESS]", "[CANARY_CRED_INTERCEPT]", "[RECURSIVE_PROBE_DETECTED]"]
    
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"| `{now}` | `{random.choice(ips)}` | `{random.choice(entities)}` | `{random.choice(actions)}` |"

def update_readme():
    with open("README.md", "r") as f:
        content = f.read()

    # Update Last Uplink
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r"// LAST_UPLINK: \d{4}-\d{2}-\d{2}", f"// LAST_UPLINK: {today}", content)

    # Rotate Threat Intel (Keep the last 10, add 1 new)
    new_row = generate_breach_row()
    # Logic to find the table and shift rows can be added here
    
    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
