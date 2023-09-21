from fastapi import FastAPI
import models
from database import engine
from Routers import Auth, todos, admin, users


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(Auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)