import logging
import asyncio
from openai import AsyncOpenAI
from config import AI_TOKEN

# Настройка логирования
logger = logging.getLogger(__name__)

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1/chat/completions",
  api_key=AI_TOKEN,
)

async def ai_generate(text: str):
    try:
        logger.info(f"Отправка запроса к модели с текстом: {text}")
        completion = await client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        logger.info("Ответ от модели получен")
        return completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Ошибка при запросе к модели: {e}")
        return "Произошла ошибка при генерации ответа. Пожалуйста, попробуйте позже."
