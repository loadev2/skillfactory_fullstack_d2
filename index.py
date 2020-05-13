import os
import sentry_sdk
from bottle import route, run, Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://e05149b306b44a41a0e707667a36b226@o392259.ingest.sentry.io/5239530",
    integrations=[BottleIntegration()]
)
app = Bottle()

@app.route("/success")
def generateHelloWorld():
    return 'Hello world'

@app.route("/fail")
def generateRuntimeError():
    raise RuntimeError('Some runtime error')

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)