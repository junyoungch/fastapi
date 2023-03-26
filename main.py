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
def read_item():
    recon_drone = Recon_Drone
    #drone = {"drone_name": Recon_Drone.name, "drone_state": Recon_Drone.state}
    # name = recon_drone.name
    # state = recon_drone.state
    return recon_drone

@app.get("/drones/{drone_id}")
async def read_drone_state(drone_id: str, state: Union[int, None] = None):
    if state == 0:
        recon = {"쉼"}
    if state == 1:
        recon = {"fly"}
    #recon = {"drone_id": drone_id, "state": state}
    return recon

@app.get("/drones/recon-drone/{drone_state}")
async def read_drone_state(drone_state: int = 0):
    if drone_state == 0:
        drone = {"드론 쉬고있음"}
    if drone_state == 1:
        drone = {"드론 날고있음"}
    return drone

# @app.post("/drones/recon-drone/{drone_state}")
# async def create_item(recon_drone: Recon_Drone, drone_state: int):
#     recon_drone.state = drone_state
#     return {"drone_name": recon_drone.name, "drone_state": drone_state, "recon_state": recon_drone.state}
    
# @app.put("/drones/recon-drone/{drone_state}")
# def update_item(recon_drone: Recon_Drone, drone_state: int):
#     recon_drone.state = drone_state
#     return {"drone_name": recon_drone.name, "drone_state": drone_state, "recon_state": recon_drone.state}   