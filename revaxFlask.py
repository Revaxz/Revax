from flask import Flask,render_template
from threading import Thread
import random
import os
os.system("pip install flask")
app = Flask('')

@app.route('/')
def home():
 return "hi ur script is on now"

def run():
  app.run(
  host='0.0.0.0',
  port=random.randint(1000,9000)
 )

def revaxflask():
 '''
 Creates and starts new thread that runs the function run.
 '''
 t = Thread(target=run)
 t.start()
