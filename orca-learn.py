from flask import Flask
app = Flask(__name__)

@app.route('/post/<string:app_token>', methods=['GET'])
def show_post(app_token):
    # show the post with the given id, the id is an integer
    return 'Token: ' % app_token