
import multiprocessing
import requests



def download(url, output):
    print(f"File {output} starting download")
    response = requests.get(url)
    open(f"{output}.jpg", "wb").write(response.content)
    print(f"File {output} downloaded")


url = "https://picsum.photos/2000/3000"

pros = []
if __name__ == '__main__':
    for i in range(5):
        # download(url, i)
        p = multiprocessing.Process(target=download, args=[url, i])

        p.start()
        pros.append(p)


for p in pros:
    p.join()

