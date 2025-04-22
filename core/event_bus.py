```python
import queue
import threading

class EventBus:
    def __init__(self):
        self.queue = queue.Queue()

    def publish(self, event):
        self.queue.put(event)

    def subscribe(self):
        while True:
            yield self.queue.get()
```
