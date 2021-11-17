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

    def create_image(
        self,
        request: pai_dsw_20210226_models.CreateImageRequest,
    ) -> pai_dsw_20210226_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_image_with_options(request, headers, runtime)

    async def create_image_async(
        self,
        request: pai_dsw_20210226_models.CreateImageRequest,
    ) -> pai_dsw_20210226_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_image_with_options_async(request, headers, runtime)

    def create_image_with_options(
        self,
        request: pai_dsw_20210226_models.CreateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.repository):
            body['Repository'] = request.repository
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateImageResponse(),
            self.do_roarequest('CreateImage', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: pai_dsw_20210226_models.CreateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.CreateImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.repository):
            body['Repository'] = request.repository
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateImageResponse(),
            await self.do_roarequest_async('CreateImage', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/images', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            await self.do_roarequest_async('CreateInstance', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('CreateInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            await self.do_roarequest_async('CreateInstanceSnapshot', '2021-02-26', 'HTTPS', 'POST', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            await self.do_roarequest_async('DeleteInstance', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('DeleteInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            await self.do_roarequest_async('DeleteInstanceSnapshot', '2021-02-26', 'HTTPS', 'DELETE', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetDashboardStatisticsResponse(),
            self.do_roarequest('GetDashboardStatistics', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/dashboard', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetDashboardStatisticsResponse(),
            await self.do_roarequest_async('GetDashboardStatistics', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/dashboard', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            await self.do_roarequest_async('GetInstance', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}', 'json', req, runtime)
        )

    def get_instance_image(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_image_with_options(instance_id, headers, runtime)

    async def get_instance_image_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_image_with_options_async(instance_id, headers, runtime)

    def get_instance_image_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceImageResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceImageResponse(),
            self.do_roarequest('GetInstanceImage', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/image', 'json', req, runtime)
        )

    async def get_instance_image_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceImageResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceImageResponse(),
            await self.do_roarequest_async('GetInstanceImage', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/image', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            await self.do_roarequest_async('GetInstanceShutdownTimer', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/shutdownTimer', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            await self.do_roarequest_async('GetInstanceSnapshot', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots/{instance_snapshot_id}', 'json', req, runtime)
        )

    def get_instance_type(
        self,
        instance_type_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_type_with_options(instance_type_id, headers, runtime)

    async def get_instance_type_async(
        self,
        instance_type_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_type_with_options_async(instance_type_id, headers, runtime)

    def get_instance_type_with_options(
        self,
        instance_type_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceTypeResponse:
        instance_type_id = OpenApiUtilClient.get_encode_param(instance_type_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceTypeResponse(),
            self.do_roarequest('GetInstanceType', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instanceTypes/{instance_type_id}', 'json', req, runtime)
        )

    async def get_instance_type_with_options_async(
        self,
        instance_type_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceTypeResponse:
        instance_type_id = OpenApiUtilClient.get_encode_param(instance_type_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceTypeResponse(),
            await self.do_roarequest_async('GetInstanceType', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instanceTypes/{instance_type_id}', 'json', req, runtime)
        )

    def get_instance_url(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_url_with_options(instance_id, headers, runtime)

    async def get_instance_url_async(
        self,
        instance_id: str,
    ) -> pai_dsw_20210226_models.GetInstanceUrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_url_with_options_async(instance_id, headers, runtime)

    def get_instance_url_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceUrlResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceUrlResponse(),
            self.do_roarequest('GetInstanceUrl', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/url', 'json', req, runtime)
        )

    async def get_instance_url_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetInstanceUrlResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceUrlResponse(),
            await self.do_roarequest_async('GetInstanceUrl', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/url', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstancesStatisticsResponse(),
            self.do_roarequest('GetInstancesStatistics', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/instances', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstancesStatisticsResponse(),
            await self.do_roarequest_async('GetInstancesStatistics', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/instances', 'json', req, runtime)
        )

    def get_user_config(self) -> pai_dsw_20210226_models.GetUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_config_with_options(headers, runtime)

    async def get_user_config_async(self) -> pai_dsw_20210226_models.GetUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_config_with_options_async(headers, runtime)

    def get_user_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserConfigResponse(),
            self.do_roarequest('GetUserConfig', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/config', 'json', req, runtime)
        )

    async def get_user_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserConfigResponse(),
            await self.do_roarequest_async('GetUserConfig', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/config', 'json', req, runtime)
        )

    def get_user_resource_authorization_status(self) -> pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_resource_authorization_status_with_options(headers, runtime)

    async def get_user_resource_authorization_status_async(self) -> pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_resource_authorization_status_with_options_async(headers, runtime)

    def get_user_resource_authorization_status_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse(),
            self.do_roarequest('GetUserResourceAuthorizationStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/resourceAuthorizationStatus', 'json', req, runtime)
        )

    async def get_user_resource_authorization_status_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserResourceAuthorizationStatusResponse(),
            await self.do_roarequest_async('GetUserResourceAuthorizationStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/resourceAuthorizationStatus', 'json', req, runtime)
        )

    def get_user_resource_status(self) -> pai_dsw_20210226_models.GetUserResourceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_resource_status_with_options(headers, runtime)

    async def get_user_resource_status_async(self) -> pai_dsw_20210226_models.GetUserResourceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_resource_status_with_options_async(headers, runtime)

    def get_user_resource_status_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserResourceStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserResourceStatusResponse(),
            self.do_roarequest('GetUserResourceStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/resourceStatus', 'json', req, runtime)
        )

    async def get_user_resource_status_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserResourceStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserResourceStatusResponse(),
            await self.do_roarequest_async('GetUserResourceStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/resourceStatus', 'json', req, runtime)
        )

    def get_user_special_version_gpu_resource_info(
        self,
        request: pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoRequest,
    ) -> pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_special_version_gpu_resource_info_with_options(request, headers, runtime)

    async def get_user_special_version_gpu_resource_info_async(
        self,
        request: pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoRequest,
    ) -> pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_special_version_gpu_resource_info_with_options_async(request, headers, runtime)

    def get_user_special_version_gpu_resource_info_with_options(
        self,
        request: pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse(),
            self.do_roarequest('GetUserSpecialVersionGpuResourceInfo', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/specialVersionGpuResourceInfo', 'json', req, runtime)
        )

    async def get_user_special_version_gpu_resource_info_with_options_async(
        self,
        request: pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserSpecialVersionGpuResourceInfoResponse(),
            await self.do_roarequest_async('GetUserSpecialVersionGpuResourceInfo', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/specialVersionGpuResourceInfo', 'json', req, runtime)
        )

    def list_configs(self) -> pai_dsw_20210226_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(headers, runtime)

    async def list_configs_async(self) -> pai_dsw_20210226_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_configs_with_options_async(headers, runtime)

    def list_configs_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListConfigsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListConfigsResponse(),
            self.do_roarequest('ListConfigs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/configs', 'json', req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListConfigsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListConfigsResponse(),
            await self.do_roarequest_async('ListConfigs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/configs', 'json', req, runtime)
        )

    def list_datasets(
        self,
        request: pai_dsw_20210226_models.ListDatasetsRequest,
    ) -> pai_dsw_20210226_models.ListDatasetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasets_with_options(request, headers, runtime)

    async def list_datasets_async(
        self,
        request: pai_dsw_20210226_models.ListDatasetsRequest,
    ) -> pai_dsw_20210226_models.ListDatasetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasets_with_options_async(request, headers, runtime)

    def list_datasets_with_options(
        self,
        request: pai_dsw_20210226_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListDatasetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListDatasetsResponse(),
            self.do_roarequest('ListDatasets', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/datasets', 'json', req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListDatasetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListDatasetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListDatasetsResponse(),
            await self.do_roarequest_async('ListDatasets', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/datasets', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            await self.do_roarequest_async('ListImages', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            await self.do_roarequest_async('ListInstanceSnapshots', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances/{instance_id}/snapshots', 'json', req, runtime)
        )

    def list_instance_types(
        self,
        request: pai_dsw_20210226_models.ListInstanceTypesRequest,
    ) -> pai_dsw_20210226_models.ListInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_types_with_options(request, headers, runtime)

    async def list_instance_types_async(
        self,
        request: pai_dsw_20210226_models.ListInstanceTypesRequest,
    ) -> pai_dsw_20210226_models.ListInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_types_with_options_async(request, headers, runtime)

    def list_instance_types_with_options(
        self,
        request: pai_dsw_20210226_models.ListInstanceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceTypesResponse(),
            self.do_roarequest('ListInstanceTypes', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instanceTypes', 'json', req, runtime)
        )

    async def list_instance_types_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListInstanceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceTypesResponse(),
            await self.do_roarequest_async('ListInstanceTypes', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instanceTypes', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            await self.do_roarequest_async('ListInstances', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/instances', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesStatusResponse(),
            self.do_roarequest('ListInstancesStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statuses/instances', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesStatusResponse(),
            await self.do_roarequest_async('ListInstancesStatus', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/statuses/instances', 'json', req, runtime)
        )

    def list_namespaces(self) -> pai_dsw_20210226_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespaces_with_options(headers, runtime)

    async def list_namespaces_async(self) -> pai_dsw_20210226_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_namespaces_with_options_async(headers, runtime)

    def list_namespaces_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNamespacesResponse(),
            self.do_roarequest('ListNamespaces', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/imageRegistry/namespaces', 'json', req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNamespacesResponse(),
            await self.do_roarequest_async('ListNamespaces', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/imageRegistry/namespaces', 'json', req, runtime)
        )

    def list_nases(self) -> pai_dsw_20210226_models.ListNasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nases_with_options(headers, runtime)

    async def list_nases_async(self) -> pai_dsw_20210226_models.ListNasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_nases_with_options_async(headers, runtime)

    def list_nases_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNasesResponse(),
            self.do_roarequest('ListNases', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/nases', 'json', req, runtime)
        )

    async def list_nases_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNasesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNasesResponse(),
            await self.do_roarequest_async('ListNases', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/nases', 'json', req, runtime)
        )

    def list_network_security_groups(
        self,
        vpc_id: str,
    ) -> pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_network_security_groups_with_options(vpc_id, headers, runtime)

    async def list_network_security_groups_async(
        self,
        vpc_id: str,
    ) -> pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_network_security_groups_with_options_async(vpc_id, headers, runtime)

    def list_network_security_groups_with_options(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse:
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse(),
            self.do_roarequest('ListNetworkSecurityGroups', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs/{vpc_id}/securityGroups', 'json', req, runtime)
        )

    async def list_network_security_groups_with_options_async(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse:
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkSecurityGroupsResponse(),
            await self.do_roarequest_async('ListNetworkSecurityGroups', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs/{vpc_id}/securityGroups', 'json', req, runtime)
        )

    def list_network_vswitches(
        self,
        vpc_id: str,
    ) -> pai_dsw_20210226_models.ListNetworkVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_network_vswitches_with_options(vpc_id, headers, runtime)

    async def list_network_vswitches_async(
        self,
        vpc_id: str,
    ) -> pai_dsw_20210226_models.ListNetworkVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_network_vswitches_with_options_async(vpc_id, headers, runtime)

    def list_network_vswitches_with_options(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkVSwitchesResponse:
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkVSwitchesResponse(),
            self.do_roarequest('ListNetworkVSwitches', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs/{vpc_id}/vSwitches', 'json', req, runtime)
        )

    async def list_network_vswitches_with_options_async(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkVSwitchesResponse:
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkVSwitchesResponse(),
            await self.do_roarequest_async('ListNetworkVSwitches', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs/{vpc_id}/vSwitches', 'json', req, runtime)
        )

    def list_network_vpcs(self) -> pai_dsw_20210226_models.ListNetworkVpcsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_network_vpcs_with_options(headers, runtime)

    async def list_network_vpcs_async(self) -> pai_dsw_20210226_models.ListNetworkVpcsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_network_vpcs_with_options_async(headers, runtime)

    def list_network_vpcs_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkVpcsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkVpcsResponse(),
            self.do_roarequest('ListNetworkVpcs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs', 'json', req, runtime)
        )

    async def list_network_vpcs_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListNetworkVpcsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListNetworkVpcsResponse(),
            await self.do_roarequest_async('ListNetworkVpcs', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/network/vpcs', 'json', req, runtime)
        )

    def list_regions(self) -> pai_dsw_20210226_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> pai_dsw_20210226_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListRegionsResponse(),
            self.do_roarequest('ListRegions', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/configs/regions', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListRegionsResponse(),
            await self.do_roarequest_async('ListRegions', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/configs/regions', 'json', req, runtime)
        )

    def list_repositories(
        self,
        namespace: str,
    ) -> pai_dsw_20210226_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(namespace, headers, runtime)

    async def list_repositories_async(
        self,
        namespace: str,
    ) -> pai_dsw_20210226_models.ListRepositoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repositories_with_options_async(namespace, headers, runtime)

    def list_repositories_with_options(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListRepositoriesResponse:
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListRepositoriesResponse(),
            self.do_roarequest('ListRepositories', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/imageRegistry/namespaces/{namespace}/repositories', 'json', req, runtime)
        )

    async def list_repositories_with_options_async(
        self,
        namespace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListRepositoriesResponse:
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListRepositoriesResponse(),
            await self.do_roarequest_async('ListRepositories', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/imageRegistry/namespaces/{namespace}/repositories', 'json', req, runtime)
        )

    def list_user_clusters(self) -> pai_dsw_20210226_models.ListUserClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_clusters_with_options(headers, runtime)

    async def list_user_clusters_async(self) -> pai_dsw_20210226_models.ListUserClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_clusters_with_options_async(headers, runtime)

    def list_user_clusters_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListUserClustersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListUserClustersResponse(),
            self.do_roarequest('ListUserClusters', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/clusters', 'json', req, runtime)
        )

    async def list_user_clusters_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListUserClustersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListUserClustersResponse(),
            await self.do_roarequest_async('ListUserClusters', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/clusters', 'json', req, runtime)
        )

    def list_user_work_nodes(
        self,
        request: pai_dsw_20210226_models.ListUserWorkNodesRequest,
    ) -> pai_dsw_20210226_models.ListUserWorkNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_work_nodes_with_options(request, headers, runtime)

    async def list_user_work_nodes_async(
        self,
        request: pai_dsw_20210226_models.ListUserWorkNodesRequest,
    ) -> pai_dsw_20210226_models.ListUserWorkNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_work_nodes_with_options_async(request, headers, runtime)

    def list_user_work_nodes_with_options(
        self,
        request: pai_dsw_20210226_models.ListUserWorkNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListUserWorkNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListUserWorkNodesResponse(),
            self.do_roarequest('ListUserWorkNodes', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/workerNodes', 'json', req, runtime)
        )

    async def list_user_work_nodes_with_options_async(
        self,
        request: pai_dsw_20210226_models.ListUserWorkNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dsw_20210226_models.ListUserWorkNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListUserWorkNodesResponse(),
            await self.do_roarequest_async('ListUserWorkNodes', '2021-02-26', 'HTTPS', 'GET', 'AK', f'/api/v1/users/workerNodes', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            await self.do_roarequest_async('StartInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/start', 'json', req, runtime)
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
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            self.do_roarequest('StopInstance', '2021-02-26', 'HTTPS', 'PUT', 'AK', f'/api/v1/instances/{instance_id}/stop', 'json', req, runtime)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
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
