import redisService
import datetime

# redis_key
REDIS_PREFIX = 'Fpldle'
DICTIONARY = 'Dictionary'
DAILY = 'Daily'
RESULT = 'Result'
USER_STATISTIC = 'UserStatistic'
DATE_STATISTIC = 'DateStatistic'
USER = 'User'
USER_RELATION = 'UserRelation'
PICTURE = 'Picture'
# wechat_app
APP_ID = 'wxb105fb69e8d9a10e'
SECRET_ID = '66544f4be5cfae2637c3ac6c999d1f4a'


def get_service_date():
    return datetime.date.today().__format__('%m%d')


def get_daily_fpldle():
    key = '::'.join([REDIS_PREFIX, DAILY])
    return redisService.get_hash_value(key)
