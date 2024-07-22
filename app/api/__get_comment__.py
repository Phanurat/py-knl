import requests

def get_random_comment():
    global selected_comment
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]

        # ค่าเดิมจากสุ่มรอบแรง
        # selected_comment = random.choice(comments)

        # Try Test
        selected_comment = comments
        #print("Fetched random comments.")
        return selected_comment

    else:
        print(f"Error Status Code: {response.status_code}")
        return None