from app import app as application
from app.settings import APP_PORT

if __name__ == '__main__':
    application.run(port=APP_PORT)
