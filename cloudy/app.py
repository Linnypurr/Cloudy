from flask import Flask

from cloudy.cloud_info import lookup_cloud_info
from cloudy.cloud_processor import determine_cloud_probabilities


app = Flask(__name__)


@app.route('/health')
def health_check():
    return 'Health ok!'


@app.route('/cloud/info', defaults={'cloud_name': 'all_clouds'})
@app.route('/cloud/info/<cloud_name>')
def get_cloud_info(cloud_name):
    return lookup_cloud_info(cloud_name)


@app.route('/cloud/prob/<zipcode>')
def get_cloud_probabilities(zipcode):
    return determine_cloud_probabilities(zipcode)

if __name__ == '__main__':
    app.run()
