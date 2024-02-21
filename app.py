from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    print("Testing new Git branch")
    return f'Hello {name}'

if __name__=='__main__':
    app.run(debug=True)

