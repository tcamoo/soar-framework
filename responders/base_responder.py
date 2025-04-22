```python
class BaseResponder:
    """
    抽象响应器基类，定义接口供具体响应器实现。
    """
    def respond(self, event, detection_result):
        """执行响应动作"""
        raise NotImplementedError
```
