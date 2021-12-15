from flask import *
import json, time
from flask_cors import CORS

app = Flask(__name__)


CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})

@app.route('/', methods=['GET'])
def website():
    data_set = {'test_number': '12', 'test_zahl': '25'}
    json_output = json.dumps(data_set)

    return json_output


if __name__ == '__main__':
    app.run(port=2000)