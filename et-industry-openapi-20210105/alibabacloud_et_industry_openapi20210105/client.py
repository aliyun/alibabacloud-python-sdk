# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_et_industry_openapi20210105 import models as et_industry_openapi_20210105_models
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
            'cn-hangzhou': 'et-industry.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('et-industry-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def open_api_invoke(
        self,
        request: et_industry_openapi_20210105_models.OpenApiInvokeRequest,
    ) -> et_industry_openapi_20210105_models.OpenApiInvokeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_api_invoke_with_options(request, headers, runtime)

    async def open_api_invoke_async(
        self,
        request: et_industry_openapi_20210105_models.OpenApiInvokeRequest,
    ) -> et_industry_openapi_20210105_models.OpenApiInvokeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_api_invoke_with_options_async(request, headers, runtime)

    def open_api_invoke_with_options(
        self,
        request: et_industry_openapi_20210105_models.OpenApiInvokeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20210105_models.OpenApiInvokeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.node_id):
            query['nodeId'] = request.node_id
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            et_industry_openapi_20210105_models.OpenApiInvokeResponse(),
            self.do_roarequest('OpenApiInvoke', '2021-01-05', 'HTTPS', 'POST', 'AK', f'/aics/api/openapi/invoke', 'json', req, runtime)
        )

    async def open_api_invoke_with_options_async(
        self,
        request: et_industry_openapi_20210105_models.OpenApiInvokeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> et_industry_openapi_20210105_models.OpenApiInvokeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.node_id):
            query['nodeId'] = request.node_id
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            et_industry_openapi_20210105_models.OpenApiInvokeResponse(),
            await self.do_roarequest_async('OpenApiInvoke', '2021-01-05', 'HTTPS', 'POST', 'AK', f'/aics/api/openapi/invoke', 'json', req, runtime)
        )
