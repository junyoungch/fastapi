from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import requests, json

from sens.sens import send_sms_area1, send_sms_area2, send_sms_area3, url, uri, header

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
    if state == 2:
        drone_state = {"집으로 복귀중"}
    recon = {"drone_name": drone_id, "state": drone_state}
    return recon

@app.get("/send_msg")
async def send_msg(state: Union[int, None]=None):
    if state == 0:
        ditto = send_sms_area1.data
    if state == 1:
        ditto = send_sms_area2.data
    if state == 2:
        ditto = send_sms_area3.data
    requests.post(url+uri, headers=header, data = json.dumps(ditto))
    return ditto


# @app.get("/drones/recon-drone/{drone_state}")
# async def read_drone_state(drone_state: int = 0):
#     if drone_state == 0:
#         drone = {"드론 쉬고있음"}
#     if drone_state == 1:
#         drone = {"드론 날고있음"}
#     return drone