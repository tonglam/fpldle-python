from flask import Flask
from service import fpldleService

app = Flask(__name__)


@app.route('/fpldle/getServiceDate')
def get_daily_fpldle():
    return fpldleService.get_service_date()


@app.route('/fpldle/getDailyFpldle')
def get_daily_fpldle():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
