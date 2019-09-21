import urllib.request
import re
from bs4 import BeautifulSoup
import csv

page = urllib.request.urlopen('https://feheroes.gamepedia.com/Summonable_Heroes')
soup = BeautifulSoup(page, "html.parser")

page_bs = soup.get_text()

# Rarity543The above table, in numbers by color only.Rarity543

rarities = re.findall("^Rarity543The.*", page_bs, re.MULTILINE)
rarities = rarities[0]
print("String obtained: ", rarities)

with open('permanent_pool.csv', 'wt', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["#Red,Blue,Green,Gray"])
    csv_writer.writerow( [ str( int( rarities[65:67]) + int(rarities[67:69] )), str( int( rarities[75:77]) + int(rarities[77:79] )), str( int( rarities[86:88]) + int(rarities[88:90] )), str( int( rarities[101:103]) + int(rarities[103:105] )) ] )
    csv_writer.writerow( [rarities[63:65], rarities[73:75], rarities[84:86], rarities[99:101]])
