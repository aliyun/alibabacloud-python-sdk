# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliyunape20210908 import models as aliyunape_20210908_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aliyunape', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def execute_with_options(
        self,
        tmp_req: aliyunape_20210908_models.ExecuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ExecuteResponse:
        UtilClient.validate_model(tmp_req)
        request = aliyunape_20210908_models.ExecuteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_param):
            request.extend_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_param, 'ExtendParam', 'json')
        if not UtilClient.is_unset(tmp_req.service_param):
            request.service_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_param, 'ServiceParam', 'json')
        query = {}
        query['AppName'] = request.app_name
        query['Channel'] = request.channel
        query['ExtendParam'] = request.extend_param_shrink
        query['OrderId'] = request.order_id
        query['RequestId'] = request.request_id
        query['ServiceParam'] = request.service_param_shrink
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='Execute',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ExecuteResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_with_options_async(
        self,
        tmp_req: aliyunape_20210908_models.ExecuteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ExecuteResponse:
        UtilClient.validate_model(tmp_req)
        request = aliyunape_20210908_models.ExecuteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_param):
            request.extend_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_param, 'ExtendParam', 'json')
        if not UtilClient.is_unset(tmp_req.service_param):
            request.service_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_param, 'ServiceParam', 'json')
        query = {}
        query['AppName'] = request.app_name
        query['Channel'] = request.channel
        query['ExtendParam'] = request.extend_param_shrink
        query['OrderId'] = request.order_id
        query['RequestId'] = request.request_id
        query['ServiceParam'] = request.service_param_shrink
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='Execute',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ExecuteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute(
        self,
        request: aliyunape_20210908_models.ExecuteRequest,
    ) -> aliyunape_20210908_models.ExecuteResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_with_options(request, runtime)

    async def execute_async(
        self,
        request: aliyunape_20210908_models.ExecuteRequest,
    ) -> aliyunape_20210908_models.ExecuteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_with_options_async(request, runtime)

    def weathermonitor_province_hour_with_options(
        self,
        tmp_req: aliyunape_20210908_models.WeathermonitorProvinceHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorProvinceHourResponse:
        UtilClient.validate_model(tmp_req)
        request = aliyunape_20210908_models.WeathermonitorProvinceHourShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_param):
            request.extend_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_param, 'ExtendParam', 'json')
        if not UtilClient.is_unset(tmp_req.service_param):
            request.service_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_param, 'ServiceParam', 'json')
        query = {}
        query['AppName'] = request.app_name
        query['Channel'] = request.channel
        query['ExtendParam'] = request.extend_param_shrink
        query['OrderId'] = request.order_id
        query['RequestId'] = request.request_id
        query['ServiceParam'] = request.service_param_shrink
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='WeathermonitorProvinceHour',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorProvinceHourResponse(),
            self.call_api(params, req, runtime)
        )

    async def weathermonitor_province_hour_with_options_async(
        self,
        tmp_req: aliyunape_20210908_models.WeathermonitorProvinceHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorProvinceHourResponse:
        UtilClient.validate_model(tmp_req)
        request = aliyunape_20210908_models.WeathermonitorProvinceHourShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_param):
            request.extend_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_param, 'ExtendParam', 'json')
        if not UtilClient.is_unset(tmp_req.service_param):
            request.service_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_param, 'ServiceParam', 'json')
        query = {}
        query['AppName'] = request.app_name
        query['Channel'] = request.channel
        query['ExtendParam'] = request.extend_param_shrink
        query['OrderId'] = request.order_id
        query['RequestId'] = request.request_id
        query['ServiceParam'] = request.service_param_shrink
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='WeathermonitorProvinceHour',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorProvinceHourResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def weathermonitor_province_hour(
        self,
        request: aliyunape_20210908_models.WeathermonitorProvinceHourRequest,
    ) -> aliyunape_20210908_models.WeathermonitorProvinceHourResponse:
        runtime = util_models.RuntimeOptions()
        return self.weathermonitor_province_hour_with_options(request, runtime)

    async def weathermonitor_province_hour_async(
        self,
        request: aliyunape_20210908_models.WeathermonitorProvinceHourRequest,
    ) -> aliyunape_20210908_models.WeathermonitorProvinceHourResponse:
        runtime = util_models.RuntimeOptions()
        return await self.weathermonitor_province_hour_with_options_async(request, runtime)
