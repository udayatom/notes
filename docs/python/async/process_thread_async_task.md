# Python Concurrency Hierarchy: Process vs Thread vs Async Task

## Overview

Python has three common concurrency concepts:

1. **Process**
2. **Thread**
3. **Async Task (Coroutine)**

They work at different levels.

---

# Hierarchy

```text
Computer
│
├── CPU Cores
│
└── Process
    │
    ├── Memory Space
    │
    ├── Thread 1
    │   │
    │   └── Event Loop
    │       │
    │       ├── Async Task 1
    │       ├── Async Task 2
    │       └── Async Task 3
    │
    ├── Thread 2
    │
    └── Thread 3
```

---

# 1. Process

## Definition

A process is an independent running program.

Example:

```python
from multiprocessing import Process


def work():
    print("Process running")


p = Process(target=work)

p.start()
```

Structure:

```text
Operating System

Process 1
│
├── Memory
├── Thread 1
└── Thread 2


Process 2
│
├── Memory
├── Thread 1
└── Thread 2
```

## Characteristics

* Has its own memory
* Isolated from other processes
* Can run on different CPU cores
* More expensive to create
* Best for CPU-heavy work

## Examples

Good use cases:

* Video processing
* Image processing
* Machine learning calculations
* Large mathematical operations

Example:

```text
CPU Core 1 → Process 1
CPU Core 2 → Process 2
CPU Core 3 → Process 3
CPU Core 4 → Process 4
```

---

# 2. Thread

## Definition

A thread is a smaller execution unit inside a process.

Example:

```python
import threading


def work():
    print("Thread running")


t = threading.Thread(target=work)

t.start()
```

Structure:

```text
Process

├── Thread 1
├── Thread 2
└── Thread 3
```

## Characteristics

* Shares process memory
* Managed by operating system
* Less expensive than processes
* Multiple threads can exist inside one process

Example:

```text
Web Application Process

Thread 1 → Handle User A
Thread 2 → Handle User B
Thread 3 → Handle User C
```

---

# 3. Async Task (Coroutine)

## Definition

An async task is a lightweight task managed by an event loop.

Example:

```python
async def get_data():
    result = await api_call()
    return result
```

Structure:

```text
Process

└── Thread

    └── Event Loop

        ├── Async Task 1
        ├── Async Task 2
        ├── Async Task 3
        └── Async Task 10000
```

## Characteristics

* Usually runs in one thread
* Managed by event loop
* Switching happens at `await`
* Very lightweight
* Best for I/O operations

Example:

```text
One Thread

Event Loop

Task 1 → waiting for API
Task 2 → waiting for database
Task 3 → waiting for file
```

---

# Complete Relationship

```text
                 PROCESS
                    |
        -------------------------
        |                       |
     THREAD                  THREAD
        |
        |
   EVENT LOOP
        |
 -------------------
 |        |          |
Task 1  Task 2    Task 3
```

---

# API Request Example

## Option 1: Multiprocessing

```text
4 CPU cores

Process 1 → API calls
Process 2 → API calls
Process 3 → API calls
Process 4 → API calls
```

Usually not required for API waiting.

---

## Option 2: Multithreading

```text
One Process

Thread 1 → API call
Thread 2 → API call
Thread 3 → API call
...
Thread 100
```

Good when using blocking libraries.

Example:

```python
ThreadPoolExecutor(max_workers=10)
```

Means:

```text
Maximum 10 threads running
```

---

## Option 3: Asyncio

```text
One Process

One Thread

Event Loop

Task 1 → API waiting
Task 2 → API waiting
Task 3 → API waiting
...
Task 10000
```

Good for many network requests.

Example:

```python
asyncio.Semaphore(100)
```

Means:

```text
Maximum 100 async tasks active
```

---

# Thread vs Async Task

|                 | Thread             | Async Task         |
| --------------- | ------------------ | ------------------ |
| Managed by      | Operating System   | Event Loop         |
| Runs inside     | Process            | Thread             |
| Switching       | OS decides         | `await` decides    |
| Memory          | Higher             | Lower              |
| Best for        | Blocking work      | I/O waiting        |
| Number possible | Hundreds/thousands | Thousands/millions |

---

# Process vs Thread

|                 | Process        | Thread            |
| --------------- | -------------- | ----------------- |
| Memory          | Separate       | Shared            |
| Creation cost   | High           | Lower             |
| CPU parallelism | Yes            | Limited in Python |
| Communication   | More difficult | Easier            |
| Best for        | CPU work       | I/O work          |

---

# Choosing the Right Tool

| Scenario               | Use             |
| ---------------------- | --------------- |
| Many API calls         | asyncio         |
| WebSocket connections  | asyncio         |
| Database async queries | asyncio         |
| Blocking API/library   | Threading       |
| Background worker      | Threading       |
| CPU calculations       | Multiprocessing |
| Video encoding         | Multiprocessing |

---

# Simple Mental Model

```text
Process
=
Company


Thread
=
Employee


Async Task
=
Small jobs handled by one employee
```

Meaning:

* Process → separate resource environment
* Thread → worker inside the process
* Async Task → lightweight work managed by a thread's event loop

---

# Key Points

1. A process can contain multiple threads.
2. A thread can run an async event loop.
3. Async tasks run inside the event loop.
4. Async does not create new threads.
5. Threads do not automatically use multiple CPU cores in Python.
6. Multiprocessing is used for CPU-heavy work.
7. Asyncio is mainly for high-volume I/O operations.
