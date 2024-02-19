# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_edas20170405 import models as edas_20170405_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
            'ap-northeast-2-pop': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-southeast-3': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'edas.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'edas.aliyuncs.com',
            'cn-beijing-finance-pop': 'edas.aliyuncs.com',
            'cn-beijing-gov-1': 'edas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'edas.aliyuncs.com',
            'cn-chengdu': 'edas.aliyuncs.com',
            'cn-edge-1': 'edas.aliyuncs.com',
            'cn-fujian': 'edas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'edas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'edas.aliyuncs.com',
            'cn-hangzhou-finance': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'edas.aliyuncs.com',
            'cn-hangzhou-test-306': 'edas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'edas.aliyuncs.com',
            'cn-huhehaote': 'edas.aliyuncs.com',
            'cn-qingdao-nebula': 'edas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'edas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'edas.aliyuncs.com',
            'cn-shanghai-finance-1': 'edas.aliyuncs.com',
            'cn-shanghai-inner': 'edas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'edas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'edas.aliyuncs.com',
            'cn-shenzhen-inner': 'edas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'edas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'edas.aliyuncs.com',
            'cn-wuhan': 'edas.aliyuncs.com',
            'cn-yushanfang': 'edas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'edas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'edas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'edas.aliyuncs.com',
            'eu-west-1': 'edas.ap-northeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'edas.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'edas.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'edas.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'edas.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('edas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def edas_produce_with_options(
        self,
        request: edas_20170405_models.EdasProduceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170405_models.EdasProduceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        if not UtilClient.is_unset(request.source_flag):
            query['sourceFlag'] = request.source_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EdasProduce',
            version='2017-04-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170405_models.EdasProduceResponse(),
            self.call_api(params, req, runtime)
        )

    async def edas_produce_with_options_async(
        self,
        request: edas_20170405_models.EdasProduceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170405_models.EdasProduceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        if not UtilClient.is_unset(request.source_flag):
            query['sourceFlag'] = request.source_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EdasProduce',
            version='2017-04-05',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170405_models.EdasProduceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edas_produce(
        self,
        request: edas_20170405_models.EdasProduceRequest,
    ) -> edas_20170405_models.EdasProduceResponse:
        runtime = util_models.RuntimeOptions()
        return self.edas_produce_with_options(request, runtime)

    async def edas_produce_async(
        self,
        request: edas_20170405_models.EdasProduceRequest,
    ) -> edas_20170405_models.EdasProduceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edas_produce_with_options_async(request, runtime)
