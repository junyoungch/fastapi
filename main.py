from typing import Union

from fastapi import FastAPI, Query


import requests, json

from sens.sens import send_sms_area1, send_sms_area2, send_sms_area3, url, uri, header

app = FastAPI()

class StateInfo:
    patrol_status = "PATROL_STANDBY"
    warning_status = "WARNING_STANDBY"
    detect_status = "DETECT_NO_POINT1"
    gps_coordinate = "0"

@app.get("/")
async def read_root():
    return {"Welcome to gabozaing"}

# PATROL_DRONE 상태 변경 API
@app.get("/StateInfo/PATROL_STATUS")
async def change_PATROL_status(STATUS: str = Query(None)):
    global StateInfo
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, patrol상태 변경
        if STATUS.upper() == "PATROL_STANDBY":
            StateInfo.patrol_status = "PATROL_STANDBY"
        elif STATUS.upper() == "PATROL_TAKEOFF":
            StateInfo.patrol_status = "PATROL_TAKEOFF"    
        elif STATUS.upper() == "PATROL_MOVE1":
            StateInfo.patrol_status = "PATROL_MOVE1"
        elif STATUS.upper() == "PATROL_MOVE2":
            StateInfo.patrol_status = "PATROL_MOVE2"
        elif STATUS.upper() == "PATROL_MOVE3":
            StateInfo.patrol_status = "PATROL_MOVE3"
        elif STATUS.upper() == "PATROL_DETECTED":
            StateInfo.patrol_status = "PATROL_DETECTED"
        elif STATUS.upper() == "PATROL_RETURN":
            StateInfo.patrol_status = "PATROL_RETURN"
            
        else:
            StateInfo.patrol_status = "다시 입력해주세요."

    return {"PATROL_STATUS": StateInfo.patrol_status}

# WARNING_DRONE 상태변경
@app.get("/StateInfo/WARNING_STATUS")
async def change_WARNING_status(STATUS: str = Query(None)):
    global warning_status
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, warning 상태 변경
        if STATUS.upper() == "WARNING_STANDBY":
            StateInfo.warning_status = "WARNING_STANDBY"
        elif STATUS.upper() == "WARNING_MOVE":
            StateInfo.warning_status = "WARNING_MOVE"
        elif STATUS.upper() == "WARNING_ALARM":
            StateInfo.warning_status = "WARNING_ALARM"
        elif STATUS.upper() == "WARNING_RETURN":
            StateInfo.warning_status = "WARNING_RETURN"
        else:
            StateInfo.warning_status = "다시 입력해주세요."

    return {"WARNING_STATUS": StateInfo.warning_status}

# 
@app.get("/StateInfo/DETECT_STATUS")
async def change_CAMERA_status(STATUS: str = Query(None)):
    global StateInfo
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, camera상태 변경
        if STATUS.upper() == "DETECT_POINT1":
            StateInfo.detect_status = "DETECT_POINT1"
        elif STATUS.upper() == "DETECT_POINT2":
            StateInfo.detect_status = "DETECT_POINT2"
        elif STATUS.upper() == "DETECT_NO_POINT1":
            StateInfo.camera_status = "DETECT_NO_POINT1"    
        else:
            StateInfo.camera_status = "다시 입력해주세요."

    return {"DETECTION_STATUS": StateInfo.camera_status}

#GPS좌표 받아오기
@app.get("/StateInfo/GPS_COORDINATE")
async def get_gps_value(GPS_VALUE: str = Query(None)):
    global StateInfo
    if GPS_VALUE is not None:
        StateInfo.gps_coordinate = GPS_VALUE

    return {"GPS_VALUE":StateInfo.gps_coordinate}
    
# 관리자에게 메시지 전송
@app.get("/send_msg")
async def send_msg(state: Union[int, None]=None):
    if state == 0 or state == 1 or state == 2:
        if state == 0:
            ditto = send_sms_area1.data
        if state == 1:
            ditto = send_sms_area2.data
        if state == 2:
            ditto = send_sms_area3.data
        requests.post(url+uri, headers=header, data = json.dumps(ditto))
        send_message = "관리자에게 메시지를 전송을 성공하였습니다."
    else:
        send_message = "관리자에게 메시지 전송을 실패하였습니다."
    return send_message