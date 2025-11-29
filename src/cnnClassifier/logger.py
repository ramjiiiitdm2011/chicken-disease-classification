import logging
import os
from datetime import datetime

# Create logs folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="[%(asctime)s]: %(levelname)s: %(message)s",
)

logger = logging.getLogger("cnnClassifierLogger")
