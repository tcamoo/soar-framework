```python
class BaseDetector:
    """
    抽象检测器基类，定义接口供具体检测器实现。
    """
    def detect(self, event):
        """接收事件并返回检测结果"""
        raise NotImplementedError
```
