from dotenv import load_dotenv
load_dotenv()
from Library import app


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)