import re
from datetime import datetime


def validate_email(email: str) -> bool:
    pattern = re.compile("\w[\w\.-]*@\w[\w\.-]+\.\w+")
    return bool(pattern.search(email))


def validate_phone(phone: str) -> bool:
    pattern = re.compile('(^8|7|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))')
    return bool(pattern.search(phone))


def validate_date(date_text: str) -> bool:
    formats = ['%Y-%m-%d', '%d-%m-%Y']
    for date_format in formats:
        try:
            return bool(datetime.strptime(date_text, date_format))
        except ValueError:
            pass
    return False


def validate_text(text):
    return True
