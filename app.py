from flask import Flask, render_template, request

from  AltruistsEgoists import AESim

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

def network():
    return render_template("network.html")

@app.route("/network.html", methods=["POST", "GET"])
def result():
    output = request.form.to_dict()
    number = output["num"]
    print(type(number), " ", int(number))
    AESim(int(number),.55,.25,True).runSim(50,True)
    return render_template("templates/network.html", number=number)

if __name__ == '__main__':
    app.run(debug=True,port=5001)