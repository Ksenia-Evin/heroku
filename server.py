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

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p class="small">Чтобы сформировать одно утверждение перейдите по пути /api/generate</p>
      <p class="small">Чтобы сформировать несколько утверждений перейдите по пути /api/generate/количество желаемых утверждений.</p>
      <p class="small">Например, хочу 8 утверждений! api/generate/8</p>
    </div>
  </body>
</html>
"""
    return html

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
