from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "You touch my tralala"

@app.route("/order-animation")
def order_animation():
  return render_template(
    "order.html",
    invitation="Welocme")

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
