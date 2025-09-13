from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock in-memory storage
waste_listings = []
fertilizer_listings = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_waste', methods=['POST'])
def add_waste():
    waste = {
        "name": request.form["name"],
        "quantity": request.form["quantity"],
        "location": request.form["location"]
    }
    waste_listings.append(waste)
    return redirect(url_for("view_waste"))

@app.route('/waste')
def view_waste():
    return render_template("waste.html", wastes=waste_listings)

@app.route('/add_fertilizer', methods=['POST'])
def add_fertilizer():
    fert = {
        "name": request.form["name"],
        "price": request.form["price"],
        "quantity": request.form["quantity"]
    }
    fertilizer_listings.append(fert)
    return redirect(url_for("view_fertilizer"))

@app.route('/fertilizer')
def view_fertilizer():
    return render_template("fertilizer.html", fertilizers=fertilizer_listings)

if __name__ == "__main__":
    app.run(debug=True)
