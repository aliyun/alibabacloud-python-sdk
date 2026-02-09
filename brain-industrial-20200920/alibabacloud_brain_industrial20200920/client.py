# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_brain_industrial20200920 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('brain-industrial', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_license_with_options(
        self,
        request: main_models.ActivateLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateLicense',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_license_with_options_async(
        self,
        request: main_models.ActivateLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateLicense',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_license(
        self,
        request: main_models.ActivateLicenseRequest,
    ) -> main_models.ActivateLicenseResponse:
        runtime = RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: main_models.ActivateLicenseRequest,
    ) -> main_models.ActivateLicenseResponse:
        runtime = RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def aics_open_api_invoke_with_options(
        self,
        tmp_req: main_models.AicsOpenApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AicsOpenApiInvokeResponse:
        tmp_req.validate()
        request = main_models.AicsOpenApiInvokeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.param):
            request.param_shrink = Utils.array_to_string_with_specified_style(tmp_req.param, 'Param', 'json')
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.param_shrink):
            body['Param'] = request.param_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AicsOpenApiInvoke',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AicsOpenApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def aics_open_api_invoke_with_options_async(
        self,
        tmp_req: main_models.AicsOpenApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AicsOpenApiInvokeResponse:
        tmp_req.validate()
        request = main_models.AicsOpenApiInvokeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.param):
            request.param_shrink = Utils.array_to_string_with_specified_style(tmp_req.param, 'Param', 'json')
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.param_shrink):
            body['Param'] = request.param_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AicsOpenApiInvoke',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AicsOpenApiInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aics_open_api_invoke(
        self,
        request: main_models.AicsOpenApiInvokeRequest,
    ) -> main_models.AicsOpenApiInvokeResponse:
        runtime = RuntimeOptions()
        return self.aics_open_api_invoke_with_options(request, runtime)

    async def aics_open_api_invoke_async(
        self,
        request: main_models.AicsOpenApiInvokeRequest,
    ) -> main_models.AicsOpenApiInvokeResponse:
        runtime = RuntimeOptions()
        return await self.aics_open_api_invoke_with_options_async(request, runtime)

    def create_ess_opt_job_with_options(
        self,
        tmp_req: main_models.CreateEssOptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEssOptJobResponse:
        tmp_req.validate()
        request = main_models.CreateEssOptJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.elec_price):
            request.elec_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.elec_price, 'ElecPrice', 'json')
        if not DaraCore.is_null(tmp_req.gen_price):
            request.gen_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.gen_price, 'GenPrice', 'json')
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not DaraCore.is_null(tmp_req.system_data):
            request.system_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_data, 'SystemData', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.elec_price_shrink):
            body['ElecPrice'] = request.elec_price_shrink
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.gen_price_shrink):
            body['GenPrice'] = request.gen_price_shrink
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_data_shrink):
            body['SystemData'] = request.system_data_shrink
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.topo_type):
            body['TopoType'] = request.topo_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEssOptJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEssOptJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ess_opt_job_with_options_async(
        self,
        tmp_req: main_models.CreateEssOptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEssOptJobResponse:
        tmp_req.validate()
        request = main_models.CreateEssOptJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.elec_price):
            request.elec_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.elec_price, 'ElecPrice', 'json')
        if not DaraCore.is_null(tmp_req.gen_price):
            request.gen_price_shrink = Utils.array_to_string_with_specified_style(tmp_req.gen_price, 'GenPrice', 'json')
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not DaraCore.is_null(tmp_req.system_data):
            request.system_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.system_data, 'SystemData', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.elec_price_shrink):
            body['ElecPrice'] = request.elec_price_shrink
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.gen_price_shrink):
            body['GenPrice'] = request.gen_price_shrink
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_data_shrink):
            body['SystemData'] = request.system_data_shrink
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.topo_type):
            body['TopoType'] = request.topo_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEssOptJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEssOptJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ess_opt_job(
        self,
        request: main_models.CreateEssOptJobRequest,
    ) -> main_models.CreateEssOptJobResponse:
        runtime = RuntimeOptions()
        return self.create_ess_opt_job_with_options(request, runtime)

    async def create_ess_opt_job_async(
        self,
        request: main_models.CreateEssOptJobRequest,
    ) -> main_models.CreateEssOptJobResponse:
        runtime = RuntimeOptions()
        return await self.create_ess_opt_job_with_options_async(request, runtime)

    def create_load_forecast_by_file_url_job_with_options(
        self,
        request: main_models.CreateLoadForecastByFileUrlJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadForecastByFileUrlJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_url):
            body['HistoryUrl'] = request.history_url
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_column):
            body['TimeColumn'] = request.time_column
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.value_column):
            body['ValueColumn'] = request.value_column
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadForecastByFileUrlJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadForecastByFileUrlJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_forecast_by_file_url_job_with_options_async(
        self,
        request: main_models.CreateLoadForecastByFileUrlJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadForecastByFileUrlJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_url):
            body['HistoryUrl'] = request.history_url
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_column):
            body['TimeColumn'] = request.time_column
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.value_column):
            body['ValueColumn'] = request.value_column
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadForecastByFileUrlJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadForecastByFileUrlJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_forecast_by_file_url_job(
        self,
        request: main_models.CreateLoadForecastByFileUrlJobRequest,
    ) -> main_models.CreateLoadForecastByFileUrlJobResponse:
        runtime = RuntimeOptions()
        return self.create_load_forecast_by_file_url_job_with_options(request, runtime)

    async def create_load_forecast_by_file_url_job_async(
        self,
        request: main_models.CreateLoadForecastByFileUrlJobRequest,
    ) -> main_models.CreateLoadForecastByFileUrlJobResponse:
        runtime = RuntimeOptions()
        return await self.create_load_forecast_by_file_url_job_with_options_async(request, runtime)

    def create_load_forecast_job_with_options(
        self,
        tmp_req: main_models.CreateLoadForecastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadForecastJobResponse:
        tmp_req.validate()
        request = main_models.CreateLoadForecastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history_data):
            request.history_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadForecastJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadForecastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_forecast_job_with_options_async(
        self,
        tmp_req: main_models.CreateLoadForecastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadForecastJobResponse:
        tmp_req.validate()
        request = main_models.CreateLoadForecastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history_data):
            request.history_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadForecastJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadForecastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_forecast_job(
        self,
        request: main_models.CreateLoadForecastJobRequest,
    ) -> main_models.CreateLoadForecastJobResponse:
        runtime = RuntimeOptions()
        return self.create_load_forecast_job_with_options(request, runtime)

    async def create_load_forecast_job_async(
        self,
        request: main_models.CreateLoadForecastJobRequest,
    ) -> main_models.CreateLoadForecastJobResponse:
        runtime = RuntimeOptions()
        return await self.create_load_forecast_job_with_options_async(request, runtime)

    def create_power_forecast_by_file_url_job_with_options(
        self,
        tmp_req: main_models.CreatePowerForecastByFileUrlJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePowerForecastByFileUrlJobResponse:
        tmp_req.validate()
        request = main_models.CreatePowerForecastByFileUrlJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_url):
            body['HistoryUrl'] = request.history_url
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_column):
            body['TimeColumn'] = request.time_column
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.value_column):
            body['ValueColumn'] = request.value_column
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePowerForecastByFileUrlJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePowerForecastByFileUrlJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_power_forecast_by_file_url_job_with_options_async(
        self,
        tmp_req: main_models.CreatePowerForecastByFileUrlJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePowerForecastByFileUrlJobResponse:
        tmp_req.validate()
        request = main_models.CreatePowerForecastByFileUrlJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_url):
            body['HistoryUrl'] = request.history_url
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_column):
            body['TimeColumn'] = request.time_column
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not DaraCore.is_null(request.value_column):
            body['ValueColumn'] = request.value_column
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePowerForecastByFileUrlJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePowerForecastByFileUrlJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_power_forecast_by_file_url_job(
        self,
        request: main_models.CreatePowerForecastByFileUrlJobRequest,
    ) -> main_models.CreatePowerForecastByFileUrlJobResponse:
        runtime = RuntimeOptions()
        return self.create_power_forecast_by_file_url_job_with_options(request, runtime)

    async def create_power_forecast_by_file_url_job_async(
        self,
        request: main_models.CreatePowerForecastByFileUrlJobRequest,
    ) -> main_models.CreatePowerForecastByFileUrlJobResponse:
        runtime = RuntimeOptions()
        return await self.create_power_forecast_by_file_url_job_with_options_async(request, runtime)

    def create_power_forecast_job_with_options(
        self,
        tmp_req: main_models.CreatePowerForecastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePowerForecastJobResponse:
        tmp_req.validate()
        request = main_models.CreatePowerForecastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history_data):
            request.history_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePowerForecastJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePowerForecastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_power_forecast_job_with_options_async(
        self,
        tmp_req: main_models.CreatePowerForecastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePowerForecastJobResponse:
        tmp_req.validate()
        request = main_models.CreatePowerForecastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history_data):
            request.history_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        if not DaraCore.is_null(tmp_req.location):
            request.location_shrink = Utils.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not DaraCore.is_null(request.business_key):
            body['BusinessKey'] = request.business_key
        if not DaraCore.is_null(request.data_mode):
            body['DataMode'] = request.data_mode
        if not DaraCore.is_null(request.device_type):
            body['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.forecast_horizon):
            body['ForecastHorizon'] = request.forecast_horizon
        if not DaraCore.is_null(request.freq):
            body['Freq'] = request.freq
        if not DaraCore.is_null(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not DaraCore.is_null(request.location_shrink):
            body['Location'] = request.location_shrink
        if not DaraCore.is_null(request.model_version):
            body['ModelVersion'] = request.model_version
        if not DaraCore.is_null(request.run_date):
            body['RunDate'] = request.run_date
        if not DaraCore.is_null(request.system_type):
            body['SystemType'] = request.system_type
        if not DaraCore.is_null(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePowerForecastJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePowerForecastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_power_forecast_job(
        self,
        request: main_models.CreatePowerForecastJobRequest,
    ) -> main_models.CreatePowerForecastJobResponse:
        runtime = RuntimeOptions()
        return self.create_power_forecast_job_with_options(request, runtime)

    async def create_power_forecast_job_async(
        self,
        request: main_models.CreatePowerForecastJobRequest,
    ) -> main_models.CreatePowerForecastJobResponse:
        runtime = RuntimeOptions()
        return await self.create_power_forecast_job_with_options_async(request, runtime)

    def get_aivpp_algo_job_with_options(
        self,
        request: main_models.GetAivppAlgoJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAivppAlgoJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAivppAlgoJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAivppAlgoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aivpp_algo_job_with_options_async(
        self,
        request: main_models.GetAivppAlgoJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAivppAlgoJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAivppAlgoJob',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAivppAlgoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aivpp_algo_job(
        self,
        request: main_models.GetAivppAlgoJobRequest,
    ) -> main_models.GetAivppAlgoJobResponse:
        runtime = RuntimeOptions()
        return self.get_aivpp_algo_job_with_options(request, runtime)

    async def get_aivpp_algo_job_async(
        self,
        request: main_models.GetAivppAlgoJobRequest,
    ) -> main_models.GetAivppAlgoJobResponse:
        runtime = RuntimeOptions()
        return await self.get_aivpp_algo_job_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: main_models.GetLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLicense',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_license_with_options_async(
        self,
        request: main_models.GetLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLicense',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_license(
        self,
        request: main_models.GetLicenseRequest,
    ) -> main_models.GetLicenseResponse:
        runtime = RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    async def get_license_async(
        self,
        request: main_models.GetLicenseRequest,
    ) -> main_models.GetLicenseResponse:
        runtime = RuntimeOptions()
        return await self.get_license_with_options_async(request, runtime)

    def list_aivpp_resources_with_options(
        self,
        request: main_models.ListAivppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAivppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAivppResources',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAivppResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aivpp_resources_with_options_async(
        self,
        request: main_models.ListAivppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAivppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAivppResources',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAivppResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aivpp_resources(
        self,
        request: main_models.ListAivppResourcesRequest,
    ) -> main_models.ListAivppResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_aivpp_resources_with_options(request, runtime)

    async def list_aivpp_resources_async(
        self,
        request: main_models.ListAivppResourcesRequest,
    ) -> main_models.ListAivppResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_aivpp_resources_with_options_async(request, runtime)

    def list_licenses_with_options(
        self,
        request: main_models.ListLicensesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLicensesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLicenses',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLicensesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_licenses_with_options_async(
        self,
        request: main_models.ListLicensesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLicensesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLicenses',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLicensesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_licenses(
        self,
        request: main_models.ListLicensesRequest,
    ) -> main_models.ListLicensesResponse:
        runtime = RuntimeOptions()
        return self.list_licenses_with_options(request, runtime)

    async def list_licenses_async(
        self,
        request: main_models.ListLicensesRequest,
    ) -> main_models.ListLicensesResponse:
        runtime = RuntimeOptions()
        return await self.list_licenses_with_options_async(request, runtime)

    def list_user_resources_with_options(
        self,
        request: main_models.ListUserResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserResources',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_resources_with_options_async(
        self,
        request: main_models.ListUserResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserResources',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_resources(
        self,
        request: main_models.ListUserResourcesRequest,
    ) -> main_models.ListUserResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_user_resources_with_options(request, runtime)

    async def list_user_resources_async(
        self,
        request: main_models.ListUserResourcesRequest,
    ) -> main_models.ListUserResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_resources_with_options_async(request, runtime)

    def update_license_description_with_options(
        self,
        request: main_models.UpdateLicenseDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLicenseDescriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLicenseDescription',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLicenseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_license_description_with_options_async(
        self,
        request: main_models.UpdateLicenseDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLicenseDescriptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLicenseDescription',
            version = '2020-09-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLicenseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_license_description(
        self,
        request: main_models.UpdateLicenseDescriptionRequest,
    ) -> main_models.UpdateLicenseDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_license_description_with_options(request, runtime)

    async def update_license_description_async(
        self,
        request: main_models.UpdateLicenseDescriptionRequest,
    ) -> main_models.UpdateLicenseDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_license_description_with_options_async(request, runtime)
