from flask import Flask, send_from_directory

from app.routes.employee_routes import employee_routes

app = Flask(__name__, static_folder="../frontend", static_url_path="")

app.register_blueprint(employee_routes)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
