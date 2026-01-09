# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pai_dsw20220101 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_diagnosis_with_options(
        self,
        request: main_models.CreateDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gmt_failure_time):
            body['GmtFailureTime'] = request.gmt_failure_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.problem_category):
            body['ProblemCategory'] = request.problem_category
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosis',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/diagnoses',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnosis_with_options_async(
        self,
        request: main_models.CreateDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gmt_failure_time):
            body['GmtFailureTime'] = request.gmt_failure_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.problem_category):
            body['ProblemCategory'] = request.problem_category
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosis',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/diagnoses',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnosis(
        self,
        request: main_models.CreateDiagnosisRequest,
    ) -> main_models.CreateDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_diagnosis_with_options(request, headers, runtime)

    async def create_diagnosis_async(
        self,
        request: main_models.CreateDiagnosisRequest,
    ) -> main_models.CreateDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_diagnosis_with_options_async(request, headers, runtime)

    def create_idle_instance_culler_with_options(
        self,
        instance_id: str,
        request: main_models.CreateIdleInstanceCullerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdleInstanceCullerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cpu_percent_threshold):
            body['CpuPercentThreshold'] = request.cpu_percent_threshold
        if not DaraCore.is_null(request.gpu_percent_threshold):
            body['GpuPercentThreshold'] = request.gpu_percent_threshold
        if not DaraCore.is_null(request.max_idle_time_in_minutes):
            body['MaxIdleTimeInMinutes'] = request.max_idle_time_in_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateIdleInstanceCullerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdleInstanceCullerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cpu_percent_threshold):
            body['CpuPercentThreshold'] = request.cpu_percent_threshold
        if not DaraCore.is_null(request.gpu_percent_threshold):
            body['GpuPercentThreshold'] = request.gpu_percent_threshold
        if not DaraCore.is_null(request.max_idle_time_in_minutes):
            body['MaxIdleTimeInMinutes'] = request.max_idle_time_in_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idle_instance_culler(
        self,
        instance_id: str,
        request: main_models.CreateIdleInstanceCullerRequest,
    ) -> main_models.CreateIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_idle_instance_culler_with_options(instance_id, request, headers, runtime)

    async def create_idle_instance_culler_async(
        self,
        instance_id: str,
        request: main_models.CreateIdleInstanceCullerRequest,
    ) -> main_models.CreateIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_idle_instance_culler_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.affinity):
            body['Affinity'] = request.affinity
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.datasets):
            body['Datasets'] = request.datasets
        if not DaraCore.is_null(request.driver):
            body['Driver'] = request.driver
        if not DaraCore.is_null(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not DaraCore.is_null(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not DaraCore.is_null(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.migration_options):
            body['MigrationOptions'] = request.migration_options
        if not DaraCore.is_null(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.spot_spec):
            body['SpotSpec'] = request.spot_spec
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.affinity):
            body['Affinity'] = request.affinity
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.datasets):
            body['Datasets'] = request.datasets
        if not DaraCore.is_null(request.driver):
            body['Driver'] = request.driver
        if not DaraCore.is_null(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not DaraCore.is_null(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not DaraCore.is_null(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.migration_options):
            body['MigrationOptions'] = request.migration_options
        if not DaraCore.is_null(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.spot_spec):
            body['SpotSpec'] = request.spot_spec
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        request: main_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceShutdownTimerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.due_time):
            body['DueTime'] = request.due_time
        if not DaraCore.is_null(request.remaining_time_in_ms):
            body['RemainingTimeInMs'] = request.remaining_time_in_ms
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceShutdownTimerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.due_time):
            body['DueTime'] = request.due_time
        if not DaraCore.is_null(request.remaining_time_in_ms):
            body['RemainingTimeInMs'] = request.remaining_time_in_ms
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_shutdown_timer(
        self,
        instance_id: str,
        request: main_models.CreateInstanceShutdownTimerRequest,
    ) -> main_models.CreateInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_with_options(instance_id, request, headers, runtime)

    async def create_instance_shutdown_timer_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceShutdownTimerRequest,
    ) -> main_models.CreateInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_shutdown_timer_with_options_async(instance_id, request, headers, runtime)

    def create_instance_snapshot_with_options(
        self,
        instance_id: str,
        request: main_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceSnapshotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_paths):
            body['ExcludePaths'] = request.exclude_paths
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not DaraCore.is_null(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceSnapshotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exclude_paths):
            body['ExcludePaths'] = request.exclude_paths
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not DaraCore.is_null(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_snapshot(
        self,
        instance_id: str,
        request: main_models.CreateInstanceSnapshotRequest,
    ) -> main_models.CreateInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_instance_snapshot_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceSnapshotRequest,
    ) -> main_models.CreateInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def create_sanity_check_task_with_options(
        self,
        check_type: str,
        request: main_models.CreateSanityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSanityCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSanityCheckTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/sanitychecks/{DaraURL.percent_encode(check_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSanityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sanity_check_task_with_options_async(
        self,
        check_type: str,
        request: main_models.CreateSanityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSanityCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSanityCheckTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/sanitychecks/{DaraURL.percent_encode(check_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSanityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sanity_check_task(
        self,
        check_type: str,
        request: main_models.CreateSanityCheckTaskRequest,
    ) -> main_models.CreateSanityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sanity_check_task_with_options(check_type, request, headers, runtime)

    async def create_sanity_check_task_async(
        self,
        check_type: str,
        request: main_models.CreateSanityCheckTaskRequest,
    ) -> main_models.CreateSanityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sanity_check_task_with_options_async(check_type, request, headers, runtime)

    def delete_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdleInstanceCullerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdleInstanceCullerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_idle_instance_culler(
        self,
        instance_id: str,
    ) -> main_models.DeleteIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def delete_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> main_models.DeleteIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_labels_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceLabels',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_labels_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_keys):
            query['LabelKeys'] = request.label_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceLabels',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_labels(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceLabelsRequest,
    ) -> main_models.DeleteInstanceLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_labels_with_options(instance_id, request, headers, runtime)

    async def delete_instance_labels_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceLabelsRequest,
    ) -> main_models.DeleteInstanceLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_labels_with_options_async(instance_id, request, headers, runtime)

    def delete_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceShutdownTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceShutdownTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def delete_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def delete_instance_snapshot_with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots/{DaraURL.percent_encode(snapshot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots/{DaraURL.percent_encode(snapshot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_snapshot(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> main_models.DeleteInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def delete_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> main_models.DeleteInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_snapshot_with_options_async(instance_id, snapshot_id, headers, runtime)

    def delete_instances_with_options(
        self,
        request: main_models.DeleteInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/batch/instances/delete',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instances_with_options_async(
        self,
        request: main_models.DeleteInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/batch/instances/delete',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instances(
        self,
        request: main_models.DeleteInstancesRequest,
    ) -> main_models.DeleteInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instances_with_options(request, headers, runtime)

    async def delete_instances_async(
        self,
        request: main_models.DeleteInstancesRequest,
    ) -> main_models.DeleteInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instances_with_options_async(request, headers, runtime)

    def get_idle_instance_culler_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdleInstanceCullerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdleInstanceCullerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_idle_instance_culler_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdleInstanceCullerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdleInstanceCuller',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/idleinstanceculler',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdleInstanceCullerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_idle_instance_culler(
        self,
        instance_id: str,
    ) -> main_models.GetIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_idle_instance_culler_with_options(instance_id, headers, runtime)

    async def get_idle_instance_culler_async(
        self,
        instance_id: str,
    ) -> main_models.GetIdleInstanceCullerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_idle_instance_culler_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, request, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, request, headers, runtime)

    def get_instance_events_with_options(
        self,
        instance_id: str,
        request: main_models.GetInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceEvents',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_events_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceEvents',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_events(
        self,
        instance_id: str,
        request: main_models.GetInstanceEventsRequest,
    ) -> main_models.GetInstanceEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_events_with_options(instance_id, request, headers, runtime)

    async def get_instance_events_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceEventsRequest,
    ) -> main_models.GetInstanceEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_events_with_options_async(instance_id, request, headers, runtime)

    def get_instance_metrics_with_options(
        self,
        instance_id: str,
        request: main_models.GetInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceMetrics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instance/{DaraURL.percent_encode(instance_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_metrics_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceMetrics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instance/{DaraURL.percent_encode(instance_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_metrics(
        self,
        instance_id: str,
        request: main_models.GetInstanceMetricsRequest,
    ) -> main_models.GetInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_metrics_with_options(instance_id, request, headers, runtime)

    async def get_instance_metrics_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceMetricsRequest,
    ) -> main_models.GetInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_metrics_with_options_async(instance_id, request, headers, runtime)

    def get_instance_shutdown_timer_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceShutdownTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceShutdownTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceShutdownTimer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/shutdowntimer',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_shutdown_timer(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    async def get_instance_shutdown_timer_async(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceShutdownTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_shutdown_timer_with_options_async(instance_id, headers, runtime)

    def get_instance_snapshot_with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots/{DaraURL.percent_encode(snapshot_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots/{DaraURL.percent_encode(snapshot_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_snapshot(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> main_models.GetInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_with_options(instance_id, snapshot_id, headers, runtime)

    async def get_instance_snapshot_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> main_models.GetInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_snapshot_with_options_async(instance_id, snapshot_id, headers, runtime)

    def get_lifecycle_with_options(
        self,
        instance_id: str,
        request: main_models.GetLifecycleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLifecycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.session_number):
            query['SessionNumber'] = request.session_number
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLifecycle',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/lifecycle',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLifecycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lifecycle_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetLifecycleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLifecycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.session_number):
            query['SessionNumber'] = request.session_number
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLifecycle',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/lifecycle',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLifecycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lifecycle(
        self,
        instance_id: str,
        request: main_models.GetLifecycleRequest,
    ) -> main_models.GetLifecycleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_lifecycle_with_options(instance_id, request, headers, runtime)

    async def get_lifecycle_async(
        self,
        instance_id: str,
        request: main_models.GetLifecycleRequest,
    ) -> main_models.GetLifecycleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_lifecycle_with_options_async(instance_id, request, headers, runtime)

    def get_metrics_with_options(
        self,
        instance_id: str,
        request: main_models.GetMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetrics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instance/{DaraURL.percent_encode(instance_id)}/cms/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metrics_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetrics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instance/{DaraURL.percent_encode(instance_id)}/cms/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metrics(
        self,
        instance_id: str,
        request: main_models.GetMetricsRequest,
    ) -> main_models.GetMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_metrics_with_options(instance_id, request, headers, runtime)

    async def get_metrics_async(
        self,
        instance_id: str,
        request: main_models.GetMetricsRequest,
    ) -> main_models.GetMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_metrics_with_options_async(instance_id, request, headers, runtime)

    def get_resource_group_statistics_with_options(
        self,
        request: main_models.GetResourceGroupStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupStatistics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resourcegroupstatistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_statistics_with_options_async(
        self,
        request: main_models.GetResourceGroupStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupStatistics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/resourcegroupstatistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_statistics(
        self,
        request: main_models.GetResourceGroupStatisticsRequest,
    ) -> main_models.GetResourceGroupStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_statistics_with_options(request, headers, runtime)

    async def get_resource_group_statistics_async(
        self,
        request: main_models.GetResourceGroupStatisticsRequest,
    ) -> main_models.GetResourceGroupStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_statistics_with_options_async(request, headers, runtime)

    def get_sanity_check_task_with_options(
        self,
        check_type: str,
        task_id: str,
        request: main_models.GetSanityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSanityCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSanityCheckTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/sanitychecks/{DaraURL.percent_encode(check_type)}/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSanityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sanity_check_task_with_options_async(
        self,
        check_type: str,
        task_id: str,
        request: main_models.GetSanityCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSanityCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSanityCheckTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/sanitychecks/{DaraURL.percent_encode(check_type)}/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSanityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sanity_check_task(
        self,
        check_type: str,
        task_id: str,
        request: main_models.GetSanityCheckTaskRequest,
    ) -> main_models.GetSanityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sanity_check_task_with_options(check_type, task_id, request, headers, runtime)

    async def get_sanity_check_task_async(
        self,
        check_type: str,
        task_id: str,
        request: main_models.GetSanityCheckTaskRequest,
    ) -> main_models.GetSanityCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sanity_check_task_with_options_async(check_type, task_id, request, headers, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audience):
            query['Audience'] = request.audience
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audience):
            query['Audience'] = request.audience
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_user_command_with_options(
        self,
        user_command_id: str,
        request: main_models.GetUserCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCommand',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/usercommands/{DaraURL.percent_encode(user_command_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_command_with_options_async(
        self,
        user_command_id: str,
        request: main_models.GetUserCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCommand',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/usercommands/{DaraURL.percent_encode(user_command_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_command(
        self,
        user_command_id: str,
        request: main_models.GetUserCommandRequest,
    ) -> main_models.GetUserCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_command_with_options(user_command_id, request, headers, runtime)

    async def get_user_command_async(
        self,
        user_command_id: str,
        request: main_models.GetUserCommandRequest,
    ) -> main_models.GetUserCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_command_with_options_async(user_command_id, request, headers, runtime)

    def get_user_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUserConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/userconfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUserConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/userconfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_config(self) -> main_models.GetUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_config_with_options(headers, runtime)

    async def get_user_config_async(self) -> main_models.GetUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_config_with_options_async(headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: main_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsSpecs',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/ecsspecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: main_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsSpecs',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/ecsspecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_specs(
        self,
        request: main_models.ListEcsSpecsRequest,
    ) -> main_models.ListEcsSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: main_models.ListEcsSpecsRequest,
    ) -> main_models.ListEcsSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_instance_snapshot_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceSnapshot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_snapshot(
        self,
        instance_id: str,
        request: main_models.ListInstanceSnapshotRequest,
    ) -> main_models.ListInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_snapshot_with_options(instance_id, request, headers, runtime)

    async def list_instance_snapshot_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceSnapshotRequest,
    ) -> main_models.ListInstanceSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_snapshot_with_options_async(instance_id, request, headers, runtime)

    def list_instance_statistics_with_options(
        self,
        request: main_models.ListInstanceStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatistics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instancestatistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_statistics_with_options_async(
        self,
        request: main_models.ListInstanceStatisticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceStatistics',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instancestatistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_statistics(
        self,
        request: main_models.ListInstanceStatisticsRequest,
    ) -> main_models.ListInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_statistics_with_options(request, headers, runtime)

    async def list_instance_statistics_async(
        self,
        request: main_models.ListInstanceStatisticsRequest,
    ) -> main_models.ListInstanceStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_statistics_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.gpu_type):
            query['GpuType'] = request.gpu_type
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.max_cpu):
            query['MaxCpu'] = request.max_cpu
        if not DaraCore.is_null(request.max_gpu):
            query['MaxGpu'] = request.max_gpu
        if not DaraCore.is_null(request.max_gpu_memory):
            query['MaxGpuMemory'] = request.max_gpu_memory
        if not DaraCore.is_null(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not DaraCore.is_null(request.min_cpu):
            query['MinCpu'] = request.min_cpu
        if not DaraCore.is_null(request.min_gpu):
            query['MinGpu'] = request.min_gpu
        if not DaraCore.is_null(request.min_gpu_memory):
            query['MinGpuMemory'] = request.min_gpu_memory
        if not DaraCore.is_null(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not DaraCore.is_null(request.oversold_type):
            query['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.gpu_type):
            query['GpuType'] = request.gpu_type
        if not DaraCore.is_null(request.image_name):
            query['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.max_cpu):
            query['MaxCpu'] = request.max_cpu
        if not DaraCore.is_null(request.max_gpu):
            query['MaxGpu'] = request.max_gpu
        if not DaraCore.is_null(request.max_gpu_memory):
            query['MaxGpuMemory'] = request.max_gpu_memory
        if not DaraCore.is_null(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not DaraCore.is_null(request.min_cpu):
            query['MinCpu'] = request.min_cpu
        if not DaraCore.is_null(request.min_gpu):
            query['MinGpu'] = request.min_gpu
        if not DaraCore.is_null(request.min_gpu_memory):
            query['MinGpuMemory'] = request.min_gpu_memory
        if not DaraCore.is_null(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not DaraCore.is_null(request.oversold_type):
            query['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_system_logs_with_options(
        self,
        request: main_models.ListSystemLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gmt_end_time):
            query['GmtEndTime'] = request.gmt_end_time
        if not DaraCore.is_null(request.gmt_start_time):
            query['GmtStartTime'] = request.gmt_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lifecycle_id):
            query['LifecycleId'] = request.lifecycle_id
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.log_repository):
            query['LogRepository'] = request.log_repository
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.problem_category):
            query['ProblemCategory'] = request.problem_category
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemLogs',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/systemlogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_logs_with_options_async(
        self,
        request: main_models.ListSystemLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gmt_end_time):
            query['GmtEndTime'] = request.gmt_end_time
        if not DaraCore.is_null(request.gmt_start_time):
            query['GmtStartTime'] = request.gmt_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lifecycle_id):
            query['LifecycleId'] = request.lifecycle_id
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.log_repository):
            query['LogRepository'] = request.log_repository
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.problem_category):
            query['ProblemCategory'] = request.problem_category
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemLogs',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/systemlogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_logs(
        self,
        request: main_models.ListSystemLogsRequest,
    ) -> main_models.ListSystemLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_system_logs_with_options(request, headers, runtime)

    async def list_system_logs_async(
        self,
        request: main_models.ListSystemLogsRequest,
    ) -> main_models.ListSystemLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_system_logs_with_options_async(request, headers, runtime)

    def start_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        instance_id: str,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_instance_with_options(instance_id, headers, runtime)

    async def start_instance_async(
        self,
        instance_id: str,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_instance_with_options_async(instance_id, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        request: main_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, request, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, request, headers, runtime)

    def stop_instances_with_options(
        self,
        request: main_models.StopInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/batch/instances/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: main_models.StopInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopInstances',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/batch/instances/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instances(
        self,
        request: main_models.StopInstancesRequest,
    ) -> main_models.StopInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_instances_with_options(request, headers, runtime)

    async def stop_instances_async(
        self,
        request: main_models.StopInstancesRequest,
    ) -> main_models.StopInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_instances_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.affinity):
            body['Affinity'] = request.affinity
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.datasets):
            body['Datasets'] = request.datasets
        if not DaraCore.is_null(request.disassociate_assign_node):
            body['DisassociateAssignNode'] = request.disassociate_assign_node
        if not DaraCore.is_null(request.disassociate_credential):
            body['DisassociateCredential'] = request.disassociate_credential
        if not DaraCore.is_null(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not DaraCore.is_null(request.disassociate_driver):
            body['DisassociateDriver'] = request.disassociate_driver
        if not DaraCore.is_null(request.disassociate_environment_variables):
            body['DisassociateEnvironmentVariables'] = request.disassociate_environment_variables
        if not DaraCore.is_null(request.disassociate_forward_infos):
            body['DisassociateForwardInfos'] = request.disassociate_forward_infos
        if not DaraCore.is_null(request.disassociate_migration_options):
            body['DisassociateMigrationOptions'] = request.disassociate_migration_options
        if not DaraCore.is_null(request.disassociate_spot):
            body['DisassociateSpot'] = request.disassociate_spot
        if not DaraCore.is_null(request.disassociate_user_command):
            body['DisassociateUserCommand'] = request.disassociate_user_command
        if not DaraCore.is_null(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not DaraCore.is_null(request.driver):
            body['Driver'] = request.driver
        if not DaraCore.is_null(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not DaraCore.is_null(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not DaraCore.is_null(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.migration_options):
            body['MigrationOptions'] = request.migration_options
        if not DaraCore.is_null(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not DaraCore.is_null(request.spot_spec):
            body['SpotSpec'] = request.spot_spec
        if not DaraCore.is_null(request.start_instance):
            body['StartInstance'] = request.start_instance
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.affinity):
            body['Affinity'] = request.affinity
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.cloud_disks):
            body['CloudDisks'] = request.cloud_disks
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.datasets):
            body['Datasets'] = request.datasets
        if not DaraCore.is_null(request.disassociate_assign_node):
            body['DisassociateAssignNode'] = request.disassociate_assign_node
        if not DaraCore.is_null(request.disassociate_credential):
            body['DisassociateCredential'] = request.disassociate_credential
        if not DaraCore.is_null(request.disassociate_datasets):
            body['DisassociateDatasets'] = request.disassociate_datasets
        if not DaraCore.is_null(request.disassociate_driver):
            body['DisassociateDriver'] = request.disassociate_driver
        if not DaraCore.is_null(request.disassociate_environment_variables):
            body['DisassociateEnvironmentVariables'] = request.disassociate_environment_variables
        if not DaraCore.is_null(request.disassociate_forward_infos):
            body['DisassociateForwardInfos'] = request.disassociate_forward_infos
        if not DaraCore.is_null(request.disassociate_migration_options):
            body['DisassociateMigrationOptions'] = request.disassociate_migration_options
        if not DaraCore.is_null(request.disassociate_spot):
            body['DisassociateSpot'] = request.disassociate_spot
        if not DaraCore.is_null(request.disassociate_user_command):
            body['DisassociateUserCommand'] = request.disassociate_user_command
        if not DaraCore.is_null(request.disassociate_vpc):
            body['DisassociateVpc'] = request.disassociate_vpc
        if not DaraCore.is_null(request.driver):
            body['Driver'] = request.driver
        if not DaraCore.is_null(request.dynamic_mount):
            body['DynamicMount'] = request.dynamic_mount
        if not DaraCore.is_null(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not DaraCore.is_null(request.image_auth):
            body['ImageAuth'] = request.image_auth
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.migration_options):
            body['MigrationOptions'] = request.migration_options
        if not DaraCore.is_null(request.oversold_type):
            body['OversoldType'] = request.oversold_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.requested_resource):
            body['RequestedResource'] = request.requested_resource
        if not DaraCore.is_null(request.spot_spec):
            body['SpotSpec'] = request.spot_spec
        if not DaraCore.is_null(request.start_instance):
            body['StartInstance'] = request.start_instance
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_source):
            body['WorkspaceSource'] = request.workspace_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_labels_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceLabels',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_labels_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceLabels',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = f'/api/v2/instances/{DaraURL.percent_encode(instance_id)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_labels(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceLabelsRequest,
    ) -> main_models.UpdateInstanceLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_labels_with_options(instance_id, request, headers, runtime)

    async def update_instance_labels_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceLabelsRequest,
    ) -> main_models.UpdateInstanceLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_labels_with_options_async(instance_id, request, headers, runtime)
