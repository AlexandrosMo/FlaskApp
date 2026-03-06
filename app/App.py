from flask import Flask
import datetime
from psutil import cpu_percent
from psutil import virtual_memory

app = Flask (__name__)
@app.get("/")
def home():
    return """
    <h1>Flask Monitor API</h1>
    <ul>
        <li><a href="/health">Health</a></li>
        <li><a href="/system">System</a></li>
        <li><a href="/time">Time</a></li>
    </ul>
    """
@app.get("/health")
def home ():
    return {"status":"ok"}

@app.get("/system")
def system ():
    CPU = cpu_percent()
    RAM = virtual_memory().percent
    return {"CPU":CPU,
            "RAM":RAM}
@app.get("/time")
def get_time():
    TIME = datetime.datetime.now()
    return {"TIME":TIME}

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
