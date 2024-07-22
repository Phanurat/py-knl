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

def loop_link(link_url):
    for url in link_url:
        print(url)
        time.sleep(1)
        for url in range(1):
            break

loop_link(link_url)