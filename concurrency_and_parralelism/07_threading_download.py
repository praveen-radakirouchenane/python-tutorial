import threading
import time
import requests

def download_image(url):
    print(f"Your downloadble url is {url}")
    image = requests.get(url)
    print(f"Your download for this url: {url} is completed, and the size of the content is {len(image.content)} bytes")

start = time.time()

threads = []

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

for url in urls:
    t=threading.Thread(target=download_image, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end=time.time()

print(f"Total time taken to download all the images is {end-start:.2f} seconds")