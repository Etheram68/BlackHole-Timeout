import os, sys
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)

LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
logger.setLevel(LOGLEVEL)

log_filename = "./logs/output.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
handler_file = RotatingFileHandler(log_filename, maxBytes=5*2**20, backupCount=5)
handler_file.setLevel(LOGLEVEL)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(LOGLEVEL)

formatter = logging.Formatter(' %(levelname)s %(filename)s:%(lineno)d - %(message)s')

handler.setFormatter(formatter)
handler_file.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(handler_file)
# logger.addHandler(handler_db)
