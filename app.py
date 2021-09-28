from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Learning Flask, first commit!'

if __name__=='__main__':
    app.run(debug=True, port=3333)