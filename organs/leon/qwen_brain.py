from http import HTTPStatus
import dashscope
from config.qwen_config import QwenConfig

class QwenBrain:
    def __init__(self):
        dashscope.api_key = QwenConfig.API_KEY

    def generate_response(self, prompt: str):
        # Updated to current DashScope API syntax
        response = dashscope.Generation.call(
            model=QwenConfig.MODEL,
            prompt=prompt
        )
        if response.status_code == HTTPStatus.OK:
            return response.output.text
        else:
            return f\"Error: {response.code} - {response.message}\"
