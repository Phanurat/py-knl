import time
def api_link():
    link_url = [
        'link_a',
        'link_b',
        'link_c',
        'link_d',
        'link_e'
    ]
    return link_url

link_url = api_link()

for url in link_url:
    print(url)
    time.sleep(1)
