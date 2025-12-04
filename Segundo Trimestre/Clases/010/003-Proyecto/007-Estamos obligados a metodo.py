from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

@app.route("/api",methods=['POST'])
def api():
  codigo = request.data.decode("utf-8")
  resultado = eval(codigo, {"__builtins__": {}}, {})
  return str(resultado)

if __name__ == "__main__":
  app.run(debug=True)
