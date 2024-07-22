# main.py

from api.__api_link__ import api_link

test_link = api_link()

for i in test_link:
    print(f"Links ==> {i}")
