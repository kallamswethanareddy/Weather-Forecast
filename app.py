from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    
    if request.method == "POST":
        city = request.form["city"]
        api_key = os.getenv("API_KEY")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        data = requests.get(url).json()

        if "main" in data:
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"]
            }
        else:
            weather = {"error": data.get("message", "Error")}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)