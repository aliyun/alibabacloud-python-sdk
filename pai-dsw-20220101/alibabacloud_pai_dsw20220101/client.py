# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pai_dsw20220101 import models as pai_dsw_20220101_models
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

    def create_idle_instance_culler_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateIdleInstanceCullerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateIdleInstanceCullerResponse:
        """
        @summary Creates an automatic stop policy for a specific Data Science Workshop (DSW) instance. When the conditions are met, the instance is automatically stopped. You can create only one automatic stop policy for an idle DSW instance. If the specific instance has an automatic stop policy, call DeleteIdleInstanceCuller to delete it first.
        
        @param request: CreateIdleInstanceCullerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdleInstanceCullerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_percent_threshold):
            body['CpuPercentThreshold'] = request.cpu_percent_threshold
        if not UtilClient.is_unset(request.gpu_percent_threshold):
            body['GpuPercentThreshold'] = request.gpu_percent_threshold
        if not UtilClient.is_unset(request.max_idle_time_in_minutes):
            body['MaxIdleTimeInMinutes'] = request.max_idle_time_in_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateIdleInstanceCullerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateIdleInstanceCullerResponse:
        """
        @summary Creates an automatic stop policy for a specific Data Science Workshop (DSW) instance. When the conditions are met, the instance is automatically stopped. You can create only one automatic stop policy for an idle DSW instance. If the specific instance has an automatic stop policy, call DeleteIdleInstanceCuller to delete it first.
        
        @param request: CreateIdleInstanceCullerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdleInstanceCullerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_percent_threshold):
            body['CpuPercentThreshold'] = request.cpu_percent_threshold
        if not UtilClient.is_unset(request.gpu_percent_threshold):
            body['GpuPercentThreshold'] = request.gpu_percent_threshold
        if not UtilClient.is_unset(request.max_idle_time_in_minutes):
            body['MaxIdleTimeInMinutes'] = request.max_idle_time_in_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idle_instance_culler(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateIdleInstanceCullerRequest,
    ) -> pai_dsw_20220101_models.CreateIdleInstanceCullerResponse:
        """
        @summary Creates an automatic stop policy for a specific Data Science Workshop (DSW) instance. When the conditions are met, the instance is automatically stopped. You can create only one automatic stop policy for an idle DSW instance. If the specific instance has an automatic stop policy, call DeleteIdleInstanceCuller to delete it first.
        
        @param request: CreateIdleInstanceCullerRequest
        @return: CreateIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_idle_instance_culler_with_options(instance_id, request, headers, runtime)

    async def create_idle_instance_culler_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateIdleInstanceCullerRequest,
    ) -> pai_dsw_20220101_models.CreateIdleInstanceCullerResponse:
        """
        @summary Creates an automatic stop policy for a specific Data Science Workshop (DSW) instance. When the conditions are met, the instance is automatically stopped. You can create only one automatic stop policy for an idle DSW instance. If the specific instance has an automatic stop policy, call DeleteIdleInstanceCuller to delete it first.
        
        @param request: CreateIdleInstanceCullerRequest
        @return: CreateIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_idle_instance_culler_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
        """
        @summary Creates a Data Science Workshop (DSW) instance.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.affinity):
            body['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.driver):
            body['Driver'] = request.driver
        if not UtilClient.is_unset(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
        """
        @summary Creates a Data Science Workshop (DSW) instance.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.affinity):
            body['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.driver):
            body['Driver'] = request.driver
        if not UtilClient.is_unset(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
        """
        @summary Creates a Data Science Workshop (DSW) instance.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
        """
        @summary Creates a Data Science Workshop (DSW) instance.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse:
        """
        @summary Creates a scheduled stop task for an instance.
        
        @param request: CreateInstanceShutdownTimerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceShutdownTimerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['DueTime'] = request.due_time
        if not UtilClient.is_unset(request.remaining_time_in_ms):
            body['RemainingTimeInMs'] = request.remaining_time_in_ms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse:
        """
        @summary Creates a scheduled stop task for an instance.
        
        @param request: CreateInstanceShutdownTimerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceShutdownTimerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['DueTime'] = request.due_time
        if not UtilClient.is_unset(request.remaining_time_in_ms):
            body['RemainingTimeInMs'] = request.remaining_time_in_ms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_shutdown_timer(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceShutdownTimerRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse:
        """
        @summary Creates a scheduled stop task for an instance.
        
        @param request: CreateInstanceShutdownTimerRequest
        @return: CreateInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_with_options(instance_id, request, headers, runtime)

    async def create_instance_shutdown_timer_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceShutdownTimerRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse:
        """
        @summary Creates a scheduled stop task for an instance.
        
        @param request: CreateInstanceShutdownTimerRequest
        @return: CreateInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_shutdown_timer_with_options_async(instance_id, request, headers, runtime)

    def create_instance_snapshot_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceSnapshotResponse:
        """
        @summary 创建实例快照
        
        @param request: CreateInstanceSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceSnapshotResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_paths):
            body['ExcludePaths'] = request.exclude_paths
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not UtilClient.is_unset(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceSnapshotResponse:
        """
        @summary 创建实例快照
        
        @param request: CreateInstanceSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceSnapshotResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exclude_paths):
            body['ExcludePaths'] = request.exclude_paths
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not UtilClient.is_unset(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.CreateInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_snapshot(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceSnapshotResponse:
        """
        @summary 创建实例快照
        
        @param request: CreateInstanceSnapshotRequest
        @return: CreateInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_instance_snapshot_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceSnapshotResponse:
        """
        @summary 创建实例快照
        
        @param request: CreateInstanceSnapshotRequest
        @return: CreateInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def delete_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
        """
        @summary Deletes the automatic stop policy of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdleInstanceCullerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
        """
        @summary Deletes the automatic stop policy of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdleInstanceCullerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_idle_instance_culler(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
        """
        @summary Deletes the automatic stop policy of an instance.
        
        @return: DeleteIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def delete_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
        """
        @summary Deletes the automatic stop policy of an instance.
        
        @return: DeleteIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
        """
        @summary Deletes a specific instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
        """
        @summary Deletes a specific instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
        """
        @summary Deletes a specific instance.
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
        """
        @summary Deletes a specific instance.
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_labels_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.DeleteInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceLabelsResponse:
        """
        @summary Delete tags from a Data Science Workshop (DSW) instance.
        
        @param request: DeleteInstanceLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceLabels',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_labels_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.DeleteInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceLabelsResponse:
        """
        @summary Delete tags from a Data Science Workshop (DSW) instance.
        
        @param request: DeleteInstanceLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceLabelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceLabels',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labels',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_labels(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.DeleteInstanceLabelsRequest,
    ) -> pai_dsw_20220101_models.DeleteInstanceLabelsResponse:
        """
        @summary Delete tags from a Data Science Workshop (DSW) instance.
        
        @param request: DeleteInstanceLabelsRequest
        @return: DeleteInstanceLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_labels_with_options(instance_id, request, headers, runtime)

    async def delete_instance_labels_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.DeleteInstanceLabelsRequest,
    ) -> pai_dsw_20220101_models.DeleteInstanceLabelsResponse:
        """
        @summary Delete tags from a Data Science Workshop (DSW) instance.
        
        @param request: DeleteInstanceLabelsRequest
        @return: DeleteInstanceLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_labels_with_options_async(instance_id, request, headers, runtime)

    def delete_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
        """
        @summary Deletes a scheduled stop task of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceShutdownTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
        """
        @summary Deletes a scheduled stop task of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceShutdownTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
        """
        @summary Deletes a scheduled stop task of an instance.
        
        @return: DeleteInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def delete_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
        """
        @summary Deletes a scheduled stop task of an instance.
        
        @return: DeleteInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def delete_instance_snapshot_with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.DeleteInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_snapshot(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @return: DeleteInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def delete_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @return: DeleteInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_snapshot_with_options_async(instance_id, snapshot_id, headers, runtime)

    def get_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
        """
        @summary Queries the information about an auto stop policy for a specific idle instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdleInstanceCullerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
        """
        @summary Queries the information about an auto stop policy for a specific idle instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdleInstanceCullerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIdleInstanceCuller',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/idleinstanceculler',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_idle_instance_culler(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
        """
        @summary Queries the information about an auto stop policy for a specific idle instance.
        
        @return: GetIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def get_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
        """
        @summary Queries the information about an auto stop policy for a specific idle instance.
        
        @return: GetIdleInstanceCullerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        """
        @summary Queries the details of a DSW instance.
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        """
        @summary Queries the details of a DSW instance.
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceRequest,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        """
        @summary Queries the details of a DSW instance.
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, request, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceRequest,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        """
        @summary Queries the details of a DSW instance.
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, request, headers, runtime)

    def get_instance_events_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceEventsResponse:
        """
        @summary Queries a list of system events for a Data Science Workshop (DSW) instance.
        
        @param request: GetInstanceEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceEvents',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_events_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceEventsResponse:
        """
        @summary Queries a list of system events for a Data Science Workshop (DSW) instance.
        
        @param request: GetInstanceEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceEvents',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_events(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceEventsRequest,
    ) -> pai_dsw_20220101_models.GetInstanceEventsResponse:
        """
        @summary Queries a list of system events for a Data Science Workshop (DSW) instance.
        
        @param request: GetInstanceEventsRequest
        @return: GetInstanceEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_events_with_options(instance_id, request, headers, runtime)

    async def get_instance_events_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceEventsRequest,
    ) -> pai_dsw_20220101_models.GetInstanceEventsResponse:
        """
        @summary Queries a list of system events for a Data Science Workshop (DSW) instance.
        
        @param request: GetInstanceEventsRequest
        @return: GetInstanceEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_events_with_options_async(instance_id, request, headers, runtime)

    def get_instance_metrics_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
        """
        @summary Queries the resource metrics of an instance.
        
        @param request: GetInstanceMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMetrics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instance/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_metrics_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
        """
        @summary Queries the resource metrics of an instance.
        
        @param request: GetInstanceMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMetrics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instance/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_metrics(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
        """
        @summary Queries the resource metrics of an instance.
        
        @param request: GetInstanceMetricsRequest
        @return: GetInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_metrics_with_options(instance_id, request, headers, runtime)

    async def get_instance_metrics_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
        """
        @summary Queries the resource metrics of an instance.
        
        @param request: GetInstanceMetricsRequest
        @return: GetInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_metrics_with_options_async(instance_id, request, headers, runtime)

    def get_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
        """
        @summary 获取定时关机任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceShutdownTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
        """
        @summary 获取定时关机任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceShutdownTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimer',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/shutdowntimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
        """
        @summary 获取定时关机任务
        
        @return: GetInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def get_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
        """
        @summary 获取定时关机任务
        
        @return: GetInstanceShutdownTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def get_instance_snapshot_with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSnapshotResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots/{OpenApiUtilClient.get_encode_param(snapshot_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_snapshot(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @return: GetInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def get_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceSnapshotResponse:
        """
        @summary 获取实例快照详情
        
        @return: GetInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_snapshot_with_options_async(instance_id, snapshot_id, headers, runtime)

    def get_lifecycle_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetLifecycleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetLifecycleResponse:
        """
        @summary Obtains the lifecycle of an instance
        
        @description Obtains the lifecycle transition information for an instance, including details on the status an instance transitions to at a specific point in time.
        
        @param request: GetLifecycleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLifecycleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.session_number):
            query['SessionNumber'] = request.session_number
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLifecycle',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/lifecycle',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetLifecycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lifecycle_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetLifecycleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetLifecycleResponse:
        """
        @summary Obtains the lifecycle of an instance
        
        @description Obtains the lifecycle transition information for an instance, including details on the status an instance transitions to at a specific point in time.
        
        @param request: GetLifecycleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLifecycleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.session_number):
            query['SessionNumber'] = request.session_number
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLifecycle',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/lifecycle',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetLifecycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lifecycle(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetLifecycleRequest,
    ) -> pai_dsw_20220101_models.GetLifecycleResponse:
        """
        @summary Obtains the lifecycle of an instance
        
        @description Obtains the lifecycle transition information for an instance, including details on the status an instance transitions to at a specific point in time.
        
        @param request: GetLifecycleRequest
        @return: GetLifecycleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_lifecycle_with_options(instance_id, request, headers, runtime)

    async def get_lifecycle_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetLifecycleRequest,
    ) -> pai_dsw_20220101_models.GetLifecycleResponse:
        """
        @summary Obtains the lifecycle of an instance
        
        @description Obtains the lifecycle transition information for an instance, including details on the status an instance transitions to at a specific point in time.
        
        @param request: GetLifecycleRequest
        @return: GetLifecycleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_lifecycle_with_options_async(instance_id, request, headers, runtime)

    def get_metrics_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetMetricsResponse:
        """
        @summary 获取metrics数据
        
        @param request: GetMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetrics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instance/{OpenApiUtilClient.get_encode_param(instance_id)}/cms/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metrics_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetMetricsResponse:
        """
        @summary 获取metrics数据
        
        @param request: GetMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetrics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instance/{OpenApiUtilClient.get_encode_param(instance_id)}/cms/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metrics(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetMetricsRequest,
    ) -> pai_dsw_20220101_models.GetMetricsResponse:
        """
        @summary 获取metrics数据
        
        @param request: GetMetricsRequest
        @return: GetMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_metrics_with_options(instance_id, request, headers, runtime)

    async def get_metrics_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetMetricsRequest,
    ) -> pai_dsw_20220101_models.GetMetricsResponse:
        """
        @summary 获取metrics数据
        
        @param request: GetMetricsRequest
        @return: GetMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_metrics_with_options_async(instance_id, request, headers, runtime)

    def get_resource_group_statistics_with_options(
        self,
        request: pai_dsw_20220101_models.GetResourceGroupStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetResourceGroupStatisticsResponse:
        """
        @param request: GetResourceGroupStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupStatistics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resourcegroupstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetResourceGroupStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_statistics_with_options_async(
        self,
        request: pai_dsw_20220101_models.GetResourceGroupStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetResourceGroupStatisticsResponse:
        """
        @param request: GetResourceGroupStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceGroupStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupStatistics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/resourcegroupstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetResourceGroupStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_statistics(
        self,
        request: pai_dsw_20220101_models.GetResourceGroupStatisticsRequest,
    ) -> pai_dsw_20220101_models.GetResourceGroupStatisticsResponse:
        """
        @param request: GetResourceGroupStatisticsRequest
        @return: GetResourceGroupStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_group_statistics_with_options(request, headers, runtime)

    async def get_resource_group_statistics_async(
        self,
        request: pai_dsw_20220101_models.GetResourceGroupStatisticsRequest,
    ) -> pai_dsw_20220101_models.GetResourceGroupStatisticsResponse:
        """
        @param request: GetResourceGroupStatisticsRequest
        @return: GetResourceGroupStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_group_statistics_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
        """
        @summary Obtains the temporary authentication information of a DSW instance.
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
        """
        @summary Obtains the temporary authentication information of a DSW instance.
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
        """
        @summary Obtains the temporary authentication information of a DSW instance.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
        """
        @summary Obtains the temporary authentication information of a DSW instance.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_user_command_with_options(
        self,
        user_command_id: str,
        request: pai_dsw_20220101_models.GetUserCommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetUserCommandResponse:
        """
        @summary 获取自定义用户命令
        
        @param request: GetUserCommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCommand',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/usercommands/{OpenApiUtilClient.get_encode_param(user_command_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetUserCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_command_with_options_async(
        self,
        user_command_id: str,
        request: pai_dsw_20220101_models.GetUserCommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetUserCommandResponse:
        """
        @summary 获取自定义用户命令
        
        @param request: GetUserCommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCommand',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/usercommands/{OpenApiUtilClient.get_encode_param(user_command_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetUserCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_command(
        self,
        user_command_id: str,
        request: pai_dsw_20220101_models.GetUserCommandRequest,
    ) -> pai_dsw_20220101_models.GetUserCommandResponse:
        """
        @summary 获取自定义用户命令
        
        @param request: GetUserCommandRequest
        @return: GetUserCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_command_with_options(user_command_id, request, headers, runtime)

    async def get_user_command_async(
        self,
        user_command_id: str,
        request: pai_dsw_20220101_models.GetUserCommandRequest,
    ) -> pai_dsw_20220101_models.GetUserCommandResponse:
        """
        @summary 获取自定义用户命令
        
        @param request: GetUserCommandRequest
        @return: GetUserCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_command_with_options_async(user_command_id, request, headers, runtime)

    def get_user_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetUserConfigResponse:
        """
        @summary 获取用户配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/userconfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetUserConfigResponse:
        """
        @summary 获取用户配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/userconfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.GetUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_config(self) -> pai_dsw_20220101_models.GetUserConfigResponse:
        """
        @summary 获取用户配置
        
        @return: GetUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_config_with_options(headers, runtime)

    async def get_user_config_async(self) -> pai_dsw_20220101_models.GetUserConfigResponse:
        """
        @summary 获取用户配置
        
        @return: GetUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_config_with_options_async(headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
        """
        @summary Queries a list of specifications of ECS instances.
        
        @param request: ListEcsSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
        """
        @summary Queries a list of specifications of ECS instances.
        
        @param request: ListEcsSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListEcsSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_specs(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
        """
        @summary Queries a list of specifications of ECS instances.
        
        @param request: ListEcsSpecsRequest
        @return: ListEcsSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
        """
        @summary Queries a list of specifications of ECS instances.
        
        @param request: ListEcsSpecsRequest
        @return: ListEcsSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_instance_snapshot_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.ListInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstanceSnapshotResponse:
        """
        @summary 查询实例快照列表
        
        @param request: ListInstanceSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.ListInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstanceSnapshotResponse:
        """
        @summary 查询实例快照列表
        
        @param request: ListInstanceSnapshotRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceSnapshot',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_snapshot(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.ListInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.ListInstanceSnapshotResponse:
        """
        @summary 查询实例快照列表
        
        @param request: ListInstanceSnapshotRequest
        @return: ListInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def list_instance_snapshot_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.ListInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.ListInstanceSnapshotResponse:
        """
        @summary 查询实例快照列表
        
        @param request: ListInstanceSnapshotRequest
        @return: ListInstanceSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def list_instance_statistics_with_options(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
        """
        @summary 获取实例统计信息
        
        @param request: ListInstanceStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatistics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instancestatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_statistics_with_options_async(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
        """
        @summary 获取实例统计信息
        
        @param request: ListInstanceStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatistics',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instancestatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_statistics(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
        """
        @summary 获取实例统计信息
        
        @param request: ListInstanceStatisticsRequest
        @return: ListInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_statistics_with_options(request, headers, runtime)

    async def list_instance_statistics_async(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
        """
        @summary 获取实例统计信息
        
        @param request: ListInstanceStatisticsRequest
        @return: ListInstanceStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_statistics_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: pai_dsw_20220101_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        """
        @summary Queries a list of Data Science Workshop (DSW) instances.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_dsw_20220101_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.gpu_type):
            query['GpuType'] = request.gpu_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.max_cpu):
            query['MaxCpu'] = request.max_cpu
        if not UtilClient.is_unset(request.max_gpu):
            query['MaxGpu'] = request.max_gpu
        if not UtilClient.is_unset(request.max_gpu_memory):
            query['MaxGpuMemory'] = request.max_gpu_memory
        if not UtilClient.is_unset(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not UtilClient.is_unset(request.min_cpu):
            query['MinCpu'] = request.min_cpu
        if not UtilClient.is_unset(request.min_gpu):
            query['MinGpu'] = request.min_gpu
        if not UtilClient.is_unset(request.min_gpu_memory):
            query['MinGpuMemory'] = request.min_gpu_memory
        if not UtilClient.is_unset(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not UtilClient.is_unset(request.oversold_type):
            query['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: pai_dsw_20220101_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        """
        @summary Queries a list of Data Science Workshop (DSW) instances.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_dsw_20220101_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.gpu_type):
            query['GpuType'] = request.gpu_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.max_cpu):
            query['MaxCpu'] = request.max_cpu
        if not UtilClient.is_unset(request.max_gpu):
            query['MaxGpu'] = request.max_gpu
        if not UtilClient.is_unset(request.max_gpu_memory):
            query['MaxGpuMemory'] = request.max_gpu_memory
        if not UtilClient.is_unset(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not UtilClient.is_unset(request.min_cpu):
            query['MinCpu'] = request.min_cpu
        if not UtilClient.is_unset(request.min_gpu):
            query['MinGpu'] = request.min_gpu
        if not UtilClient.is_unset(request.min_gpu_memory):
            query['MinGpuMemory'] = request.min_gpu_memory
        if not UtilClient.is_unset(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not UtilClient.is_unset(request.oversold_type):
            query['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: pai_dsw_20220101_models.ListInstancesRequest,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        """
        @summary Queries a list of Data Science Workshop (DSW) instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_dsw_20220101_models.ListInstancesRequest,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        """
        @summary Queries a list of Data Science Workshop (DSW) instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_system_logs_with_options(
        self,
        request: pai_dsw_20220101_models.ListSystemLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListSystemLogsResponse:
        """
        @summary 获取系统日志
        
        @param request: ListSystemLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gmt_end_time):
            query['GmtEndTime'] = request.gmt_end_time
        if not UtilClient.is_unset(request.gmt_start_time):
            query['GmtStartTime'] = request.gmt_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_category):
            query['ProblemCategory'] = request.problem_category
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemLogs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/systemlogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListSystemLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_logs_with_options_async(
        self,
        request: pai_dsw_20220101_models.ListSystemLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListSystemLogsResponse:
        """
        @summary 获取系统日志
        
        @param request: ListSystemLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gmt_end_time):
            query['GmtEndTime'] = request.gmt_end_time
        if not UtilClient.is_unset(request.gmt_start_time):
            query['GmtStartTime'] = request.gmt_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_category):
            query['ProblemCategory'] = request.problem_category
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemLogs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/systemlogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListSystemLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_logs(
        self,
        request: pai_dsw_20220101_models.ListSystemLogsRequest,
    ) -> pai_dsw_20220101_models.ListSystemLogsResponse:
        """
        @summary 获取系统日志
        
        @param request: ListSystemLogsRequest
        @return: ListSystemLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_system_logs_with_options(request, headers, runtime)

    async def list_system_logs_async(
        self,
        request: pai_dsw_20220101_models.ListSystemLogsRequest,
    ) -> pai_dsw_20220101_models.ListSystemLogsResponse:
        """
        @summary 获取系统日志
        
        @param request: ListSystemLogsRequest
        @return: ListSystemLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_system_logs_with_options_async(request, headers, runtime)

    def start_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_with_options(instance_id, headers, runtime)

    async def start_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_instance_with_options_async(instance_id, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.StopInstanceResponse:
        """
        @summary 停止实例
        
        @param request: StopInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.StopInstanceResponse:
        """
        @summary 停止实例
        
        @param request: StopInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.StopInstanceRequest,
    ) -> pai_dsw_20220101_models.StopInstanceResponse:
        """
        @summary 停止实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, request, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.StopInstanceRequest,
    ) -> pai_dsw_20220101_models.StopInstanceResponse:
        """
        @summary 停止实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.UpdateInstanceResponse:
        """
        @summary Updates the properties of a DSW instance.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.affinity):
            body['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.disassociate_credential):
            body['DisassociateCredential'] = request.disassociate_credential
        if not UtilClient.is_unset(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not UtilClient.is_unset(request.disassociate_driver):
            body['DisassociateDriver'] = request.disassociate_driver
        if not UtilClient.is_unset(request.disassociate_environment_variables):
            body['DisassociateEnvironmentVariables'] = request.disassociate_environment_variables
        if not UtilClient.is_unset(request.disassociate_forward_infos):
            body['DisassociateForwardInfos'] = request.disassociate_forward_infos
        if not UtilClient.is_unset(request.disassociate_user_command):
            body['DisassociateUserCommand'] = request.disassociate_user_command
        if not UtilClient.is_unset(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not UtilClient.is_unset(request.driver):
            body['Driver'] = request.driver
        if not UtilClient.is_unset(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.UpdateInstanceResponse:
        """
        @summary Updates the properties of a DSW instance.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.affinity):
            body['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.disassociate_credential):
            body['DisassociateCredential'] = request.disassociate_credential
        if not UtilClient.is_unset(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not UtilClient.is_unset(request.disassociate_driver):
            body['DisassociateDriver'] = request.disassociate_driver
        if not UtilClient.is_unset(request.disassociate_environment_variables):
            body['DisassociateEnvironmentVariables'] = request.disassociate_environment_variables
        if not UtilClient.is_unset(request.disassociate_forward_infos):
            body['DisassociateForwardInfos'] = request.disassociate_forward_infos
        if not UtilClient.is_unset(request.disassociate_user_command):
            body['DisassociateUserCommand'] = request.disassociate_user_command
        if not UtilClient.is_unset(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not UtilClient.is_unset(request.driver):
            body['Driver'] = request.driver
        if not UtilClient.is_unset(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceRequest,
    ) -> pai_dsw_20220101_models.UpdateInstanceResponse:
        """
        @summary Updates the properties of a DSW instance.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceRequest,
    ) -> pai_dsw_20220101_models.UpdateInstanceResponse:
        """
        @summary Updates the properties of a DSW instance.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_labels_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.UpdateInstanceLabelsResponse:
        """
        @summary Updates the tags of a Data Science Workshop (DSW) instance. If the tags do not exist, the system adds tags.
        
        @param request: UpdateInstanceLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceLabels',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.UpdateInstanceLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_labels_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.UpdateInstanceLabelsResponse:
        """
        @summary Updates the tags of a Data Science Workshop (DSW) instance. If the tags do not exist, the system adds tags.
        
        @param request: UpdateInstanceLabelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceLabels',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labels',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.UpdateInstanceLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_labels(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceLabelsRequest,
    ) -> pai_dsw_20220101_models.UpdateInstanceLabelsResponse:
        """
        @summary Updates the tags of a Data Science Workshop (DSW) instance. If the tags do not exist, the system adds tags.
        
        @param request: UpdateInstanceLabelsRequest
        @return: UpdateInstanceLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_labels_with_options(instance_id, request, headers, runtime)

    async def update_instance_labels_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceLabelsRequest,
    ) -> pai_dsw_20220101_models.UpdateInstanceLabelsResponse:
        """
        @summary Updates the tags of a Data Science Workshop (DSW) instance. If the tags do not exist, the system adds tags.
        
        @param request: UpdateInstanceLabelsRequest
        @return: UpdateInstanceLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_labels_with_options_async(instance_id, request, headers, runtime)
