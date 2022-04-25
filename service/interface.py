import constant
import requests


def get_auth_token_info():
    response = requests.get(constant.TOKEN, params={'grant_type': 'client_credential', 'appid': constant.APP_ID,
                                                    'secret': constant.SECRET_ID})
    return response.text

