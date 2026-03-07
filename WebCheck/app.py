from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.post("/check")
def check():
    try:

        data = request.get_json()
        url = data["url"]
        start = time.time()
        end = time.time()
        response_time = end - start
        status = "UP"
    except:
        status = "DOWN"
        response_time = None
    return {"URL":url,
            "STATUS":status,
            "response_time":response_time}

@app.get ("/history")

def history():
    return {"history":[]}

@app.get ("/health")

def health():
    return {"status":"ok"}

if __name__ == "__main__":
    app.run (host="0.0.0.0", port = 5000)

