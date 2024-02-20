from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/main",method=["GET","POST"])
def main():
  r = request.form.get("r")
  return(render_template("main.html",r=r))

@app.route("/image_gpt",method=["GET","POST"])
def image_gpt():
  r = request.form.get("r")
  return(render_template("image_gpt.html",r=r))


if __name__=="__main__":
         app.run()
