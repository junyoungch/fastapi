from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Recon_Drone(BaseModel):
    name= str("recon")
    state = int("0")

@app.get("/")
def read_root():
    return {"Welcome to gabozaing"}

@app.get("/drones")
def read_item(recon_drone: Recon_Drone):
    name = recon_drone.name
    state = recon_drone.state
    return {"name": name, "state": state}

@app.post("/drones/recon-drone/{drone_state}")
async def create_item(recon_drone: Recon_Drone, drone_state: int):
    recon_drone.state = drone_state
    return {"drone_name": recon_drone.name, "drone_state": drone_state, "recon_state": recon_drone.state}
    
@app.put("/drones/recon-drone/{drone_state}")
def update_item(recon_drone: Recon_Drone, drone_state: int):
    recon_drone.state = drone_state
    return {"drone_name": recon_drone.name, "drone_state": drone_state, "recon_state": recon_drone.state}   