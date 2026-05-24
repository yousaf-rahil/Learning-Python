
import threading
import requests
from concurrent.futures import ThreadPoolExecutor
import time

def func(x):
    print(f"Sleeping time is {x}")
    time.sleep(x)

#       Normal execution

# time1 = time.perf_counter()
# func(4)
# func(5)
# func(2)
# time2 = time.perf_counter()

# print(time2 - time1)
#       Threading
# time1 = time.perf_counter()
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[5])
# t3 = threading.Thread(target=func, args=[2])

# t1.start()
# t2.start()
# t3.start()
# time2 = time.perf_counter()

# print("\n", time2 - time1)


def poolingdemo():
    with ThreadPoolExecutor() as executor:

                        # submit function
        # future = executor.submit(func, 3)
        # future = executor.submit(func, 5)
        # print(future.result())
        # print(future.result())
                        # Map function
        l = [1,2,3]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingdemo()

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
        t1 = threading.Thread(target=download, args=[url, i])

        t1.start()
        pros.append(t1)

for t in pros:
    t1.join()


