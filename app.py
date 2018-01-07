from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/jz2896', methods=['GET'])
def jz2896():
    return render_template('janet.html', src='static/windows.jpg')

if __name__ == '__main__':
    app.debug = True
    app.run()
