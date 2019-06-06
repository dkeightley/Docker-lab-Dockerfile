from flask import Flask, render_template
import random
import signal
import sys

def exit_gracefully(signumber, frame):
  print("Received signal", signumber, "cleaning up...")
  sys.exit(0)

app = Flask(__name__)

# list of cat images
images = [
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr01/15/9/anigif_enhanced-buzz-31540-1381844535-8.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr02/15/9/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-18774-1381844645-6.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr09/anigif_enhanced-22194-1446481827-6.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr08/anigif_enhanced-11728-1446481996-20.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr11/anigif_enhanced-19791-1446482500-3.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr13/anigif_enhanced-17467-1446482522-2.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/13/enhanced/webdr01/anigif_enhanced-21301-1446489701-6.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr09/anigif_enhanced-26523-1446483536-5.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, exit_gracefully)
    app.run(host="0.0.0.0",threaded=True)
