import requests

try:
    print("Testing /ask endpoint with empty body...")
    response = requests.post("http://localhost:8000/ask", json={})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
