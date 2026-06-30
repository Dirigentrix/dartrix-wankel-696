import os

class QwenConfig:
    API_KEY = os.getenv("DASHSCOPE_API_KEY", "your-api-key-here")
    MODEL = "qwen-max"
