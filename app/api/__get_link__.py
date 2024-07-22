import requests

def get_random_link():
    global selected_link
    # URL ของ Google Apps Script API
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"

    # ส่งคำขอ GET ไปยัง API
    response = requests.get(api_link_url)

    # ตรวจสอบสถานะคำขอ
    if response.status_code == 200:
        # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
        data = response.json()

        # สร้าง list ของ comment
        selected_link = [item['link'] for item in data['data']]
        
        #print("Fetched random links.")
        return selected_link

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None