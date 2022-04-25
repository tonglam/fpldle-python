from flask import Flask, request, Response, jsonify
from service import fpldle

app = Flask(__name__)


@app.route('/python/fpldle//getServiceDate')
def get_service_date():
    return Response(fpldle.get_service_date(), mimetype='text/plain')


@app.route('/python/fpldle/getDailyFpldle')
def get_daily_fpldle():
    data = fpldle.get_daily_fpldle()
    return jsonify(data)


@app.route('/python/fpldle/getFpldleByName')
def get_fpldle_by_name():
    name = request.args.get('name')
    return fpldle.get_fpldle_by_name(name)


@app.route('/python/fpldle/getWechatAccessToken')
def get_wechat_access_token():
    return Response(fpldle.get_wechat_access_token(), mimetype='text/plain')


@app.route('/python/fpldle/getDailyResult')
def get_daily_result():
    open_id = request.args.get('openId')
    return jsonify(fpldle.get_daily_result(open_id))


@app.route('/python/fpldle/getDateVerifyList')
def get_date_verify_list():
    open_id = request.args.get('openId')
    date = request.args.get('date')
    return jsonify(fpldle.get_date_verify_list(open_id, date))


@app.route('/python/fpldle/getPlayerPicture')
def get_player_picture():
    code = request.args.get('code')
    return Response(fpldle.get_player_picture(code), mimetype='text/plain')


@app.route('/python/fpldle/getHistoryFpldle')
def get_history_fpldle():
    return jsonify(fpldle.get_history_fpldle())


@app.route('/python/fpldle/getRecordList')
def get_record_list():
    open_id = request.args.get('openId')
    return jsonify(fpldle.get_record_list(open_id))


@app.route('/python/fpldle/getLastDayHitRank')
def get_last_day_hit_rank():
    return jsonify(fpldle.get_last_day_hit_rank())


@app.route('/python/fpldle/getConsecutiveHitRank')
def get_consecutive_hit_rank():
    return jsonify(fpldle.get_consecutive_hit_rank())


@app.route('/python/fpldle/getAverageHitTimesRank')
def get_average_hit_times_rank():
    return jsonify(fpldle.get_average_hit_times_rank())


if __name__ == '__main__':
    app.run()
