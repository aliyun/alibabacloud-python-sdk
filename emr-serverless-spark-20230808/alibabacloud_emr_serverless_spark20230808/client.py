# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_emr_serverless_spark20230808 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('emr-serverless-spark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_members_with_options(
        self,
        request: main_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMembers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_members_with_options_async(
        self,
        request: main_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMembers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_members(
        self,
        request: main_models.AddMembersRequest,
    ) -> main_models.AddMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_members_with_options(request, headers, runtime)

    async def add_members_async(
        self,
        request: main_models.AddMembersRequest,
    ) -> main_models.AddMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_members_with_options_async(request, headers, runtime)

    def cancel_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.CancelJobRunRequest,
    ) -> main_models.CancelJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def cancel_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.CancelJobRunRequest,
    ) -> main_models.CancelJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def cancel_kyuubi_spark_application_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        application_id: str,
        request: main_models.CancelKyuubiSparkApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelKyuubiSparkApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelKyuubiSparkApplication',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/application/{DaraURL.percent_encode(application_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelKyuubiSparkApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_kyuubi_spark_application_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        application_id: str,
        request: main_models.CancelKyuubiSparkApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelKyuubiSparkApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelKyuubiSparkApplication',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/application/{DaraURL.percent_encode(application_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelKyuubiSparkApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_kyuubi_spark_application(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        application_id: str,
        request: main_models.CancelKyuubiSparkApplicationRequest,
    ) -> main_models.CancelKyuubiSparkApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_kyuubi_spark_application_with_options(workspace_id, kyuubi_service_id, application_id, request, headers, runtime)

    async def cancel_kyuubi_spark_application_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        application_id: str,
        request: main_models.CancelKyuubiSparkApplicationRequest,
    ) -> main_models.CancelKyuubiSparkApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_kyuubi_spark_application_with_options_async(workspace_id, kyuubi_service_id, application_id, request, headers, runtime)

    def create_kyuubi_service_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateKyuubiServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKyuubiServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not DaraCore.is_null(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not DaraCore.is_null(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue):
            body['queue'] = request.queue
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.replica):
            body['replica'] = request.replica
        if not DaraCore.is_null(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateKyuubiServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKyuubiServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not DaraCore.is_null(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not DaraCore.is_null(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue):
            body['queue'] = request.queue
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.replica):
            body['replica'] = request.replica
        if not DaraCore.is_null(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kyuubi_service(
        self,
        workspace_id: str,
        request: main_models.CreateKyuubiServiceRequest,
    ) -> main_models.CreateKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_kyuubi_service_with_options(workspace_id, request, headers, runtime)

    async def create_kyuubi_service_async(
        self,
        workspace_id: str,
        request: main_models.CreateKyuubiServiceRequest,
    ) -> main_models.CreateKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_kyuubi_service_with_options_async(workspace_id, request, headers, runtime)

    def create_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.CreateKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.CreateKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.CreateKyuubiTokenRequest,
    ) -> main_models.CreateKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_kyuubi_token_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def create_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.CreateKyuubiTokenRequest,
    ) -> main_models.CreateKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def create_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        request: main_models.CreateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auth_type):
            body['authType'] = request.auth_type
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not DaraCore.is_null(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not DaraCore.is_null(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_name):
            body['networkName'] = request.network_name
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        request: main_models.CreateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auth_type):
            body['authType'] = request.auth_type
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not DaraCore.is_null(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not DaraCore.is_null(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_name):
            body['networkName'] = request.network_name
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_livy_compute(
        self,
        workspace_biz_id: str,
        request: main_models.CreateLivyComputeRequest,
    ) -> main_models.CreateLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    async def create_livy_compute_async(
        self,
        workspace_biz_id: str,
        request: main_models.CreateLivyComputeRequest,
    ) -> main_models.CreateLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_livy_compute_with_options_async(workspace_biz_id, request, headers, runtime)

    def create_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.CreateLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.CreateLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.CreateLivyComputeTokenRequest,
    ) -> main_models.CreateLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def create_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.CreateLivyComputeTokenRequest,
    ) -> main_models.CreateLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def create_process_definition_with_schedule_with_options(
        self,
        biz_id: str,
        tmp_req: main_models.CreateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProcessDefinitionWithScheduleResponse:
        tmp_req.validate()
        request = main_models.CreateProcessDefinitionWithScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_params):
            request.global_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not DaraCore.is_null(tmp_req.task_definition_json):
            request.task_definition_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not DaraCore.is_null(tmp_req.task_relation_json):
            request.task_relation_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.execution_type):
            query['executionType'] = request.execution_type
        if not DaraCore.is_null(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.publish):
            query['publish'] = request.publish
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not DaraCore.is_null(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not DaraCore.is_null(request.run_as):
            query['runAs'] = request.run_as
        if not DaraCore.is_null(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not DaraCore.is_null(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not DaraCore.is_null(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not DaraCore.is_null(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProcessDefinitionWithSchedule',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/process-definition',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_process_definition_with_schedule_with_options_async(
        self,
        biz_id: str,
        tmp_req: main_models.CreateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProcessDefinitionWithScheduleResponse:
        tmp_req.validate()
        request = main_models.CreateProcessDefinitionWithScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_params):
            request.global_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not DaraCore.is_null(tmp_req.task_definition_json):
            request.task_definition_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not DaraCore.is_null(tmp_req.task_relation_json):
            request.task_relation_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.execution_type):
            query['executionType'] = request.execution_type
        if not DaraCore.is_null(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.publish):
            query['publish'] = request.publish
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not DaraCore.is_null(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not DaraCore.is_null(request.run_as):
            query['runAs'] = request.run_as
        if not DaraCore.is_null(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not DaraCore.is_null(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not DaraCore.is_null(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not DaraCore.is_null(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProcessDefinitionWithSchedule',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/process-definition',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProcessDefinitionWithScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_process_definition_with_schedule(
        self,
        biz_id: str,
        request: main_models.CreateProcessDefinitionWithScheduleRequest,
    ) -> main_models.CreateProcessDefinitionWithScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_process_definition_with_schedule_with_options(biz_id, request, headers, runtime)

    async def create_process_definition_with_schedule_async(
        self,
        biz_id: str,
        request: main_models.CreateProcessDefinitionWithScheduleRequest,
    ) -> main_models.CreateProcessDefinitionWithScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_process_definition_with_schedule_with_options_async(biz_id, request, headers, runtime)

    def create_session_cluster_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.application_configs):
            body['applicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.env_id):
            body['envId'] = request.env_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.kind):
            body['kind'] = request.kind
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.application_configs):
            body['applicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.env_id):
            body['envId'] = request.env_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.kind):
            body['kind'] = request.kind
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session_cluster(
        self,
        workspace_id: str,
        request: main_models.CreateSessionClusterRequest,
    ) -> main_models.CreateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def create_session_cluster_async(
        self,
        workspace_id: str,
        request: main_models.CreateSessionClusterRequest,
    ) -> main_models.CreateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def create_sql_statement_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.code_content):
            body['codeContent'] = request.code_content
        if not DaraCore.is_null(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not DaraCore.is_null(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        if not DaraCore.is_null(request.task_biz_id):
            body['taskBizId'] = request.task_biz_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_statement_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.code_content):
            body['codeContent'] = request.code_content
        if not DaraCore.is_null(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not DaraCore.is_null(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        if not DaraCore.is_null(request.task_biz_id):
            body['taskBizId'] = request.task_biz_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_statement(
        self,
        workspace_id: str,
        request: main_models.CreateSqlStatementRequest,
    ) -> main_models.CreateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sql_statement_with_options(workspace_id, request, headers, runtime)

    async def create_sql_statement_async(
        self,
        workspace_id: str,
        request: main_models.CreateSqlStatementRequest,
    ) -> main_models.CreateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sql_statement_with_options_async(workspace_id, request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.auto_renew_period_unit):
            body['autoRenewPeriodUnit'] = request.auto_renew_period_unit
        if not DaraCore.is_null(request.auto_start_session_cluster):
            body['autoStartSessionCluster'] = request.auto_start_session_cluster
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dlf_catalog_id):
            body['dlfCatalogId'] = request.dlf_catalog_id
        if not DaraCore.is_null(request.dlf_type):
            body['dlfType'] = request.dlf_type
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.oss_bucket):
            body['ossBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.ram_role_name):
            body['ramRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.release_type):
            body['releaseType'] = request.release_type
        if not DaraCore.is_null(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.auto_renew_period_unit):
            body['autoRenewPeriodUnit'] = request.auto_renew_period_unit
        if not DaraCore.is_null(request.auto_start_session_cluster):
            body['autoStartSessionCluster'] = request.auto_start_session_cluster
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dlf_catalog_id):
            body['dlfCatalogId'] = request.dlf_catalog_id
        if not DaraCore.is_null(request.dlf_type):
            body['dlfType'] = request.dlf_type
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.oss_bucket):
            body['ossBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.ram_role_name):
            body['ramRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.release_type):
            body['releaseType'] = request.release_type
        if not DaraCore.is_null(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def delete_kyuubi_service_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kyuubi_service(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.DeleteKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    async def delete_kyuubi_service_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.DeleteKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_kyuubi_service_with_options_async(workspace_id, kyuubi_service_id, headers, runtime)

    def delete_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.DeleteKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.DeleteKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.DeleteKyuubiTokenRequest,
    ) -> main_models.DeleteKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    async def delete_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.DeleteKyuubiTokenRequest,
    ) -> main_models.DeleteKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def delete_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.DeleteLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.DeleteLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.DeleteLivyComputeRequest,
    ) -> main_models.DeleteLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def delete_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.DeleteLivyComputeRequest,
    ) -> main_models.DeleteLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def delete_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.DeleteLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.DeleteLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.DeleteLivyComputeTokenRequest,
    ) -> main_models.DeleteLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def delete_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.DeleteLivyComputeTokenRequest,
    ) -> main_models.DeleteLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def edit_workspace_queue_with_options(
        self,
        request: main_models.EditWorkspaceQueueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditWorkspaceQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.environments):
            body['environments'] = request.environments
        if not DaraCore.is_null(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_queue_name):
            body['workspaceQueueName'] = request.workspace_queue_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditWorkspaceQueue',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/queues/action/edit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditWorkspaceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_workspace_queue_with_options_async(
        self,
        request: main_models.EditWorkspaceQueueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditWorkspaceQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.environments):
            body['environments'] = request.environments
        if not DaraCore.is_null(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_queue_name):
            body['workspaceQueueName'] = request.workspace_queue_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditWorkspaceQueue',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/queues/action/edit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditWorkspaceQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_workspace_queue(
        self,
        request: main_models.EditWorkspaceQueueRequest,
    ) -> main_models.EditWorkspaceQueueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.edit_workspace_queue_with_options(request, headers, runtime)

    async def edit_workspace_queue_async(
        self,
        request: main_models.EditWorkspaceQueueRequest,
    ) -> main_models.EditWorkspaceQueueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.edit_workspace_queue_with_options_async(request, headers, runtime)

    def generate_task_codes_with_options(
        self,
        biz_id: str,
        request: main_models.GenerateTaskCodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTaskCodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gen_num):
            query['genNum'] = request.gen_num
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTaskCodes',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/task-definition/gen-task-codes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTaskCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_task_codes_with_options_async(
        self,
        biz_id: str,
        request: main_models.GenerateTaskCodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTaskCodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gen_num):
            query['genNum'] = request.gen_num
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTaskCodes',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/task-definition/gen-task-codes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTaskCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_task_codes(
        self,
        biz_id: str,
        request: main_models.GenerateTaskCodesRequest,
    ) -> main_models.GenerateTaskCodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_task_codes_with_options(biz_id, request, headers, runtime)

    async def generate_task_codes_async(
        self,
        biz_id: str,
        request: main_models.GenerateTaskCodesRequest,
    ) -> main_models.GenerateTaskCodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_task_codes_with_options_async(biz_id, request, headers, runtime)

    def get_cu_hours_with_options(
        self,
        workspace_id: str,
        queue: str,
        request: main_models.GetCuHoursRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCuHoursResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCuHours',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/metric/cuHours/{DaraURL.percent_encode(queue)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCuHoursResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cu_hours_with_options_async(
        self,
        workspace_id: str,
        queue: str,
        request: main_models.GetCuHoursRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCuHoursResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCuHours',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/metric/cuHours/{DaraURL.percent_encode(queue)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCuHoursResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cu_hours(
        self,
        workspace_id: str,
        queue: str,
        request: main_models.GetCuHoursRequest,
    ) -> main_models.GetCuHoursResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cu_hours_with_options(workspace_id, queue, request, headers, runtime)

    async def get_cu_hours_async(
        self,
        workspace_id: str,
        queue: str,
        request: main_models.GetCuHoursRequest,
    ) -> main_models.GetCuHoursResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cu_hours_with_options_async(workspace_id, queue, request, headers, runtime)

    def get_doctor_application_with_options(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetDoctorApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale):
            query['locale'] = request.locale
        if not DaraCore.is_null(request.query_time):
            query['queryTime'] = request.query_time
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorApplication',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/runs/{DaraURL.percent_encode(run_id)}/action/getDoctorApplication',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_application_with_options_async(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetDoctorApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locale):
            query['locale'] = request.locale
        if not DaraCore.is_null(request.query_time):
            query['queryTime'] = request.query_time
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorApplication',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/runs/{DaraURL.percent_encode(run_id)}/action/getDoctorApplication',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_application(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetDoctorApplicationRequest,
    ) -> main_models.GetDoctorApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_doctor_application_with_options(workspace_id, run_id, request, headers, runtime)

    async def get_doctor_application_async(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetDoctorApplicationRequest,
    ) -> main_models.GetDoctorApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_doctor_application_with_options_async(workspace_id, run_id, request, headers, runtime)

    def get_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.GetJobRunRequest,
    ) -> main_models.GetJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def get_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.GetJobRunRequest,
    ) -> main_models.GetJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def get_kyuubi_service_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kyuubi_service(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.GetKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    async def get_kyuubi_service_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.GetKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_kyuubi_service_with_options_async(workspace_id, kyuubi_service_id, headers, runtime)

    def get_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.GetKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.GetKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.GetKyuubiTokenRequest,
    ) -> main_models.GetKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    async def get_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.GetKyuubiTokenRequest,
    ) -> main_models.GetKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def get_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.GetLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.GetLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.GetLivyComputeRequest,
    ) -> main_models.GetLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def get_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.GetLivyComputeRequest,
    ) -> main_models.GetLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def get_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.GetLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.GetLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.GetLivyComputeTokenRequest,
    ) -> main_models.GetLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def get_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.GetLivyComputeTokenRequest,
    ) -> main_models.GetLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def get_run_configuration_with_options(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetRunConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunConfiguration',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/runs/{DaraURL.percent_encode(run_id)}/action/getRunConfiguration',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_run_configuration_with_options_async(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetRunConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunConfiguration',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/runs/{DaraURL.percent_encode(run_id)}/action/getRunConfiguration',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_run_configuration(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetRunConfigurationRequest,
    ) -> main_models.GetRunConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_run_configuration_with_options(workspace_id, run_id, request, headers, runtime)

    async def get_run_configuration_async(
        self,
        workspace_id: str,
        run_id: str,
        request: main_models.GetRunConfigurationRequest,
    ) -> main_models.GetRunConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_run_configuration_with_options_async(workspace_id, run_id, request, headers, runtime)

    def get_session_cluster_with_options(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: main_models.GetSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/{DaraURL.percent_encode(session_cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_cluster_with_options_async(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: main_models.GetSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/{DaraURL.percent_encode(session_cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_cluster(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: main_models.GetSessionClusterRequest,
    ) -> main_models.GetSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_session_cluster_with_options(workspace_id, session_cluster_id, request, headers, runtime)

    async def get_session_cluster_async(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: main_models.GetSessionClusterRequest,
    ) -> main_models.GetSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_session_cluster_with_options_async(workspace_id, session_cluster_id, request, headers, runtime)

    def get_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement/{DaraURL.percent_encode(statement_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement/{DaraURL.percent_encode(statement_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.GetSqlStatementRequest,
    ) -> main_models.GetSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def get_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.GetSqlStatementRequest,
    ) -> main_models.GetSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)

    def get_template_with_options(
        self,
        workspace_biz_id: str,
        request: main_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.template_biz_id):
            query['templateBizId'] = request.template_biz_id
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        workspace_biz_id: str,
        request: main_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.template_biz_id):
            query['templateBizId'] = request.template_biz_id
        if not DaraCore.is_null(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        workspace_biz_id: str,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_with_options(workspace_biz_id, request, headers, runtime)

    async def get_template_async(
        self,
        workspace_biz_id: str,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(workspace_biz_id, request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: main_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleToUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        if not DaraCore.is_null(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRoleToUsers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/roles/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: main_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleToUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.role_arn):
            body['roleArn'] = request.role_arn
        if not DaraCore.is_null(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRoleToUsers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/roles/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: main_models.GrantRoleToUsersRequest,
    ) -> main_models.GrantRoleToUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: main_models.GrantRoleToUsersRequest,
    ) -> main_models.GrantRoleToUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def list_catalogs_with_options(
        self,
        workspace_id: str,
        request: main_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['environment'] = request.environment
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['environment'] = request.environment
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        workspace_id: str,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(workspace_id, request, headers, runtime)

    async def list_catalogs_async(
        self,
        workspace_id: str,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_catalogs_with_options_async(workspace_id, request, headers, runtime)

    def list_job_executors_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.ListJobExecutorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.executor_type):
            query['executorType'] = request.executor_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutors',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}/executors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_executors_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.ListJobExecutorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobExecutorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.executor_type):
            query['executorType'] = request.executor_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobExecutors',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns/{DaraURL.percent_encode(job_run_id)}/executors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_executors(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.ListJobExecutorsRequest,
    ) -> main_models.ListJobExecutorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_executors_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def list_job_executors_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: main_models.ListJobExecutorsRequest,
    ) -> main_models.ListJobExecutorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_executors_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def list_job_runs_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobRunsResponse:
        tmp_req.validate()
        request = main_models.ListJobRunsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.end_time):
            request.end_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not DaraCore.is_null(tmp_req.start_time):
            request.start_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not DaraCore.is_null(tmp_req.states):
            request.states_shrink = Utils.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['applicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.creator):
            query['creator'] = request.creator
        if not DaraCore.is_null(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not DaraCore.is_null(request.is_workflow):
            query['isWorkflow'] = request.is_workflow
        if not DaraCore.is_null(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not DaraCore.is_null(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.runtime_configs):
            query['runtimeConfigs'] = request.runtime_configs
        if not DaraCore.is_null(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not DaraCore.is_null(request.states_shrink):
            query['states'] = request.states_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobRuns',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_runs_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobRunsResponse:
        tmp_req.validate()
        request = main_models.ListJobRunsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.end_time):
            request.end_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not DaraCore.is_null(tmp_req.start_time):
            request.start_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not DaraCore.is_null(tmp_req.states):
            request.states_shrink = Utils.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['applicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.creator):
            query['creator'] = request.creator
        if not DaraCore.is_null(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not DaraCore.is_null(request.is_workflow):
            query['isWorkflow'] = request.is_workflow
        if not DaraCore.is_null(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not DaraCore.is_null(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.runtime_configs):
            query['runtimeConfigs'] = request.runtime_configs
        if not DaraCore.is_null(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not DaraCore.is_null(request.states_shrink):
            query['states'] = request.states_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobRuns',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_runs(
        self,
        workspace_id: str,
        request: main_models.ListJobRunsRequest,
    ) -> main_models.ListJobRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_runs_with_options(workspace_id, request, headers, runtime)

    async def list_job_runs_async(
        self,
        workspace_id: str,
        request: main_models.ListJobRunsRequest,
    ) -> main_models.ListJobRunsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_runs_with_options_async(workspace_id, request, headers, runtime)

    def list_kyuubi_services_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiServicesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiServices',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_services_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiServicesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiServices',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_services(
        self,
        workspace_id: str,
    ) -> main_models.ListKyuubiServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_kyuubi_services_with_options(workspace_id, headers, runtime)

    async def list_kyuubi_services_async(
        self,
        workspace_id: str,
    ) -> main_models.ListKyuubiServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_services_with_options_async(workspace_id, headers, runtime)

    def list_kyuubi_spark_applications_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        tmp_req: main_models.ListKyuubiSparkApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiSparkApplicationsResponse:
        tmp_req.validate()
        request = main_models.ListKyuubiSparkApplicationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_by):
            request.order_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_by, 'orderBy', 'json')
        if not DaraCore.is_null(tmp_req.start_time):
            request.start_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['applicationId'] = request.application_id
        if not DaraCore.is_null(request.application_name):
            query['applicationName'] = request.application_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_shrink):
            query['orderBy'] = request.order_by_shrink
        if not DaraCore.is_null(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiSparkApplications',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiSparkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_spark_applications_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        tmp_req: main_models.ListKyuubiSparkApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiSparkApplicationsResponse:
        tmp_req.validate()
        request = main_models.ListKyuubiSparkApplicationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_by):
            request.order_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_by, 'orderBy', 'json')
        if not DaraCore.is_null(tmp_req.start_time):
            request.start_time_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['applicationId'] = request.application_id
        if not DaraCore.is_null(request.application_name):
            query['applicationName'] = request.application_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_shrink):
            query['orderBy'] = request.order_by_shrink
        if not DaraCore.is_null(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiSparkApplications',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiSparkApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_spark_applications(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiSparkApplicationsRequest,
    ) -> main_models.ListKyuubiSparkApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_kyuubi_spark_applications_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def list_kyuubi_spark_applications_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiSparkApplicationsRequest,
    ) -> main_models.ListKyuubiSparkApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_spark_applications_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiTokenRequest,
    ) -> main_models.ListKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_kyuubi_token_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def list_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.ListKyuubiTokenRequest,
    ) -> main_models.ListKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        request: main_models.ListLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        request: main_models.ListLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_livy_compute(
        self,
        workspace_biz_id: str,
        request: main_models.ListLivyComputeRequest,
    ) -> main_models.ListLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    async def list_livy_compute_async(
        self,
        workspace_biz_id: str,
        request: main_models.ListLivyComputeRequest,
    ) -> main_models.ListLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_livy_compute_with_options_async(workspace_biz_id, request, headers, runtime)

    def list_livy_compute_sessions_with_options(
        self,
        workspace_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyComputeSessions',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/session',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_livy_compute_sessions_with_options_async(
        self,
        workspace_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyComputeSessions',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/session',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_livy_compute_sessions(
        self,
        workspace_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeSessionsRequest,
    ) -> main_models.ListLivyComputeSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_livy_compute_sessions_with_options(workspace_id, livy_compute_id, request, headers, runtime)

    async def list_livy_compute_sessions_async(
        self,
        workspace_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeSessionsRequest,
    ) -> main_models.ListLivyComputeSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_livy_compute_sessions_with_options_async(workspace_id, livy_compute_id, request, headers, runtime)

    def list_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeTokenRequest,
    ) -> main_models.ListLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def list_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.ListLivyComputeTokenRequest,
    ) -> main_models.ListLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def list_log_contents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListLogContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.length):
            query['length'] = request.length
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogContents',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/action/listLogContents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_contents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListLogContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.length):
            query['length'] = request.length
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogContents',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/action/listLogContents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_contents(
        self,
        workspace_id: str,
        request: main_models.ListLogContentsRequest,
    ) -> main_models.ListLogContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_log_contents_with_options(workspace_id, request, headers, runtime)

    async def list_log_contents_async(
        self,
        workspace_id: str,
        request: main_models.ListLogContentsRequest,
    ) -> main_models.ListLogContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_log_contents_with_options_async(workspace_id, request, headers, runtime)

    def list_members_with_options(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/auth/{DaraURL.percent_encode(workspace_id)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_members_with_options(workspace_id, request, headers, runtime)

    async def list_members_async(
        self,
        workspace_id: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_members_with_options_async(workspace_id, request, headers, runtime)

    def list_release_versions_with_options(
        self,
        request: main_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReleaseVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.release_type):
            query['releaseType'] = request.release_type
        if not DaraCore.is_null(request.release_version):
            query['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        if not DaraCore.is_null(request.service_filter):
            query['serviceFilter'] = request.service_filter
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReleaseVersions',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/releaseVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_release_versions_with_options_async(
        self,
        request: main_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReleaseVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.release_type):
            query['releaseType'] = request.release_type
        if not DaraCore.is_null(request.release_version):
            query['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        if not DaraCore.is_null(request.service_filter):
            query['serviceFilter'] = request.service_filter
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReleaseVersions',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/releaseVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReleaseVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_release_versions(
        self,
        request: main_models.ListReleaseVersionsRequest,
    ) -> main_models.ListReleaseVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_release_versions_with_options(request, headers, runtime)

    async def list_release_versions_async(
        self,
        request: main_models.ListReleaseVersionsRequest,
    ) -> main_models.ListReleaseVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_release_versions_with_options_async(request, headers, runtime)

    def list_session_clusters_with_options(
        self,
        workspace_id: str,
        request: main_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kind):
            query['kind'] = request.kind
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.queue_name):
            query['queueName'] = request.queue_name
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessionClusters',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_clusters_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kind):
            query['kind'] = request.kind
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.queue_name):
            query['queueName'] = request.queue_name
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessionClusters',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_clusters(
        self,
        workspace_id: str,
        request: main_models.ListSessionClustersRequest,
    ) -> main_models.ListSessionClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_session_clusters_with_options(workspace_id, request, headers, runtime)

    async def list_session_clusters_async(
        self,
        workspace_id: str,
        request: main_models.ListSessionClustersRequest,
    ) -> main_models.ListSessionClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_session_clusters_with_options_async(workspace_id, request, headers, runtime)

    def list_sql_statement_contents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListSqlStatementContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSqlStatementContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSqlStatementContents',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/action/listSqlStatementContents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSqlStatementContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sql_statement_contents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListSqlStatementContentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSqlStatementContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSqlStatementContents',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/action/listSqlStatementContents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSqlStatementContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sql_statement_contents(
        self,
        workspace_id: str,
        request: main_models.ListSqlStatementContentsRequest,
    ) -> main_models.ListSqlStatementContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sql_statement_contents_with_options(workspace_id, request, headers, runtime)

    async def list_sql_statement_contents_async(
        self,
        workspace_id: str,
        request: main_models.ListSqlStatementContentsRequest,
    ) -> main_models.ListSqlStatementContentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sql_statement_contents_with_options_async(workspace_id, request, headers, runtime)

    def list_template_with_options(
        self,
        workspace_biz_id: str,
        request: main_models.ListTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplate',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/template/listing',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_with_options_async(
        self,
        workspace_biz_id: str,
        request: main_models.ListTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplate',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/template/listing',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template(
        self,
        workspace_biz_id: str,
        request: main_models.ListTemplateRequest,
    ) -> main_models.ListTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_template_with_options(workspace_biz_id, request, headers, runtime)

    async def list_template_async(
        self,
        workspace_biz_id: str,
        request: main_models.ListTemplateRequest,
    ) -> main_models.ListTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_template_with_options_async(workspace_biz_id, request, headers, runtime)

    def list_workspace_queues_with_options(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceQueuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['environment'] = request.environment
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceQueues',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/queues',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_queues_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceQueuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['environment'] = request.environment
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceQueues',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/queues',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_queues(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceQueuesRequest,
    ) -> main_models.ListWorkspaceQueuesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspace_queues_with_options(workspace_id, request, headers, runtime)

    async def list_workspace_queues_async(
        self,
        workspace_id: str,
        request: main_models.ListWorkspaceQueuesRequest,
    ) -> main_models.ListWorkspaceQueuesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspace_queues_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        tmp_req.validate()
        request = main_models.ListWorkspacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        tmp_req.validate()
        request = main_models.ListWorkspacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def refresh_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.RefreshLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.RefreshLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshLivyComputeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshLivyComputeToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.RefreshLivyComputeTokenRequest,
    ) -> main_models.RefreshLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.refresh_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def refresh_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: main_models.RefreshLivyComputeTokenRequest,
    ) -> main_models.RefreshLivyComputeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.refresh_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def start_job_run_with_options(
        self,
        workspace_id: str,
        request: main_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code_type):
            body['codeType'] = request.code_type
        if not DaraCore.is_null(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not DaraCore.is_null(request.job_id):
            body['jobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_run_with_options_async(
        self,
        workspace_id: str,
        request: main_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartJobRunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code_type):
            body['codeType'] = request.code_type
        if not DaraCore.is_null(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not DaraCore.is_null(request.job_id):
            body['jobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartJobRun',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/jobRuns',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_run(
        self,
        workspace_id: str,
        request: main_models.StartJobRunRequest,
    ) -> main_models.StartJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_job_run_with_options(workspace_id, request, headers, runtime)

    async def start_job_run_async(
        self,
        workspace_id: str,
        request: main_models.StartJobRunRequest,
    ) -> main_models.StartJobRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_job_run_with_options_async(workspace_id, request, headers, runtime)

    def start_kyuubi_service_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_kyuubi_service(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.StartKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    async def start_kyuubi_service_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.StartKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_kyuubi_service_with_options_async(workspace_id, kyuubi_service_id, headers, runtime)

    def start_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StartLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StartLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StartLivyComputeRequest,
    ) -> main_models.StartLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def start_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StartLivyComputeRequest,
    ) -> main_models.StartLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def start_process_instance_with_options(
        self,
        biz_id: str,
        request: main_models.StartProcessInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartProcessInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.comments):
            query['comments'] = request.comments
        if not DaraCore.is_null(request.email):
            query['email'] = request.email
        if not DaraCore.is_null(request.interval):
            query['interval'] = request.interval
        if not DaraCore.is_null(request.is_prod):
            query['isProd'] = request.is_prod
        if not DaraCore.is_null(request.process_definition_code):
            query['processDefinitionCode'] = request.process_definition_code
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.runtime_queue):
            query['runtimeQueue'] = request.runtime_queue
        if not DaraCore.is_null(request.version_hash_code):
            query['versionHashCode'] = request.version_hash_code
        if not DaraCore.is_null(request.version_number):
            query['versionNumber'] = request.version_number
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartProcessInstance',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/executors/start-process-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartProcessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_process_instance_with_options_async(
        self,
        biz_id: str,
        request: main_models.StartProcessInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartProcessInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.comments):
            query['comments'] = request.comments
        if not DaraCore.is_null(request.email):
            query['email'] = request.email
        if not DaraCore.is_null(request.interval):
            query['interval'] = request.interval
        if not DaraCore.is_null(request.is_prod):
            query['isProd'] = request.is_prod
        if not DaraCore.is_null(request.process_definition_code):
            query['processDefinitionCode'] = request.process_definition_code
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.runtime_queue):
            query['runtimeQueue'] = request.runtime_queue
        if not DaraCore.is_null(request.version_hash_code):
            query['versionHashCode'] = request.version_hash_code
        if not DaraCore.is_null(request.version_number):
            query['versionNumber'] = request.version_number
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartProcessInstance',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/executors/start-process-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartProcessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_process_instance(
        self,
        biz_id: str,
        request: main_models.StartProcessInstanceRequest,
    ) -> main_models.StartProcessInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_process_instance_with_options(biz_id, request, headers, runtime)

    async def start_process_instance_async(
        self,
        biz_id: str,
        request: main_models.StartProcessInstanceRequest,
    ) -> main_models.StartProcessInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_process_instance_with_options_async(biz_id, request, headers, runtime)

    def start_session_cluster_with_options(
        self,
        workspace_id: str,
        request: main_models.StartSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/action/startSessionCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: main_models.StartSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/action/startSessionCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_session_cluster(
        self,
        workspace_id: str,
        request: main_models.StartSessionClusterRequest,
    ) -> main_models.StartSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def start_session_cluster_async(
        self,
        workspace_id: str,
        request: main_models.StartSessionClusterRequest,
    ) -> main_models.StartSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def stop_kyuubi_service_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopKyuubiServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_kyuubi_service(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.StopKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_kyuubi_service_with_options(workspace_id, kyuubi_service_id, headers, runtime)

    async def stop_kyuubi_service_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
    ) -> main_models.StopKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_kyuubi_service_with_options_async(workspace_id, kyuubi_service_id, headers, runtime)

    def stop_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StopLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StopLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StopLivyComputeRequest,
    ) -> main_models.StopLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def stop_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.StopLivyComputeRequest,
    ) -> main_models.StopLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def stop_session_cluster_with_options(
        self,
        workspace_id: str,
        request: main_models.StopSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/action/stopSessionCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: main_models.StopSessionClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSessionClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopSessionCluster',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/sessionClusters/action/stopSessionCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_session_cluster(
        self,
        workspace_id: str,
        request: main_models.StopSessionClusterRequest,
    ) -> main_models.StopSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def stop_session_cluster_async(
        self,
        workspace_id: str,
        request: main_models.StopSessionClusterRequest,
    ) -> main_models.StopSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def terminate_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TerminateSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement/{DaraURL.percent_encode(statement_id)}/terminate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TerminateSqlStatementResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TerminateSqlStatement',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_id)}/statement/{DaraURL.percent_encode(statement_id)}/terminate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.TerminateSqlStatementRequest,
    ) -> main_models.TerminateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.terminate_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def terminate_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: main_models.TerminateSqlStatementRequest,
    ) -> main_models.TerminateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.terminate_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)

    def update_kyuubi_service_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.UpdateKyuubiServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKyuubiServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not DaraCore.is_null(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not DaraCore.is_null(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue):
            body['queue'] = request.queue
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.replica):
            body['replica'] = request.replica
        if not DaraCore.is_null(request.restart):
            body['restart'] = request.restart
        if not DaraCore.is_null(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKyuubiServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kyuubi_service_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.UpdateKyuubiServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKyuubiServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compute_instance):
            body['computeInstance'] = request.compute_instance
        if not DaraCore.is_null(request.kyuubi_configs):
            body['kyuubiConfigs'] = request.kyuubi_configs
        if not DaraCore.is_null(request.kyuubi_release_version):
            body['kyuubiReleaseVersion'] = request.kyuubi_release_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not DaraCore.is_null(request.queue):
            body['queue'] = request.queue
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        if not DaraCore.is_null(request.replica):
            body['replica'] = request.replica
        if not DaraCore.is_null(request.restart):
            body['restart'] = request.restart
        if not DaraCore.is_null(request.spark_configs):
            body['sparkConfigs'] = request.spark_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKyuubiService',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/kyuubi/{DaraURL.percent_encode(workspace_id)}/{DaraURL.percent_encode(kyuubi_service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKyuubiServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kyuubi_service(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.UpdateKyuubiServiceRequest,
    ) -> main_models.UpdateKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_kyuubi_service_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def update_kyuubi_service_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: main_models.UpdateKyuubiServiceRequest,
    ) -> main_models.UpdateKyuubiServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_kyuubi_service_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def update_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.UpdateKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.UpdateKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKyuubiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not DaraCore.is_null(request.member_arns):
            body['memberArns'] = request.member_arns
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.token):
            body['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKyuubiToken',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/v1/workspaces/{DaraURL.percent_encode(workspace_id)}/kyuubiService/{DaraURL.percent_encode(kyuubi_service_id)}/token/{DaraURL.percent_encode(token_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.UpdateKyuubiTokenRequest,
    ) -> main_models.UpdateKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_kyuubi_token_with_options(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    async def update_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        token_id: str,
        request: main_models.UpdateKyuubiTokenRequest,
    ) -> main_models.UpdateKyuubiTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, token_id, request, headers, runtime)

    def update_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.UpdateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auth_type):
            body['authType'] = request.auth_type
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not DaraCore.is_null(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not DaraCore.is_null(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_name):
            body['networkName'] = request.network_name
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.UpdateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLivyComputeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auth_type):
            body['authType'] = request.auth_type
        if not DaraCore.is_null(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not DaraCore.is_null(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not DaraCore.is_null(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not DaraCore.is_null(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.fusion):
            body['fusion'] = request.fusion
        if not DaraCore.is_null(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not DaraCore.is_null(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not DaraCore.is_null(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_name):
            body['networkName'] = request.network_name
        if not DaraCore.is_null(request.queue_name):
            body['queueName'] = request.queue_name
        if not DaraCore.is_null(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLivyCompute',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/api/interactive/v1/workspace/{DaraURL.percent_encode(workspace_biz_id)}/livycompute/{DaraURL.percent_encode(livy_compute_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.UpdateLivyComputeRequest,
    ) -> main_models.UpdateLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def update_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: main_models.UpdateLivyComputeRequest,
    ) -> main_models.UpdateLivyComputeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def update_process_definition_with_schedule_with_options(
        self,
        biz_id: str,
        code: str,
        tmp_req: main_models.UpdateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProcessDefinitionWithScheduleResponse:
        tmp_req.validate()
        request = main_models.UpdateProcessDefinitionWithScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_params):
            request.global_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not DaraCore.is_null(tmp_req.task_definition_json):
            request.task_definition_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not DaraCore.is_null(tmp_req.task_relation_json):
            request.task_relation_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.execution_type):
            query['executionType'] = request.execution_type
        if not DaraCore.is_null(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.publish):
            query['publish'] = request.publish
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.release_state):
            query['releaseState'] = request.release_state
        if not DaraCore.is_null(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not DaraCore.is_null(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not DaraCore.is_null(request.run_as):
            query['runAs'] = request.run_as
        if not DaraCore.is_null(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not DaraCore.is_null(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not DaraCore.is_null(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not DaraCore.is_null(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProcessDefinitionWithSchedule',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/process-definition/{DaraURL.percent_encode(code)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_process_definition_with_schedule_with_options_async(
        self,
        biz_id: str,
        code: str,
        tmp_req: main_models.UpdateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProcessDefinitionWithScheduleResponse:
        tmp_req.validate()
        request = main_models.UpdateProcessDefinitionWithScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.global_params):
            request.global_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not DaraCore.is_null(tmp_req.task_definition_json):
            request.task_definition_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not DaraCore.is_null(tmp_req.task_relation_json):
            request.task_relation_json_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not DaraCore.is_null(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.execution_type):
            query['executionType'] = request.execution_type
        if not DaraCore.is_null(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not DaraCore.is_null(request.publish):
            query['publish'] = request.publish
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.release_state):
            query['releaseState'] = request.release_state
        if not DaraCore.is_null(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not DaraCore.is_null(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not DaraCore.is_null(request.run_as):
            query['runAs'] = request.run_as
        if not DaraCore.is_null(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not DaraCore.is_null(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not DaraCore.is_null(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not DaraCore.is_null(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProcessDefinitionWithSchedule',
            version = '2023-08-08',
            protocol = 'HTTPS',
            pathname = f'/dolphinscheduler/projects/{DaraURL.percent_encode(biz_id)}/process-definition/{DaraURL.percent_encode(code)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProcessDefinitionWithScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_process_definition_with_schedule(
        self,
        biz_id: str,
        code: str,
        request: main_models.UpdateProcessDefinitionWithScheduleRequest,
    ) -> main_models.UpdateProcessDefinitionWithScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_process_definition_with_schedule_with_options(biz_id, code, request, headers, runtime)

    async def update_process_definition_with_schedule_async(
        self,
        biz_id: str,
        code: str,
        request: main_models.UpdateProcessDefinitionWithScheduleRequest,
    ) -> main_models.UpdateProcessDefinitionWithScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_process_definition_with_schedule_with_options_async(biz_id, code, request, headers, runtime)
