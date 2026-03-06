import requests
try:
    resp = requests.get("https://career-genome-python.onrender.com/api/roles", timeout=5)
    print(f"Status: {resp.status_code}")
    print(f"Content: {resp.text[:100]}...")
except Exception as e:
    print(f"Error: {e}")
