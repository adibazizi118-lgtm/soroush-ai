import requests

URL = "https://splus.ir"

try:
    response = requests.get(URL, timeout=15)
    print("SoroushPlus status:", response.status_code)
    print("Connection test completed.")
except Exception as error:
    print("Connection error:", error)
