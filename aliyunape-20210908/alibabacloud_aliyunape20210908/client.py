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

    def weathermonitor_with_options(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            self.do_rpcrequest('Weathermonitor', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def weathermonitor_with_options_async(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            await self.do_rpcrequest_async('Weathermonitor', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weathermonitor(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.weathermonitor_with_options(request, runtime)

    async def weathermonitor_async(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.weathermonitor_with_options_async(request, runtime)

    def weatherforecast_time_with_options(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            self.do_rpcrequest('WeatherforecastTime', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def weatherforecast_time_with_options_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            await self.do_rpcrequest_async('WeatherforecastTime', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weatherforecast_time(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_time_with_options(request, runtime)

    async def weatherforecast_time_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.weatherforecast_time_with_options_async(request, runtime)

    def station_day_with_options(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.StationDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            self.do_rpcrequest('StationDay', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def station_day_with_options_async(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.StationDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            await self.do_rpcrequest_async('StationDay', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def station_day(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
    ) -> aliyunape_20210908_models.StationDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.station_day_with_options(request, runtime)

    async def station_day_async(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
    ) -> aliyunape_20210908_models.StationDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.station_day_with_options_async(request, runtime)

    def weatherforecast_with_options(
        self,
        request: aliyunape_20210908_models.WeatherforecastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            self.do_rpcrequest('Weatherforecast', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def weatherforecast_with_options_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            await self.do_rpcrequest_async('Weatherforecast', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weatherforecast(
        self,
        request: aliyunape_20210908_models.WeatherforecastRequest,
    ) -> aliyunape_20210908_models.WeatherforecastResponse:
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_with_options(request, runtime)

    async def weatherforecast_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastRequest,
    ) -> aliyunape_20210908_models.WeatherforecastResponse:
        runtime = util_models.RuntimeOptions()
        return await self.weatherforecast_with_options_async(request, runtime)

    def historical_with_options(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            self.do_rpcrequest('Historical', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def historical_with_options_async(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            await self.do_rpcrequest_async('Historical', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def historical(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.historical_with_options(request, runtime)

    async def historical_async(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.historical_with_options_async(request, runtime)
