import requests
try:
    resp = requests.get("https://career-genome-python.onrender.com/api/collections", timeout=5)
    print(f"Status: {resp.status_code}")
    print(f"Collections: {resp.json()}")
except Exception as e:
    print(f"Error: {e}")
