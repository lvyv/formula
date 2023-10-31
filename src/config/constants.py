
from config.config import ConfigSet

cfg = ConfigSet.get_cfg()
# 所有后端的科学计算模型，MODEL类型
MDL_IMGAGE_OUTLINE = 'image_outline'
# DEV_VRLA = 'vrla'
# DEV_CELLPACK = 'cellpack'
# DEV_CANNED_MOTOR_PUMP = 'canned motor pump'
# DEV_CENTRIFUGAL_PUMP = 'centrifugal pump'
# DEV_AC_FAN = 'air conditioner fan'
# DEV_CHILLER = 'chiller'

# 各种状态常量
REQ_STATUS_PENDING = 'pending'
REQ_STATUS_SETTLED = 'settled'

# 后台ai模型的地址
REST_REQUEST_TIMEOUT = 10

# 后台ai模型的地址
URL_SOH = cfg['url_soh']
#UPL_SOH = "https://127.0.0.1:29082/api/v1/soh"
URL_CLUSTER = cfg['url_cluster']
#URL_CLUSTER = "https://127.0.0.1:29082/api/v1/cluster"
# 后台ai模型mock的地址
#AIURL_SOH = 'https://127.0.0.1:29083/api/v1/soh'


# phmMS启动的地址、端口、证书等
SCHEDULE_HOST = cfg['schedule_host']
SCHEDULE_PORT = cfg['schedule_port']
SCHEDULE_KEY = cfg['schedule_key']
SCHEDULE_CER = cfg['schedule_cer']

