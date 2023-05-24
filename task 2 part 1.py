import requests
import os
import re
import time as t
def sanitize_filename(filename):
    # Remove invalid characters from the filename
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return sanitized_filename
def download_page(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    response = requests.get(url)
    data = response.json()
    title = data['title']
    sanitized_title = sanitize_filename(title)
    folder_path = r"C:\Users\MOHUL DUTTA\Desktop\synch download of json"  # Specify the folder path
    filename = os.path.join(folder_path, f"{sanitized_title}.json")
    with open(filename, 'w') as file:
        file.write(str(data))
def main():
    start=t.time()
    for comic_id in range(1, 201):
        download_page(comic_id)
    print(t.time()-start)
main()

