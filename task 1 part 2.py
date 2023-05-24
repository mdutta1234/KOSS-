import aiohttp
import asyncio
import time as t
import os
async def download_page(el):
    url = f"https://reqres.in/api/users?page{el}"	
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()			
            return data
async def main():
    arr = [1, 2, 3]
    tasks = []
    folder_path = r"C:\Users\MOHUL DUTTA\Desktop\json files download"  
    start=t.time()
    for el in arr:
        task = asyncio.create_task(download_page(el))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results, start=1):
        filename = os.path.join(folder_path, f"page_{i}.html")  # Specify the filename pattern with .html extension
        with open(filename, 'w') as file:
            file.write(result)
    print(t.time()-start)
asyncio.run(main())

