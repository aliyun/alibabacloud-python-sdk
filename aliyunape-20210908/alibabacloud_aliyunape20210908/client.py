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

    def ape_inner_common_api_with_options(
        self,
        request: aliyunape_20210908_models.ApeInnerCommonApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ApeInnerCommonApiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApeInnerCommonApi',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ApeInnerCommonApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def ape_inner_common_api_with_options_async(
        self,
        request: aliyunape_20210908_models.ApeInnerCommonApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ApeInnerCommonApiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApeInnerCommonApi',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ApeInnerCommonApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ape_inner_common_api(
        self,
        request: aliyunape_20210908_models.ApeInnerCommonApiRequest,
    ) -> aliyunape_20210908_models.ApeInnerCommonApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.ape_inner_common_api_with_options(request, runtime)

    async def ape_inner_common_api_async(
        self,
        request: aliyunape_20210908_models.ApeInnerCommonApiRequest,
    ) -> aliyunape_20210908_models.ApeInnerCommonApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ape_inner_common_api_with_options_async(request, runtime)

    def ape_province_station_ref_with_options(
        self,
        request: aliyunape_20210908_models.ApeProvinceStationRefRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ApeProvinceStationRefResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adcode):
            query['Adcode'] = request.adcode
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.cnty):
            query['Cnty'] = request.cnty
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.province_code):
            query['ProvinceCode'] = request.province_code
        if not UtilClient.is_unset(request.province_name):
            query['ProvinceName'] = request.province_name
        if not UtilClient.is_unset(request.station_name):
            query['StationName'] = request.station_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApeProvinceStationRef',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ApeProvinceStationRefResponse(),
            self.call_api(params, req, runtime)
        )

    async def ape_province_station_ref_with_options_async(
        self,
        request: aliyunape_20210908_models.ApeProvinceStationRefRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.ApeProvinceStationRefResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adcode):
            query['Adcode'] = request.adcode
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.cnty):
            query['Cnty'] = request.cnty
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.province_code):
            query['ProvinceCode'] = request.province_code
        if not UtilClient.is_unset(request.province_name):
            query['ProvinceName'] = request.province_name
        if not UtilClient.is_unset(request.station_name):
            query['StationName'] = request.station_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApeProvinceStationRef',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ApeProvinceStationRefResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ape_province_station_ref(
        self,
        request: aliyunape_20210908_models.ApeProvinceStationRefRequest,
    ) -> aliyunape_20210908_models.ApeProvinceStationRefResponse:
        runtime = util_models.RuntimeOptions()
        return self.ape_province_station_ref_with_options(request, runtime)

    async def ape_province_station_ref_async(
        self,
        request: aliyunape_20210908_models.ApeProvinceStationRefRequest,
    ) -> aliyunape_20210908_models.ApeProvinceStationRefResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ape_province_station_ref_with_options_async(request, runtime)

    def historical_with_options(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.station):
            query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Historical',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def historical_with_options_async(
        self,
        request: aliyunape_20210908_models.HistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.HistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.station):
            query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Historical',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            await self.call_api_async(params, req, runtime)
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

    def station_day_with_options(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.StationDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.start_forecast):
            query['StartForecast'] = request.start_forecast
        if not UtilClient.is_unset(request.station):
            query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StationDay',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def station_day_with_options_async(
        self,
        request: aliyunape_20210908_models.StationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.StationDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.start_forecast):
            query['StartForecast'] = request.start_forecast
        if not UtilClient.is_unset(request.station):
            query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StationDay',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lon):
            query['Lon'] = request.lon
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.start_forecast):
            query['StartForecast'] = request.start_forecast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Weatherforecast',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            self.call_api(params, req, runtime)
        )

    async def weatherforecast_with_options_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lon):
            query['Lon'] = request.lon
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.start_forecast):
            query['StartForecast'] = request.start_forecast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Weatherforecast',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            await self.call_api_async(params, req, runtime)
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

    def weatherforecast_time_with_options(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_hour):
            query['CurHour'] = request.cur_hour
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lon):
            query['Lon'] = request.lon
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WeatherforecastTime',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def weatherforecast_time_with_options_async(
        self,
        request: aliyunape_20210908_models.WeatherforecastTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeatherforecastTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_hour):
            query['CurHour'] = request.cur_hour
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lon):
            query['Lon'] = request.lon
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WeatherforecastTime',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def weathermonitor_with_options(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_hour):
            query['CurHour'] = request.cur_hour
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Weathermonitor',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def weathermonitor_with_options_async(
        self,
        request: aliyunape_20210908_models.WeathermonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aliyunape_20210908_models.WeathermonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_hour):
            query['CurHour'] = request.cur_hour
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Weathermonitor',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            await self.call_api_async(params, req, runtime)
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
