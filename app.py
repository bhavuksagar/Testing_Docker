from flask import Flask


app=Flask(__name__)

@app.route('/')
def welcome():
    print("Hey Print")
    return "Hello, It's a flask app. Hey this is main root."


@app.route("/index")
#with html tag
def index():
    return "<html><h1>Hey from Index</h1></html>"


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)