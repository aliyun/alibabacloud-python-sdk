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
        if not UtilClient.is_unset(request.dataset_list):
            body['DatasetList'] = request.dataset_list
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environments):
            body['Environments'] = request.environments
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_public):
            body['IsPublic'] = request.is_public
        if not UtilClient.is_unset(request.nas_file_system_id):
            body['NasFileSystemId'] = request.nas_file_system_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
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
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: pai_dsw_20210226_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_list):
            body['DatasetList'] = request.dataset_list
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environments):
            body['Environments'] = request.environments
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_public):
            body['IsPublic'] = request.is_public
        if not UtilClient.is_unset(request.nas_file_system_id):
            body['NasFileSystemId'] = request.nas_file_system_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
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
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.schedule_time):
            body['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.ttl_in_millis):
            body['TtlInMillis'] = request.ttl_in_millis
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.schedule_time):
            body['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.ttl_in_millis):
            body['TtlInMillis'] = request.ttl_in_millis
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_shutdown_timer_v2(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_v2with_options(instance_id, request, headers, runtime)

    async def create_instance_shutdown_timer_v2_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_shutdown_timer_v2with_options_async(instance_id, request, headers, runtime)

    def create_instance_shutdown_timer_v2with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='CreateInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_shutdown_timer_v2with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='CreateInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response(),
            await self.call_api_async(params, req, runtime)
        )

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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_description):
            body['InstanceSnapshotDescription'] = request.instance_snapshot_description
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        if not UtilClient.is_unset(request.instance_snapshot_repo_url):
            body['InstanceSnapshotRepoUrl'] = request.instance_snapshot_repo_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_description):
            body['InstanceSnapshotDescription'] = request.instance_snapshot_description
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        if not UtilClient.is_unset(request.instance_snapshot_repo_url):
            body['InstanceSnapshotRepoUrl'] = request.instance_snapshot_repo_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_snapshot_v2(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_v2with_options(instance_id, request, headers, runtime)

    async def create_instance_snapshot_v2_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_snapshot_v2with_options_async(instance_id, request, headers, runtime)

    def create_instance_snapshot_v2with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not UtilClient.is_unset(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_snapshot_v2with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.CreateInstanceSnapshotV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceSnapshotV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not UtilClient.is_unset(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_v2(
        self,
        request: pai_dsw_20210226_models.CreateInstanceV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_v2with_options(request, headers, runtime)

    async def create_instance_v2_async(
        self,
        request: pai_dsw_20210226_models.CreateInstanceV2Request,
    ) -> pai_dsw_20210226_models.CreateInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_v2with_options_async(request, headers, runtime)

    def create_instance_v2with_options(
        self,
        request: pai_dsw_20210226_models.CreateInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceV2Response:
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
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_v2with_options_async(
        self,
        request: pai_dsw_20210226_models.CreateInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateInstanceV2Response:
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
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_shutdown_timer_v2(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_v2with_options(instance_id, headers, runtime)

    async def delete_instance_shutdown_timer_v2_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_shutdown_timer_v2with_options_async(instance_id, headers, runtime)

    def delete_instance_shutdown_timer_v2with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_shutdown_timer_v2with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_snapshot_v2(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_v2with_options(instance_id, snapshot_id, headers, runtime)

    async def delete_instance_snapshot_v2_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_snapshot_v2with_options_async(instance_id, snapshot_id, headers, runtime)

    def delete_instance_snapshot_v2with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots/{snapshot_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_snapshot_v2with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots/{snapshot_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_v2(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_v2with_options(instance_id, headers, runtime)

    async def delete_instance_v2_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.DeleteInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_v2with_options_async(instance_id, headers, runtime)

    def delete_instance_v2with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_v2with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.DeleteInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='Foobar',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/foobar',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.FoobarResponse(),
            self.call_api(params, req, runtime)
        )

    async def foobar_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.FoobarResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Foobar',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/foobar',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.FoobarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def foobar_1(self) -> pai_dsw_20210226_models.Foobar1Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.foobar_1with_options(headers, runtime)

    async def foobar_1_async(self) -> pai_dsw_20210226_models.Foobar1Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.foobar_1with_options_async(headers, runtime)

    def foobar_1with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.Foobar1Response:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Foobar1',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/foobar1',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.Foobar1Response(),
            self.call_api(params, req, runtime)
        )

    async def foobar_1with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.Foobar1Response:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Foobar1',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/foobar1',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.Foobar1Response(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/authorization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetAuthorizationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/authorization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dashboard_statistics(
        self,
        request: pai_dsw_20210226_models.GetDashboardStatisticsRequest,
    ) -> pai_dsw_20210226_models.GetDashboardStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_statistics_with_options(request, headers, runtime)

    async def get_dashboard_statistics_async(
        self,
        request: pai_dsw_20210226_models.GetDashboardStatisticsRequest,
    ) -> pai_dsw_20210226_models.GetDashboardStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dashboard_statistics_with_options_async(request, headers, runtime)

    def get_dashboard_statistics_with_options(
        self,
        request: pai_dsw_20210226_models.GetDashboardStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetDashboardStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDashboardStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/dashboard',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetDashboardStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dashboard_statistics_with_options_async(
        self,
        request: pai_dsw_20210226_models.GetDashboardStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetDashboardStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDashboardStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/dashboard',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetDashboardStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_shutdown_timer_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/shutdownTimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_shutdown_timer_v2(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_v2with_options(instance_id, headers, runtime)

    async def get_instance_shutdown_timer_v2_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_shutdown_timer_v2with_options_async(instance_id, headers, runtime)

    def get_instance_shutdown_timer_v2with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_shutdown_timer_v2with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/shutdowntimer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_snapshot_with_options_async(
        self,
        instance_id: str,
        instance_snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_snapshot_v2(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_v2with_options(instance_id, snapshot_id, headers, runtime)

    async def get_instance_snapshot_v2_async(
        self,
        instance_id: str,
        snapshot_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_snapshot_v2with_options_async(instance_id, snapshot_id, headers, runtime)

    def get_instance_snapshot_v2with_options(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots/{snapshot_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_snapshot_v2with_options_async(
        self,
        instance_id: str,
        snapshot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceSnapshotV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots/{snapshot_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_v2(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_v2with_options(instance_id, headers, runtime)

    async def get_instance_v2_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_v2with_options_async(instance_id, headers, runtime)

    def get_instance_v2with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_v2with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instances_statistics(
        self,
        request: pai_dsw_20210226_models.GetInstancesStatisticsRequest,
    ) -> pai_dsw_20210226_models.GetInstancesStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instances_statistics_with_options(request, headers, runtime)

    async def get_instances_statistics_async(
        self,
        request: pai_dsw_20210226_models.GetInstancesStatisticsRequest,
    ) -> pai_dsw_20210226_models.GetInstancesStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instances_statistics_with_options_async(request, headers, runtime)

    def get_instances_statistics_with_options(
        self,
        request: pai_dsw_20210226_models.GetInstancesStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstancesStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstancesStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instances_statistics_with_options_async(
        self,
        request: pai_dsw_20210226_models.GetInstancesStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstancesStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstancesStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_config_v2(self) -> pai_dsw_20210226_models.GetUserConfigV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_config_v2with_options(headers, runtime)

    async def get_user_config_v2_async(self) -> pai_dsw_20210226_models.GetUserConfigV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_config_v2with_options_async(headers, runtime)

    def get_user_config_v2with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserConfigV2Response:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserConfigV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/userconfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserConfigV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_user_config_v2with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserConfigV2Response:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserConfigV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/userconfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserConfigV2Response(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/ecsSpecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/ecsSpecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_specs_v2(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsV2Request,
    ) -> pai_dsw_20210226_models.ListEcsSpecsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_v2with_options(request, headers, runtime)

    async def list_ecs_specs_v2_async(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsV2Request,
    ) -> pai_dsw_20210226_models.ListEcsSpecsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_v2with_options_async(request, headers, runtime)

    def list_ecs_specs_v2with_options(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListEcsSpecsV2Response:
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
            action='ListEcsSpecsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_specs_v2with_options_async(
        self,
        request: pai_dsw_20210226_models.ListEcsSpecsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListEcsSpecsV2Response:
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
            action='ListEcsSpecsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsV2Response(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.image_name_contains):
            query['ImageNameContains'] = request.image_name_contains
        if not UtilClient.is_unset(request.image_type_equals):
            query['ImageTypeEquals'] = request.image_type_equals
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.image_name_contains):
            query['ImageNameContains'] = request.image_name_contains
        if not UtilClient.is_unset(request.image_type_equals):
            query['ImageTypeEquals'] = request.image_type_equals
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_snapshot_v2(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.ListInstanceSnapshotV2Request,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshot_v2with_options(instance_id, request, headers, runtime)

    async def list_instance_snapshot_v2_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.ListInstanceSnapshotV2Request,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_snapshot_v2with_options_async(instance_id, request, headers, runtime)

    def list_instance_snapshot_v2with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.ListInstanceSnapshotV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='ListInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_snapshot_v2with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.ListInstanceSnapshotV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='ListInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceSnapshots',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_snapshots_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceSnapshotsResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceSnapshots',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_statistics_v2(
        self,
        request: pai_dsw_20210226_models.ListInstanceStatisticsV2Request,
    ) -> pai_dsw_20210226_models.ListInstanceStatisticsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_statistics_v2with_options(request, headers, runtime)

    async def list_instance_statistics_v2_async(
        self,
        request: pai_dsw_20210226_models.ListInstanceStatisticsV2Request,
    ) -> pai_dsw_20210226_models.ListInstanceStatisticsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_statistics_v2with_options_async(request, headers, runtime)

    def list_instance_statistics_v2with_options(
        self,
        request: pai_dsw_20210226_models.ListInstanceStatisticsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceStatisticsV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatisticsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instancestatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceStatisticsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_statistics_v2with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstanceStatisticsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceStatisticsV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatisticsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instancestatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceStatisticsV2Response(),
            await self.call_api_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.in_workspace):
            query['InWorkspace'] = request.in_workspace
        if not UtilClient.is_unset(request.instance_name_contains):
            query['InstanceNameContains'] = request.instance_name_contains
        if not UtilClient.is_unset(request.instance_status_equals):
            query['InstanceStatusEquals'] = request.instance_status_equals
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.workspace_id_equals):
            query['WorkspaceIdEquals'] = request.workspace_id_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.in_workspace):
            query['InWorkspace'] = request.in_workspace
        if not UtilClient.is_unset(request.instance_name_contains):
            query['InstanceNameContains'] = request.instance_name_contains
        if not UtilClient.is_unset(request.instance_status_equals):
            query['InstanceStatusEquals'] = request.instance_status_equals
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.workspace_id_equals):
            query['WorkspaceIdEquals'] = request.workspace_id_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_status(
        self,
        request: pai_dsw_20210226_models.ListInstancesStatusRequest,
    ) -> pai_dsw_20210226_models.ListInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_status_with_options(request, headers, runtime)

    async def list_instances_status_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesStatusRequest,
    ) -> pai_dsw_20210226_models.ListInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_status_with_options_async(request, headers, runtime)

    def list_instances_status_with_options(
        self,
        request: pai_dsw_20210226_models.ListInstancesStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesStatus',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statuses/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_status_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesStatus',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/statuses/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_v2(
        self,
        request: pai_dsw_20210226_models.ListInstancesV2Request,
    ) -> pai_dsw_20210226_models.ListInstancesV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_v2with_options(request, headers, runtime)

    async def list_instances_v2_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesV2Request,
    ) -> pai_dsw_20210226_models.ListInstancesV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_v2with_options_async(request, headers, runtime)

    def list_instances_v2with_options(
        self,
        request: pai_dsw_20210226_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='ListInstancesV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_v2with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstancesV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='ListInstancesV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StartInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance_v2(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StartInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_v2with_options(instance_id, headers, runtime)

    async def start_instance_v2_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.StartInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_instance_v2with_options_async(instance_id, headers, runtime)

    def start_instance_v2with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StartInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_v2with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StartInstanceV2Response:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceRequest,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, request, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceRequest,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, request, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance_v2(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceV2Request,
    ) -> pai_dsw_20210226_models.StopInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_v2with_options(instance_id, request, headers, runtime)

    async def stop_instance_v2_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceV2Request,
    ) -> pai_dsw_20210226_models.StopInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_v2with_options_async(instance_id, request, headers, runtime)

    def stop_instance_v2with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.save_image):
            body['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_v2with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.StopInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.StopInstanceV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.save_image):
            body['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_v2(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceV2Request,
    ) -> pai_dsw_20210226_models.UpdateInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_v2with_options(instance_id, request, headers, runtime)

    async def update_instance_v2_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceV2Request,
    ) -> pai_dsw_20210226_models.UpdateInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_v2with_options_async(instance_id, request, headers, runtime)

    def update_instance_v2with_options(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.accelerator_type):
            body['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.accumulated_running_time_in_ms):
            body['AccumulatedRunningTimeInMs'] = request.accumulated_running_time_in_ms
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.gmt_create_time):
            body['GmtCreateTime'] = request.gmt_create_time
        if not UtilClient.is_unset(request.gmt_modified_time):
            body['GmtModifiedTime'] = request.gmt_modified_time
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_shutdown_timer):
            body['InstanceShutdownTimer'] = request.instance_shutdown_timer
        if not UtilClient.is_unset(request.instance_url):
            body['InstanceUrl'] = request.instance_url
        if not UtilClient.is_unset(request.jupyterlab_url):
            body['JupyterlabUrl'] = request.jupyterlab_url
        if not UtilClient.is_unset(request.latest_snapshot):
            body['LatestSnapshot'] = request.latest_snapshot
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.reason_code):
            body['ReasonCode'] = request.reason_code
        if not UtilClient.is_unset(request.reason_message):
            body['ReasonMessage'] = request.reason_message
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.terminal_url):
            body['TerminalUrl'] = request.terminal_url
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.web_ideurl):
            body['WebIDEUrl'] = request.web_ideurl
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_v2with_options_async(
        self,
        instance_id: str,
        request: pai_dsw_20210226_models.UpdateInstanceV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateInstanceV2Response:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.accelerator_type):
            body['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.accumulated_running_time_in_ms):
            body['AccumulatedRunningTimeInMs'] = request.accumulated_running_time_in_ms
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.gmt_create_time):
            body['GmtCreateTime'] = request.gmt_create_time
        if not UtilClient.is_unset(request.gmt_modified_time):
            body['GmtModifiedTime'] = request.gmt_modified_time
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_shutdown_timer):
            body['InstanceShutdownTimer'] = request.instance_shutdown_timer
        if not UtilClient.is_unset(request.instance_url):
            body['InstanceUrl'] = request.instance_url
        if not UtilClient.is_unset(request.jupyterlab_url):
            body['JupyterlabUrl'] = request.jupyterlab_url
        if not UtilClient.is_unset(request.latest_snapshot):
            body['LatestSnapshot'] = request.latest_snapshot
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.reason_code):
            body['ReasonCode'] = request.reason_code
        if not UtilClient.is_unset(request.reason_message):
            body['ReasonMessage'] = request.reason_message
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.terminal_url):
            body['TerminalUrl'] = request.terminal_url
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.web_ideurl):
            body['WebIDEUrl'] = request.web_ideurl
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v2/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_v3instance_by_user(
        self,
        request: pai_dsw_20210226_models.UpdateV3InstanceByUserRequest,
    ) -> pai_dsw_20210226_models.UpdateV3InstanceByUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_v3instance_by_user_with_options(request, headers, runtime)

    async def update_v3instance_by_user_async(
        self,
        request: pai_dsw_20210226_models.UpdateV3InstanceByUserRequest,
    ) -> pai_dsw_20210226_models.UpdateV3InstanceByUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_v3instance_by_user_with_options_async(request, headers, runtime)

    def update_v3instance_by_user_with_options(
        self,
        request: pai_dsw_20210226_models.UpdateV3InstanceByUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateV3InstanceByUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateV3InstanceByUser',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/migrate/user',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateV3InstanceByUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_v3instance_by_user_with_options_async(
        self,
        request: pai_dsw_20210226_models.UpdateV3InstanceByUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.UpdateV3InstanceByUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateV3InstanceByUser',
            version='2021-02-26',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/migrate/user',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateV3InstanceByUserResponse(),
            await self.call_api_async(params, req, runtime)
        )
