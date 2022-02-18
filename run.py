import platform
from app import app

OS_NAME = platform.system()

if OS_NAME == "Linux":
    app.config["ENV"] = "production"
else:
    app.config["ENV"] = "development"

if __name__ == "__main__":
    app.run(debug=True)
