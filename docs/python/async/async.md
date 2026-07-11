# Python Async Programming Reference

## 1. What is Async Programming?

Async programming allows a program to start a slow operation (usually I/O) and continue doing other work while waiting.

Common use cases:

* HTTP/API requests
* Database queries
* File operations
* WebSocket connections
* Message queues

Async programming is mainly about **concurrency**, not making CPU calculations faster.

---

# 2. Synchronous vs Asynchronous

## Synchronous

Operations run one after another.

```python
data = get_data()
process(data)
```

Flow:

```
get_data()
    |
    | wait
    |
process(data)
```

The program blocks until `get_data()` completes.

---

## Asynchronous

Operations can pause while waiting.

```python
data = await get_data()
process(data)
```

Flow:

```
get_data()
    |
    | waiting
    |
other tasks run
    |
get_data finishes
    |
continue
```

---

# 3. async def

An async function is created using `async def`.

```python
async def get_data():
    return "hello"
```

Calling it does not execute immediately.

```python
result = get_data()

print(result)
```

Output:

```
<coroutine object get_data>
```

It returns a coroutine object.

---

# 4. Coroutine

A coroutine is a function that can pause and resume.

Example:

```python
import asyncio

async def task():
    print("Start")

    await asyncio.sleep(3)

    print("Finished")


asyncio.run(task())
```

Execution:

```
task starts
 |
print Start
 |
pause for 3 seconds
 |
event loop handles other work
 |
resume task
 |
print Finished
```

---

# 5. await

`await` waits for an async operation to complete.

Example:

```python
async def main():

    result = await get_data()

    print(result)
```

Important:

`await` pauses only the current coroutine.

It does not block the whole event loop.

---

# 6. Event Loop

The event loop manages async tasks.

Example:

```
Event Loop

Task A
 |
 | waiting for network
 |
 v

Task B
 |
 | running
 |
 v

Task C
 |
 | waiting
```

When one task waits, another task can run.

---

# 7. asyncio.run()

Starts the event loop.

Example:

```python
async def main():
    await task()


asyncio.run(main())
```

Usually used once at the program entry point.

---

# 8. Creating Tasks

## Sequential

```python
await task1()
await task2()
```

Execution:

```
task1 ------>
            task2 ------>
```

Total time:

```
task1 time + task2 time
```

---

## Concurrent Tasks

```python
task1 = asyncio.create_task(job1())
task2 = asyncio.create_task(job2())

await task1
await task2
```

Execution:

```
task1 ------>
task2 ------>
```

Tasks run concurrently.

---

# 9. asyncio.gather()

Runs multiple async operations and waits for results.

Example:

```python
results = await asyncio.gather(
    task1(),
    task2()
)
```

Equivalent to:

```python
tasks = [
    task1(),
    task2()
]

results = await asyncio.gather(*tasks)
```

---

# 10. The * Operator

`*` is argument unpacking.

Example:

```python
values = [10, 20, 30]

test(*values)
```

Equivalent:

```python
test(10, 20, 30)
```

For asyncio:

```python
tasks = [
    job(1),
    job(2),
    job(3)
]

await asyncio.gather(*tasks)
```

means:

```python
await asyncio.gather(
    job(1),
    job(2),
    job(3)
)
```

---

# 11. API Example: 1000 Requests

Problem:

```
GET /getinfo/1
GET /getinfo/2
...
GET /getinfo/1000
```

## Sequential

```python
for i in range(1,1001):
    requests.get(url)
```

Slow because every request waits.

---

## Async Version

Install:

```bash
pip install aiohttp
```

Example:

```python
import asyncio
import aiohttp


async def get_info(session, id):

    url = f"https://api.example.com/getinfo/{id}"

    async with session.get(url) as response:
        return await response.json()


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = [
            get_info(session, i)
            for i in range(1,1001)
        ]

        results = await asyncio.gather(*tasks)

        print(results)


asyncio.run(main())
```

---

# 12. Limiting Concurrent Requests

Sending 1000 requests at once may overload a server.

Use Semaphore:

```python
semaphore = asyncio.Semaphore(50)
```

Example:

```python
async def get_info(session, id):

    async with semaphore:

        async with session.get(url) as response:
            return await response.json()
```

Now:

```
Maximum active requests = 50
```

---

# 13. Async vs Threading

## Async

```
One thread

Event Loop
 |
 +-- Task 1
 +-- Task 2
 +-- Task 3
 +-- Task 1000
```

Best for:

* Network
* API calls
* Database waiting

---

## Threading

```
Process

Thread 1
Thread 2
Thread 3
```

Each thread executes independently.

Best for:

* Blocking libraries
* Background work
* Legacy code

---

# 14. Async + Threading Together

Possible architecture:

```
Process

Thread
 |
 asyncio event loop
 |
 +-- async tasks
 |
 +-- thread pool
       |
       +-- blocking functions
```

Example:

```python
result = await asyncio.to_thread(
    blocking_function
)
```

---

# 15. Async vs Multiprocessing

For CPU-heavy work:

```
CPU Core 1
 |
 Process 1


CPU Core 2
 |
 Process 2
```

Use:

* multiprocessing
* worker processes

Async does not improve CPU calculations.

---

# 16. Blocking Code Problem

Bad:

```python
async def task():

    time.sleep(5)
```

`time.sleep()` blocks the event loop.

Correct:

```python
async def task():

    await asyncio.sleep(5)
```

---

# 17. Mental Model

```
async def
    |
    v
Coroutine
    |
    v
await
    |
    v
Event Loop
    |
    v
Pause / Resume
    |
    v
Result
```

---

# Quick Rules

| Situation            | Use               |
| -------------------- | ----------------- |
| Many API calls       | asyncio           |
| Database waiting     | asyncio           |
| Web server requests  | asyncio           |
| Blocking library     | threading         |
| CPU calculation      | multiprocessing   |
| Mix async + blocking | asyncio + threads |

---

# Key Concepts to Remember

1. `async def` creates coroutines
2. Coroutine does not run until awaited or scheduled
3. `await` pauses only the current coroutine
4. Event loop manages async execution
5. `create_task()` starts concurrent work
6. `gather()` waits for multiple tasks
7. `*tasks` unpacks a list into arguments
8. Async is for I/O concurrency, not CPU speed
