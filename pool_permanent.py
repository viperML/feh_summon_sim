import urllib.request
import re
from bs4 import BeautifulSoup
import numpy as np

url = 'https://feheroes.gamepedia.com/Summonable_Heroes'
print("Connecting to", url)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

page_bs = soup.get_text()

# Rarity543The above table, in numbers by color only.Rarity543

rarities = re.findall("^Rarity543The.*", page_bs, re.MULTILINE)
rarities = rarities[0]
print("String obtained: ", rarities)
print("Parsing data...")

r = [ [ int(rarities[65:67]) + int(rarities[67:69]), int(rarities[75:77]) + int(rarities[77:79]), int( rarities[86:88]) + int(rarities[88:90]), int( rarities[101:103]) + int(rarities[103:105])],
    [ int(rarities[63:65]), int(rarities[73:75]), int(rarities[84:86]), int(rarities[99:101])] ]

np.save('pool_permanent.npy', r)



print("pool_permanent.csv generated succesfully")