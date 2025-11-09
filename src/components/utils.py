import logging
from datetime import datetime

def get_current_datetime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def validate_form_data(data: dict, required_fields: list) -> bool:
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True