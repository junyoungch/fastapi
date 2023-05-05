from typing import Union

from fastapi import FastAPI, Query
from pydantic import BaseModel

import requests, json

from sens.sens import send_sms_area1, send_sms_area2, send_sms_area3, url, uri, header

app = FastAPI()
droen = "10"

patrol_status = "PATROL_STANDBY"
warning_status = "WARNING_STANDBY"
camera_status = "NO_DETECTION"

@app.get("/")
async def read_root():
    return {"Welcome to gabozaing"}

@app.get("/drones/{drone_id}")
async def read_drone_state(drone_id: str, state: Union[int, None] = None):
   # drone_name = drone_id
    drone_state = {"?"}
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


@app.get("/drone/recon")
async def sen(state:str = Query(None)):
    global droen
    if state == "1":
        droen = "10"

    if state == "2":
        droen = "20"
    
    return droen

# DRONE 상태 변경 API
@app.get("/PATROL_DRONE")
async def change_PATROL_status(STATUS: str = Query(None)):
    global patrol_status
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, patrol상태 변경
        if STATUS.upper() == "PATROL_STANDBY":
            patrol_status = "PATROL_STANDBY"
        elif STATUS.upper() == "PATROL_TAKEOFF":
            patrol_status = "PATROL_TAKEOFF"    
        elif STATUS.upper() == "PATROL_MOVE1":
            patrol_status = "PATROL_MOVE1"
        elif STATUS.upper() == "PATROL_MOVE2":
            patrol_status = "PATROL_MOVE2"
        elif STATUS.upper() == "PATROL_MOVE3":
            patrol_status = "PATROL_MOVE3"
    # 현재 LED 상태 반환
    return {"PATROL_STATUS": patrol_status}

@app.get("/CAMERA")
async def change_CAMERA_status(STATUS: str = Query(None)):
    global camera_status
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, patrol상태 변경
        if STATUS.upper() == "DETECT_POINT":
            camera_status = "DETECT_POINT"
        elif STATUS.upper() == "DETECT_NO_POINT":
            camera_status = "DETECT_NO_POINT"    
    # 현재 LED 상태 반환
    return {"DETECTION_STATUS": camera_status}

@app.get("/WARNING_DRONE")
async def change_WARNING_status(STATUS: str = Query(None)):
    global warning_status
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, warning 상태 변경
        if STATUS.upper() == "WARNING_STANDBY":
            warning_status = "WARNING_STANDBY"
        elif STATUS.upper() == "WARNING_MOVE":
            warning_status = "WARNING_MOVE"
    # 현재 LED 상태 반환
    return {"WARNING_STATUS": warning_status}