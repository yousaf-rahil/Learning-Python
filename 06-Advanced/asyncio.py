import asyncio

async def func1():
    for i in range(200):
        print(i)
    print("Done")
    await asyncio.sleep(3)
async def func2():
    for i in range(200):
        print(i)
    print("Done")
    await asyncio.sleep(3)
async def func3():
    for i in range(200):
        print(i)
    print("Done")
    await asyncio.sleep(3)

async def main():
    await func1(),
    await func2(),
    await func3()
    return 3

# l = await asyncio.gather(
#     func1(),
#     func2(),
#     func3(),
# )

# print(l)
asyncio.run(main())
