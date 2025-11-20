from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openkitx403 import OpenKit403Middleware


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    OpenKit403Middleware,
    audience="[velocity endpoint]",
    issuer="velocity-v1",
    excluded_paths=[
                    "excluded paths here"
                    ]
                )


@app.get("/accountlogin")
def AccountLogin(request:Request):
    return {"message":"loggedin"}
