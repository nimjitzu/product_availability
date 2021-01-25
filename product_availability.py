"""Product availability script
1.  scrape product page
2.  search for "out of stock"
3.  if found, do nothing
4.  If not found, notify via email, sms"""

import urllib
import re

urls = ["https://www.repfitness.com/rep-ab-3100-fi-bench",
        "https://www.ikea.com/us/en/p/linnmon-adils-table-white-s69929643/"]

product_status = "Out of stock"
from urllib.request import urlopen

for i in urls:
    html_content = urlopen(i).read()
    html_content = html_content.decode('ISO-8859-1')

    matches = re.findall(product_status, html_content)

    if len(matches) == 0:
        print('Cant find string OUT OF STOCK on ', i)
    else:
        print('Found string OUT OF STOCK on ', i)
