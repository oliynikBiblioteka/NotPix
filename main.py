import asyncio
from contextlib import suppress
from bot.utils import logger
from bot.utils.launcher import process
import requests

async def main():
    try:
        external_ip = requests.get('https://api.ipify.org').text
        print(f"Ваша зовнішня IP-адреса: {external_ip}")
        await asyncio.wait_for(process(), timeout=150.0)  # Тайм-аут 10 секунд
    except asyncio.TimeoutError:
        logger.warning("<r>Bot stopped due to timeout...</r>")
        # Можна коректно завершити роботу без виклику sys.exit(1)
    except Exception as e:
        logger.error(f"<r>Unexpected error: {e}</r>")
        sys.exit(1)  # Завершуємо через помилку


if __name__ == '__main__':
    try:
        with suppress(KeyboardInterrupt):
            asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("<r>Bot stopped by user...</r>")
        sys.exit(2)
