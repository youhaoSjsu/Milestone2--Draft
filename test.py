import flask


app =flask.Flask(__name__)
@app.route("/")
def hello():
    return flask.render_template('test.html')

if __name__ == '__main__':
    app.run()