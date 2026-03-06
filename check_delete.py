import requests
try:
    resp = requests.delete("https://career-genome-python.onrender.com/api/skill-gap/roadmap?email=test@example.com", timeout=5)
    print(f"Status: {resp.status_code}")
    print(f"Message: {resp.json()}")
except Exception as e:
    print(f"Error: {e}")
