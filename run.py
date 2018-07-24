"""Here my api starts running"""

from app import app

@app.route('/', methods=['GET'])
def index():
    return ('Welcome to  my-diary  API. \
     Test the endpoints with postman')


if __name__ == '__main__':

    app.run(port=5000, debug=True)
