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
            'cn-hangzhou': 'linkedmall.aliyuncs.com',
            'cn-shanghai': 'linkedmall.aliyuncs.com',
            'ap-northeast-1': 'linkedmall.aliyuncs.com',
            'ap-northeast-2-pop': 'linkedmall.aliyuncs.com',
            'ap-south-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-2': 'linkedmall.aliyuncs.com',
            'ap-southeast-3': 'linkedmall.aliyuncs.com',
            'ap-southeast-5': 'linkedmall.aliyuncs.com',
            'cn-beijing': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-beijing-gov-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkedmall.aliyuncs.com',
            'cn-chengdu': 'linkedmall.aliyuncs.com',
            'cn-edge-1': 'linkedmall.aliyuncs.com',
            'cn-fujian': 'linkedmall.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-finance': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkedmall.aliyuncs.com',
            'cn-hongkong': 'linkedmall.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-huhehaote': 'linkedmall.aliyuncs.com',
            'cn-north-2-gov-1': 'linkedmall.aliyuncs.com',
            'cn-qingdao': 'linkedmall.aliyuncs.com',
            'cn-qingdao-nebula': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shanghai-inner': 'linkedmall.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-inner': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkedmall.aliyuncs.com',
            'cn-wuhan': 'linkedmall.aliyuncs.com',
            'cn-yushanfang': 'linkedmall.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkedmall.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkedmall.aliyuncs.com',
            'eu-central-1': 'linkedmall.aliyuncs.com',
            'eu-west-1': 'linkedmall.aliyuncs.com',
            'eu-west-1-oxs': 'linkedmall.aliyuncs.com',
            'me-east-1': 'linkedmall.aliyuncs.com',
            'rus-west-1-pop': 'linkedmall.aliyuncs.com',
            'us-east-1': 'linkedmall.aliyuncs.com',
            'us-west-1': 'linkedmall.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkedmall', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
