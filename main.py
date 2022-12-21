import asyncio
import random
import vdworker
print_process = True
count_acync_get = 0
count_acync_write = 0
requests = 1000
values = 1000000


async def async_make_read():
    user = random.randint(1, values)
    result = await vdworker.get_user_attribute(user, "test")
    global count_acync_get
    count_acync_get += 1
    if print_process is True:
        print(f"async_read - {result}")
        print(count_acync_get+count_acync_write)


async def async_make_write():
    user = random.randint(1, values)
    data = random.randint(1, values)
    result = await vdworker.write_user_attribute(user, "test", data)
    global count_acync_write
    count_acync_write += 1
    if print_process is True:
        print(f"async_write - {result}")
        print(count_acync_get + count_acync_write)

async def async_main():
    for x in range(requests):
        loop.create_task(async_make_read())
        loop.create_task(async_make_write())

loop = asyncio.new_event_loop()
loop.run_until_complete(async_main())


print(f"async writes: {count_acync_get}")
print(f"async reads: {count_acync_write}")