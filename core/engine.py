```python
import threading

class Engine:
    def __init__(self, detectors, responders, event_bus):
        self.detectors = detectors
        self.responders = responders
        self.bus = event_bus

    def start(self):
        for event in self.bus.subscribe():
            for detector in self.detectors:
                result = detector.detect(event)
                if result:
                    for responder in self.responders:
                        responder.respond(event, result)
```
