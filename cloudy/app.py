import json
from flask import Flask, Response

from cloudy.cloud_info import lookup_cloud_info
from cloudy.cloud_processor import determine_cloud_probabilities


app = Flask(__name__)


@app.route('/health')
def health_check():
    return 'Health ok!'


@app.route('/cloud/info', defaults={'cloud_name': 'all_clouds'})
@app.route('/cloud/info/<cloud_name>')
def get_cloud_info(cloud_name):
    info = json.dumps(lookup_cloud_info(cloud_name))
    resp = Response(info)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/cloud/prob/<zipcode>')
def get_cloud_probabilities(zipcode):
    probabilities = json.dumps(determine_cloud_probabilities(zipcode))
    resp = Response(probabilities)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run()
