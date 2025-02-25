from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel

app = FastAPI()

from app import routes


class Settings(BaseModel):
    # TODO: Read secret from env
    authjwt_secret_key: str = "d705d174474c4fb5ac00eb1946936fc4"


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"reason": exc.message})


@app.get("/")
def home():
    return {"status": "OK"}
