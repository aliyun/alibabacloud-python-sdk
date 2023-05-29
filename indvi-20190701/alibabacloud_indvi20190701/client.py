# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_indvi20190701 import models as indvi_20190701_models
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
            'ap-northeast-1': 'indvi.aliyuncs.com',
            'ap-northeast-2-pop': 'indvi.aliyuncs.com',
            'ap-south-1': 'indvi.aliyuncs.com',
            'ap-southeast-1': 'indvi.aliyuncs.com',
            'ap-southeast-2': 'indvi.aliyuncs.com',
            'ap-southeast-3': 'indvi.aliyuncs.com',
            'ap-southeast-5': 'indvi.aliyuncs.com',
            'cn-beijing': 'indvi.aliyuncs.com',
            'cn-beijing-finance-1': 'indvi.aliyuncs.com',
            'cn-beijing-finance-pop': 'indvi.aliyuncs.com',
            'cn-beijing-gov-1': 'indvi.aliyuncs.com',
            'cn-beijing-nu16-b01': 'indvi.aliyuncs.com',
            'cn-chengdu': 'indvi.aliyuncs.com',
            'cn-edge-1': 'indvi.aliyuncs.com',
            'cn-fujian': 'indvi.aliyuncs.com',
            'cn-haidian-cm12-c01': 'indvi.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'indvi.aliyuncs.com',
            'cn-hangzhou-finance': 'indvi.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'indvi.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'indvi.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'indvi.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'indvi.aliyuncs.com',
            'cn-hangzhou-test-306': 'indvi.aliyuncs.com',
            'cn-hongkong': 'indvi.aliyuncs.com',
            'cn-hongkong-finance-pop': 'indvi.aliyuncs.com',
            'cn-huhehaote': 'indvi.aliyuncs.com',
            'cn-north-2-gov-1': 'indvi.aliyuncs.com',
            'cn-qingdao': 'indvi.aliyuncs.com',
            'cn-qingdao-nebula': 'indvi.aliyuncs.com',
            'cn-shanghai-et15-b01': 'indvi.aliyuncs.com',
            'cn-shanghai-et2-b01': 'indvi.aliyuncs.com',
            'cn-shanghai-finance-1': 'indvi.aliyuncs.com',
            'cn-shanghai-inner': 'indvi.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'indvi.aliyuncs.com',
            'cn-shenzhen': 'indvi.aliyuncs.com',
            'cn-shenzhen-finance-1': 'indvi.aliyuncs.com',
            'cn-shenzhen-inner': 'indvi.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'indvi.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'indvi.aliyuncs.com',
            'cn-wuhan': 'indvi.aliyuncs.com',
            'cn-yushanfang': 'indvi.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'indvi.aliyuncs.com',
            'cn-zhangjiakou': 'indvi.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'indvi.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'indvi.aliyuncs.com',
            'eu-central-1': 'indvi.aliyuncs.com',
            'eu-west-1': 'indvi.aliyuncs.com',
            'eu-west-1-oxs': 'indvi.aliyuncs.com',
            'me-east-1': 'indvi.aliyuncs.com',
            'rus-west-1-pop': 'indvi.aliyuncs.com',
            'us-east-1': 'indvi.aliyuncs.com',
            'us-west-1': 'indvi.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('indvi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_detection_result_with_options(
        self,
        request: indvi_20190701_models.GetDetectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> indvi_20190701_models.GetDetectionResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detect_path):
            query['DetectPath'] = request.detect_path
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetectionResult',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            indvi_20190701_models.GetDetectionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detection_result_with_options_async(
        self,
        request: indvi_20190701_models.GetDetectionResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> indvi_20190701_models.GetDetectionResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detect_path):
            query['DetectPath'] = request.detect_path
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.platform_type):
            query['PlatformType'] = request.platform_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDetectionResult',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            indvi_20190701_models.GetDetectionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detection_result(
        self,
        request: indvi_20190701_models.GetDetectionResultRequest,
    ) -> indvi_20190701_models.GetDetectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detection_result_with_options(request, runtime)

    async def get_detection_result_async(
        self,
        request: indvi_20190701_models.GetDetectionResultRequest,
    ) -> indvi_20190701_models.GetDetectionResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detection_result_with_options_async(request, runtime)
