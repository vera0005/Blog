from apiflask import APIFlask

app=APIFlask(__name__)


@app.route('/')
def hello_world():
    return 'hello_world'


if __name__ == '__main__':
    app.run()
