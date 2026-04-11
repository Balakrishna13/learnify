import requests

url = "http://127.0.0.1:5000/process"

data = {
    "mode": "notes",
    "text": "Operating systems manage hardware. They handle processes. They allocate memory. They manage files."
}

response = requests.post(url, json=data)

print(response.json())