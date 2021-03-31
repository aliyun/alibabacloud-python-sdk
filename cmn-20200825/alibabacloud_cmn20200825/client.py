# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cmn20200825 import models as cmn_20200825_models
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
        self._endpoint = self.get_endpoint('cmn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDedicatedLineResponse(),
            self.do_rpcrequest('CreateDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDedicatedLineResponse(),
            await self.do_rpcrequest_async('CreateDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_line(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_line_with_options(request, runtime)

    async def create_dedicated_line_async(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_line_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceResponse(),
            self.do_rpcrequest('CreateDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceResponse(),
            await self.do_rpcrequest_async('CreateDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_device_form_with_options(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceFormResponse(),
            self.do_rpcrequest('CreateDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_form_with_options_async(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceFormResponse(),
            await self.do_rpcrequest_async('CreateDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_form(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_form_with_options(request, runtime)

    async def create_device_form_async(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_form_with_options_async(request, runtime)

    def create_device_property_with_options(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicePropertyResponse(),
            self.do_rpcrequest('CreateDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_property_with_options_async(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicePropertyResponse(),
            await self.do_rpcrequest_async('CreateDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_property(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_property_with_options(request, runtime)

    async def create_device_property_async(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_property_with_options_async(request, runtime)

    def create_monitor_item_with_options(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateMonitorItemResponse(),
            self.do_rpcrequest('CreateMonitorItem', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_item_with_options_async(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateMonitorItemResponse(),
            await self.do_rpcrequest_async('CreateMonitorItem', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_item(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_item_with_options(request, runtime)

    async def create_monitor_item_async(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_item_with_options_async(request, runtime)

    def create_physical_space_with_options(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreatePhysicalSpaceResponse(),
            self.do_rpcrequest('CreatePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreatePhysicalSpaceResponse(),
            await self.do_rpcrequest_async('CreatePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_space(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_space_with_options(request, runtime)

    async def create_physical_space_async(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_space_with_options_async(request, runtime)

    def create_realtime_task_with_options(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateRealtimeTaskResponse(),
            self.do_rpcrequest('CreateRealtimeTask', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_realtime_task_with_options_async(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateRealtimeTaskResponse(),
            await self.do_rpcrequest_async('CreateRealtimeTask', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_realtime_task(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_realtime_task_with_options(request, runtime)

    async def create_realtime_task_async(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_realtime_task_with_options_async(request, runtime)

    def create_time_period_with_options(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTimePeriodResponse(),
            self.do_rpcrequest('CreateTimePeriod', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_time_period_with_options_async(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTimePeriodResponse(),
            await self.do_rpcrequest_async('CreateTimePeriod', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_time_period(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_time_period_with_options(request, runtime)

    async def create_time_period_async(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_time_period_with_options_async(request, runtime)

    def delete_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDedicatedLineResponse(),
            self.do_rpcrequest('DeleteDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDedicatedLineResponse(),
            await self.do_rpcrequest_async('DeleteDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_line(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_line_with_options(request, runtime)

    async def delete_dedicated_line_async(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_line_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResponse(),
            self.do_rpcrequest('DeleteDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResponse(),
            await self.do_rpcrequest_async('DeleteDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_device_form_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceFormResponse(),
            self.do_rpcrequest('DeleteDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_form_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceFormResponse(),
            await self.do_rpcrequest_async('DeleteDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device_form(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_form_with_options(request, runtime)

    async def delete_device_form_async(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_form_with_options_async(request, runtime)

    def delete_device_property_with_options(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicePropertyResponse(),
            self.do_rpcrequest('DeleteDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_property_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicePropertyResponse(),
            await self.do_rpcrequest_async('DeleteDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device_property(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_property_with_options(request, runtime)

    async def delete_device_property_async(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_property_with_options_async(request, runtime)

    def delete_inspection_task_with_options(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteInspectionTaskResponse(),
            self.do_rpcrequest('DeleteInspectionTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_inspection_task_with_options_async(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteInspectionTaskResponse(),
            await self.do_rpcrequest_async('DeleteInspectionTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_inspection_task(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_inspection_task_with_options(request, runtime)

    async def delete_inspection_task_async(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_inspection_task_with_options_async(request, runtime)

    def delete_physical_space_with_options(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeletePhysicalSpaceResponse(),
            self.do_rpcrequest('DeletePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeletePhysicalSpaceResponse(),
            await self.do_rpcrequest_async('DeletePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_physical_space(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_space_with_options(request, runtime)

    async def delete_physical_space_async(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_physical_space_with_options_async(request, runtime)

    def disable_notification_with_options(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DisableNotificationResponse(),
            self.do_rpcrequest('DisableNotification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_notification_with_options_async(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DisableNotificationResponse(),
            await self.do_rpcrequest_async('DisableNotification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_notification(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_notification_with_options(request, runtime)

    async def disable_notification_async(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_notification_with_options_async(request, runtime)

    def enable_notification_with_options(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.EnableNotificationResponse(),
            self.do_rpcrequest('EnableNotification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_notification_with_options_async(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.EnableNotificationResponse(),
            await self.do_rpcrequest_async('EnableNotification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_notification(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_notification_with_options(request, runtime)

    async def enable_notification_async(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_notification_with_options_async(request, runtime)

    def get_alarm_status_with_options(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetAlarmStatusResponse(),
            self.do_rpcrequest('GetAlarmStatus', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_alarm_status_with_options_async(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetAlarmStatusResponse(),
            await self.do_rpcrequest_async('GetAlarmStatus', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_alarm_status(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alarm_status_with_options(request, runtime)

    async def get_alarm_status_async(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alarm_status_with_options_async(request, runtime)

    def get_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDedicatedLineResponse(),
            self.do_rpcrequest('GetDedicatedLine', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDedicatedLineResponse(),
            await self.do_rpcrequest_async('GetDedicatedLine', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_dedicated_line(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dedicated_line_with_options(request, runtime)

    async def get_dedicated_line_async(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dedicated_line_with_options_async(request, runtime)

    def get_device_with_options(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResponse(),
            self.do_rpcrequest('GetDevice', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResponse(),
            await self.do_rpcrequest_async('GetDevice', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
    ) -> cmn_20200825_models.GetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_with_options(request, runtime)

    async def get_device_async(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
    ) -> cmn_20200825_models.GetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_with_options_async(request, runtime)

    def get_device_config_with_options(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigResponse(),
            self.do_rpcrequest('GetDeviceConfig', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_config_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigResponse(),
            await self.do_rpcrequest_async('GetDeviceConfig', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device_config(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    async def get_device_config_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_with_options_async(request, runtime)

    def get_device_config_diff_with_options(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDiffResponse(),
            self.do_rpcrequest('GetDeviceConfigDiff', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_config_diff_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDiffResponse(),
            await self.do_rpcrequest_async('GetDeviceConfigDiff', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device_config_diff(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_diff_with_options(request, runtime)

    async def get_device_config_diff_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_diff_with_options_async(request, runtime)

    def get_device_form_with_options(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceFormResponse(),
            self.do_rpcrequest('GetDeviceForm', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_form_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceFormResponse(),
            await self.do_rpcrequest_async('GetDeviceForm', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device_form(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_form_with_options(request, runtime)

    async def get_device_form_async(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_form_with_options_async(request, runtime)

    def get_device_property_with_options(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDevicePropertyResponse(),
            self.do_rpcrequest('GetDeviceProperty', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_property_with_options_async(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDevicePropertyResponse(),
            await self.do_rpcrequest_async('GetDeviceProperty', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device_property(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_property_with_options(request, runtime)

    async def get_device_property_async(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_property_with_options_async(request, runtime)

    def get_inspection_task_with_options(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetInspectionTaskResponse(),
            self.do_rpcrequest('GetInspectionTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_inspection_task_with_options_async(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetInspectionTaskResponse(),
            await self.do_rpcrequest_async('GetInspectionTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_inspection_task(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inspection_task_with_options(request, runtime)

    async def get_inspection_task_async(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inspection_task_with_options_async(request, runtime)

    def get_physical_space_with_options(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceResponse(),
            self.do_rpcrequest('GetPhysicalSpace', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceResponse(),
            await self.do_rpcrequest_async('GetPhysicalSpace', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_physical_space(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_with_options(request, runtime)

    async def get_physical_space_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_space_with_options_async(request, runtime)

    def get_realtime_task_with_options(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetRealtimeTaskResponse(),
            self.do_rpcrequest('GetRealtimeTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_realtime_task_with_options_async(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetRealtimeTaskResponse(),
            await self.do_rpcrequest_async('GetRealtimeTask', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_realtime_task(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_task_with_options(request, runtime)

    async def get_realtime_task_async(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_task_with_options_async(request, runtime)

    def list_alarm_status_with_options(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusResponse(),
            self.do_rpcrequest('ListAlarmStatus', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_status_with_options_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusResponse(),
            await self.do_rpcrequest_async('ListAlarmStatus', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_status(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_with_options(request, runtime)

    async def list_alarm_status_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_status_with_options_async(request, runtime)

    def list_alarm_status_histories_with_options(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusHistoriesResponse(),
            self.do_rpcrequest('ListAlarmStatusHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_status_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusHistoriesResponse(),
            await self.do_rpcrequest_async('ListAlarmStatusHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_status_histories(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_histories_with_options(request, runtime)

    async def list_alarm_status_histories_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_status_histories_with_options_async(request, runtime)

    def list_dedicated_lines_with_options(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDedicatedLinesResponse(),
            self.do_rpcrequest('ListDedicatedLines', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_dedicated_lines_with_options_async(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDedicatedLinesResponse(),
            await self.do_rpcrequest_async('ListDedicatedLines', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_dedicated_lines(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dedicated_lines_with_options(request, runtime)

    async def list_dedicated_lines_async(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dedicated_lines_with_options_async(request, runtime)

    def list_device_forms_with_options(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceFormsResponse(),
            self.do_rpcrequest('ListDeviceForms', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_forms_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceFormsResponse(),
            await self.do_rpcrequest_async('ListDeviceForms', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_forms(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_forms_with_options(request, runtime)

    async def list_device_forms_async(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_forms_with_options_async(request, runtime)

    def list_device_properties_with_options(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicePropertiesResponse(),
            self.do_rpcrequest('ListDeviceProperties', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_properties_with_options_async(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicePropertiesResponse(),
            await self.do_rpcrequest_async('ListDeviceProperties', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_properties(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_properties_with_options(request, runtime)

    async def list_device_properties_async(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_properties_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicesResponse(),
            self.do_rpcrequest('ListDevices', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicesResponse(),
            await self.do_rpcrequest_async('ListDevices', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devices(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
    ) -> cmn_20200825_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
    ) -> cmn_20200825_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_device_values_with_options(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceValuesResponse(),
            self.do_rpcrequest('ListDeviceValues', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_values_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceValuesResponse(),
            await self.do_rpcrequest_async('ListDeviceValues', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_values(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_values_with_options(request, runtime)

    async def list_device_values_async(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_values_with_options_async(request, runtime)

    def list_inspection_tasks_with_options(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTasksResponse(),
            self.do_rpcrequest('ListInspectionTasks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_inspection_tasks_with_options_async(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTasksResponse(),
            await self.do_rpcrequest_async('ListInspectionTasks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_inspection_tasks(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_tasks_with_options(request, runtime)

    async def list_inspection_tasks_async(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_tasks_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListInstancesResponse(),
            await self.do_rpcrequest_async('ListInstances', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_instances(self) -> cmn_20200825_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(runtime)

    async def list_instances_async(self) -> cmn_20200825_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(runtime)

    def list_monitor_data_with_options(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListMonitorDataResponse(),
            self.do_rpcrequest('ListMonitorData', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_monitor_data_with_options_async(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListMonitorDataResponse(),
            await self.do_rpcrequest_async('ListMonitorData', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_monitor_data(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_monitor_data_with_options(request, runtime)

    async def list_monitor_data_async(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_monitor_data_with_options_async(request, runtime)

    def list_notification_histories_with_options(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesResponse(),
            self.do_rpcrequest('ListNotificationHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_notification_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesResponse(),
            await self.do_rpcrequest_async('ListNotificationHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_notification_histories(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notification_histories_with_options(request, runtime)

    async def list_notification_histories_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notification_histories_with_options_async(request, runtime)

    def list_physical_spaces_with_options(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListPhysicalSpacesResponse(),
            self.do_rpcrequest('ListPhysicalSpaces', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_physical_spaces_with_options_async(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListPhysicalSpacesResponse(),
            await self.do_rpcrequest_async('ListPhysicalSpaces', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_physical_spaces(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_physical_spaces_with_options(request, runtime)

    async def list_physical_spaces_async(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_physical_spaces_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListRegionsResponse(),
            await self.do_rpcrequest_async('ListRegions', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_regions(self) -> cmn_20200825_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> cmn_20200825_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_tasks_histories_with_options(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTasksHistoriesResponse(),
            self.do_rpcrequest('ListTasksHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_tasks_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTasksHistoriesResponse(),
            await self.do_rpcrequest_async('ListTasksHistories', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tasks_histories(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_histories_with_options(request, runtime)

    async def list_tasks_histories_async(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_histories_with_options_async(request, runtime)

    def retry_tasks_with_options(
        self,
        tmp_req: cmn_20200825_models.RetryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RetryTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.RetryTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_tasks):
            request.retry_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_tasks, 'RetryTasks', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.RetryTasksResponse(),
            self.do_rpcrequest('RetryTasks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def retry_tasks_with_options_async(
        self,
        tmp_req: cmn_20200825_models.RetryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RetryTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.RetryTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_tasks):
            request.retry_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_tasks, 'RetryTasks', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.RetryTasksResponse(),
            await self.do_rpcrequest_async('RetryTasks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def retry_tasks(
        self,
        request: cmn_20200825_models.RetryTasksRequest,
    ) -> cmn_20200825_models.RetryTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_tasks_with_options(request, runtime)

    async def retry_tasks_async(
        self,
        request: cmn_20200825_models.RetryTasksRequest,
    ) -> cmn_20200825_models.RetryTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_tasks_with_options_async(request, runtime)

    def update_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDedicatedLineResponse(),
            self.do_rpcrequest('UpdateDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDedicatedLineResponse(),
            await self.do_rpcrequest_async('UpdateDedicatedLine', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dedicated_line(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dedicated_line_with_options(request, runtime)

    async def update_dedicated_line_async(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dedicated_line_with_options_async(request, runtime)

    def update_device_with_options(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResponse(),
            self.do_rpcrequest('UpdateDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResponse(),
            await self.do_rpcrequest_async('UpdateDevice', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    async def update_device_async(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_with_options_async(request, runtime)

    def update_device_form_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceFormShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_list):
            request.attribute_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_list, 'AttributeList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceFormResponse(),
            self.do_rpcrequest('UpdateDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_form_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceFormShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_list):
            request.attribute_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_list, 'AttributeList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceFormResponse(),
            await self.do_rpcrequest_async('UpdateDeviceForm', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_form(
        self,
        request: cmn_20200825_models.UpdateDeviceFormRequest,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_form_with_options(request, runtime)

    async def update_device_form_async(
        self,
        request: cmn_20200825_models.UpdateDeviceFormRequest,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_form_with_options_async(request, runtime)

    def update_device_property_with_options(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicePropertyResponse(),
            self.do_rpcrequest('UpdateDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_property_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicePropertyResponse(),
            await self.do_rpcrequest_async('UpdateDeviceProperty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_property(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_property_with_options(request, runtime)

    async def update_device_property_async(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_property_with_options_async(request, runtime)

    def update_devices_with_options(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicesResponse(),
            self.do_rpcrequest('UpdateDevices', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_devices_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicesResponse(),
            await self.do_rpcrequest_async('UpdateDevices', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devices(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_devices_with_options(request, runtime)

    async def update_devices_async(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_devices_with_options_async(request, runtime)

    def update_physical_space_with_options(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdatePhysicalSpaceResponse(),
            self.do_rpcrequest('UpdatePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdatePhysicalSpaceResponse(),
            await self.do_rpcrequest_async('UpdatePhysicalSpace', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_physical_space(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_physical_space_with_options(request, runtime)

    async def update_physical_space_async(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_physical_space_with_options_async(request, runtime)
