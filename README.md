# flask_remote
Flask programming exercise from progbook.org to control a music player remotely

To run it you need Python3 and mpv.

1) $ . venv/bin/activate
2) $ export FLASK_APP=hello.py
3) $ flask run --host=0.0.0.0
4) Check your local network ip address (e.g. 192.168.1.245)
5) Open a browser on another device and go to that address with ':5000' at the end (e.g. http://192.168.1.245:5000)
6) You should get a page with two buttons to start and stop playing music
