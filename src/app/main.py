from fastapi import FastAPI
import logging
import uvicorn
import json
from typing import List
from fastapi import APIRouter, File, UploadFile
import cv2
import numpy as np
from app.nougat_run import NougatInference
from fastapi.responses import JSONResponse


# 配置logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app6 = FastAPI(
    title="文字识别微服务",
    version="0.1.0"
)


@app6.post("/nougat/")  # 接收图片，将ocr传入队列
async def getnougat(files: List[UploadFile] = File(...)):
    result = []
    for file in files:
        file_bytes = await file.read()
        image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
        text_result = nougat_inference.gat_nougat(image)
        result.append(text_result)
    return result


if __name__ == '__main__':
    nougat_inference = NougatInference()

    # 启动fastAPI

    uvicorn.run(app6,
                port=29001
                )
