import logging

logging.basicConfig(level=logging.DEBUG, filename='my_logging.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding = 'utf-8', filemode='w')

logging.debug('Дебаг')
logging.info('инфо')
logging.warning('Варнинг')
logging.error('Эррор')
logging.critical('Критикал')

try:
    10 / 0
except Exception as e:
    logging.exception(e)

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Давай протестируем файл на данные!')