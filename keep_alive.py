from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)


@app.route('/bot')
def index():
  return "the Bot is alive"


def run():
  app.run(host='0.0.0.0', port=3000)


def keep_alive():
  t = Thread(target=run)
  t.start()
