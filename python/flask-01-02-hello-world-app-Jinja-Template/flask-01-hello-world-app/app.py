from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>You are gonna be a good DevOps and AWS Solution Architect</h1>"

@app.route("/second")
def second():
    return "This is the second page"

@app.route("/third/alpi ")
def third():
    return "This is the subpath of third path"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__=="__main__":
    app.run(debug=True)
    