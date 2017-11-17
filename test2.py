import sched, time
import requests

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    req = requests.get('https://46ce604b.ngrok.io/')
    print(req.content)
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()
