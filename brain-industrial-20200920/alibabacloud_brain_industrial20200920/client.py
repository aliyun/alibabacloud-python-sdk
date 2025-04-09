# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_brain_industrial20200920 import models as brain_industrial_20200920_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_license_with_options(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ActivateLicenseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ActivateLicenseResponse(),
                self.execute(params, req, runtime)
            )

    async def activate_license_with_options_async(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ActivateLicenseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ActivateLicenseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def activate_license(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def aics_open_api_invoke_with_options(
        self,
        tmp_req: brain_industrial_20200920_models.AicsOpenApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.AicsOpenApiInvokeResponse:
        """
        @summary 调用aics openapi
        
        @param tmp_req: AicsOpenApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AicsOpenApiInvokeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.AicsOpenApiInvokeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.param, 'Param', 'json')
        query = {}
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.param_shrink):
            body['Param'] = request.param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AicsOpenApiInvoke',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.AicsOpenApiInvokeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.AicsOpenApiInvokeResponse(),
                self.execute(params, req, runtime)
            )

    async def aics_open_api_invoke_with_options_async(
        self,
        tmp_req: brain_industrial_20200920_models.AicsOpenApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.AicsOpenApiInvokeResponse:
        """
        @summary 调用aics openapi
        
        @param tmp_req: AicsOpenApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AicsOpenApiInvokeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.AicsOpenApiInvokeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.param, 'Param', 'json')
        query = {}
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.param_shrink):
            body['Param'] = request.param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AicsOpenApiInvoke',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.AicsOpenApiInvokeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.AicsOpenApiInvokeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def aics_open_api_invoke(
        self,
        request: brain_industrial_20200920_models.AicsOpenApiInvokeRequest,
    ) -> brain_industrial_20200920_models.AicsOpenApiInvokeResponse:
        """
        @summary 调用aics openapi
        
        @param request: AicsOpenApiInvokeRequest
        @return: AicsOpenApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.aics_open_api_invoke_with_options(request, runtime)

    async def aics_open_api_invoke_async(
        self,
        request: brain_industrial_20200920_models.AicsOpenApiInvokeRequest,
    ) -> brain_industrial_20200920_models.AicsOpenApiInvokeResponse:
        """
        @summary 调用aics openapi
        
        @param request: AicsOpenApiInvokeRequest
        @return: AicsOpenApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.aics_open_api_invoke_with_options_async(request, runtime)

    def create_ess_opt_job_with_options(
        self,
        tmp_req: brain_industrial_20200920_models.CreateEssOptJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreateEssOptJobResponse:
        """
        @summary 创建储能运行优化任务
        
        @param tmp_req: CreateEssOptJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEssOptJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreateEssOptJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.elec_price):
            request.elec_price_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.elec_price, 'ElecPrice', 'json')
        if not UtilClient.is_unset(tmp_req.gen_price):
            request.gen_price_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gen_price, 'GenPrice', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.system_data):
            request.system_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.system_data, 'SystemData', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.elec_price_shrink):
            body['ElecPrice'] = request.elec_price_shrink
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.gen_price_shrink):
            body['GenPrice'] = request.gen_price_shrink
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_data_shrink):
            body['SystemData'] = request.system_data_shrink
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.topo_type):
            body['TopoType'] = request.topo_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEssOptJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateEssOptJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateEssOptJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_ess_opt_job_with_options_async(
        self,
        tmp_req: brain_industrial_20200920_models.CreateEssOptJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreateEssOptJobResponse:
        """
        @summary 创建储能运行优化任务
        
        @param tmp_req: CreateEssOptJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEssOptJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreateEssOptJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.elec_price):
            request.elec_price_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.elec_price, 'ElecPrice', 'json')
        if not UtilClient.is_unset(tmp_req.gen_price):
            request.gen_price_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gen_price, 'GenPrice', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.system_data):
            request.system_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.system_data, 'SystemData', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.elec_price_shrink):
            body['ElecPrice'] = request.elec_price_shrink
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.gen_price_shrink):
            body['GenPrice'] = request.gen_price_shrink
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_data_shrink):
            body['SystemData'] = request.system_data_shrink
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.topo_type):
            body['TopoType'] = request.topo_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEssOptJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateEssOptJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateEssOptJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_ess_opt_job(
        self,
        request: brain_industrial_20200920_models.CreateEssOptJobRequest,
    ) -> brain_industrial_20200920_models.CreateEssOptJobResponse:
        """
        @summary 创建储能运行优化任务
        
        @param request: CreateEssOptJobRequest
        @return: CreateEssOptJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ess_opt_job_with_options(request, runtime)

    async def create_ess_opt_job_async(
        self,
        request: brain_industrial_20200920_models.CreateEssOptJobRequest,
    ) -> brain_industrial_20200920_models.CreateEssOptJobResponse:
        """
        @summary 创建储能运行优化任务
        
        @param request: CreateEssOptJobRequest
        @return: CreateEssOptJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ess_opt_job_with_options_async(request, runtime)

    def create_load_forecast_job_with_options(
        self,
        tmp_req: brain_industrial_20200920_models.CreateLoadForecastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreateLoadForecastJobResponse:
        """
        @summary 创建用电负荷预测任务
        
        @param tmp_req: CreateLoadForecastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadForecastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreateLoadForecastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.history_data):
            request.history_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadForecastJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateLoadForecastJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateLoadForecastJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_load_forecast_job_with_options_async(
        self,
        tmp_req: brain_industrial_20200920_models.CreateLoadForecastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreateLoadForecastJobResponse:
        """
        @summary 创建用电负荷预测任务
        
        @param tmp_req: CreateLoadForecastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadForecastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreateLoadForecastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.history_data):
            request.history_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadForecastJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateLoadForecastJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreateLoadForecastJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_load_forecast_job(
        self,
        request: brain_industrial_20200920_models.CreateLoadForecastJobRequest,
    ) -> brain_industrial_20200920_models.CreateLoadForecastJobResponse:
        """
        @summary 创建用电负荷预测任务
        
        @param request: CreateLoadForecastJobRequest
        @return: CreateLoadForecastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_forecast_job_with_options(request, runtime)

    async def create_load_forecast_job_async(
        self,
        request: brain_industrial_20200920_models.CreateLoadForecastJobRequest,
    ) -> brain_industrial_20200920_models.CreateLoadForecastJobResponse:
        """
        @summary 创建用电负荷预测任务
        
        @param request: CreateLoadForecastJobRequest
        @return: CreateLoadForecastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_forecast_job_with_options_async(request, runtime)

    def create_power_forecast_job_with_options(
        self,
        tmp_req: brain_industrial_20200920_models.CreatePowerForecastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreatePowerForecastJobResponse:
        """
        @summary 创建发电功率预测任务
        
        @param tmp_req: CreatePowerForecastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePowerForecastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreatePowerForecastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.history_data):
            request.history_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePowerForecastJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreatePowerForecastJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreatePowerForecastJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_power_forecast_job_with_options_async(
        self,
        tmp_req: brain_industrial_20200920_models.CreatePowerForecastJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.CreatePowerForecastJobResponse:
        """
        @summary 创建发电功率预测任务
        
        @param tmp_req: CreatePowerForecastJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePowerForecastJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = brain_industrial_20200920_models.CreatePowerForecastJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.history_data):
            request.history_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.history_data, 'HistoryData', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.freq):
            body['Freq'] = request.freq
        if not UtilClient.is_unset(request.history_data_shrink):
            body['HistoryData'] = request.history_data_shrink
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.run_date):
            body['RunDate'] = request.run_date
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePowerForecastJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreatePowerForecastJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.CreatePowerForecastJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_power_forecast_job(
        self,
        request: brain_industrial_20200920_models.CreatePowerForecastJobRequest,
    ) -> brain_industrial_20200920_models.CreatePowerForecastJobResponse:
        """
        @summary 创建发电功率预测任务
        
        @param request: CreatePowerForecastJobRequest
        @return: CreatePowerForecastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_power_forecast_job_with_options(request, runtime)

    async def create_power_forecast_job_async(
        self,
        request: brain_industrial_20200920_models.CreatePowerForecastJobRequest,
    ) -> brain_industrial_20200920_models.CreatePowerForecastJobResponse:
        """
        @summary 创建发电功率预测任务
        
        @param request: CreatePowerForecastJobRequest
        @return: CreatePowerForecastJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_power_forecast_job_with_options_async(request, runtime)

    def get_aivpp_algo_job_with_options(
        self,
        request: brain_industrial_20200920_models.GetAivppAlgoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetAivppAlgoJobResponse:
        """
        @summary 查询aivpp算法job
        
        @param request: GetAivppAlgoJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAivppAlgoJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAivppAlgoJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetAivppAlgoJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetAivppAlgoJobResponse(),
                self.execute(params, req, runtime)
            )

    async def get_aivpp_algo_job_with_options_async(
        self,
        request: brain_industrial_20200920_models.GetAivppAlgoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetAivppAlgoJobResponse:
        """
        @summary 查询aivpp算法job
        
        @param request: GetAivppAlgoJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAivppAlgoJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAivppAlgoJob',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetAivppAlgoJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetAivppAlgoJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_aivpp_algo_job(
        self,
        request: brain_industrial_20200920_models.GetAivppAlgoJobRequest,
    ) -> brain_industrial_20200920_models.GetAivppAlgoJobResponse:
        """
        @summary 查询aivpp算法job
        
        @param request: GetAivppAlgoJobRequest
        @return: GetAivppAlgoJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aivpp_algo_job_with_options(request, runtime)

    async def get_aivpp_algo_job_async(
        self,
        request: brain_industrial_20200920_models.GetAivppAlgoJobRequest,
    ) -> brain_industrial_20200920_models.GetAivppAlgoJobResponse:
        """
        @summary 查询aivpp算法job
        
        @param request: GetAivppAlgoJobRequest
        @return: GetAivppAlgoJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aivpp_algo_job_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetLicenseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetLicenseResponse(),
                self.execute(params, req, runtime)
            )

    async def get_license_with_options_async(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetLicenseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.GetLicenseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_license(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @return: GetLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    async def get_license_async(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @return: GetLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_license_with_options_async(request, runtime)

    def list_aivpp_resources_with_options(
        self,
        request: brain_industrial_20200920_models.ListAivppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListAivppResourcesResponse:
        """
        @summary 获取用户AIVPP资源列表
        
        @param request: ListAivppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAivppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAivppResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListAivppResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListAivppResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_aivpp_resources_with_options_async(
        self,
        request: brain_industrial_20200920_models.ListAivppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListAivppResourcesResponse:
        """
        @summary 获取用户AIVPP资源列表
        
        @param request: ListAivppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAivppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAivppResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListAivppResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListAivppResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_aivpp_resources(
        self,
        request: brain_industrial_20200920_models.ListAivppResourcesRequest,
    ) -> brain_industrial_20200920_models.ListAivppResourcesResponse:
        """
        @summary 获取用户AIVPP资源列表
        
        @param request: ListAivppResourcesRequest
        @return: ListAivppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aivpp_resources_with_options(request, runtime)

    async def list_aivpp_resources_async(
        self,
        request: brain_industrial_20200920_models.ListAivppResourcesRequest,
    ) -> brain_industrial_20200920_models.ListAivppResourcesResponse:
        """
        @summary 获取用户AIVPP资源列表
        
        @param request: ListAivppResourcesRequest
        @return: ListAivppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aivpp_resources_with_options_async(request, runtime)

    def list_licenses_with_options(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLicenses',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListLicensesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListLicensesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_licenses_with_options_async(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLicenses',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListLicensesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListLicensesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_licenses(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @return: ListLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_licenses_with_options(request, runtime)

    async def list_licenses_async(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @return: ListLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_licenses_with_options_async(request, runtime)

    def list_user_resources_with_options(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListUserResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListUserResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_user_resources_with_options_async(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListUserResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.ListUserResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_user_resources(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @return: ListUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_resources_with_options(request, runtime)

    async def list_user_resources_async(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @return: ListUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_resources_with_options_async(request, runtime)

    def update_license_description_with_options(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLicenseDescriptionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLicenseDescription',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def update_license_description_with_options_async(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLicenseDescriptionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLicenseDescription',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_license_description(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @return: UpdateLicenseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_license_description_with_options(request, runtime)

    async def update_license_description_async(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @return: UpdateLicenseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_license_description_with_options_async(request, runtime)
