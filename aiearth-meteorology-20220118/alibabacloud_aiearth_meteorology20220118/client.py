# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiearth_meteorology20220118 import models as aiearth__meteorology_20220118_models
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
        self._endpoint = self.get_endpoint('aiearth-meteorology', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def daily_weather_query(
        self,
        request: aiearth__meteorology_20220118_models.DailyWeatherQueryRequest,
    ) -> aiearth__meteorology_20220118_models.DailyWeatherQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.daily_weather_query_with_options(request, headers, runtime)

    async def daily_weather_query_async(
        self,
        request: aiearth__meteorology_20220118_models.DailyWeatherQueryRequest,
    ) -> aiearth__meteorology_20220118_models.DailyWeatherQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.daily_weather_query_with_options_async(request, headers, runtime)

    def daily_weather_query_with_options(
        self,
        request: aiearth__meteorology_20220118_models.DailyWeatherQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20220118_models.DailyWeatherQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.location):
            query['location'] = request.location
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DailyWeatherQuery',
            version='2022-01-18',
            protocol='HTTPS',
            pathname=f'/weather/v2/daily',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__meteorology_20220118_models.DailyWeatherQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def daily_weather_query_with_options_async(
        self,
        request: aiearth__meteorology_20220118_models.DailyWeatherQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20220118_models.DailyWeatherQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.location):
            query['location'] = request.location
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DailyWeatherQuery',
            version='2022-01-18',
            protocol='HTTPS',
            pathname=f'/weather/v2/daily',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__meteorology_20220118_models.DailyWeatherQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grid_weather_query(
        self,
        request: aiearth__meteorology_20220118_models.GridWeatherQueryRequest,
    ) -> aiearth__meteorology_20220118_models.GridWeatherQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grid_weather_query_with_options(request, headers, runtime)

    async def grid_weather_query_async(
        self,
        request: aiearth__meteorology_20220118_models.GridWeatherQueryRequest,
    ) -> aiearth__meteorology_20220118_models.GridWeatherQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grid_weather_query_with_options_async(request, headers, runtime)

    def grid_weather_query_with_options(
        self,
        request: aiearth__meteorology_20220118_models.GridWeatherQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20220118_models.GridWeatherQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.observation_timestamp):
            query['observationTimestamp'] = request.observation_timestamp
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.report_timestamp):
            query['reportTimestamp'] = request.report_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GridWeatherQuery',
            version='2022-01-18',
            protocol='HTTPS',
            pathname=f'/weather/v2/grid',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__meteorology_20220118_models.GridWeatherQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def grid_weather_query_with_options_async(
        self,
        request: aiearth__meteorology_20220118_models.GridWeatherQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20220118_models.GridWeatherQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.observation_timestamp):
            query['observationTimestamp'] = request.observation_timestamp
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.report_timestamp):
            query['reportTimestamp'] = request.report_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GridWeatherQuery',
            version='2022-01-18',
            protocol='HTTPS',
            pathname=f'/weather/v2/grid',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__meteorology_20220118_models.GridWeatherQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )
