```python
from setuptools import setup, find_packages

setup(
    name='soar_framework',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML>=5.4',
    ],
    entry_points={
        'console_scripts': [
            'soar=main:main',
        ],
    }
)
```
