from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variables globales para almacenar votos
votes = {"option1": 0, "option2": 0}

@app.route("/")
def index():
    return render_template("index.html", votes=votes)

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    option = data.get("option")
    if option in votes:
        votes[option] += 1
        return jsonify({"status": "success", "votes": votes})
    return jsonify({"status": "error", "message": "Invalid option"}), 400

if __name__ == "__main__":
    # Cambia `host` para permitir acceso desde cualquier dispositivo en tu red.
    app.run(host="0.0.0.0", port=5000, debug=True)
