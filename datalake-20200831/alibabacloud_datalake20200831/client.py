# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'datalake-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'datalake-daily.aliyuncs.com',
            'ap-south-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-2': 'datalake-daily.aliyuncs.com',
            'ap-southeast-3': 'datalake-daily.aliyuncs.com',
            'ap-southeast-5': 'datalake-daily.aliyuncs.com',
            'cn-beijing': 'dlf.cn-beijing.aliyuncs.com',
            'cn-beijing-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'datalake-daily.aliyuncs.com',
            'cn-chengdu': 'datalake-daily.aliyuncs.com',
            'cn-edge-1': 'datalake-daily.aliyuncs.com',
            'cn-fujian': 'datalake-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou': 'dlf.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'datalake-daily.aliyuncs.com',
            'cn-hongkong': 'datalake-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'datalake-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-qingdao': 'datalake-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'datalake-daily.aliyuncs.com',
            'cn-shanghai': 'dlf.cn-shanghai.aliyuncs.com',
            'cn-shanghai-et15-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-inner': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen': 'dlf.cn-shenzhen.aliyuncs.com',
            'cn-shenzhen-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'datalake-daily.aliyuncs.com',
            'cn-wuhan': 'datalake-daily.aliyuncs.com',
            'cn-wulanchabu': 'datalake-daily.aliyuncs.com',
            'cn-yushanfang': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'datalake-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'datalake-daily.aliyuncs.com',
            'eu-central-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1-oxs': 'datalake-daily.aliyuncs.com',
            'me-east-1': 'datalake-daily.aliyuncs.com',
            'rus-west-1-pop': 'datalake-daily.aliyuncs.com',
            'us-east-1': 'datalake-daily.aliyuncs.com',
            'us-west-1': 'datalake-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('datalake', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
