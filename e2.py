import requests
from bs4 import BeautifulSoup as bs

for line in open ("ELECTION_ID"):
    part = line.split()
    year=part[0]
    eleID = line.split(" ")[1].strip()
    url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(eleID)
    resp = requests.get(url)
    soup = bs (resp.content, "html.parser")
    name = year + ".csv"
    with open(name, "w") as out:
        out.write(resp.text)
