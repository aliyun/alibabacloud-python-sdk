# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pai_dsw20210226 import models as pai_dsw_20210226_models
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
        self._endpoint = self.get_endpoint('pai-dsw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_instance_snapshot(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_instance_snapshot_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def create_instance_snapshot_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        if not UtilClient.is_unset(request.instance_snapshot_repo_url):
            body['InstanceSnapshotRepoUrl'] = request.instance_snapshot_repo_url
        if not UtilClient.is_unset(request.instance_snapshot_description):
            body['InstanceSnapshotDescription'] = request.instance_snapshot_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            self.do_roarequest('CreateInstanceSnapshot', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    async def create_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        if not UtilClient.is_unset(request.instance_snapshot_repo_url):
            body['InstanceSnapshotRepoUrl'] = request.instance_snapshot_repo_url
        if not UtilClient.is_unset(request.instance_snapshot_description):
            body['InstanceSnapshotDescription'] = request.instance_snapshot_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            await self.do_roarequest_async('CreateInstanceSnapshot', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    def delete_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def delete_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def delete_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            self.do_roarequest('DeleteInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    async def delete_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('DeleteInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    def get_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def get_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def get_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            self.do_roarequest('GetInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    async def get_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('GetInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            self.do_roarequest('StopInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/stop', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            await self.do_roarequest_async('StopInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/stop', 'json', req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceRequest,
    ) -> pai_dsw_20210226_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceRequest,
    ) -> pai_dsw_20210226_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceResponse(),
            self.do_roarequest('UpdateInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceResponse(),
            await self.do_roarequest_async('UpdateInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    def list_ecs_specs(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsRequest,
    ) -> pai_dsw_20210226_models.ListEcsSpecsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsRequest,
    ) -> pai_dsw_20210226_models.ListEcsSpecsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListEcsSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsResponse(),
            self.do_roarequest('ListEcsSpecs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/ecsSpecs', 'json', req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListEcsSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsResponse(),
            await self.do_roarequest_async('ListEcsSpecs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/ecsSpecs', 'json', req, runtime)
        )

    def delete_instance_snapshot(
        self,
        instance_id: str,
        instance_snapshot_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_with_options(instance_id, instance_snapshot_id, headers, runtime)

    async def delete_instance_snapshot_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_snapshot_with_options_async(instance_id, instance_snapshot_id, headers, runtime)

    def delete_instance_snapshot_with_options(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            self.do_roarequest('DeleteInstanceSnapshot', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    async def delete_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            await self.do_roarequest_async('DeleteInstanceSnapshot', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    def update_instance_snapshot(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceSnapshotRequest,
    ) -> pai_dsw_20210226_models.UpdateInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_snapshot_with_options(instance_id, instance_snapshot_id, request, headers, runtime)

    async def update_instance_snapshot_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceSnapshotRequest,
    ) -> pai_dsw_20210226_models.UpdateInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_snapshot_with_options_async(instance_id, instance_snapshot_id, request, headers, runtime)

    def update_instance_snapshot_with_options(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceSnapshotResponse(),
            self.do_roarequest('UpdateInstanceSnapshot', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    async def update_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceSnapshotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceSnapshotResponse(),
            await self.do_roarequest_async('UpdateInstanceSnapshot', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: pai_dsw_20210226_models.CreateInstanceRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: pai_dsw_20210226_models.CreateInstanceRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: pai_dsw_20210226_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.nas_file_system_id):
            body['NasFileSystemId'] = request.nas_file_system_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            self.do_roarequest('CreateInstance', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: pai_dsw_20210226_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.nas_file_system_id):
            body['NasFileSystemId'] = request.nas_file_system_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            await self.do_roarequest_async('CreateInstance', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/', 'json', req, runtime)
        )

    def get_authorization(self) -> pai_dsw_20210226_models.GetAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_authorization_with_options(headers, runtime)

    async def get_authorization_async(self) -> pai_dsw_20210226_models.GetAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_authorization_with_options_async(headers, runtime)

    def get_authorization_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetAuthorizationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetAuthorizationResponse(),
            self.do_roarequest('GetAuthorization', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/authorization', 'json', req, runtime)
        )

    async def get_authorization_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetAuthorizationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetAuthorizationResponse(),
            await self.do_roarequest_async('GetAuthorization', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/authorization', 'json', req, runtime)
        )

    def list_images(
        self,
        request: pai_dsw_20210226_models.ListImagesRequest,
    ) -> pai_dsw_20210226_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: pai_dsw_20210226_models.ListImagesRequest,
    ) -> pai_dsw_20210226_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: pai_dsw_20210226_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        if not UtilClient.is_unset(request.image_type_equals):
            query['ImageTypeEquals'] = request.image_type_equals
        if not UtilClient.is_unset(request.image_name_contains):
            query['ImageNameContains'] = request.image_name_contains
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            self.do_roarequest('ListImages', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        if not UtilClient.is_unset(request.image_type_equals):
            query['ImageTypeEquals'] = request.image_type_equals
        if not UtilClient.is_unset(request.image_name_contains):
            query['ImageNameContains'] = request.image_name_contains
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            await self.do_roarequest_async('ListImages', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    def foobar(self) -> pai_dsw_20210226_models.FoobarResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.foobar_with_options(headers, runtime)

    async def foobar_async(self) -> pai_dsw_20210226_models.FoobarResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.foobar_with_options_async(headers, runtime)

    def foobar_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.FoobarResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.FoobarResponse(),
            self.do_roarequest('Foobar', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/foobar', 'json', req, runtime)
        )

    async def foobar_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.FoobarResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.FoobarResponse(),
            await self.do_roarequest_async('Foobar', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/foobar', 'json', req, runtime)
        )

    def list_instance_snapshots(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshots_with_options(instance_id, headers, runtime)

    async def list_instance_snapshots_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_snapshots_with_options_async(instance_id, headers, runtime)

    def list_instance_snapshots_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            self.do_roarequest('ListInstanceSnapshots', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    async def list_instance_snapshots_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            await self.do_roarequest_async('ListInstanceSnapshots', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    def create_instance_shutdown_timer(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_with_options(instance_id, request, headers, runtime)

    async def create_instance_shutdown_timer_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerRequest,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_shutdown_timer_with_options_async(instance_id, request, headers, runtime)

    def create_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.schedule_time):
            body['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            self.do_roarequest('CreateInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    async def create_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.schedule_time):
            body['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('CreateInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            self.do_roarequest('GetInstance', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            await self.do_roarequest_async('GetInstance', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: pai_dsw_20210226_models.ListInstancesRequest,
    ) -> pai_dsw_20210226_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesRequest,
    ) -> pai_dsw_20210226_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_dsw_20210226_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name_contains):
            query['InstanceNameContains'] = request.instance_name_contains
        if not UtilClient.is_unset(request.instance_status_equals):
            query['InstanceStatusEquals'] = request.instance_status_equals
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            self.do_roarequest('ListInstances', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name_contains):
            query['InstanceNameContains'] = request.instance_name_contains
        if not UtilClient.is_unset(request.instance_status_equals):
            query['InstanceStatusEquals'] = request.instance_status_equals
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            await self.do_roarequest_async('ListInstances', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances', 'json', req, runtime)
        )

    def get_instance_snapshot(
        self,
        instance_id: str,
        instance_snapshot_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_with_options(instance_id, instance_snapshot_id, headers, runtime)

    async def get_instance_snapshot_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_snapshot_with_options_async(instance_id, instance_snapshot_id, headers, runtime)

    def get_instance_snapshot_with_options(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            self.do_roarequest('GetInstanceSnapshot', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    async def get_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            await self.do_roarequest_async('GetInstanceSnapshot', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    def start_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_with_options(instance_id, headers, runtime)

    async def start_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_instance_with_options_async(instance_id, headers, runtime)

    def start_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StartInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            self.do_roarequest('StartInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/start', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StartInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            await self.do_roarequest_async('StartInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/start', 'json', req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            self.do_roarequest('DeleteInstance', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            await self.do_roarequest_async('DeleteInstance', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )
