from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # Sets up the RPi lib to use the Broadcom pin mappings
                        #  for the pin names. This corresponds to the pin names
                        #  given in most documentation of the Pi header
GPIO.setwarnings(False) # Turn off warnings that may crop up if you have the
                        #  GPIO pins exported for use via command line
GPIO.setup(17, GPIO.OUT) # Set GPIO2 as an output

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'yellow hellou!'

    # The magic happens here. When some http request comes in with a path of
#  gpio/x/y, the Flask app will attempt to parse that as x=pin and y=level.
#  Note that there is no error handling here! Failure to properly specify the
#  route will result in a 404 error.
@app.route('/')
def setPinLevel(id = 17 , level = 1):
    GPIO.output(int(id), int(level))
    GPIO.output(int(id), int(0))
    return "OH MY GOD! :DDD"

# If we're running this script directly, this portion executes. The Flask
#  instance runs with the given parameters. Note that the "host=0.0.0.0" part
#  is essential to telling the system that we want the app visible to the 
#  outside world.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')