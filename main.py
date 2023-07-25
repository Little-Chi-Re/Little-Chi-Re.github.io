from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    return '?'


if __name__ == '__main__':
    # print(scanDir(comicsList()[0]))
    app.run(host="0.0.0.0", debug=True)
