from ystreamer import YahooStreamer
import time

def on_data(data):
    print(data)

stream = YahooStreamer(["AAPL", "MSFT"], on_data)
stream.start()

# Stream continues to run in the background so must wait indefinately 
# or the program will exit
while True:
    time.sleep(1)