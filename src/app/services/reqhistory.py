


from app.services.main import AppService
from app.models.dao_reqhistory import RequestHistoryCRUD
from app.utils.service_result import ServiceResult
# from utils.app_exceptions import AppException


class ReqHistoryService(AppService):
    def update_item(self, reqid, res) -> ServiceResult:
        req_item = RequestHistoryCRUD(self.db).update_record(reqid, res)
        if not req_item:
            # return ServiceResult(AppException.FooCreateItem())
            pass
        return ServiceResult(req_item)

    def get_item(self, item_id: int) -> ServiceResult:
        req_item = RequestHistoryCRUD(self.db).get_record(item_id)
        # if not req_item:
        #     return ServiceResult(AppException.FooGetItem({"item_id": item_id}))
        # if not req_item.public:
        #     return ServiceResult(AppException.FooItemRequiresAuth())
        return ServiceResult(req_item)
