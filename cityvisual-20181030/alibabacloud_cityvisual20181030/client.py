# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cityvisual20181030 import models as cityvisual_20181030_models
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
        self._endpoint = self.get_endpoint('cityvisual', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_stream_with_options(
        self,
        request: cityvisual_20181030_models.AttachStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.AttachStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.AttachStreamResponse().from_map(
            self.do_rpcrequest('AttachStream', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_stream_with_options_async(
        self,
        request: cityvisual_20181030_models.AttachStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.AttachStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.AttachStreamResponse().from_map(
            await self.do_rpcrequest_async('AttachStream', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_stream(
        self,
        request: cityvisual_20181030_models.AttachStreamRequest,
    ) -> cityvisual_20181030_models.AttachStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_stream_with_options(request, runtime)

    async def attach_stream_async(
        self,
        request: cityvisual_20181030_models.AttachStreamRequest,
    ) -> cityvisual_20181030_models.AttachStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_stream_with_options_async(request, runtime)

    def batch_modify_camera_status_with_options(
        self,
        request: cityvisual_20181030_models.BatchModifyCameraStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.BatchModifyCameraStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.BatchModifyCameraStatusResponse().from_map(
            self.do_rpcrequest('BatchModifyCameraStatus', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_modify_camera_status_with_options_async(
        self,
        request: cityvisual_20181030_models.BatchModifyCameraStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.BatchModifyCameraStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.BatchModifyCameraStatusResponse().from_map(
            await self.do_rpcrequest_async('BatchModifyCameraStatus', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_modify_camera_status(
        self,
        request: cityvisual_20181030_models.BatchModifyCameraStatusRequest,
    ) -> cityvisual_20181030_models.BatchModifyCameraStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_modify_camera_status_with_options(request, runtime)

    async def batch_modify_camera_status_async(
        self,
        request: cityvisual_20181030_models.BatchModifyCameraStatusRequest,
    ) -> cityvisual_20181030_models.BatchModifyCameraStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_modify_camera_status_with_options_async(request, runtime)

    def create_algo_lib_with_options(
        self,
        request: cityvisual_20181030_models.CreateAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateAlgoLibResponse().from_map(
            self.do_rpcrequest('CreateAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_algo_lib_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateAlgoLibResponse().from_map(
            await self.do_rpcrequest_async('CreateAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_algo_lib(
        self,
        request: cityvisual_20181030_models.CreateAlgoLibRequest,
    ) -> cityvisual_20181030_models.CreateAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_algo_lib_with_options(request, runtime)

    async def create_algo_lib_async(
        self,
        request: cityvisual_20181030_models.CreateAlgoLibRequest,
    ) -> cityvisual_20181030_models.CreateAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_algo_lib_with_options_async(request, runtime)

    def create_camera_with_options(
        self,
        request: cityvisual_20181030_models.CreateCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateCameraResponse().from_map(
            self.do_rpcrequest('CreateCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateCameraResponse().from_map(
            await self.do_rpcrequest_async('CreateCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_camera(
        self,
        request: cityvisual_20181030_models.CreateCameraRequest,
    ) -> cityvisual_20181030_models.CreateCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_camera_with_options(request, runtime)

    async def create_camera_async(
        self,
        request: cityvisual_20181030_models.CreateCameraRequest,
    ) -> cityvisual_20181030_models.CreateCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_camera_with_options_async(request, runtime)

    def create_capability_with_options(
        self,
        request: cityvisual_20181030_models.CreateCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateCapabilityResponse().from_map(
            self.do_rpcrequest('CreateCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_capability_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateCapabilityResponse().from_map(
            await self.do_rpcrequest_async('CreateCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_capability(
        self,
        request: cityvisual_20181030_models.CreateCapabilityRequest,
    ) -> cityvisual_20181030_models.CreateCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_capability_with_options(request, runtime)

    async def create_capability_async(
        self,
        request: cityvisual_20181030_models.CreateCapabilityRequest,
    ) -> cityvisual_20181030_models.CreateCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_capability_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: cityvisual_20181030_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: cityvisual_20181030_models.CreateInstanceRequest,
    ) -> cityvisual_20181030_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: cityvisual_20181030_models.CreateInstanceRequest,
    ) -> cityvisual_20181030_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_job_group_with_options(
        self,
        request: cityvisual_20181030_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateJobGroupResponse().from_map(
            self.do_rpcrequest('CreateJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_group_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateJobGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job_group(
        self,
        request: cityvisual_20181030_models.CreateJobGroupRequest,
    ) -> cityvisual_20181030_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    async def create_job_group_async(
        self,
        request: cityvisual_20181030_models.CreateJobGroupRequest,
    ) -> cityvisual_20181030_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_group_with_options_async(request, runtime)

    def create_resource_profile_with_options(
        self,
        request: cityvisual_20181030_models.CreateResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateResourceProfileResponse().from_map(
            self.do_rpcrequest('CreateResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_profile_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateResourceProfileResponse().from_map(
            await self.do_rpcrequest_async('CreateResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_profile(
        self,
        request: cityvisual_20181030_models.CreateResourceProfileRequest,
    ) -> cityvisual_20181030_models.CreateResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_profile_with_options(request, runtime)

    async def create_resource_profile_async(
        self,
        request: cityvisual_20181030_models.CreateResourceProfileRequest,
    ) -> cityvisual_20181030_models.CreateResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_profile_with_options_async(request, runtime)

    def create_work_group_with_options(
        self,
        request: cityvisual_20181030_models.CreateWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateWorkGroupResponse().from_map(
            self.do_rpcrequest('CreateWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_work_group_with_options_async(
        self,
        request: cityvisual_20181030_models.CreateWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.CreateWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.CreateWorkGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_work_group(
        self,
        request: cityvisual_20181030_models.CreateWorkGroupRequest,
    ) -> cityvisual_20181030_models.CreateWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_work_group_with_options(request, runtime)

    async def create_work_group_async(
        self,
        request: cityvisual_20181030_models.CreateWorkGroupRequest,
    ) -> cityvisual_20181030_models.CreateWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_work_group_with_options_async(request, runtime)

    def delete_algo_lib_with_options(
        self,
        request: cityvisual_20181030_models.DeleteAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteAlgoLibResponse().from_map(
            self.do_rpcrequest('DeleteAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_algo_lib_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteAlgoLibResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_algo_lib(
        self,
        request: cityvisual_20181030_models.DeleteAlgoLibRequest,
    ) -> cityvisual_20181030_models.DeleteAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_algo_lib_with_options(request, runtime)

    async def delete_algo_lib_async(
        self,
        request: cityvisual_20181030_models.DeleteAlgoLibRequest,
    ) -> cityvisual_20181030_models.DeleteAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_algo_lib_with_options_async(request, runtime)

    def delete_camera_with_options(
        self,
        request: cityvisual_20181030_models.DeleteCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteCameraResponse().from_map(
            self.do_rpcrequest('DeleteCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteCameraResponse().from_map(
            await self.do_rpcrequest_async('DeleteCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_camera(
        self,
        request: cityvisual_20181030_models.DeleteCameraRequest,
    ) -> cityvisual_20181030_models.DeleteCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_camera_with_options(request, runtime)

    async def delete_camera_async(
        self,
        request: cityvisual_20181030_models.DeleteCameraRequest,
    ) -> cityvisual_20181030_models.DeleteCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_camera_with_options_async(request, runtime)

    def delete_capability_with_options(
        self,
        request: cityvisual_20181030_models.DeleteCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteCapabilityResponse().from_map(
            self.do_rpcrequest('DeleteCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_capability_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteCapabilityResponse().from_map(
            await self.do_rpcrequest_async('DeleteCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_capability(
        self,
        request: cityvisual_20181030_models.DeleteCapabilityRequest,
    ) -> cityvisual_20181030_models.DeleteCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_capability_with_options(request, runtime)

    async def delete_capability_async(
        self,
        request: cityvisual_20181030_models.DeleteCapabilityRequest,
    ) -> cityvisual_20181030_models.DeleteCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_capability_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: cityvisual_20181030_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: cityvisual_20181030_models.DeleteInstanceRequest,
    ) -> cityvisual_20181030_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: cityvisual_20181030_models.DeleteInstanceRequest,
    ) -> cityvisual_20181030_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_job_group_with_options(
        self,
        request: cityvisual_20181030_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteJobGroupResponse().from_map(
            self.do_rpcrequest('DeleteJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_group_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteJobGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job_group(
        self,
        request: cityvisual_20181030_models.DeleteJobGroupRequest,
    ) -> cityvisual_20181030_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    async def delete_job_group_async(
        self,
        request: cityvisual_20181030_models.DeleteJobGroupRequest,
    ) -> cityvisual_20181030_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_group_with_options_async(request, runtime)

    def delete_resource_profile_with_options(
        self,
        request: cityvisual_20181030_models.DeleteResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteResourceProfileResponse().from_map(
            self.do_rpcrequest('DeleteResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_resource_profile_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteResourceProfileResponse().from_map(
            await self.do_rpcrequest_async('DeleteResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_resource_profile(
        self,
        request: cityvisual_20181030_models.DeleteResourceProfileRequest,
    ) -> cityvisual_20181030_models.DeleteResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_profile_with_options(request, runtime)

    async def delete_resource_profile_async(
        self,
        request: cityvisual_20181030_models.DeleteResourceProfileRequest,
    ) -> cityvisual_20181030_models.DeleteResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_profile_with_options_async(request, runtime)

    def delete_work_group_with_options(
        self,
        request: cityvisual_20181030_models.DeleteWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteWorkGroupResponse().from_map(
            self.do_rpcrequest('DeleteWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_work_group_with_options_async(
        self,
        request: cityvisual_20181030_models.DeleteWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DeleteWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DeleteWorkGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_work_group(
        self,
        request: cityvisual_20181030_models.DeleteWorkGroupRequest,
    ) -> cityvisual_20181030_models.DeleteWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_work_group_with_options(request, runtime)

    async def delete_work_group_async(
        self,
        request: cityvisual_20181030_models.DeleteWorkGroupRequest,
    ) -> cityvisual_20181030_models.DeleteWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_work_group_with_options_async(request, runtime)

    def describe_algo_libs_with_options(
        self,
        request: cityvisual_20181030_models.DescribeAlgoLibsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeAlgoLibsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeAlgoLibsResponse().from_map(
            self.do_rpcrequest('DescribeAlgoLibs', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_algo_libs_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeAlgoLibsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeAlgoLibsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeAlgoLibsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAlgoLibs', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_algo_libs(
        self,
        request: cityvisual_20181030_models.DescribeAlgoLibsRequest,
    ) -> cityvisual_20181030_models.DescribeAlgoLibsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_algo_libs_with_options(request, runtime)

    async def describe_algo_libs_async(
        self,
        request: cityvisual_20181030_models.DescribeAlgoLibsRequest,
    ) -> cityvisual_20181030_models.DescribeAlgoLibsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_algo_libs_with_options_async(request, runtime)

    def describe_cameras_with_options(
        self,
        request: cityvisual_20181030_models.DescribeCamerasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeCamerasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeCamerasResponse().from_map(
            self.do_rpcrequest('DescribeCameras', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cameras_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeCamerasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeCamerasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeCamerasResponse().from_map(
            await self.do_rpcrequest_async('DescribeCameras', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cameras(
        self,
        request: cityvisual_20181030_models.DescribeCamerasRequest,
    ) -> cityvisual_20181030_models.DescribeCamerasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cameras_with_options(request, runtime)

    async def describe_cameras_async(
        self,
        request: cityvisual_20181030_models.DescribeCamerasRequest,
    ) -> cityvisual_20181030_models.DescribeCamerasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cameras_with_options_async(request, runtime)

    def describe_capabilities_with_options(
        self,
        request: cityvisual_20181030_models.DescribeCapabilitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeCapabilitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeCapabilitiesResponse().from_map(
            self.do_rpcrequest('DescribeCapabilities', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_capabilities_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeCapabilitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeCapabilitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeCapabilitiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCapabilities', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_capabilities(
        self,
        request: cityvisual_20181030_models.DescribeCapabilitiesRequest,
    ) -> cityvisual_20181030_models.DescribeCapabilitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_capabilities_with_options(request, runtime)

    async def describe_capabilities_async(
        self,
        request: cityvisual_20181030_models.DescribeCapabilitiesRequest,
    ) -> cityvisual_20181030_models.DescribeCapabilitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_capabilities_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: cityvisual_20181030_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: cityvisual_20181030_models.DescribeInstancesRequest,
    ) -> cityvisual_20181030_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: cityvisual_20181030_models.DescribeInstancesRequest,
    ) -> cityvisual_20181030_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_job_groups_with_options(
        self,
        request: cityvisual_20181030_models.DescribeJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeJobGroupsResponse().from_map(
            self.do_rpcrequest('DescribeJobGroups', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_job_groups_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeJobGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeJobGroups', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_job_groups(
        self,
        request: cityvisual_20181030_models.DescribeJobGroupsRequest,
    ) -> cityvisual_20181030_models.DescribeJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_groups_with_options(request, runtime)

    async def describe_job_groups_async(
        self,
        request: cityvisual_20181030_models.DescribeJobGroupsRequest,
    ) -> cityvisual_20181030_models.DescribeJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_groups_with_options_async(request, runtime)

    def describe_protocols_with_options(
        self,
        request: cityvisual_20181030_models.DescribeProtocolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeProtocolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeProtocolsResponse().from_map(
            self.do_rpcrequest('DescribeProtocols', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_protocols_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeProtocolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeProtocolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeProtocolsResponse().from_map(
            await self.do_rpcrequest_async('DescribeProtocols', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protocols(
        self,
        request: cityvisual_20181030_models.DescribeProtocolsRequest,
    ) -> cityvisual_20181030_models.DescribeProtocolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_protocols_with_options(request, runtime)

    async def describe_protocols_async(
        self,
        request: cityvisual_20181030_models.DescribeProtocolsRequest,
    ) -> cityvisual_20181030_models.DescribeProtocolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_protocols_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cityvisual_20181030_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: cityvisual_20181030_models.DescribeRegionsRequest,
    ) -> cityvisual_20181030_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cityvisual_20181030_models.DescribeRegionsRequest,
    ) -> cityvisual_20181030_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_resource_profiles_with_options(
        self,
        request: cityvisual_20181030_models.DescribeResourceProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeResourceProfilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeResourceProfilesResponse().from_map(
            self.do_rpcrequest('DescribeResourceProfiles', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_profiles_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeResourceProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeResourceProfilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeResourceProfilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeResourceProfiles', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_profiles(
        self,
        request: cityvisual_20181030_models.DescribeResourceProfilesRequest,
    ) -> cityvisual_20181030_models.DescribeResourceProfilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_profiles_with_options(request, runtime)

    async def describe_resource_profiles_async(
        self,
        request: cityvisual_20181030_models.DescribeResourceProfilesRequest,
    ) -> cityvisual_20181030_models.DescribeResourceProfilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_profiles_with_options_async(request, runtime)

    def describe_streams_with_options(
        self,
        request: cityvisual_20181030_models.DescribeStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeStreamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeStreamsResponse().from_map(
            self.do_rpcrequest('DescribeStreams', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_streams_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeStreamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeStreamsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStreams', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_streams(
        self,
        request: cityvisual_20181030_models.DescribeStreamsRequest,
    ) -> cityvisual_20181030_models.DescribeStreamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_streams_with_options(request, runtime)

    async def describe_streams_async(
        self,
        request: cityvisual_20181030_models.DescribeStreamsRequest,
    ) -> cityvisual_20181030_models.DescribeStreamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_streams_with_options_async(request, runtime)

    def describe_work_groups_with_options(
        self,
        request: cityvisual_20181030_models.DescribeWorkGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeWorkGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeWorkGroupsResponse().from_map(
            self.do_rpcrequest('DescribeWorkGroups', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_work_groups_with_options_async(
        self,
        request: cityvisual_20181030_models.DescribeWorkGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DescribeWorkGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DescribeWorkGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWorkGroups', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_work_groups(
        self,
        request: cityvisual_20181030_models.DescribeWorkGroupsRequest,
    ) -> cityvisual_20181030_models.DescribeWorkGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_work_groups_with_options(request, runtime)

    async def describe_work_groups_async(
        self,
        request: cityvisual_20181030_models.DescribeWorkGroupsRequest,
    ) -> cityvisual_20181030_models.DescribeWorkGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_work_groups_with_options_async(request, runtime)

    def detach_stream_with_options(
        self,
        request: cityvisual_20181030_models.DetachStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DetachStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DetachStreamResponse().from_map(
            self.do_rpcrequest('DetachStream', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_stream_with_options_async(
        self,
        request: cityvisual_20181030_models.DetachStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.DetachStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.DetachStreamResponse().from_map(
            await self.do_rpcrequest_async('DetachStream', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_stream(
        self,
        request: cityvisual_20181030_models.DetachStreamRequest,
    ) -> cityvisual_20181030_models.DetachStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_stream_with_options(request, runtime)

    async def detach_stream_async(
        self,
        request: cityvisual_20181030_models.DetachStreamRequest,
    ) -> cityvisual_20181030_models.DetachStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_stream_with_options_async(request, runtime)

    def get_camera_conf_for_camera_with_options(
        self,
        request: cityvisual_20181030_models.GetCameraConfForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetCameraConfForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetCameraConfForCameraResponse().from_map(
            self.do_rpcrequest('GetCameraConfForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_camera_conf_for_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.GetCameraConfForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetCameraConfForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetCameraConfForCameraResponse().from_map(
            await self.do_rpcrequest_async('GetCameraConfForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_camera_conf_for_camera(
        self,
        request: cityvisual_20181030_models.GetCameraConfForCameraRequest,
    ) -> cityvisual_20181030_models.GetCameraConfForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_camera_conf_for_camera_with_options(request, runtime)

    async def get_camera_conf_for_camera_async(
        self,
        request: cityvisual_20181030_models.GetCameraConfForCameraRequest,
    ) -> cityvisual_20181030_models.GetCameraConfForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_camera_conf_for_camera_with_options_async(request, runtime)

    def get_compute_job_log_with_options(
        self,
        request: cityvisual_20181030_models.GetComputeJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetComputeJobLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetComputeJobLogResponse().from_map(
            self.do_rpcrequest('GetComputeJobLog', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_compute_job_log_with_options_async(
        self,
        request: cityvisual_20181030_models.GetComputeJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetComputeJobLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetComputeJobLogResponse().from_map(
            await self.do_rpcrequest_async('GetComputeJobLog', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_compute_job_log(
        self,
        request: cityvisual_20181030_models.GetComputeJobLogRequest,
    ) -> cityvisual_20181030_models.GetComputeJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_compute_job_log_with_options(request, runtime)

    async def get_compute_job_log_async(
        self,
        request: cityvisual_20181030_models.GetComputeJobLogRequest,
    ) -> cityvisual_20181030_models.GetComputeJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_compute_job_log_with_options_async(request, runtime)

    def get_play_url_for_camera_with_options(
        self,
        request: cityvisual_20181030_models.GetPlayUrlForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetPlayUrlForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetPlayUrlForCameraResponse().from_map(
            self.do_rpcrequest('GetPlayUrlForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_play_url_for_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.GetPlayUrlForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.GetPlayUrlForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.GetPlayUrlForCameraResponse().from_map(
            await self.do_rpcrequest_async('GetPlayUrlForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_play_url_for_camera(
        self,
        request: cityvisual_20181030_models.GetPlayUrlForCameraRequest,
    ) -> cityvisual_20181030_models.GetPlayUrlForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_play_url_for_camera_with_options(request, runtime)

    async def get_play_url_for_camera_async(
        self,
        request: cityvisual_20181030_models.GetPlayUrlForCameraRequest,
    ) -> cityvisual_20181030_models.GetPlayUrlForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_play_url_for_camera_with_options_async(request, runtime)

    def list_compute_job_logs_with_options(
        self,
        request: cityvisual_20181030_models.ListComputeJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListComputeJobLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListComputeJobLogsResponse().from_map(
            self.do_rpcrequest('ListComputeJobLogs', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_compute_job_logs_with_options_async(
        self,
        request: cityvisual_20181030_models.ListComputeJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListComputeJobLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListComputeJobLogsResponse().from_map(
            await self.do_rpcrequest_async('ListComputeJobLogs', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_compute_job_logs(
        self,
        request: cityvisual_20181030_models.ListComputeJobLogsRequest,
    ) -> cityvisual_20181030_models.ListComputeJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_compute_job_logs_with_options(request, runtime)

    async def list_compute_job_logs_async(
        self,
        request: cityvisual_20181030_models.ListComputeJobLogsRequest,
    ) -> cityvisual_20181030_models.ListComputeJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_compute_job_logs_with_options_async(request, runtime)

    def list_parking_results_with_options(
        self,
        request: cityvisual_20181030_models.ListParkingResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListParkingResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListParkingResultsResponse().from_map(
            self.do_rpcrequest('ListParkingResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_parking_results_with_options_async(
        self,
        request: cityvisual_20181030_models.ListParkingResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListParkingResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListParkingResultsResponse().from_map(
            await self.do_rpcrequest_async('ListParkingResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_parking_results(
        self,
        request: cityvisual_20181030_models.ListParkingResultsRequest,
    ) -> cityvisual_20181030_models.ListParkingResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parking_results_with_options(request, runtime)

    async def list_parking_results_async(
        self,
        request: cityvisual_20181030_models.ListParkingResultsRequest,
    ) -> cityvisual_20181030_models.ListParkingResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parking_results_with_options_async(request, runtime)

    def list_safety_helmet_results_with_options(
        self,
        request: cityvisual_20181030_models.ListSafetyHelmetResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListSafetyHelmetResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListSafetyHelmetResultsResponse().from_map(
            self.do_rpcrequest('ListSafetyHelmetResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_safety_helmet_results_with_options_async(
        self,
        request: cityvisual_20181030_models.ListSafetyHelmetResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListSafetyHelmetResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListSafetyHelmetResultsResponse().from_map(
            await self.do_rpcrequest_async('ListSafetyHelmetResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_safety_helmet_results(
        self,
        request: cityvisual_20181030_models.ListSafetyHelmetResultsRequest,
    ) -> cityvisual_20181030_models.ListSafetyHelmetResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_safety_helmet_results_with_options(request, runtime)

    async def list_safety_helmet_results_async(
        self,
        request: cityvisual_20181030_models.ListSafetyHelmetResultsRequest,
    ) -> cityvisual_20181030_models.ListSafetyHelmetResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_safety_helmet_results_with_options_async(request, runtime)

    def list_streams_for_cameras_with_options(
        self,
        request: cityvisual_20181030_models.ListStreamsForCamerasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListStreamsForCamerasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListStreamsForCamerasResponse().from_map(
            self.do_rpcrequest('ListStreamsForCameras', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_streams_for_cameras_with_options_async(
        self,
        request: cityvisual_20181030_models.ListStreamsForCamerasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListStreamsForCamerasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListStreamsForCamerasResponse().from_map(
            await self.do_rpcrequest_async('ListStreamsForCameras', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_streams_for_cameras(
        self,
        request: cityvisual_20181030_models.ListStreamsForCamerasRequest,
    ) -> cityvisual_20181030_models.ListStreamsForCamerasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_streams_for_cameras_with_options(request, runtime)

    async def list_streams_for_cameras_async(
        self,
        request: cityvisual_20181030_models.ListStreamsForCamerasRequest,
    ) -> cityvisual_20181030_models.ListStreamsForCamerasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_streams_for_cameras_with_options_async(request, runtime)

    def list_vehicle_entry_results_with_options(
        self,
        request: cityvisual_20181030_models.ListVehicleEntryResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListVehicleEntryResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListVehicleEntryResultsResponse().from_map(
            self.do_rpcrequest('ListVehicleEntryResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_entry_results_with_options_async(
        self,
        request: cityvisual_20181030_models.ListVehicleEntryResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ListVehicleEntryResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ListVehicleEntryResultsResponse().from_map(
            await self.do_rpcrequest_async('ListVehicleEntryResults', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_entry_results(
        self,
        request: cityvisual_20181030_models.ListVehicleEntryResultsRequest,
    ) -> cityvisual_20181030_models.ListVehicleEntryResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_entry_results_with_options(request, runtime)

    async def list_vehicle_entry_results_async(
        self,
        request: cityvisual_20181030_models.ListVehicleEntryResultsRequest,
    ) -> cityvisual_20181030_models.ListVehicleEntryResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_entry_results_with_options_async(request, runtime)

    def modify_algo_lib_with_options(
        self,
        request: cityvisual_20181030_models.ModifyAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyAlgoLibResponse().from_map(
            self.do_rpcrequest('ModifyAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_algo_lib_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyAlgoLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyAlgoLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyAlgoLibResponse().from_map(
            await self.do_rpcrequest_async('ModifyAlgoLib', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_algo_lib(
        self,
        request: cityvisual_20181030_models.ModifyAlgoLibRequest,
    ) -> cityvisual_20181030_models.ModifyAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_algo_lib_with_options(request, runtime)

    async def modify_algo_lib_async(
        self,
        request: cityvisual_20181030_models.ModifyAlgoLibRequest,
    ) -> cityvisual_20181030_models.ModifyAlgoLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_algo_lib_with_options_async(request, runtime)

    def modify_camera_with_options(
        self,
        request: cityvisual_20181030_models.ModifyCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyCameraResponse().from_map(
            self.do_rpcrequest('ModifyCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyCameraResponse().from_map(
            await self.do_rpcrequest_async('ModifyCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_camera(
        self,
        request: cityvisual_20181030_models.ModifyCameraRequest,
    ) -> cityvisual_20181030_models.ModifyCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_camera_with_options(request, runtime)

    async def modify_camera_async(
        self,
        request: cityvisual_20181030_models.ModifyCameraRequest,
    ) -> cityvisual_20181030_models.ModifyCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_camera_with_options_async(request, runtime)

    def modify_capability_with_options(
        self,
        request: cityvisual_20181030_models.ModifyCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyCapabilityResponse().from_map(
            self.do_rpcrequest('ModifyCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_capability_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyCapabilityResponse().from_map(
            await self.do_rpcrequest_async('ModifyCapability', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_capability(
        self,
        request: cityvisual_20181030_models.ModifyCapabilityRequest,
    ) -> cityvisual_20181030_models.ModifyCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_capability_with_options(request, runtime)

    async def modify_capability_async(
        self,
        request: cityvisual_20181030_models.ModifyCapabilityRequest,
    ) -> cityvisual_20181030_models.ModifyCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_capability_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: cityvisual_20181030_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyInstanceResponse().from_map(
            self.do_rpcrequest('ModifyInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstance', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance(
        self,
        request: cityvisual_20181030_models.ModifyInstanceRequest,
    ) -> cityvisual_20181030_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: cityvisual_20181030_models.ModifyInstanceRequest,
    ) -> cityvisual_20181030_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_job_group_with_options(
        self,
        request: cityvisual_20181030_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyJobGroupResponse().from_map(
            self.do_rpcrequest('ModifyJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_job_group_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyJobGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_job_group(
        self,
        request: cityvisual_20181030_models.ModifyJobGroupRequest,
    ) -> cityvisual_20181030_models.ModifyJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_job_group_with_options(request, runtime)

    async def modify_job_group_async(
        self,
        request: cityvisual_20181030_models.ModifyJobGroupRequest,
    ) -> cityvisual_20181030_models.ModifyJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_job_group_with_options_async(request, runtime)

    def modify_resource_profile_with_options(
        self,
        request: cityvisual_20181030_models.ModifyResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyResourceProfileResponse().from_map(
            self.do_rpcrequest('ModifyResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_profile_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyResourceProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyResourceProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyResourceProfileResponse().from_map(
            await self.do_rpcrequest_async('ModifyResourceProfile', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_profile(
        self,
        request: cityvisual_20181030_models.ModifyResourceProfileRequest,
    ) -> cityvisual_20181030_models.ModifyResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_profile_with_options(request, runtime)

    async def modify_resource_profile_async(
        self,
        request: cityvisual_20181030_models.ModifyResourceProfileRequest,
    ) -> cityvisual_20181030_models.ModifyResourceProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_profile_with_options_async(request, runtime)

    def modify_work_group_with_options(
        self,
        request: cityvisual_20181030_models.ModifyWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyWorkGroupResponse().from_map(
            self.do_rpcrequest('ModifyWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_work_group_with_options_async(
        self,
        request: cityvisual_20181030_models.ModifyWorkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.ModifyWorkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.ModifyWorkGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyWorkGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_work_group(
        self,
        request: cityvisual_20181030_models.ModifyWorkGroupRequest,
    ) -> cityvisual_20181030_models.ModifyWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_work_group_with_options(request, runtime)

    async def modify_work_group_async(
        self,
        request: cityvisual_20181030_models.ModifyWorkGroupRequest,
    ) -> cityvisual_20181030_models.ModifyWorkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_work_group_with_options_async(request, runtime)

    def put_camera_conf_for_camera_with_options(
        self,
        request: cityvisual_20181030_models.PutCameraConfForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.PutCameraConfForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.PutCameraConfForCameraResponse().from_map(
            self.do_rpcrequest('PutCameraConfForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_camera_conf_for_camera_with_options_async(
        self,
        request: cityvisual_20181030_models.PutCameraConfForCameraRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.PutCameraConfForCameraResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.PutCameraConfForCameraResponse().from_map(
            await self.do_rpcrequest_async('PutCameraConfForCamera', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_camera_conf_for_camera(
        self,
        request: cityvisual_20181030_models.PutCameraConfForCameraRequest,
    ) -> cityvisual_20181030_models.PutCameraConfForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_camera_conf_for_camera_with_options(request, runtime)

    async def put_camera_conf_for_camera_async(
        self,
        request: cityvisual_20181030_models.PutCameraConfForCameraRequest,
    ) -> cityvisual_20181030_models.PutCameraConfForCameraResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_camera_conf_for_camera_with_options_async(request, runtime)

    def search_images_with_options(
        self,
        request: cityvisual_20181030_models.SearchImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.SearchImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.SearchImagesResponse().from_map(
            self.do_rpcrequest('SearchImages', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_images_with_options_async(
        self,
        request: cityvisual_20181030_models.SearchImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.SearchImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.SearchImagesResponse().from_map(
            await self.do_rpcrequest_async('SearchImages', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_images(
        self,
        request: cityvisual_20181030_models.SearchImagesRequest,
    ) -> cityvisual_20181030_models.SearchImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_images_with_options(request, runtime)

    async def search_images_async(
        self,
        request: cityvisual_20181030_models.SearchImagesRequest,
    ) -> cityvisual_20181030_models.SearchImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_images_with_options_async(request, runtime)

    def start_job_group_with_options(
        self,
        request: cityvisual_20181030_models.StartJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.StartJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.StartJobGroupResponse().from_map(
            self.do_rpcrequest('StartJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_job_group_with_options_async(
        self,
        request: cityvisual_20181030_models.StartJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.StartJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.StartJobGroupResponse().from_map(
            await self.do_rpcrequest_async('StartJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_job_group(
        self,
        request: cityvisual_20181030_models.StartJobGroupRequest,
    ) -> cityvisual_20181030_models.StartJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_job_group_with_options(request, runtime)

    async def start_job_group_async(
        self,
        request: cityvisual_20181030_models.StartJobGroupRequest,
    ) -> cityvisual_20181030_models.StartJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_job_group_with_options_async(request, runtime)

    def stop_job_group_with_options(
        self,
        request: cityvisual_20181030_models.StopJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.StopJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.StopJobGroupResponse().from_map(
            self.do_rpcrequest('StopJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_job_group_with_options_async(
        self,
        request: cityvisual_20181030_models.StopJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cityvisual_20181030_models.StopJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cityvisual_20181030_models.StopJobGroupResponse().from_map(
            await self.do_rpcrequest_async('StopJobGroup', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_job_group(
        self,
        request: cityvisual_20181030_models.StopJobGroupRequest,
    ) -> cityvisual_20181030_models.StopJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_job_group_with_options(request, runtime)

    async def stop_job_group_async(
        self,
        request: cityvisual_20181030_models.StopJobGroupRequest,
    ) -> cityvisual_20181030_models.StopJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_job_group_with_options_async(request, runtime)
