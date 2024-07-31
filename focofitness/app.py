from fastapi import FastAPI

from .controllers import login, signup
from .routes import view_app

app = FastAPI()
app.mount('/views', view_app)
login.subscribe_controller(app)
signup.subscribe_controller(app)
