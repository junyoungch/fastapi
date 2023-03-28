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

@app.get("/drones/{drone_id}")
async def read_drone_state(drone_id: str, state: Union[int, None] = None):
   # drone_name = drone_id
    if state == 0:
        drone_state = {"드론 쉬는중"}
        #recon = {drone_name, "쉼"}
    if state == 1:
        drone_state = {"드론 나는중"}
       # recon = {drone_name, "fly"}
    recon = {"drone_name": drone_id, "state": drone_state}
    return recon

# @app.get("/drones/recon-drone/{drone_state}")
# async def read_drone_state(drone_state: int = 0):
#     if drone_state == 0:
#         drone = {"드론 쉬고있음"}
#     if drone_state == 1:
#         drone = {"드론 날고있음"}
#     return drone