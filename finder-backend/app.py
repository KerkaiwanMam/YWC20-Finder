from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from routes.candidates import candidates_bp

app = Flask(__name__)
CORS(app)

# Register Blueprint
app.register_blueprint(candidates_bp)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
