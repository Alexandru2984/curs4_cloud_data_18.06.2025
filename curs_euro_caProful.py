import sys
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



response = requests.get("https://www.cursbnr.ro")
print(response.text)

with open("bnr.ro.html", "w") as fwriter:
    fwriter.write(response)

