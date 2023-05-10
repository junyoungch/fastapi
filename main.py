from typing import Union

from fastapi import FastAPI, Query


import requests, json

from sens.sens import url, uri, header, send_sms_area#, send_sms_area2, send_sms_area3 

app = FastAPI()

class StateInfo:
    patrol_status = "PATROL_STANDBY"
    warning_status = "WARNING_STANDBY"
    detect_status = "DETECT_NO_POINT1"
    gps_coordinate = ""

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
        elif STATUS.upper() == "PATROL_MOVE4":
            StateInfo.patrol_status = "PATROL_MOVE4"

        elif STATUS.upper() == "PATROL_CAPTURE1":
            StateInfo.patrol_status = "PATROL_CAPTURE1"
        elif STATUS.upper() == "PATROL_CAPTURE2":
            StateInfo.patrol_status = "PATROL_CAPTURE2"
        elif STATUS.upper() == "PATROL_CAPTURE3":
            StateInfo.patrol_status = "PATROL_CAPTURE3"
        elif STATUS.upper() == "PATROL_CAPTURE4":
            StateInfo.patrol_status = "PATROL_CAPTURE4"

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
async def change_detect_status(STATUS: str = Query(None)):
    global StateInfo
    if STATUS is not None:
        # 파라미터 값이 전달된 경우, detect상태 변경
        if STATUS.upper() == "DETECT_POINT1":
            StateInfo.detect_status = "DETECT_POINT1"
        elif STATUS.upper() == "DETECT_POINT2":
            StateInfo.detect_status = "DETECT_POINT2"
        elif STATUS.upper() == "DETECT_POINT3":
            StateInfo.detect_status = "DETECT_POINT3"
        elif STATUS.upper() == "DETECT_POINT4":
            StateInfo.detect_status = "DETECT_POINT4"

        elif STATUS.upper() == "DETECT_NO_POINT1":
            StateInfo.detect_status = "DETECT_NO_POINT1" 
        elif STATUS.upper() == "DETECT_NO_POINT2":
            StateInfo.detect_status = "DETECT_NO_POINT2"    
        elif STATUS.upper() == "DETECT_NO_POINT3":
            StateInfo.detect_status = "DETECT_NO_POINT3"    
        elif STATUS.upper() == "DETECT_NO_POINT4":
            StateInfo.detect_status = "DETECT_NO_POINT4"       
        else:
            StateInfo.detect_status = "다시 입력해주세요."

    return {"DETECT_STATUS": StateInfo.detect_status}

#GPS좌표 받아오기
@app.get("/StateInfo/GPS_COORDINATE")
async def get_gps_value(GPS_VALUE: str = Query(None)):
    global StateInfo
    if GPS_VALUE is not None:
        StateInfo.gps_coordinate = GPS_VALUE

    return {"GPS_VALUE":StateInfo.gps_coordinate}

@app.get("/accident")
async def send_acc(accident: str = Query(None)):
    acc = accident
    return acc

# 관리자에게 메시지 전송
@app.get("/send_msg")
async def send_msg(point: int = Query(None), accident: str = Query(None)):
    if point == 1 or 2 or 3 or 4:
        sms = send_sms_area()
        if point == 1:
            sms.data["content"] = "1구역에서 " + accident + " 사고발생"
        if point == 2:
            sms.data["content"] = "2구역에서 " + accident + " 사고발생"
        if point == 3:
            sms.data["content"] = "3구역에서 " + accident + " 사고발생"
        if point == 4:
            sms.data["content"] = "4구역에서 " + accident + " 사고발생"

        requests.post(url+uri, headers=header, data = json.dumps(sms.data))
        send_message = "관리자에게 메시지를 전송을 성공하였습니다."
    else:
        send_message = "관리자에게 메시지 전송을 실패하였습니다."
    return send_message