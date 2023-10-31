
import json
#import cv2
#import numpy as np
import time
from fastapi import APIRouter, File, UploadFile, Depends
from app.schemas.reqhistory import ReqItemCreate
from app.services.sv_img_outline import ImageOutlineService
from app.utils.service_result import handle_result, ServiceResult
from app.utils.app_exceptions import AppException
from config.database import get_db
from pydantic import BaseModel
from typing import List
from config import constants as ct
from app.models.dao_reqhistory import RequestHistoryCRUD

import logging

from app.routers.common import img_queue


router = APIRouter(
    prefix="/api/v1/image",
    tags=["图片内容提炼模型"],
    responses={404: {"description": "Not found"}},
)


class Content:
    def __init__(self, pid, img_list):
        self.id = pid
        self.img = img_list


# 图片内容提炼模型接口，该层接口可以实现模型与调用方解耦，并添加负载均衡等扩展功能。
@router.post("/outline")
async def outline(files: List[UploadFile] = File(...), db: get_db = Depends()):
    try:
        dev_type = ct.MDL_IMGAGE_OUTLINE
        external_data = {
            'model': dev_type,
            'status': ct.REQ_STATUS_PENDING,
            'result': ct.REQ_STATUS_PENDING,
            'requestts': int(time.time() * 1000),
            # 'memo': json.dumps(devs)
        }
        item = ReqItemCreate(**external_data)

        outline_item = RequestHistoryCRUD(db).create_record(item)
        res = ServiceResult(outline_item)
        # 接下来要派发任务到队列，由消费者完成任务，并更新任务
        ImageOutlineService(db, files, res.value.id)

        # res = await bs.soh(json.loads(sohin.devices), json.loads(sohin.tags), sohin.startts, sohin.endts)
    except json.decoder.JSONDecodeError:
        res = ServiceResult(AppException.HttpRequestParamsIllegal())

    img_list = []
    for file in files:
        file_bytes = await file.read()
        img_list.append(file_bytes)
    pro = Content(res.value.id, img_list)
    img_queue.put(pro)



    return handle_result(res)
