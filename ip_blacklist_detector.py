```python
from .base_detector import BaseDetector

class IPBlacklistDetector(BaseDetector):
    def __init__(self, blacklist):
        self.blacklist = set(blacklist)

    def detect(self, event):
        ip = event.get('ip')
        return ip in self.blacklist
```
