```python
from .base_responder import BaseResponder
import subprocess

class BlockIPResponder(BaseResponder):
    def respond(self, event, detection_result):
        ip = event.get('ip')
        if detection_result:
            subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
```
