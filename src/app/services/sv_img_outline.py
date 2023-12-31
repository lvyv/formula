
# Author: Awen <26896225@qq.com>
# License: MIT

import logging
import httpx
import time
import json
from app.schemas.reqhistory import ReqItemCreate
from app.services.main import AppService
from app.models.dao_reqhistory import RequestHistoryCRUD
from app.utils.service_result import ServiceResult
from app.utils.app_exceptions import AppException
from config import constants as ct
from sqlalchemy.orm import Session


class ImageOutlineService(AppService):
    """
    图片内容提炼模型业务逻辑服务。
    1.OCR识别
    2.HDBSCAN聚类
    3.OPENAI提词
    """
    def __init__(self, db: Session, imgs: list, tid: int):
        AppService.__init__(self, db)
        self.imgs_ = imgs
        self.task_id_ = tid

    async def ocr(self, devs: list, tags: list, startts: int, endts: int) -> ServiceResult:
        """
        图片内容提炼
        :param devs:
        :param tags:
        :param startts:
        :param endts:
        :return:
        """
        dev_type = ct.MDL_IMGAGE_OUTLINE
        external_data = {
            'models': dev_type,
            'status': ct.REQ_STATUS_PENDING,
            'result': ct.REQ_STATUS_PENDING,
            'requestts': int(time.time() * 1000),
            'memo': json.dumps(devs)
        }
        item = ReqItemCreate(**external_data)
        soh_item = RequestHistoryCRUD(self.db).create_record(item)
        try:
            async with httpx.AsyncClient(timeout=ct.REST_REQUEST_TIMEOUT, verify=False) as client:
                payload = {
                    "devices": json.dumps(devs),
                    "tags": json.dumps(tags),
                    "startts": startts,
                    "endts": endts
                }
                params = {"reqid": soh_item.id}
                r = await client.post(f'{ct.URL_SOH}', json=payload, params=params)
                logging.debug(r)
                return ServiceResult(r.content)
        except httpx.ConnectTimeout:
            return ServiceResult(AppException.HttpRequestTimeout())

    async def cluster(self, devs: list, tags: list, startts: int, endts: int) -> ServiceResult:
        """
        聚类计算。
        :param devs:
        :param tags:
        :param startts:
        :param endts:
        :return:
        """
        dev_type = ct.MDL_IMGAGE_OUTLINE
        external_data = {
            'models': dev_type,
            'status': ct.REQ_STATUS_PENDING,
            'result': ct.REQ_STATUS_PENDING,
            'requestts': int(time.time() * 1000),
            'memo': json.dumps(devs)
        }
        item = ReqItemCreate(**external_data)
        cluster_item = RequestHistoryCRUD(self.db).create_record(item)
        try:
            async with httpx.AsyncClient(timeout=ct.REST_REQUEST_TIMEOUT, verify=False) as client:
                payload = {
                    "devices": json.dumps(devs),
                    "tags": json.dumps(tags),
                    "startts": startts,
                    "endts": endts
                }
                params = {"reqid": cluster_item.id}
                r = await client.post(f'{ct.URL_CLUSTER}', json=payload, params=params)
                logging.debug(r)
                return ServiceResult(r.content)
        except httpx.ConnectTimeout:
            return ServiceResult(AppException.HttpRequestTimeout())

    async def generate(self, phase: str):
        pass

    def outline_pic(self):
        pass
