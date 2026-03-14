from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

BALANCE_FILE = "balance.txt"

def get_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            content = f.read()
            if content == "":
                return 0
            return int(content)
    return 0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

@app.route("/deposit", methods=["POST"])
def deposit():
    amount = int(request.json["amount"])
    balance = get_balance()
    balance += amount
    save_balance(balance)
    return jsonify({"message": "Deposited Rs." + str(amount), "balance": balance})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    amount = int(request.json["amount"])
    balance = get_balance()
    if amount > balance:
        return jsonify({"message": "Insufficient balance!", "balance": balance})
    balance -= amount
    save_balance(balance)
    return jsonify({"message": "Withdrew Rs." + str(amount), "balance": balance})

@app.route("/balance", methods=["GET"])
def check_balance():
    balance = get_balance()
    return jsonify({"balance": balance})

if __name__ == "__main__":
    app.run(debug=True)