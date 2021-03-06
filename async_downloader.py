#!/usr/bin/env python  
 
#https://likegeeks.com/downloading-files-using-python/#Using-asyncio                                                                                                                                       
     
import asyncio 
import uuid 
import aiohttp 
import async_timeout
import sys,os
#https://stackoverflow.com/questions/18727347/how-to-extract-a-filename-from-a-url-append-a-word-to-it
import urllib.parse as urlparse
 
 
 
async def get_url(path, url, session):
 
    a = urlparse.urlparse(url)    
    file_name = os.path.basename(a.path)
    path += file_name
     
     
    async with async_timeout.timeout(120):        
        async with session.get(url) as response:            
            with open(path, 'wb') as fd:                
                async for data in response.content.iter_chunked(1024):                         
                    fd.write(data)
  
    return 'Successfully downloaded ' + file_name
  
async def main(path, urls):    
    async with aiohttp.ClientSession() as session:        
        tasks = [get_url(path, url, session) for url in urls] 
        return await asyncio.gather(*tasks)
  
 
 
 
if __name__ == '__main__':
    #use 1. argument is path in format "try/" the rest of arguments are links 
    #python3 async_downloader.py /home/... https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/170px-Tux.svg.png https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547_960_720.png
    path = sys.argv[1]
    urls = sys.argv[2:]
 
    #urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png', 'https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547_960_720.png'] 
    loop = asyncio.get_event_loop() 
    results = loop.run_until_complete(main(path, urls)) 
    print('\n'.join(results))
