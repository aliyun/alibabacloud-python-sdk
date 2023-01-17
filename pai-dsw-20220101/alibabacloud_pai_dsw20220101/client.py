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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_idle_instance_culler_with_options(instance_id, request, headers, runtime)

    async def create_idle_instance_culler_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateIdleInstanceCullerRequest,
    ) -> pai_dsw_20220101_models.CreateIdleInstanceCullerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_idle_instance_culler_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: pai_dsw_20220101_models.CreateInstanceRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_with_options(instance_id, request, headers, runtime)

    async def create_instance_shutdown_timer_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceShutdownTimerRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceShutdownTimerResponse:
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_instance_snapshot_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.CreateInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.CreateInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def delete_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def delete_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteIdleInstanceCullerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def delete_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceShutdownTimerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def delete_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.DeleteInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_snapshot_with_options_async(instance_id, snapshot_id, headers, runtime)

    def get_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def get_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetIdleInstanceCullerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
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
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_metrics_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_metrics_with_options(instance_id, request, headers, runtime)

    async def get_instance_metrics_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetInstanceMetricsRequest,
    ) -> pai_dsw_20220101_models.GetInstanceMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_metrics_with_options_async(instance_id, request, headers, runtime)

    def get_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def get_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceShutdownTimerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def get_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20220101_models.GetInstanceSnapshotResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_lifecycle_with_options(instance_id, request, headers, runtime)

    async def get_lifecycle_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.GetLifecycleRequest,
    ) -> pai_dsw_20220101_models.GetLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_lifecycle_with_options_async(instance_id, request, headers, runtime)

    def get_token_with_options(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: pai_dsw_20220101_models.GetTokenRequest,
    ) -> pai_dsw_20220101_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_user_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.GetUserConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_config_with_options(headers, runtime)

    async def get_user_config_async(self) -> pai_dsw_20220101_models.GetUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_config_with_options_async(headers, runtime)

    def list_demo_categories_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListDemoCategoriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDemoCategories',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/democategories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListDemoCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_demo_categories_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListDemoCategoriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDemoCategories',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/democategories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListDemoCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_demo_categories(self) -> pai_dsw_20220101_models.ListDemoCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_demo_categories_with_options(headers, runtime)

    async def list_demo_categories_async(self) -> pai_dsw_20220101_models.ListDemoCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_demo_categories_with_options_async(headers, runtime)

    def list_demos_with_options(
        self,
        request: pai_dsw_20220101_models.ListDemosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListDemosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.demo_name):
            query['DemoName'] = request.demo_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDemos',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/demos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListDemosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_demos_with_options_async(
        self,
        request: pai_dsw_20220101_models.ListDemosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListDemosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.demo_name):
            query['DemoName'] = request.demo_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDemos',
            version='2022-01-01',
            protocol='HTTPS',
            pathname=f'/api/v2/demos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20220101_models.ListDemosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_demos(
        self,
        request: pai_dsw_20220101_models.ListDemosRequest,
    ) -> pai_dsw_20220101_models.ListDemosResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_demos_with_options(request, headers, runtime)

    async def list_demos_async(
        self,
        request: pai_dsw_20220101_models.ListDemosRequest,
    ) -> pai_dsw_20220101_models.ListDemosResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_demos_with_options_async(request, headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: pai_dsw_20220101_models.ListEcsSpecsRequest,
    ) -> pai_dsw_20220101_models.ListEcsSpecsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def list_instance_snapshot_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.ListInstanceSnapshotRequest,
    ) -> pai_dsw_20220101_models.ListInstanceSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def list_instance_statistics_with_options(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_statistics_with_options(request, headers, runtime)

    async def list_instance_statistics_async(
        self,
        request: pai_dsw_20220101_models.ListInstanceStatisticsRequest,
    ) -> pai_dsw_20220101_models.ListInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_statistics_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_dsw_20220101_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        request: pai_dsw_20220101_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_dsw_20220101_models.ListInstancesRequest,
    ) -> pai_dsw_20220101_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def start_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_with_options(instance_id, headers, runtime)

    async def start_instance_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20220101_models.StartInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, request, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.StopInstanceRequest,
    ) -> pai_dsw_20220101_models.StopInstanceResponse:
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not UtilClient.is_unset(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not UtilClient.is_unset(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20220101_models.UpdateInstanceRequest,
    ) -> pai_dsw_20220101_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)
