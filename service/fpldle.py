import constant
import interface
import utils
import redis
from datetime import datetime, timedelta
import json

redis_pool = redis.ConnectionPool(host=constant.HOST, port=constant.PORT, password=constant.PASSWD,
                                  decode_responses=True)
redis = redis.Redis(connection_pool=redis_pool)


def get_service_date():
    return datetime.today().__format__('%m%d')


def get_daily_fpldle():
    key = '::'.join([constant.REDIS_PREFIX, constant.DAILY])
    date = datetime.today().__format__('%Y%m%d')
    value = redis.hget(key, date)
    return utils.get_actual_result(value)


def get_fpldle_by_name(name):
    key = '::'.join([constant.REDIS_PREFIX, constant.DAILY])
    value_list = redis.hgetall(key)
    for value in value_list.values():
        value = utils.get_actual_result(value)
        fpldle_name = value['name']
        if fpldle_name == name:
            return value
    return {}


def get_wechat_access_token():
    return json.loads(interface.get_auth_token_info()).get('access_token')


def get_daily_result(open_id):
    data_list = []
    key = '::'.join([constant.REDIS_PREFIX, constant.RESULT, open_id])
    date = datetime.today().__format__('%Y%m%d')
    value = redis.hget(key, date)
    result = utils.get_actual_result(value)
    for key in result:
        data_list.append(result[key])
    return data_list


def get_date_verify_list(open_id, date):
    verify_list = []
    # daily result
    result_key = '::'.join([constant.REDIS_PREFIX, constant.RESULT, open_id])
    full_date = str(utils.fill_full_year()) + date
    value = redis.hget(result_key, full_date)
    result_list = utils.get_actual_result(value)
    # fpldle
    key = '::'.join([constant.REDIS_PREFIX, constant.DAILY])
    fpldle = utils.get_actual_result(redis.hget(key, full_date))['name']
    fpldle_list = list(fpldle)
    fpldle_dict = {}
    for i in range(len(fpldle_list)):
        fpldle_dict[i] = fpldle_list[i]
    # verify
    for key in result_list:
        round_list = (str.replace(result_list[key], ',', ''))
        for i in range(len(round_list)):
            result_letter = round_list[i]
            fpldle_letter = fpldle_dict[i]
            if result_letter == fpldle_letter:
                verify_list.append(str(constant.CORRECT))
            elif str.find(fpldle, result_letter) > 0:
                verify_list.append(str(constant.ORDER))
            else:
                verify_list.append(str(constant.WRONG))
    return verify_list


def get_player_picture(code):
    key = '::'.join([constant.REDIS_PREFIX, constant.PICTURE])
    value = redis.hget(key, code)
    return value


def get_history_fpldle():
    history_list = []
    today = datetime.today().__format__('%Y%m%d')
    key = '::'.join([constant.REDIS_PREFIX, constant.DAILY])
    value_list = redis.hgetall(key)
    for date, data in value_list.items():
        if date == today:
            continue
        fpldle = utils.get_actual_result(data)
        fpldle['date'] = date
        history_list.append(fpldle)
    history_list = sorted(history_list, key=lambda x: x['date'], reverse=True)
    return history_list


def get_record_list(open_id):
    record_list = []
    today = datetime.today().__format__('%Y%m%d')
    key = '::'.join([constant.REDIS_PREFIX, constant.RESULT, open_id])
    value_list = redis.hgetall(key)
    for date, value in value_list.items():
        if date == today:
            continue
        data = utils.get_actual_result(value)
        length = len(data)
        record = {
            'openId': open_id,
            'date': date,
            'result': str(data[str(length)]).replace(',', ''),
            'tryTimes': length,
            'solve': user_daily_solve(date, data)
        }
        record_list.append(record)
    record_list = sorted(record_list, key=lambda x: x['date'], reverse=True)
    return record_list


def user_daily_solve(date, data):
    solve = False
    # get daily fpldle
    key = '::'.join([constant.REDIS_PREFIX, constant.DAILY])
    value = redis.hget(key, date)
    fpldle = dict(utils.get_actual_result(value)).get('name')
    for value in dict(data).values():
        guess = str(value).replace(',', '')
        if guess == fpldle:
            solve = True
    return solve


def get_last_day_hit_rank():
    last_day_hit_dict = {}
    key = '::'.join([constant.REDIS_PREFIX, constant.USER_STATISTIC])
    yesterday = (datetime.today() - timedelta(days=1)).__format__('%Y%m%d')
    value_list = redis.hgetall(key)
    for open_id, data_dict in value_list.items():
        data_dict = data_dict.replace('"com.tong.fpl.domain.UserStatisticData",', '')
        user_data_dict = utils.get_actual_result(data_dict)
        for date, data_list in dict(user_data_dict).items():
            if date != yesterday:
                continue
            for data in data_list:
                last_day_hit_dict.setdefault(open_id, data)
    return None


def get_consecutive_hit_rank():
    return None


def get_average_hit_times_rank():
    return None


get_last_day_hit_rank()
