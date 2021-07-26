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

    def create_configuration_specification_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationSpecificationResponse(),
            self.do_rpcrequest('CreateConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_configuration_specification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationSpecificationResponse(),
            await self.do_rpcrequest_async('CreateConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_configuration_specification(
        self,
        request: cmn_20200825_models.CreateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_specification_with_options(request, runtime)

    async def create_configuration_specification_async(
        self,
        request: cmn_20200825_models.CreateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_configuration_specification_with_options_async(request, runtime)

    def create_ip_block_with_options(
        self,
        request: cmn_20200825_models.CreateIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpBlockResponse(),
            self.do_rpcrequest('CreateIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ip_block_with_options_async(
        self,
        request: cmn_20200825_models.CreateIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpBlockResponse(),
            await self.do_rpcrequest_async('CreateIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ip_block(
        self,
        request: cmn_20200825_models.CreateIpBlockRequest,
    ) -> cmn_20200825_models.CreateIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_block_with_options(request, runtime)

    async def create_ip_block_async(
        self,
        request: cmn_20200825_models.CreateIpBlockRequest,
    ) -> cmn_20200825_models.CreateIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_block_with_options_async(request, runtime)

    def update_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationVariateResponse(),
            self.do_rpcrequest('UpdateConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationVariateResponse(),
            await self.do_rpcrequest_async('UpdateConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_configuration_variate(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_variate_with_options(request, runtime)

    async def update_configuration_variate_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_configuration_variate_with_options_async(request, runtime)

    def get_schedule_type_with_options(
        self,
        request: cmn_20200825_models.GetScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleTypeResponse(),
            self.do_rpcrequest('GetScheduleType', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_schedule_type_with_options_async(
        self,
        request: cmn_20200825_models.GetScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleTypeResponse(),
            await self.do_rpcrequest_async('GetScheduleType', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_schedule_type(
        self,
        request: cmn_20200825_models.GetScheduleTypeRequest,
    ) -> cmn_20200825_models.GetScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schedule_type_with_options(request, runtime)

    async def get_schedule_type_async(
        self,
        request: cmn_20200825_models.GetScheduleTypeRequest,
    ) -> cmn_20200825_models.GetScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schedule_type_with_options_async(request, runtime)

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

    def get_ip_block_record_with_options(
        self,
        request: cmn_20200825_models.GetIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpBlockRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpBlockRecordResponse(),
            self.do_rpcrequest('GetIpBlockRecord', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ip_block_record_with_options_async(
        self,
        request: cmn_20200825_models.GetIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpBlockRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpBlockRecordResponse(),
            await self.do_rpcrequest_async('GetIpBlockRecord', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ip_block_record(
        self,
        request: cmn_20200825_models.GetIpBlockRecordRequest,
    ) -> cmn_20200825_models.GetIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ip_block_record_with_options(request, runtime)

    async def get_ip_block_record_async(
        self,
        request: cmn_20200825_models.GetIpBlockRecordRequest,
    ) -> cmn_20200825_models.GetIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_block_record_with_options_async(request, runtime)

    def list_space_models_with_options(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSpaceModelsResponse(),
            self.do_rpcrequest('ListSpaceModels', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_space_models_with_options_async(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSpaceModelsResponse(),
            await self.do_rpcrequest_async('ListSpaceModels', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_space_models(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_space_models_with_options(request, runtime)

    async def list_space_models_async(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_space_models_with_options_async(request, runtime)

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

    def list_inspection_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.ListInspectionDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionDevicesResponse(),
            self.do_rpcrequest('ListInspectionDevices', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_inspection_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListInspectionDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionDevicesResponse(),
            await self.do_rpcrequest_async('ListInspectionDevices', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_inspection_devices(
        self,
        request: cmn_20200825_models.ListInspectionDevicesRequest,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_devices_with_options(request, runtime)

    async def list_inspection_devices_async(
        self,
        request: cmn_20200825_models.ListInspectionDevicesRequest,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_devices_with_options_async(request, runtime)

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

    def list_schedule_workers_with_options(
        self,
        request: cmn_20200825_models.ListScheduleWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleWorkersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleWorkersResponse(),
            self.do_rpcrequest('ListScheduleWorkers', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_schedule_workers_with_options_async(
        self,
        request: cmn_20200825_models.ListScheduleWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleWorkersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleWorkersResponse(),
            await self.do_rpcrequest_async('ListScheduleWorkers', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schedule_workers(
        self,
        request: cmn_20200825_models.ListScheduleWorkersRequest,
    ) -> cmn_20200825_models.ListScheduleWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schedule_workers_with_options(request, runtime)

    async def list_schedule_workers_async(
        self,
        request: cmn_20200825_models.ListScheduleWorkersRequest,
    ) -> cmn_20200825_models.ListScheduleWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schedule_workers_with_options_async(request, runtime)

    def update_project_progress_with_options(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateProjectProgressResponse(),
            self.do_rpcrequest('UpdateProjectProgress', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_progress_with_options_async(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateProjectProgressResponse(),
            await self.do_rpcrequest_async('UpdateProjectProgress', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project_progress(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_progress_with_options(request, runtime)

    async def update_project_progress_async(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_progress_with_options_async(request, runtime)

    def update_device_resource_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResourceResponse(),
            self.do_rpcrequest('UpdateDeviceResource', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_resource_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResourceResponse(),
            await self.do_rpcrequest_async('UpdateDeviceResource', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_resource(
        self,
        request: cmn_20200825_models.UpdateDeviceResourceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_resource_with_options(request, runtime)

    async def update_device_resource_async(
        self,
        request: cmn_20200825_models.UpdateDeviceResourceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_resource_with_options_async(request, runtime)

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

    def list_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceTypesResponse(),
            self.do_rpcrequest('ListResourceTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceTypesResponse(),
            await self.do_rpcrequest_async('ListResourceTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_resource_types(self) -> cmn_20200825_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(runtime)

    async def list_resource_types_async(self) -> cmn_20200825_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(runtime)

    def get_setup_project_with_options(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSetupProjectResponse(),
            self.do_rpcrequest('GetSetupProject', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSetupProjectResponse(),
            await self.do_rpcrequest_async('GetSetupProject', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_setup_project(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_setup_project_with_options(request, runtime)

    async def get_setup_project_async(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_setup_project_with_options_async(request, runtime)

    def list_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationVariateResponse(),
            self.do_rpcrequest('ListConfigurationVariate', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationVariateResponse(),
            await self.do_rpcrequest_async('ListConfigurationVariate', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_configuration_variate(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_variate_with_options(request, runtime)

    async def list_configuration_variate_async(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_configuration_variate_with_options_async(request, runtime)

    def create_space_model_with_options(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSpaceModelResponse(),
            self.do_rpcrequest('CreateSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_space_model_with_options_async(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSpaceModelResponse(),
            await self.do_rpcrequest_async('CreateSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_space_model(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_space_model_with_options(request, runtime)

    async def create_space_model_async(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_space_model_with_options_async(request, runtime)

    def delete_schedule_worker_with_options(
        self,
        request: cmn_20200825_models.DeleteScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleWorkerResponse(),
            self.do_rpcrequest('DeleteScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_schedule_worker_with_options_async(
        self,
        request: cmn_20200825_models.DeleteScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleWorkerResponse(),
            await self.do_rpcrequest_async('DeleteScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_schedule_worker(
        self,
        request: cmn_20200825_models.DeleteScheduleWorkerRequest,
    ) -> cmn_20200825_models.DeleteScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_worker_with_options(request, runtime)

    async def delete_schedule_worker_async(
        self,
        request: cmn_20200825_models.DeleteScheduleWorkerRequest,
    ) -> cmn_20200825_models.DeleteScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_worker_with_options_async(request, runtime)

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

    def update_information_key_action_with_options(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInformationKeyActionResponse(),
            self.do_rpcrequest('UpdateInformationKeyAction', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_information_key_action_with_options_async(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInformationKeyActionResponse(),
            await self.do_rpcrequest_async('UpdateInformationKeyAction', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_information_key_action(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_information_key_action_with_options(request, runtime)

    async def update_information_key_action_async(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_information_key_action_with_options_async(request, runtime)

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

    def list_schedule_types_with_options(
        self,
        request: cmn_20200825_models.ListScheduleTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleTypesResponse(),
            self.do_rpcrequest('ListScheduleTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_schedule_types_with_options_async(
        self,
        request: cmn_20200825_models.ListScheduleTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleTypesResponse(),
            await self.do_rpcrequest_async('ListScheduleTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schedule_types(
        self,
        request: cmn_20200825_models.ListScheduleTypesRequest,
    ) -> cmn_20200825_models.ListScheduleTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schedule_types_with_options(request, runtime)

    async def list_schedule_types_async(
        self,
        request: cmn_20200825_models.ListScheduleTypesRequest,
    ) -> cmn_20200825_models.ListScheduleTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schedule_types_with_options_async(request, runtime)

    def create_schedule_type_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateScheduleTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_worker):
            request.related_worker_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_worker, 'RelatedWorker', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleTypeResponse(),
            self.do_rpcrequest('CreateScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_schedule_type_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateScheduleTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_worker):
            request.related_worker_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_worker, 'RelatedWorker', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleTypeResponse(),
            await self.do_rpcrequest_async('CreateScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schedule_type(
        self,
        request: cmn_20200825_models.CreateScheduleTypeRequest,
    ) -> cmn_20200825_models.CreateScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_type_with_options(request, runtime)

    async def create_schedule_type_async(
        self,
        request: cmn_20200825_models.CreateScheduleTypeRequest,
    ) -> cmn_20200825_models.CreateScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_type_with_options_async(request, runtime)

    def get_schedule_worker_with_options(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleWorkerResponse(),
            self.do_rpcrequest('GetScheduleWorker', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_schedule_worker_with_options_async(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleWorkerResponse(),
            await self.do_rpcrequest_async('GetScheduleWorker', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_schedule_worker(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schedule_worker_with_options(request, runtime)

    async def get_schedule_worker_async(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schedule_worker_with_options_async(request, runtime)

    def create_schedule_worker_with_options(
        self,
        request: cmn_20200825_models.CreateScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleWorkerResponse(),
            self.do_rpcrequest('CreateScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_schedule_worker_with_options_async(
        self,
        request: cmn_20200825_models.CreateScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleWorkerResponse(),
            await self.do_rpcrequest_async('CreateScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schedule_worker(
        self,
        request: cmn_20200825_models.CreateScheduleWorkerRequest,
    ) -> cmn_20200825_models.CreateScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_worker_with_options(request, runtime)

    async def create_schedule_worker_async(
        self,
        request: cmn_20200825_models.CreateScheduleWorkerRequest,
    ) -> cmn_20200825_models.CreateScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_worker_with_options_async(request, runtime)

    def create_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationVariateResponse(),
            self.do_rpcrequest('CreateConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationVariateResponse(),
            await self.do_rpcrequest_async('CreateConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_configuration_variate(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_variate_with_options(request, runtime)

    async def create_configuration_variate_async(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_configuration_variate_with_options_async(request, runtime)

    def get_space_model_sort_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelSortResponse(),
            self.do_rpcrequest('GetSpaceModelSort', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_space_model_sort_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelSortResponse(),
            await self.do_rpcrequest_async('GetSpaceModelSort', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_space_model_sort(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_sort_with_options(request, runtime)

    async def get_space_model_sort_async(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_sort_with_options_async(request, runtime)

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

    def create_setup_project_with_options(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSetupProjectResponse(),
            self.do_rpcrequest('CreateSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSetupProjectResponse(),
            await self.do_rpcrequest_async('CreateSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_setup_project(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_setup_project_with_options(request, runtime)

    async def create_setup_project_async(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_setup_project_with_options_async(request, runtime)

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

    def get_os_version_with_options(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsVersionResponse(),
            self.do_rpcrequest('GetOsVersion', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_os_version_with_options_async(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsVersionResponse(),
            await self.do_rpcrequest_async('GetOsVersion', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_os_version(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_os_version_with_options(request, runtime)

    async def get_os_version_async(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_os_version_with_options_async(request, runtime)

    def update_schedule_duty_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.type_worker_list):
            request.type_worker_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type_worker_list, 'TypeWorkerList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleDutyResponse(),
            self.do_rpcrequest('UpdateScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_schedule_duty_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.type_worker_list):
            request.type_worker_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type_worker_list, 'TypeWorkerList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleDutyResponse(),
            await self.do_rpcrequest_async('UpdateScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schedule_duty(
        self,
        request: cmn_20200825_models.UpdateScheduleDutyRequest,
    ) -> cmn_20200825_models.UpdateScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_duty_with_options(request, runtime)

    async def update_schedule_duty_async(
        self,
        request: cmn_20200825_models.UpdateScheduleDutyRequest,
    ) -> cmn_20200825_models.UpdateScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_duty_with_options_async(request, runtime)

    def create_ip_record_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateIpRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device):
            request.device_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device, 'Device', 'json')
        if not UtilClient.is_unset(tmp_req.ip_code):
            request.ip_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_code, 'IpCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpRecordResponse(),
            self.do_rpcrequest('CreateIpRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ip_record_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateIpRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device):
            request.device_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device, 'Device', 'json')
        if not UtilClient.is_unset(tmp_req.ip_code):
            request.ip_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_code, 'IpCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpRecordResponse(),
            await self.do_rpcrequest_async('CreateIpRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ip_record(
        self,
        request: cmn_20200825_models.CreateIpRecordRequest,
    ) -> cmn_20200825_models.CreateIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_record_with_options(request, runtime)

    async def create_ip_record_async(
        self,
        request: cmn_20200825_models.CreateIpRecordRequest,
    ) -> cmn_20200825_models.CreateIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_record_with_options_async(request, runtime)

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

    def list_zone_types_with_options(
        self,
        request: cmn_20200825_models.ListZoneTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListZoneTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListZoneTypesResponse(),
            self.do_rpcrequest('ListZoneTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_zone_types_with_options_async(
        self,
        request: cmn_20200825_models.ListZoneTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListZoneTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListZoneTypesResponse(),
            await self.do_rpcrequest_async('ListZoneTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_zone_types(
        self,
        request: cmn_20200825_models.ListZoneTypesRequest,
    ) -> cmn_20200825_models.ListZoneTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_zone_types_with_options(request, runtime)

    async def list_zone_types_async(
        self,
        request: cmn_20200825_models.ListZoneTypesRequest,
    ) -> cmn_20200825_models.ListZoneTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_zone_types_with_options_async(request, runtime)

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

    def update_resource_instance_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_information):
            request.resource_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_information, 'ResourceInformation', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInstanceResponse(),
            self.do_rpcrequest('UpdateResourceInstance', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_resource_instance_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_information):
            request.resource_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_information, 'ResourceInformation', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInstanceResponse(),
            await self.do_rpcrequest_async('UpdateResourceInstance', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_resource_instance(
        self,
        request: cmn_20200825_models.UpdateResourceInstanceRequest,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_instance_with_options(request, runtime)

    async def update_resource_instance_async(
        self,
        request: cmn_20200825_models.UpdateResourceInstanceRequest,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_instance_with_options_async(request, runtime)

    def get_schedule_duty_with_options(
        self,
        request: cmn_20200825_models.GetScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleDutyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleDutyResponse(),
            self.do_rpcrequest('GetScheduleDuty', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_schedule_duty_with_options_async(
        self,
        request: cmn_20200825_models.GetScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleDutyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleDutyResponse(),
            await self.do_rpcrequest_async('GetScheduleDuty', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_schedule_duty(
        self,
        request: cmn_20200825_models.GetScheduleDutyRequest,
    ) -> cmn_20200825_models.GetScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schedule_duty_with_options(request, runtime)

    async def get_schedule_duty_async(
        self,
        request: cmn_20200825_models.GetScheduleDutyRequest,
    ) -> cmn_20200825_models.GetScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schedule_duty_with_options_async(request, runtime)

    def get_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationVariateResponse(),
            self.do_rpcrequest('GetConfigurationVariate', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationVariateResponse(),
            await self.do_rpcrequest_async('GetConfigurationVariate', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_configuration_variate(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_variate_with_options(request, runtime)

    async def get_configuration_variate_async(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_configuration_variate_with_options_async(request, runtime)

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

    def get_ip_record_with_options(
        self,
        request: cmn_20200825_models.GetIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpRecordResponse(),
            self.do_rpcrequest('GetIpRecord', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ip_record_with_options_async(
        self,
        request: cmn_20200825_models.GetIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpRecordResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpRecordResponse(),
            await self.do_rpcrequest_async('GetIpRecord', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ip_record(
        self,
        request: cmn_20200825_models.GetIpRecordRequest,
    ) -> cmn_20200825_models.GetIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ip_record_with_options(request, runtime)

    async def get_ip_record_async(
        self,
        request: cmn_20200825_models.GetIpRecordRequest,
    ) -> cmn_20200825_models.GetIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_record_with_options_async(request, runtime)

    def list_schedule_duties_with_options(
        self,
        request: cmn_20200825_models.ListScheduleDutiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleDutiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleDutiesResponse(),
            self.do_rpcrequest('ListScheduleDuties', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_schedule_duties_with_options_async(
        self,
        request: cmn_20200825_models.ListScheduleDutiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListScheduleDutiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListScheduleDutiesResponse(),
            await self.do_rpcrequest_async('ListScheduleDuties', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schedule_duties(
        self,
        request: cmn_20200825_models.ListScheduleDutiesRequest,
    ) -> cmn_20200825_models.ListScheduleDutiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schedule_duties_with_options(request, runtime)

    async def list_schedule_duties_async(
        self,
        request: cmn_20200825_models.ListScheduleDutiesRequest,
    ) -> cmn_20200825_models.ListScheduleDutiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schedule_duties_with_options_async(request, runtime)

    def lock_space_model_with_options(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.LockSpaceModelResponse(),
            self.do_rpcrequest('LockSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lock_space_model_with_options_async(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.LockSpaceModelResponse(),
            await self.do_rpcrequest_async('LockSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_space_model(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_space_model_with_options(request, runtime)

    async def lock_space_model_async(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_space_model_with_options_async(request, runtime)

    def update_resource_information_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.information):
            request.information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.information, 'Information', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInformationResponse(),
            self.do_rpcrequest('UpdateResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_resource_information_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.information):
            request.information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.information, 'Information', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInformationResponse(),
            await self.do_rpcrequest_async('UpdateResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_resource_information(
        self,
        request: cmn_20200825_models.UpdateResourceInformationRequest,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_information_with_options(request, runtime)

    async def update_resource_information_async(
        self,
        request: cmn_20200825_models.UpdateResourceInformationRequest,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_information_with_options_async(request, runtime)

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

    def list_inspection_task_reports_with_options(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTaskReportsResponse(),
            self.do_rpcrequest('ListInspectionTaskReports', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_inspection_task_reports_with_options_async(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTaskReportsResponse(),
            await self.do_rpcrequest_async('ListInspectionTaskReports', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_inspection_task_reports(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_task_reports_with_options(request, runtime)

    async def list_inspection_task_reports_async(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_task_reports_with_options_async(request, runtime)

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

    def update_schedule_type_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateScheduleTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_worker):
            request.related_worker_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_worker, 'RelatedWorker', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleTypeResponse(),
            self.do_rpcrequest('UpdateScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_schedule_type_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateScheduleTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_worker):
            request.related_worker_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_worker, 'RelatedWorker', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleTypeResponse(),
            await self.do_rpcrequest_async('UpdateScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schedule_type(
        self,
        request: cmn_20200825_models.UpdateScheduleTypeRequest,
    ) -> cmn_20200825_models.UpdateScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_type_with_options(request, runtime)

    async def update_schedule_type_async(
        self,
        request: cmn_20200825_models.UpdateScheduleTypeRequest,
    ) -> cmn_20200825_models.UpdateScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_type_with_options_async(request, runtime)

    def download_device_resource_with_options(
        self,
        tmp_req: cmn_20200825_models.DownloadDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DownloadDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.DownloadDeviceResourceResponse(),
            self.do_rpcrequest('DownloadDeviceResource', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def download_device_resource_with_options_async(
        self,
        tmp_req: cmn_20200825_models.DownloadDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DownloadDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.DownloadDeviceResourceResponse(),
            await self.do_rpcrequest_async('DownloadDeviceResource', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def download_device_resource(
        self,
        request: cmn_20200825_models.DownloadDeviceResourceRequest,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_device_resource_with_options(request, runtime)

    async def download_device_resource_async(
        self,
        request: cmn_20200825_models.DownloadDeviceResourceRequest,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_device_resource_with_options_async(request, runtime)

    def get_os_download_path_with_options(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsDownloadPathResponse(),
            self.do_rpcrequest('GetOsDownloadPath', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_os_download_path_with_options_async(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsDownloadPathResponse(),
            await self.do_rpcrequest_async('GetOsDownloadPath', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_os_download_path(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_os_download_path_with_options(request, runtime)

    async def get_os_download_path_async(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_os_download_path_with_options_async(request, runtime)

    def list_connection_policies_with_options(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConnectionPoliciesResponse(),
            self.do_rpcrequest('ListConnectionPolicies', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_connection_policies_with_options_async(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConnectionPoliciesResponse(),
            await self.do_rpcrequest_async('ListConnectionPolicies', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connection_policies(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connection_policies_with_options(request, runtime)

    async def list_connection_policies_async(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connection_policies_with_options_async(request, runtime)

    def update_schedule_worker_with_options(
        self,
        request: cmn_20200825_models.UpdateScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleWorkerResponse(),
            self.do_rpcrequest('UpdateScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_schedule_worker_with_options_async(
        self,
        request: cmn_20200825_models.UpdateScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateScheduleWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateScheduleWorkerResponse(),
            await self.do_rpcrequest_async('UpdateScheduleWorker', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schedule_worker(
        self,
        request: cmn_20200825_models.UpdateScheduleWorkerRequest,
    ) -> cmn_20200825_models.UpdateScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_worker_with_options(request, runtime)

    async def update_schedule_worker_async(
        self,
        request: cmn_20200825_models.UpdateScheduleWorkerRequest,
    ) -> cmn_20200825_models.UpdateScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_worker_with_options_async(request, runtime)

    def delete_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationVariateResponse(),
            self.do_rpcrequest('DeleteConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationVariateResponse(),
            await self.do_rpcrequest_async('DeleteConfigurationVariate', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_configuration_variate(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_variate_with_options(request, runtime)

    async def delete_configuration_variate_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_configuration_variate_with_options_async(request, runtime)

    def create_schedule_duty_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.schedule_type_ids):
            request.schedule_type_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_type_ids, 'ScheduleTypeIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleDutyResponse(),
            self.do_rpcrequest('CreateScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_schedule_duty_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.schedule_type_ids):
            request.schedule_type_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_type_ids, 'ScheduleTypeIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateScheduleDutyResponse(),
            await self.do_rpcrequest_async('CreateScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schedule_duty(
        self,
        request: cmn_20200825_models.CreateScheduleDutyRequest,
    ) -> cmn_20200825_models.CreateScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_duty_with_options(request, runtime)

    async def create_schedule_duty_async(
        self,
        request: cmn_20200825_models.CreateScheduleDutyRequest,
    ) -> cmn_20200825_models.CreateScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_duty_with_options_async(request, runtime)

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

    def delete_resource_information_with_options(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteResourceInformationResponse(),
            self.do_rpcrequest('DeleteResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_resource_information_with_options_async(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteResourceInformationResponse(),
            await self.do_rpcrequest_async('DeleteResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_resource_information(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_information_with_options(request, runtime)

    async def delete_resource_information_async(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_information_with_options_async(request, runtime)

    def delete_setup_project_with_options(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSetupProjectResponse(),
            self.do_rpcrequest('DeleteSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSetupProjectResponse(),
            await self.do_rpcrequest_async('DeleteSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_setup_project(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_setup_project_with_options(request, runtime)

    async def delete_setup_project_async(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_setup_project_with_options_async(request, runtime)

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

    def apply_ipwith_options(
        self,
        tmp_req: cmn_20200825_models.ApplyIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ApplyIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ApplyIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ApplyIPResponse(),
            self.do_rpcrequest('ApplyIP', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_ipwith_options_async(
        self,
        tmp_req: cmn_20200825_models.ApplyIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ApplyIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ApplyIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ApplyIPResponse(),
            await self.do_rpcrequest_async('ApplyIP', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_ip(
        self,
        request: cmn_20200825_models.ApplyIPRequest,
    ) -> cmn_20200825_models.ApplyIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ipwith_options(request, runtime)

    async def apply_ip_async(
        self,
        request: cmn_20200825_models.ApplyIPRequest,
    ) -> cmn_20200825_models.ApplyIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ipwith_options_async(request, runtime)

    def update_os_version_with_options(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateOsVersionResponse(),
            self.do_rpcrequest('UpdateOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_version_with_options_async(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateOsVersionResponse(),
            await self.do_rpcrequest_async('UpdateOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_with_options(request, runtime)

    async def update_os_version_async(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_with_options_async(request, runtime)

    def get_space_model_instance_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelInstanceResponse(),
            self.do_rpcrequest('GetSpaceModelInstance', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_space_model_instance_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelInstanceResponse(),
            await self.do_rpcrequest_async('GetSpaceModelInstance', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_space_model_instance(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_instance_with_options(request, runtime)

    async def get_space_model_instance_async(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_instance_with_options_async(request, runtime)

    def list_os_versions_with_options(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListOsVersionsResponse(),
            self.do_rpcrequest('ListOsVersions', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_os_versions_with_options_async(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListOsVersionsResponse(),
            await self.do_rpcrequest_async('ListOsVersions', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_os_versions(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_os_versions_with_options(request, runtime)

    async def list_os_versions_async(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_os_versions_with_options_async(request, runtime)

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

    def get_device_resource_with_options(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResourceResponse(),
            self.do_rpcrequest('GetDeviceResource', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_device_resource_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResourceResponse(),
            await self.do_rpcrequest_async('GetDeviceResource', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_device_resource(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_resource_with_options(request, runtime)

    async def get_device_resource_async(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_resource_with_options_async(request, runtime)

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

    def list_ip_with_options(
        self,
        request: cmn_20200825_models.ListIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpResponse(),
            self.do_rpcrequest('ListIp', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_ip_with_options_async(
        self,
        request: cmn_20200825_models.ListIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpResponse(),
            await self.do_rpcrequest_async('ListIp', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_ip(
        self,
        request: cmn_20200825_models.ListIpRequest,
    ) -> cmn_20200825_models.ListIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ip_with_options(request, runtime)

    async def list_ip_async(
        self,
        request: cmn_20200825_models.ListIpRequest,
    ) -> cmn_20200825_models.ListIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ip_with_options_async(request, runtime)

    def list_configuration_specifications_with_options(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationSpecificationsResponse(),
            self.do_rpcrequest('ListConfigurationSpecifications', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_configuration_specifications_with_options_async(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationSpecificationsResponse(),
            await self.do_rpcrequest_async('ListConfigurationSpecifications', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_configuration_specifications(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_specifications_with_options(request, runtime)

    async def list_configuration_specifications_async(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_configuration_specifications_with_options_async(request, runtime)

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

    def list_resource_instances_with_options(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInstancesResponse(),
            self.do_rpcrequest('ListResourceInstances', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_resource_instances_with_options_async(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInstancesResponse(),
            await self.do_rpcrequest_async('ListResourceInstances', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_resource_instances(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_instances_with_options(request, runtime)

    async def list_resource_instances_async(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_instances_with_options_async(request, runtime)

    def list_ip_blocks_with_options(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpBlocksResponse(),
            self.do_rpcrequest('ListIpBlocks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_ip_blocks_with_options_async(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpBlocksResponse(),
            await self.do_rpcrequest_async('ListIpBlocks', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_ip_blocks(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ip_blocks_with_options(request, runtime)

    async def list_ip_blocks_async(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ip_blocks_with_options_async(request, runtime)

    def list_device_resources_with_options(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceResourcesResponse(),
            self.do_rpcrequest('ListDeviceResources', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_resources_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceResourcesResponse(),
            await self.do_rpcrequest_async('ListDeviceResources', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_resources(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_resources_with_options(request, runtime)

    async def list_device_resources_async(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_resources_with_options_async(request, runtime)

    def list_resource_informations_with_options(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInformationsResponse(),
            self.do_rpcrequest('ListResourceInformations', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_resource_informations_with_options_async(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInformationsResponse(),
            await self.do_rpcrequest_async('ListResourceInformations', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_resource_informations(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_informations_with_options(request, runtime)

    async def list_resource_informations_async(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_informations_with_options_async(request, runtime)

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

    def get_configuration_specification_with_options(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationSpecificationResponse(),
            self.do_rpcrequest('GetConfigurationSpecification', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_configuration_specification_with_options_async(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationSpecificationResponse(),
            await self.do_rpcrequest_async('GetConfigurationSpecification', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_configuration_specification(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_specification_with_options(request, runtime)

    async def get_configuration_specification_async(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_configuration_specification_with_options_async(request, runtime)

    def delete_schedule_duty_with_options(
        self,
        tmp_req: cmn_20200825_models.DeleteScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DeleteScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.type_worker_list):
            request.type_worker_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type_worker_list, 'TypeWorkerList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleDutyResponse(),
            self.do_rpcrequest('DeleteScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_schedule_duty_with_options_async(
        self,
        tmp_req: cmn_20200825_models.DeleteScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DeleteScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.type_worker_list):
            request.type_worker_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.type_worker_list, 'TypeWorkerList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleDutyResponse(),
            await self.do_rpcrequest_async('DeleteScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_schedule_duty(
        self,
        request: cmn_20200825_models.DeleteScheduleDutyRequest,
    ) -> cmn_20200825_models.DeleteScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_duty_with_options(request, runtime)

    async def delete_schedule_duty_async(
        self,
        request: cmn_20200825_models.DeleteScheduleDutyRequest,
    ) -> cmn_20200825_models.DeleteScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_duty_with_options_async(request, runtime)

    def upload_schedule_duty_with_options(
        self,
        tmp_req: cmn_20200825_models.UploadScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UploadScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UploadScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.schedule_duty):
            request.schedule_duty_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_duty, 'ScheduleDuty', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UploadScheduleDutyResponse(),
            self.do_rpcrequest('UploadScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_schedule_duty_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UploadScheduleDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UploadScheduleDutyResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UploadScheduleDutyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.schedule_duty):
            request.schedule_duty_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_duty, 'ScheduleDuty', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UploadScheduleDutyResponse(),
            await self.do_rpcrequest_async('UploadScheduleDuty', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_schedule_duty(
        self,
        request: cmn_20200825_models.UploadScheduleDutyRequest,
    ) -> cmn_20200825_models.UploadScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_schedule_duty_with_options(request, runtime)

    async def upload_schedule_duty_async(
        self,
        request: cmn_20200825_models.UploadScheduleDutyRequest,
    ) -> cmn_20200825_models.UploadScheduleDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_schedule_duty_with_options_async(request, runtime)

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

    def get_space_model_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelResponse(),
            self.do_rpcrequest('GetSpaceModel', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_space_model_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelResponse(),
            await self.do_rpcrequest_async('GetSpaceModel', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_space_model(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_with_options(request, runtime)

    async def get_space_model_async(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_with_options_async(request, runtime)

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

    def create_resource_information_with_options(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateResourceInformationResponse(),
            self.do_rpcrequest('CreateResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_information_with_options_async(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateResourceInformationResponse(),
            await self.do_rpcrequest_async('CreateResourceInformation', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_information(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_information_with_options(request, runtime)

    async def create_resource_information_async(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_information_with_options_async(request, runtime)

    def update_space_model_instance_with_options(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelInstanceResponse(),
            self.do_rpcrequest('UpdateSpaceModelInstance', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_space_model_instance_with_options_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelInstanceResponse(),
            await self.do_rpcrequest_async('UpdateSpaceModelInstance', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_space_model_instance(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_instance_with_options(request, runtime)

    async def update_space_model_instance_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_space_model_instance_with_options_async(request, runtime)

    def update_ip_record_with_options(
        self,
        request: cmn_20200825_models.UpdateIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpRecordResponse(),
            self.do_rpcrequest('UpdateIpRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ip_record_with_options_async(
        self,
        request: cmn_20200825_models.UpdateIpRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpRecordResponse(),
            await self.do_rpcrequest_async('UpdateIpRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_record(
        self,
        request: cmn_20200825_models.UpdateIpRecordRequest,
    ) -> cmn_20200825_models.UpdateIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ip_record_with_options(request, runtime)

    async def update_ip_record_async(
        self,
        request: cmn_20200825_models.UpdateIpRecordRequest,
    ) -> cmn_20200825_models.UpdateIpRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_record_with_options_async(request, runtime)

    def release_ipwith_options(
        self,
        tmp_req: cmn_20200825_models.ReleaseIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ReleaseIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ReleaseIPResponse(),
            self.do_rpcrequest('ReleaseIP', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_ipwith_options_async(
        self,
        tmp_req: cmn_20200825_models.ReleaseIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ReleaseIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.ReleaseIPResponse(),
            await self.do_rpcrequest_async('ReleaseIP', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_ip(
        self,
        request: cmn_20200825_models.ReleaseIPRequest,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_ipwith_options(request, runtime)

    async def release_ip_async(
        self,
        request: cmn_20200825_models.ReleaseIPRequest,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_ipwith_options_async(request, runtime)

    def delete_device_resource_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResourceResponse(),
            self.do_rpcrequest('DeleteDeviceResource', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_resource_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResourceResponse(),
            await self.do_rpcrequest_async('DeleteDeviceResource', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device_resource(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_resource_with_options(request, runtime)

    async def delete_device_resource_async(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_resource_with_options_async(request, runtime)

    def get_ip_block_with_options(
        self,
        request: cmn_20200825_models.GetIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpBlockResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpBlockResponse(),
            self.do_rpcrequest('GetIpBlock', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ip_block_with_options_async(
        self,
        request: cmn_20200825_models.GetIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetIpBlockResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetIpBlockResponse(),
            await self.do_rpcrequest_async('GetIpBlock', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ip_block(
        self,
        request: cmn_20200825_models.GetIpBlockRequest,
    ) -> cmn_20200825_models.GetIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ip_block_with_options(request, runtime)

    async def get_ip_block_async(
        self,
        request: cmn_20200825_models.GetIpBlockRequest,
    ) -> cmn_20200825_models.GetIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_block_with_options_async(request, runtime)

    def delete_ip_block_with_options(
        self,
        request: cmn_20200825_models.DeleteIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteIpBlockResponse(),
            self.do_rpcrequest('DeleteIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ip_block_with_options_async(
        self,
        request: cmn_20200825_models.DeleteIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteIpBlockResponse(),
            await self.do_rpcrequest_async('DeleteIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ip_block(
        self,
        request: cmn_20200825_models.DeleteIpBlockRequest,
    ) -> cmn_20200825_models.DeleteIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_block_with_options(request, runtime)

    async def delete_ip_block_async(
        self,
        request: cmn_20200825_models.DeleteIpBlockRequest,
    ) -> cmn_20200825_models.DeleteIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_block_with_options_async(request, runtime)

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

    def delete_configuration_specification_with_options(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationSpecificationResponse(),
            self.do_rpcrequest('DeleteConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_configuration_specification_with_options_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationSpecificationResponse(),
            await self.do_rpcrequest_async('DeleteConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_configuration_specification(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_specification_with_options(request, runtime)

    async def delete_configuration_specification_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_configuration_specification_with_options_async(request, runtime)

    def list_business_types_with_options(
        self,
        request: cmn_20200825_models.ListBusinessTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListBusinessTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListBusinessTypesResponse(),
            self.do_rpcrequest('ListBusinessTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_business_types_with_options_async(
        self,
        request: cmn_20200825_models.ListBusinessTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListBusinessTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListBusinessTypesResponse(),
            await self.do_rpcrequest_async('ListBusinessTypes', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_business_types(
        self,
        request: cmn_20200825_models.ListBusinessTypesRequest,
    ) -> cmn_20200825_models.ListBusinessTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_business_types_with_options(request, runtime)

    async def list_business_types_async(
        self,
        request: cmn_20200825_models.ListBusinessTypesRequest,
    ) -> cmn_20200825_models.ListBusinessTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_business_types_with_options_async(request, runtime)

    def list_setup_projects_with_options(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSetupProjectsResponse(),
            self.do_rpcrequest('ListSetupProjects', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_setup_projects_with_options_async(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSetupProjectsResponse(),
            await self.do_rpcrequest_async('ListSetupProjects', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_setup_projects(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_setup_projects_with_options(request, runtime)

    async def list_setup_projects_async(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_setup_projects_with_options_async(request, runtime)

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

    def update_configuration_specification_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationSpecificationResponse(),
            self.do_rpcrequest('UpdateConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_configuration_specification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationSpecificationResponse(),
            await self.do_rpcrequest_async('UpdateConfigurationSpecification', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_configuration_specification(
        self,
        request: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_specification_with_options(request, runtime)

    async def update_configuration_specification_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_configuration_specification_with_options_async(request, runtime)

    def create_os_version_with_options(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateOsVersionResponse(),
            self.do_rpcrequest('CreateOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_os_version_with_options_async(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateOsVersionResponse(),
            await self.do_rpcrequest_async('CreateOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_os_version(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_os_version_with_options(request, runtime)

    async def create_os_version_async(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_os_version_with_options_async(request, runtime)

    def create_ip_block_record_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpBlockRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateIpBlockRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.zone_layer):
            request.zone_layer_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.zone_layer, 'ZoneLayer', 'json')
        if not UtilClient.is_unset(tmp_req.business_type):
            request.business_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_type, 'BusinessType', 'json')
        if not UtilClient.is_unset(tmp_req.ip_block_code):
            request.ip_block_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_block_code, 'IpBlockCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpBlockRecordResponse(),
            self.do_rpcrequest('CreateIpBlockRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ip_block_record_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateIpBlockRecordResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateIpBlockRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.zone_layer):
            request.zone_layer_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.zone_layer, 'ZoneLayer', 'json')
        if not UtilClient.is_unset(tmp_req.business_type):
            request.business_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_type, 'BusinessType', 'json')
        if not UtilClient.is_unset(tmp_req.ip_block_code):
            request.ip_block_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_block_code, 'IpBlockCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateIpBlockRecordResponse(),
            await self.do_rpcrequest_async('CreateIpBlockRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ip_block_record(
        self,
        request: cmn_20200825_models.CreateIpBlockRecordRequest,
    ) -> cmn_20200825_models.CreateIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_block_record_with_options(request, runtime)

    async def create_ip_block_record_async(
        self,
        request: cmn_20200825_models.CreateIpBlockRecordRequest,
    ) -> cmn_20200825_models.CreateIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_block_record_with_options_async(request, runtime)

    def update_ip_block_with_options(
        self,
        request: cmn_20200825_models.UpdateIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpBlockResponse(),
            self.do_rpcrequest('UpdateIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ip_block_with_options_async(
        self,
        request: cmn_20200825_models.UpdateIpBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpBlockResponse(),
            await self.do_rpcrequest_async('UpdateIpBlock', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_block(
        self,
        request: cmn_20200825_models.UpdateIpBlockRequest,
    ) -> cmn_20200825_models.UpdateIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ip_block_with_options(request, runtime)

    async def update_ip_block_async(
        self,
        request: cmn_20200825_models.UpdateIpBlockRequest,
    ) -> cmn_20200825_models.UpdateIpBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_block_with_options_async(request, runtime)

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

    def update_ip_block_record_with_options(
        self,
        request: cmn_20200825_models.UpdateIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpBlockRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpBlockRecordResponse(),
            self.do_rpcrequest('UpdateIpBlockRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ip_block_record_with_options_async(
        self,
        request: cmn_20200825_models.UpdateIpBlockRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateIpBlockRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateIpBlockRecordResponse(),
            await self.do_rpcrequest_async('UpdateIpBlockRecord', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_block_record(
        self,
        request: cmn_20200825_models.UpdateIpBlockRecordRequest,
    ) -> cmn_20200825_models.UpdateIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ip_block_record_with_options(request, runtime)

    async def update_ip_block_record_async(
        self,
        request: cmn_20200825_models.UpdateIpBlockRecordRequest,
    ) -> cmn_20200825_models.UpdateIpBlockRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_block_record_with_options_async(request, runtime)

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

    def get_physical_space_topo_with_options(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceTopoResponse(),
            self.do_rpcrequest('GetPhysicalSpaceTopo', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_physical_space_topo_with_options_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceTopoResponse(),
            await self.do_rpcrequest_async('GetPhysicalSpaceTopo', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_physical_space_topo(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_topo_with_options(request, runtime)

    async def get_physical_space_topo_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_space_topo_with_options_async(request, runtime)

    def get_oss_policy_with_options(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOssPolicyResponse(),
            self.do_rpcrequest('GetOssPolicy', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_oss_policy_with_options_async(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOssPolicyResponse(),
            await self.do_rpcrequest_async('GetOssPolicy', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_oss_policy(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    async def get_oss_policy_async(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_policy_with_options_async(request, runtime)

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

    def update_setup_project_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSetupProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.packages):
            request.packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.packages, 'Packages', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSetupProjectResponse(),
            self.do_rpcrequest('UpdateSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_setup_project_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSetupProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.packages):
            request.packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.packages, 'Packages', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSetupProjectResponse(),
            await self.do_rpcrequest_async('UpdateSetupProject', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_setup_project(
        self,
        request: cmn_20200825_models.UpdateSetupProjectRequest,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_setup_project_with_options(request, runtime)

    async def update_setup_project_async(
        self,
        request: cmn_20200825_models.UpdateSetupProjectRequest,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_setup_project_with_options_async(request, runtime)

    def update_space_model_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelResponse(),
            self.do_rpcrequest('UpdateSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_space_model_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelResponse(),
            await self.do_rpcrequest_async('UpdateSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_space_model(
        self,
        request: cmn_20200825_models.UpdateSpaceModelRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_with_options(request, runtime)

    async def update_space_model_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_space_model_with_options_async(request, runtime)

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

    def delete_space_model_with_options(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSpaceModelResponse(),
            self.do_rpcrequest('DeleteSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_space_model_with_options_async(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSpaceModelResponse(),
            await self.do_rpcrequest_async('DeleteSpaceModel', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_space_model(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_space_model_with_options(request, runtime)

    async def delete_space_model_async(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_space_model_with_options_async(request, runtime)

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

    def list_architecture_attribute_with_options(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListArchitectureAttributeResponse(),
            self.do_rpcrequest('ListArchitectureAttribute', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_architecture_attribute_with_options_async(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListArchitectureAttributeResponse(),
            await self.do_rpcrequest_async('ListArchitectureAttribute', '2020-08-25', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_architecture_attribute(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_architecture_attribute_with_options(request, runtime)

    async def list_architecture_attribute_async(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_architecture_attribute_with_options_async(request, runtime)

    def delete_os_version_with_options(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteOsVersionResponse(),
            self.do_rpcrequest('DeleteOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_os_version_with_options_async(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteOsVersionResponse(),
            await self.do_rpcrequest_async('DeleteOsVersion', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_os_version(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_os_version_with_options(request, runtime)

    async def delete_os_version_async(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_os_version_with_options_async(request, runtime)

    def delete_schedule_type_with_options(
        self,
        request: cmn_20200825_models.DeleteScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleTypeResponse(),
            self.do_rpcrequest('DeleteScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_schedule_type_with_options_async(
        self,
        request: cmn_20200825_models.DeleteScheduleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteScheduleTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteScheduleTypeResponse(),
            await self.do_rpcrequest_async('DeleteScheduleType', '2020-08-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_schedule_type(
        self,
        request: cmn_20200825_models.DeleteScheduleTypeRequest,
    ) -> cmn_20200825_models.DeleteScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_type_with_options(request, runtime)

    async def delete_schedule_type_async(
        self,
        request: cmn_20200825_models.DeleteScheduleTypeRequest,
    ) -> cmn_20200825_models.DeleteScheduleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_type_with_options_async(request, runtime)

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
