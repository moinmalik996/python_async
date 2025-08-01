import os
import threading

print(f"The current process is main process with id {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread()

print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread is {thread_name}')