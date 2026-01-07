### Hukamnama Screen

Its a basic project to show a Hukamnama of a particular Gurdwara on a screen using an single board
computer like a Raspberry Pi and being able to remotely manage the screen.

### How to

#### Install

Its a simple flask project. Running it behind a wsgi server with nginx configuration can be found in many different tutorial sites.

> [!note]
> Due to a limitation with OSX requiring to install a special version of uwsgi being built with OpenSSL
> headers, I chose to just use the socketio dedicated gevent server.


##### Running the application

1. `uv venv` to activate the environment - the virtual env is in the `.venv` directory by default.
2. `uv run python app.py` to start the application using the virtual environment.
3. Then visit `http://127.0.0.1:5000/signup` to create a new account.
4. Search for a pankti
5. Click "Save as current hukamnama" to update all the client's using the home page as a display.
6. Visit `http://127.0.0.1:5000` to see the newly set hukamnama.

##### Deployment

Take a look at `.example.systemd.conf` to set it up as a systemd service, and make sure
to enable it in order for the application server to start at startup. Once the application is serving traffic, set up
another systemd service to run chromium in kiosk mode and visit the page `127.0.0.1:5000` or your nginx reverse proxy
that you have setup (an example can be found in .example.hukamnama.nginx file: highly recommended if you are controlling
this by a remote device such as a smartphone.)

### Application architecture

It's a simple application using `socket.io` + `flask` to run a simple web application server that would be accessible through the reverse proxy.

The screen can be running a browser (Android, iPhone, or SBC like raspberry pi in kiosk mode) and showing the page pointing to the index page of
the flask application. Everytime anyone updates the current hukamnama, the screen would automatically refresh and show the latest content.
