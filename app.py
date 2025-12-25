"""
This is the uwsgi entry point for the Hukamnama application.
"""

from hukamnama import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
