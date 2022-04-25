import json
import datetime


def get_actual_result(value):
    left = value.find(',{') + 1
    right = value.rfind(']')
    return json.loads(value[left:right])


def fill_full_year():
    return datetime.date.today().year
