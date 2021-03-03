from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app=FastAPI()

class Name(BaseModel):
    name : str

class User(BaseModel):
    u1 : str    

class Update(BaseModel):
    ud : str

@app.get("/")
def basic():
    return "Hello welcome to the API server"

@app.get("/date")
def date():
    return "3-3-21"

@app.post("/name")
def h(name_variable:Name):
    name_en=jsonable_encoder(name_variable)
    n=name_en["name"]
    return "hi "+ n +" have a nice day"

@app.post("/user")
def user(username:User):
    user_en=jsonable_encoder(username)
    return user_en

@app.get("/user/{user_id}")
def read_userid(user_id):
    return {"user_id" : user_id}

@app.put("/update")
def h(update_variable : Update):
    name_en=jsonable_encoder(update_variable)
    u=name_en["ud"]
    return  u 

@app.get("/author")
def Author():
    return { "Author" : "Sriranga",
             "SRN" : "PES2UG20CS179",
             "FUN FACT" : "I make jokes when I'm uncomfortable"}

#end