from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return "hi All this is my Flask CI/CD Deployment Success 🚀"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
