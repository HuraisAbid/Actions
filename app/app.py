from flask import Flask, render_template, request

app = Flask(__name__)

# Car data
cars = [
    {"id": 1, "name": "Honda Civic", "price": 80},
    {"id": 2, "name": "Toyota Corolla", "price": 70},
    {"id": 3, "name": "Suzuki Alto", "price": 50},
]

@app.route("/")
def home():
    return render_template("index.html", cars=cars)

@app.route("/rent", methods=["POST"])
def rent():
    car_id = int(request.form["car_id"])
    car = next((c for c in cars if c["id"] == car_id), None)
    if not car:
        return "Car not found", 404
    return render_template("rent.html", car=car)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

