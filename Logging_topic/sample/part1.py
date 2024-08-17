import logging

# Настройка базового логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Запись различных уровней сообщений в лог
logging.debug("Это сообщение для отладки")
logging.info("Информационное сообщение")
logging.warning("Предупреждение")
logging.error("Ошибка")
logging.critical("Критическая ошибка")


import logging

# Настройка логгирования в файл
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

logging.info('Это лог-сообщение будет записано в файл')
