from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variables globales para almacenar votos y las IPs de los votantes
votes = {"option1": 0, "option2": 0}
voted_ips = set()

@app.route("/")
def index():
    return render_template("index.html", votes=votes)

@app.route("/vote", methods=["POST"])
def vote():
    # Obtener la IP del usuario
    user_ip = request.remote_addr
    if user_ip in voted_ips:
        return jsonify({"status": "error", "message": "Ya votaste"}), 403

    # Procesar el voto
    data = request.json
    option = data.get("option")
    if option in votes:
        votes[option] += 1
        voted_ips.add(user_ip)  # Registrar la IP
        return jsonify({"status": "success", "votes": votes})
    return jsonify({"status": "error", "message": "Opción inválida"}), 400

if __name__ == "__main__":
    # Cambia `host` para permitir acceso desde cualquier dispositivo en tu red.
    app.run(host="0.0.0.0", port=5000, debug=True)
