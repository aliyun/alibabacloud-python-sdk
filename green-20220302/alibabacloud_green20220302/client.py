# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20220302 import models as green_20220302_models
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
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def text_moderation_with_options(
        self,
        request: green_20220302_models.TextModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_moderation_with_options_async(
        self,
        request: green_20220302_models.TextModerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220302_models.TextModerationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TextModeration',
            version='2022-03-02',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220302_models.TextModerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_moderation(
        self,
        request: green_20220302_models.TextModerationRequest,
    ) -> green_20220302_models.TextModerationResponse:
        runtime = util_models.RuntimeOptions()
        return self.text_moderation_with_options(request, runtime)

    async def text_moderation_async(
        self,
        request: green_20220302_models.TextModerationRequest,
    ) -> green_20220302_models.TextModerationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.text_moderation_with_options_async(request, runtime)
