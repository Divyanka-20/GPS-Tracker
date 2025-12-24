from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store all users' locations
users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    user_id = data["user_id"]

    users[user_id] = {
        "lat": data["latitude"],
        "lng": data["longitude"]
    }

    return jsonify({"status": "updated"})

@app.route("/get_locations")
def get_locations():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
