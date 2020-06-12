import os
import random
import json

from bottle import route, run
from data import sayings

def test(num):
  message = []
  for i in range(num):
     message.append(generate_message())
  return {"message": message}

def generate_message():
  return '{0} {1} {2} {3} {4}'.format(random.choice(sayings.beginnings), random.choice(sayings.subjects),random.choice(sayings.verbs), random.choice(sayings.actions), random.choice(sayings.ends))

@route("/api/generate")
def receive_json():
    return json.dumps(test(1), ensure_ascii=False)

@route("/api/generate/<num:int>")
def api_response(num):
    return json.dumps(test(num), ensure_ascii=False)

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
