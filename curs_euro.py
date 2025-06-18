import requests
from bs4 import BeautifulSoup
import re

url = "https://www.cursbnr.ro/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Găsire text exact "1 EURO =" folosind string (fără DeprecationWarning)
line = soup.find(string=lambda t: t and "1 EURO =" in t)
if not line:
    raise RuntimeError("Nu am găsit cursul EUR pe pagina principală")

# Extragere numerică: 5.0325
match = re.search(r"1 EURO =\s*([0-9]+\.[0-9]+)", line)
if not match:
    raise RuntimeError("Format neconform al liniei de curs")
eur_rate = match.group(1)
date_line = soup.find(string=lambda t: t and "comunicat în" in t)
date = date_line.split("comunicat în")[-1].strip() if date_line else "data necunoscută"
print(f"{date}: 1 EURO = {eur_rate} Lei")

