# Threading
GIL (Global Interpreter Lock) doesn't allow more than one insturcion run at a time with threading.But it can switch between them by time interval.

GIL prevents the case when two or more threads try to modify the same structure at the same time, which leads to unexpected behaviour.
Threading functionality is implemented in operating system, and not in python iteslef

Since python3.2, threads are changes in an interval of 5 milliseconds
The interval can be adjusted `sys.setswitchinterval`


In earlier version GIL were released after 100 virtual instructions

``` Python
x = threading.Thread(target=thread_function, args=(1,), daemon=True)
```

## Thead types
- *Treads* are awaited (join) before program finishes by default
- *Daemon threads* are not awaited when the program ends. They run in the background.

## Join
To tell one thread to wait for another thread, we use `thr.join()`


## ThreadPoolExecutor
``` Python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
	executor.map(func, args)

```