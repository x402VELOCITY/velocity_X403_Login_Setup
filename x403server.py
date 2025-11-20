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
                    "/setupaccount",
                    "/checkaccount", 
                    "/register_endpoint",
                    "/register_dynamic_endpoint",
                    "/delete_endpoint",
                    "/delete_dynamic_endpoint",
                    "/checkendpoints",
                    "/checkdynamicendpoints",
                    "/update_dynamic_endpoint",
                    "/update_endpoint_price",
                    "/update_dynamic_endpoint_price",
                    "/docs",
                    "/openapi.json",
                    "/invoices"
                   
                   ]
                )


@app.get("/accountlogin")
def AccountLogin(request:Request):
    return {"message":"loggedin"}
