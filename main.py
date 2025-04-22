```python
import yaml
from core.event_bus import EventBus
from core.engine import Engine
from detectors.ip_blacklist_detector import IPBlacklistDetector
from responders.block_ip_responder import BlockIPResponder

if __name__ == '__main__':
    config = yaml.safe_load(open('config.yaml'))
    bus = EventBus()
    detectors = [IPBlacklistDetector(config['blacklist'])]
    responders = [BlockIPResponder()]
    engine = Engine(detectors, responders, bus)

    # 启动引擎线程
    threading.Thread(target=engine.start, daemon=True).start()

    # 模拟事件输入
    for ip in ['192.168.1.100', '10.0.0.5']:
        bus.publish({'ip': ip, 'timestamp': '2025-04-22T10:00:00Z'})
```
