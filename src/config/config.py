
import json
import logging

# 配置logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ConfigSet:
    cfg_ = None             # 下发配置
    path2cfg_ = None        # 下发配置路径

    @classmethod
    def load_json(cls, fp):
        try:
            load_dict = None
            cls.path2cfg_ = fp
            with open(fp, 'r', encoding='UTF-8') as load_f:
                load_dict = json.load(load_f)
                load_f.close()
        except Exception as e:
            print(e)
        finally:
            return load_dict

    @classmethod
    def save_json(cls):
        formatted_cfg = json.dumps(cls.cfg_, ensure_ascii=False, indent=2)
        if cls.path2cfg_:
            with open(cls.path2cfg_, 'w', encoding='utf-8') as fp:
                fp.write(formatted_cfg)
                fp.close()

    @classmethod
    def get_cfg(cls, pathtocfg='/Users/d/PycharmProjects/github/formula/formula/src/config/model_service.cfg'):
        if cls.cfg_ is None:
            cls.cfg_ = cls.load_json(pathtocfg)
            logger.info(f'Config file {pathtocfg} loaded.')
        return cls.cfg_


# a=1
cfg = ConfigSet.get_cfg()
URL_SOH = cfg['url_soh']
#URL_SOH = "https://127.0.0.1:29082/api/v1/soh"