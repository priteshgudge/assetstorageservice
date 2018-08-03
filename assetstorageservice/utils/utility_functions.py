from datetime import datetime
import pytz
import time
import os


def current_time():
    return datetime.now(pytz.timezone('Asia/Kolkata'))


def get_utc_ms_time(date):
    try:
        return int(time.mktime(date.timetuple())) * 1000
    except Exception as e:
        return None


def get_str_datetime(date):
    try:
        return date.strftime('%d %b %Y %H:%M')
    except Exception as e:
        return None

def utc_ms_to_date(utc_ts):
    try:
        date_obj = datetime.fromtimestamp(float(utc_ts) / 1000.0)
    except Exception as e:
        date_obj = None

    return date_obj

def get_service_env():
    return os.environ['ENVIRONMENT']


def default_date_now():
    return datetime.now(pytz.timezone('Asia/Kolkata'))
