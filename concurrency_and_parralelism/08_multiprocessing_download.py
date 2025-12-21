from multiprocessing import Process
import requests
import time

def download_image(url):
    print(f"Your downloadble url is {url}")
    image = requests.get(url)
    print(f"Your download for this url: {url} is completed, and the size of the content is {len(image.content)} bytes")

if __name__ == "__main__":
    start = time.time()

    process = []

    urls = [
        "https://httpbin.org/image/jpeg",
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg"
    ]

    for url in urls:
        p = Process(target=download_image, args=(url,))
        p.start()
        process.append(p)

    for p in process:
        p.join()

    end=time.time()

    print(f"Total time taken to download all the images is {end-start:.2f} seconds")