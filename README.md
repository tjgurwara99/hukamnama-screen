### Hukamnama Screen

Its a basic project to show a Hukamnama of a particular Gurdwara on a screen using an single board
computer like a Raspberry Pi and being able to remotely manage the screen.

### How to

#### Install

Its a simple flask project. Running it behind a wsgi server with nginx configuration can be found in many different tutorial sites.

#### Testing wsgi server is working as expected

```
uv run uwsgi --socket 0.0.0.0:8000 --protocol=http -w app:app
```

Check by going to the http://0.0.0.0:8000

```
sudo chown hukamnama:www-data /home/hukamnama
```
