import aiohttp
import asyncio
import os
import time as t
import re
def sanitize_filename(filename):
    # Remove invalid characters from the filename
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return sanitized_filename
async def download_page(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            title = data['title']
            sanitized_title = sanitize_filename(title)
            folder_path = r"C:\Users\MOHUL DUTTA\Desktop\json files download"  # Use raw string or double backslashes
            filename = os.path.join(folder_path, f"{sanitized_title}.json")
            with open(filename, 'w') as file:
                file.write(str(data))
async def main():
    tasks = []
    start = t.time()
    for comic_id in range(1, 201):
        task = asyncio.create_task(download_page(comic_id))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(t.time() - start)
asyncio.run(main())
