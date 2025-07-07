# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr_serverless_spark20230808 import models as emr_serverless_spark_20230808_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_members_with_options(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.AddMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_members_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.AddMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_members(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @return: AddMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_members_with_options(request, headers, runtime)

    async def add_members_async(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @return: AddMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_members_with_options_async(request, headers, runtime)

    def cancel_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @return: CancelJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def cancel_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @return: CancelJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def create_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeResponse:
        """
        @summary 创建Livy compute
        
        @param request: CreateLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeResponse:
        """
        @summary 创建Livy compute
        
        @param request: CreateLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_livy_compute(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeResponse:
        """
        @summary 创建Livy compute
        
        @param request: CreateLivyComputeRequest
        @return: CreateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    async def create_livy_compute_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeResponse:
        """
        @summary 创建Livy compute
        
        @param request: CreateLivyComputeRequest
        @return: CreateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_livy_compute_with_options_async(workspace_biz_id, request, headers, runtime)

    def create_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse:
        """
        @summary 创建Livy Compute的token
        
        @param request: CreateLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse:
        """
        @summary 创建Livy Compute的token
        
        @param request: CreateLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse:
        """
        @summary 创建Livy Compute的token
        
        @param request: CreateLivyComputeTokenRequest
        @return: CreateLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def create_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.CreateLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.CreateLivyComputeTokenResponse:
        """
        @summary 创建Livy Compute的token
        
        @param request: CreateLivyComputeTokenRequest
        @return: CreateLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def create_process_definition_with_schedule_with_options(
        self,
        biz_id: str,
        tmp_req: emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse:
        """
        @summary Creates a workflow.
        
        @param tmp_req: CreateProcessDefinitionWithScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/process-definition',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_process_definition_with_schedule_with_options_async(
        self,
        biz_id: str,
        tmp_req: emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse:
        """
        @summary Creates a workflow.
        
        @param tmp_req: CreateProcessDefinitionWithScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/process-definition',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_process_definition_with_schedule(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleRequest,
    ) -> emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse:
        """
        @summary Creates a workflow.
        
        @param request: CreateProcessDefinitionWithScheduleRequest
        @return: CreateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_process_definition_with_schedule_with_options(biz_id, request, headers, runtime)

    async def create_process_definition_with_schedule_async(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleRequest,
    ) -> emr_serverless_spark_20230808_models.CreateProcessDefinitionWithScheduleResponse:
        """
        @summary Creates a workflow.
        
        @param request: CreateProcessDefinitionWithScheduleRequest
        @return: CreateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_process_definition_with_schedule_with_options_async(biz_id, request, headers, runtime)

    def create_session_cluster_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSessionClusterResponse:
        """
        @summary Creates a session.
        
        @param request: CreateSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.application_configs):
            body['applicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.kind):
            body['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSessionClusterResponse:
        """
        @summary Creates a session.
        
        @param request: CreateSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.application_configs):
            body['applicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.kind):
            body['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            body['publicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session_cluster(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSessionClusterResponse:
        """
        @summary Creates a session.
        
        @param request: CreateSessionClusterRequest
        @return: CreateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def create_session_cluster_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSessionClusterResponse:
        """
        @summary Creates a session.
        
        @param request: CreateSessionClusterRequest
        @return: CreateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def create_sql_statement_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary Creates an SQL query task.
        
        @param request: CreateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.code_content):
            body['codeContent'] = request.code_content
        if not UtilClient.is_unset(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not UtilClient.is_unset(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_statement_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary Creates an SQL query task.
        
        @param request: CreateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.code_content):
            body['codeContent'] = request.code_content
        if not UtilClient.is_unset(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not UtilClient.is_unset(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_statement(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary Creates an SQL query task.
        
        @param request: CreateSqlStatementRequest
        @return: CreateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sql_statement_with_options(workspace_id, request, headers, runtime)

    async def create_sql_statement_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary Creates an SQL query task.
        
        @param request: CreateSqlStatementRequest
        @return: CreateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sql_statement_with_options_async(workspace_id, request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: emr_serverless_spark_20230808_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_renew_period_unit):
            body['autoRenewPeriodUnit'] = request.auto_renew_period_unit
        if not UtilClient.is_unset(request.auto_start_session_cluster):
            body['autoStartSessionCluster'] = request.auto_start_session_cluster
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dlf_catalog_id):
            body['dlfCatalogId'] = request.dlf_catalog_id
        if not UtilClient.is_unset(request.dlf_type):
            body['dlfType'] = request.dlf_type
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.oss_bucket):
            body['ossBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.ram_role_name):
            body['ramRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.release_type):
            body['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        if not UtilClient.is_unset(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkspaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_renew_period_unit):
            body['autoRenewPeriodUnit'] = request.auto_renew_period_unit
        if not UtilClient.is_unset(request.auto_start_session_cluster):
            body['autoStartSessionCluster'] = request.auto_start_session_cluster
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dlf_catalog_id):
            body['dlfCatalogId'] = request.dlf_catalog_id
        if not UtilClient.is_unset(request.dlf_type):
            body['dlfType'] = request.dlf_type
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.oss_bucket):
            body['ossBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.ram_role_name):
            body['ramRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.release_type):
            body['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        if not UtilClient.is_unset(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: emr_serverless_spark_20230808_models.CreateWorkspaceRequest,
    ) -> emr_serverless_spark_20230808_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: emr_serverless_spark_20230808_models.CreateWorkspaceRequest,
    ) -> emr_serverless_spark_20230808_models.CreateWorkspaceResponse:
        """
        @summary Creates a workspace.
        
        @param request: CreateWorkspaceRequest
        @return: CreateWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def delete_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeResponse:
        """
        @summary 删除livy compute
        
        @param request: DeleteLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeResponse:
        """
        @summary 删除livy compute
        
        @param request: DeleteLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeResponse:
        """
        @summary 删除livy compute
        
        @param request: DeleteLivyComputeRequest
        @return: DeleteLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def delete_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeResponse:
        """
        @summary 删除livy compute
        
        @param request: DeleteLivyComputeRequest
        @return: DeleteLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def delete_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse:
        """
        @summary 删除Livy Compute的token
        
        @param request: DeleteLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse:
        """
        @summary 删除Livy Compute的token
        
        @param request: DeleteLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse:
        """
        @summary 删除Livy Compute的token
        
        @param request: DeleteLivyComputeTokenRequest
        @return: DeleteLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def delete_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.DeleteLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.DeleteLivyComputeTokenResponse:
        """
        @summary 删除Livy Compute的token
        
        @param request: DeleteLivyComputeTokenRequest
        @return: DeleteLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def edit_workspace_queue_with_options(
        self,
        request: emr_serverless_spark_20230808_models.EditWorkspaceQueueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse:
        """
        @summary Modifies the queue of a workspace.
        
        @param request: EditWorkspaceQueueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditWorkspaceQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.environments):
            body['environments'] = request.environments
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_queue_name):
            body['workspaceQueueName'] = request.workspace_queue_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditWorkspaceQueue',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/queues/action/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_workspace_queue_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.EditWorkspaceQueueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse:
        """
        @summary Modifies the queue of a workspace.
        
        @param request: EditWorkspaceQueueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditWorkspaceQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.environments):
            body['environments'] = request.environments
        if not UtilClient.is_unset(request.resource_spec):
            body['resourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_queue_name):
            body['workspaceQueueName'] = request.workspace_queue_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditWorkspaceQueue',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/queues/action/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_workspace_queue(
        self,
        request: emr_serverless_spark_20230808_models.EditWorkspaceQueueRequest,
    ) -> emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse:
        """
        @summary Modifies the queue of a workspace.
        
        @param request: EditWorkspaceQueueRequest
        @return: EditWorkspaceQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edit_workspace_queue_with_options(request, headers, runtime)

    async def edit_workspace_queue_async(
        self,
        request: emr_serverless_spark_20230808_models.EditWorkspaceQueueRequest,
    ) -> emr_serverless_spark_20230808_models.EditWorkspaceQueueResponse:
        """
        @summary Modifies the queue of a workspace.
        
        @param request: EditWorkspaceQueueRequest
        @return: EditWorkspaceQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.edit_workspace_queue_with_options_async(request, headers, runtime)

    def get_cu_hours_with_options(
        self,
        workspace_id: str,
        queue: str,
        request: emr_serverless_spark_20230808_models.GetCuHoursRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetCuHoursResponse:
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        
        @param request: GetCuHoursRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCuHoursResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCuHours',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/metric/cuHours/{OpenApiUtilClient.get_encode_param(queue)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetCuHoursResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cu_hours_with_options_async(
        self,
        workspace_id: str,
        queue: str,
        request: emr_serverless_spark_20230808_models.GetCuHoursRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetCuHoursResponse:
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        
        @param request: GetCuHoursRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCuHoursResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCuHours',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/metric/cuHours/{OpenApiUtilClient.get_encode_param(queue)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetCuHoursResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cu_hours(
        self,
        workspace_id: str,
        queue: str,
        request: emr_serverless_spark_20230808_models.GetCuHoursRequest,
    ) -> emr_serverless_spark_20230808_models.GetCuHoursResponse:
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        
        @param request: GetCuHoursRequest
        @return: GetCuHoursResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cu_hours_with_options(workspace_id, queue, request, headers, runtime)

    async def get_cu_hours_async(
        self,
        workspace_id: str,
        queue: str,
        request: emr_serverless_spark_20230808_models.GetCuHoursRequest,
    ) -> emr_serverless_spark_20230808_models.GetCuHoursResponse:
        """
        @summary Queries the number of CU-hours consumed by a queue during a specified cycle.
        
        @param request: GetCuHoursRequest
        @return: GetCuHoursResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cu_hours_with_options_async(workspace_id, queue, request, headers, runtime)

    def get_doctor_application_with_options(
        self,
        workspace_id: str,
        run_id: str,
        request: emr_serverless_spark_20230808_models.GetDoctorApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @param request: GetDoctorApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['locale'] = request.locale
        if not UtilClient.is_unset(request.query_time):
            query['queryTime'] = request.query_time
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/runs/{OpenApiUtilClient.get_encode_param(run_id)}/action/getDoctorApplication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_application_with_options_async(
        self,
        workspace_id: str,
        run_id: str,
        request: emr_serverless_spark_20230808_models.GetDoctorApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @param request: GetDoctorApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['locale'] = request.locale
        if not UtilClient.is_unset(request.query_time):
            query['queryTime'] = request.query_time
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/runs/{OpenApiUtilClient.get_encode_param(run_id)}/action/getDoctorApplication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetDoctorApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_application(
        self,
        workspace_id: str,
        run_id: str,
        request: emr_serverless_spark_20230808_models.GetDoctorApplicationRequest,
    ) -> emr_serverless_spark_20230808_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @param request: GetDoctorApplicationRequest
        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_doctor_application_with_options(workspace_id, run_id, request, headers, runtime)

    async def get_doctor_application_async(
        self,
        workspace_id: str,
        run_id: str,
        request: emr_serverless_spark_20230808_models.GetDoctorApplicationRequest,
    ) -> emr_serverless_spark_20230808_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @param request: GetDoctorApplicationRequest
        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_doctor_application_with_options_async(workspace_id, run_id, request, headers, runtime)

    def get_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @return: GetJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def get_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @return: GetJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def get_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeResponse:
        """
        @summary 获取livy compute
        
        @param request: GetLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeResponse:
        """
        @summary 获取livy compute
        
        @param request: GetLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeResponse:
        """
        @summary 获取livy compute
        
        @param request: GetLivyComputeRequest
        @return: GetLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def get_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeResponse:
        """
        @summary 获取livy compute
        
        @param request: GetLivyComputeRequest
        @return: GetLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def get_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse:
        """
        @summary 获取livy compute token
        
        @param request: GetLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse:
        """
        @summary 获取livy compute token
        
        @param request: GetLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse:
        """
        @summary 获取livy compute token
        
        @param request: GetLivyComputeTokenRequest
        @return: GetLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def get_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.GetLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.GetLivyComputeTokenResponse:
        """
        @summary 获取livy compute token
        
        @param request: GetLivyComputeTokenRequest
        @return: GetLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def get_session_cluster_with_options(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: emr_serverless_spark_20230808_models.GetSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSessionClusterResponse:
        """
        @summary Queries the information about a session.
        
        @param request: GetSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/{OpenApiUtilClient.get_encode_param(session_cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_cluster_with_options_async(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: emr_serverless_spark_20230808_models.GetSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSessionClusterResponse:
        """
        @summary Queries the information about a session.
        
        @param request: GetSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/{OpenApiUtilClient.get_encode_param(session_cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_cluster(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: emr_serverless_spark_20230808_models.GetSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.GetSessionClusterResponse:
        """
        @summary Queries the information about a session.
        
        @param request: GetSessionClusterRequest
        @return: GetSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_session_cluster_with_options(workspace_id, session_cluster_id, request, headers, runtime)

    async def get_session_cluster_async(
        self,
        workspace_id: str,
        session_cluster_id: str,
        request: emr_serverless_spark_20230808_models.GetSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.GetSessionClusterResponse:
        """
        @summary Queries the information about a session.
        
        @param request: GetSessionClusterRequest
        @return: GetSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_session_cluster_with_options_async(workspace_id, session_cluster_id, request, headers, runtime)

    def get_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary Queries the status of an SQL query task.
        
        @param request: GetSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary Queries the status of an SQL query task.
        
        @param request: GetSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary Queries the status of an SQL query task.
        
        @param request: GetSqlStatementRequest
        @return: GetSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def get_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary Queries the status of an SQL query task.
        
        @param request: GetSqlStatementRequest
        @return: GetSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)

    def get_template_with_options(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetTemplateResponse:
        """
        @summary Queries task templates.
        
        @param request: GetTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.template_biz_id):
            query['templateBizId'] = request.template_biz_id
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetTemplateResponse:
        """
        @summary Queries task templates.
        
        @param request: GetTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.template_biz_id):
            query['templateBizId'] = request.template_biz_id
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.GetTemplateRequest,
    ) -> emr_serverless_spark_20230808_models.GetTemplateResponse:
        """
        @summary Queries task templates.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(workspace_biz_id, request, headers, runtime)

    async def get_template_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.GetTemplateRequest,
    ) -> emr_serverless_spark_20230808_models.GetTemplateResponse:
        """
        @summary Queries task templates.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(workspace_biz_id, request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def list_job_runs_with_options(
        self,
        workspace_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param tmp_req: ListJobRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobRunsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.is_workflow):
            query['isWorkflow'] = request.is_workflow
        if not UtilClient.is_unset(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_runs_with_options_async(
        self,
        workspace_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param tmp_req: ListJobRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobRunsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.is_workflow):
            query['isWorkflow'] = request.is_workflow
        if not UtilClient.is_unset(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_runs(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListJobRunsRequest,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param request: ListJobRunsRequest
        @return: ListJobRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_runs_with_options(workspace_id, request, headers, runtime)

    async def list_job_runs_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListJobRunsRequest,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param request: ListJobRunsRequest
        @return: ListJobRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_runs_with_options_async(workspace_id, request, headers, runtime)

    def list_kyuubi_services_with_options(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiServicesResponse:
        """
        @summary ListKyuubiServices
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiServicesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListKyuubiServices',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/kyuubi/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_services_with_options_async(
        self,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiServicesResponse:
        """
        @summary ListKyuubiServices
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiServicesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListKyuubiServices',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/kyuubi/{OpenApiUtilClient.get_encode_param(workspace_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_services(
        self,
        workspace_id: str,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiServicesResponse:
        """
        @summary ListKyuubiServices
        
        @return: ListKyuubiServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_services_with_options(workspace_id, headers, runtime)

    async def list_kyuubi_services_async(
        self,
        workspace_id: str,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiServicesResponse:
        """
        @summary ListKyuubiServices
        
        @return: ListKyuubiServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_services_with_options_async(workspace_id, headers, runtime)

    def list_kyuubi_spark_applications_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse:
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        
        @param tmp_req: ListKyuubiSparkApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiSparkApplicationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'orderBy', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['applicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_name):
            query['applicationName'] = request.application_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_shrink):
            query['orderBy'] = request.order_by_shrink
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiSparkApplications',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/kyuubi/{OpenApiUtilClient.get_encode_param(workspace_id)}/{OpenApiUtilClient.get_encode_param(kyuubi_service_id)}/applications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_spark_applications_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse:
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        
        @param tmp_req: ListKyuubiSparkApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiSparkApplicationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'orderBy', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['applicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_name):
            query['applicationName'] = request.application_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.min_duration):
            query['minDuration'] = request.min_duration
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_shrink):
            query['orderBy'] = request.order_by_shrink
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiSparkApplications',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/kyuubi/{OpenApiUtilClient.get_encode_param(workspace_id)}/{OpenApiUtilClient.get_encode_param(kyuubi_service_id)}/applications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_spark_applications(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsRequest,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse:
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        
        @param request: ListKyuubiSparkApplicationsRequest
        @return: ListKyuubiSparkApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_spark_applications_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def list_kyuubi_spark_applications_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsRequest,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiSparkApplicationsResponse:
        """
        @summary Queries the applications that are submitted by using a Kyuubi gateway.
        
        @param request: ListKyuubiSparkApplicationsRequest
        @return: ListKyuubiSparkApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_spark_applications_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_kyuubi_token_with_options(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiTokenResponse:
        """
        @summary 列出compute的token
        
        @param request: ListKyuubiTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/kyuubiService/{OpenApiUtilClient.get_encode_param(kyuubi_service_id)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kyuubi_token_with_options_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiTokenResponse:
        """
        @summary 列出compute的token
        
        @param request: ListKyuubiTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKyuubiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKyuubiToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/kyuubiService/{OpenApiUtilClient.get_encode_param(kyuubi_service_id)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListKyuubiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kyuubi_token(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiTokenRequest,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiTokenResponse:
        """
        @summary 列出compute的token
        
        @param request: ListKyuubiTokenRequest
        @return: ListKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kyuubi_token_with_options(workspace_id, kyuubi_service_id, request, headers, runtime)

    async def list_kyuubi_token_async(
        self,
        workspace_id: str,
        kyuubi_service_id: str,
        request: emr_serverless_spark_20230808_models.ListKyuubiTokenRequest,
    ) -> emr_serverless_spark_20230808_models.ListKyuubiTokenResponse:
        """
        @summary 列出compute的token
        
        @param request: ListKyuubiTokenRequest
        @return: ListKyuubiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_kyuubi_token_with_options_async(workspace_id, kyuubi_service_id, request, headers, runtime)

    def list_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeResponse:
        """
        @summary 列出livy compute
        
        @param request: ListLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeResponse:
        """
        @summary 列出livy compute
        
        @param request: ListLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_livy_compute(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeResponse:
        """
        @summary 列出livy compute
        
        @param request: ListLivyComputeRequest
        @return: ListLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_livy_compute_with_options(workspace_biz_id, request, headers, runtime)

    async def list_livy_compute_async(
        self,
        workspace_biz_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeResponse:
        """
        @summary 列出livy compute
        
        @param request: ListLivyComputeRequest
        @return: ListLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_livy_compute_with_options_async(workspace_biz_id, request, headers, runtime)

    def list_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse:
        """
        @summary 列出livy compute token
        
        @param request: ListLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse:
        """
        @summary 列出livy compute token
        
        @param request: ListLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse:
        """
        @summary 列出livy compute token
        
        @param request: ListLivyComputeTokenRequest
        @return: ListLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def list_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.ListLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.ListLivyComputeTokenResponse:
        """
        @summary 列出livy compute token
        
        @param request: ListLivyComputeTokenRequest
        @return: ListLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def list_log_contents_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListLogContentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLogContentsResponse:
        """
        @summary Get Log Content
        
        @param request: ListLogContentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.length):
            query['length'] = request.length
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogContents',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/action/listLogContents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLogContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_contents_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListLogContentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListLogContentsResponse:
        """
        @summary Get Log Content
        
        @param request: ListLogContentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogContentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.length):
            query['length'] = request.length
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogContents',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/action/listLogContents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListLogContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_contents(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListLogContentsRequest,
    ) -> emr_serverless_spark_20230808_models.ListLogContentsResponse:
        """
        @summary Get Log Content
        
        @param request: ListLogContentsRequest
        @return: ListLogContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_contents_with_options(workspace_id, request, headers, runtime)

    async def list_log_contents_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListLogContentsRequest,
    ) -> emr_serverless_spark_20230808_models.ListLogContentsResponse:
        """
        @summary Get Log Content
        
        @param request: ListLogContentsRequest
        @return: ListLogContentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_log_contents_with_options_async(workspace_id, request, headers, runtime)

    def list_release_versions_with_options(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        
        @param request: ListReleaseVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_type):
            query['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.release_version):
            query['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        if not UtilClient.is_unset(request.service_filter):
            query['serviceFilter'] = request.service_filter
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/releaseVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_release_versions_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        
        @param request: ListReleaseVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_type):
            query['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.release_version):
            query['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        if not UtilClient.is_unset(request.service_filter):
            query['serviceFilter'] = request.service_filter
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/releaseVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListReleaseVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_release_versions(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_release_versions_with_options(request, headers, runtime)

    async def list_release_versions_async(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary Queries the list of published versions of E-MapReduce (EMR) Serverless Spark.
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_release_versions_with_options_async(request, headers, runtime)

    def list_session_clusters_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary Queries the list of sessions.
        
        @param request: ListSessionClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.queue_name):
            query['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_clusters_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary Queries the list of sessions.
        
        @param request: ListSessionClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.queue_name):
            query['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSessionClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_clusters(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary Queries the list of sessions.
        
        @param request: ListSessionClustersRequest
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_session_clusters_with_options(workspace_id, request, headers, runtime)

    async def list_session_clusters_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary Queries the list of sessions.
        
        @param request: ListSessionClustersRequest
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_session_clusters_with_options_async(workspace_id, request, headers, runtime)

    def list_workspace_queues_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary Queries the list of queues in a Spark workspace.
        
        @param request: ListWorkspaceQueuesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceQueuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceQueues',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/queues',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_queues_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary Queries the list of queues in a Spark workspace.
        
        @param request: ListWorkspaceQueuesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceQueuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceQueues',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/queues',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_queues(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary Queries the list of queues in a Spark workspace.
        
        @param request: ListWorkspaceQueuesRequest
        @return: ListWorkspaceQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspace_queues_with_options(workspace_id, request, headers, runtime)

    async def list_workspace_queues_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary Queries the list of queues in a Spark workspace.
        
        @param request: ListWorkspaceQueuesRequest
        @return: ListWorkspaceQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspace_queues_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def refresh_livy_compute_token_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.RefreshLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse:
        """
        @summary 更新Livy Compute的token
        
        @param request: RefreshLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_livy_compute_token_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.RefreshLivyComputeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse:
        """
        @summary 更新Livy Compute的token
        
        @param request: RefreshLivyComputeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshLivyComputeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_expire_configuration):
            body['autoExpireConfiguration'] = request.auto_expire_configuration
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshLivyComputeToken',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/token/{OpenApiUtilClient.get_encode_param(token_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_livy_compute_token(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.RefreshLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse:
        """
        @summary 更新Livy Compute的token
        
        @param request: RefreshLivyComputeTokenRequest
        @return: RefreshLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_livy_compute_token_with_options(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    async def refresh_livy_compute_token_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        token_id: str,
        request: emr_serverless_spark_20230808_models.RefreshLivyComputeTokenRequest,
    ) -> emr_serverless_spark_20230808_models.RefreshLivyComputeTokenResponse:
        """
        @summary 更新Livy Compute的token
        
        @param request: RefreshLivyComputeTokenRequest
        @return: RefreshLivyComputeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refresh_livy_compute_token_with_options_async(workspace_biz_id, livy_compute_id, token_id, request, headers, runtime)

    def start_job_run_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_run_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_run(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @return: StartJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_job_run_with_options(workspace_id, request, headers, runtime)

    async def start_job_run_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @return: StartJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_job_run_with_options_async(workspace_id, request, headers, runtime)

    def start_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StartLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartLivyComputeResponse:
        """
        @summary 启动livy compute
        
        @param request: StartLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StartLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartLivyComputeResponse:
        """
        @summary 启动livy compute
        
        @param request: StartLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StartLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.StartLivyComputeResponse:
        """
        @summary 启动livy compute
        
        @param request: StartLivyComputeRequest
        @return: StartLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def start_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StartLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.StartLivyComputeResponse:
        """
        @summary 启动livy compute
        
        @param request: StartLivyComputeRequest
        @return: StartLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def start_process_instance_with_options(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.StartProcessInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartProcessInstanceResponse:
        """
        @summary Manually runs a workflow.
        
        @param request: StartProcessInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProcessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.comments):
            query['comments'] = request.comments
        if not UtilClient.is_unset(request.email):
            query['email'] = request.email
        if not UtilClient.is_unset(request.interval):
            query['interval'] = request.interval
        if not UtilClient.is_unset(request.is_prod):
            query['isProd'] = request.is_prod
        if not UtilClient.is_unset(request.process_definition_code):
            query['processDefinitionCode'] = request.process_definition_code
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.runtime_queue):
            query['runtimeQueue'] = request.runtime_queue
        if not UtilClient.is_unset(request.version_hash_code):
            query['versionHashCode'] = request.version_hash_code
        if not UtilClient.is_unset(request.version_number):
            query['versionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartProcessInstance',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/executors/start-process-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartProcessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_process_instance_with_options_async(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.StartProcessInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartProcessInstanceResponse:
        """
        @summary Manually runs a workflow.
        
        @param request: StartProcessInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProcessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        if not UtilClient.is_unset(request.comments):
            query['comments'] = request.comments
        if not UtilClient.is_unset(request.email):
            query['email'] = request.email
        if not UtilClient.is_unset(request.interval):
            query['interval'] = request.interval
        if not UtilClient.is_unset(request.is_prod):
            query['isProd'] = request.is_prod
        if not UtilClient.is_unset(request.process_definition_code):
            query['processDefinitionCode'] = request.process_definition_code
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.runtime_queue):
            query['runtimeQueue'] = request.runtime_queue
        if not UtilClient.is_unset(request.version_hash_code):
            query['versionHashCode'] = request.version_hash_code
        if not UtilClient.is_unset(request.version_number):
            query['versionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartProcessInstance',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/executors/start-process-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartProcessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_process_instance(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.StartProcessInstanceRequest,
    ) -> emr_serverless_spark_20230808_models.StartProcessInstanceResponse:
        """
        @summary Manually runs a workflow.
        
        @param request: StartProcessInstanceRequest
        @return: StartProcessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_process_instance_with_options(biz_id, request, headers, runtime)

    async def start_process_instance_async(
        self,
        biz_id: str,
        request: emr_serverless_spark_20230808_models.StartProcessInstanceRequest,
    ) -> emr_serverless_spark_20230808_models.StartProcessInstanceResponse:
        """
        @summary Manually runs a workflow.
        
        @param request: StartProcessInstanceRequest
        @return: StartProcessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_process_instance_with_options_async(biz_id, request, headers, runtime)

    def start_session_cluster_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartSessionClusterResponse:
        """
        @summary Starts a session.
        
        @param request: StartSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/action/startSessionCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartSessionClusterResponse:
        """
        @summary Starts a session.
        
        @param request: StartSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/action/startSessionCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_session_cluster(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.StartSessionClusterResponse:
        """
        @summary Starts a session.
        
        @param request: StartSessionClusterRequest
        @return: StartSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def start_session_cluster_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.StartSessionClusterResponse:
        """
        @summary Starts a session.
        
        @param request: StartSessionClusterRequest
        @return: StartSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def stop_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StopLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StopLivyComputeResponse:
        """
        @summary 停止livy compute
        
        @param request: StopLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StopLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StopLivyComputeResponse:
        """
        @summary 停止livy compute
        
        @param request: StopLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StopLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.StopLivyComputeResponse:
        """
        @summary 停止livy compute
        
        @param request: StopLivyComputeRequest
        @return: StopLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def stop_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.StopLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.StopLivyComputeResponse:
        """
        @summary 停止livy compute
        
        @param request: StopLivyComputeRequest
        @return: StopLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def stop_session_cluster_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StopSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StopSessionClusterResponse:
        """
        @summary Stops a session.
        
        @param request: StopSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/action/stopSessionCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_session_cluster_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StopSessionClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StopSessionClusterResponse:
        """
        @summary Stops a session.
        
        @param request: StopSessionClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSessionClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.session_cluster_id):
            body['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopSessionCluster',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters/action/stopSessionCluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StopSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_session_cluster(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StopSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.StopSessionClusterResponse:
        """
        @summary Stops a session.
        
        @param request: StopSessionClusterRequest
        @return: StopSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_session_cluster_with_options(workspace_id, request, headers, runtime)

    async def stop_session_cluster_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StopSessionClusterRequest,
    ) -> emr_serverless_spark_20230808_models.StopSessionClusterResponse:
        """
        @summary Stops a session.
        
        @param request: StopSessionClusterRequest
        @return: StopSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_session_cluster_with_options_async(workspace_id, request, headers, runtime)

    def terminate_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary Terminates an SQL query task.
        
        @param request: TerminateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.TerminateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary Terminates an SQL query task.
        
        @param request: TerminateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.TerminateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary Terminates an SQL query task.
        
        @param request: TerminateSqlStatementRequest
        @return: TerminateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def terminate_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary Terminates an SQL query task.
        
        @param request: TerminateSqlStatementRequest
        @return: TerminateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.terminate_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)

    def update_livy_compute_with_options(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.UpdateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.UpdateLivyComputeResponse:
        """
        @summary 更新livy compute
        
        @param request: UpdateLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateLivyComputeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_livy_compute_with_options_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.UpdateLivyComputeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.UpdateLivyComputeResponse:
        """
        @summary 更新livy compute
        
        @param request: UpdateLivyComputeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLivyComputeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auth_type):
            body['authType'] = request.auth_type
        if not UtilClient.is_unset(request.auto_start_configuration):
            body['autoStartConfiguration'] = request.auto_start_configuration
        if not UtilClient.is_unset(request.auto_stop_configuration):
            body['autoStopConfiguration'] = request.auto_stop_configuration
        if not UtilClient.is_unset(request.cpu_limit):
            body['cpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.display_release_version):
            body['displayReleaseVersion'] = request.display_release_version
        if not UtilClient.is_unset(request.enable_public):
            body['enablePublic'] = request.enable_public
        if not UtilClient.is_unset(request.environment_id):
            body['environmentId'] = request.environment_id
        if not UtilClient.is_unset(request.fusion):
            body['fusion'] = request.fusion
        if not UtilClient.is_unset(request.livy_server_conf):
            body['livyServerConf'] = request.livy_server_conf
        if not UtilClient.is_unset(request.livy_version):
            body['livyVersion'] = request.livy_version
        if not UtilClient.is_unset(request.memory_limit):
            body['memoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.network_name):
            body['networkName'] = request.network_name
        if not UtilClient.is_unset(request.queue_name):
            body['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLivyCompute',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_biz_id)}/livycompute/{OpenApiUtilClient.get_encode_param(livy_compute_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateLivyComputeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_livy_compute(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.UpdateLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.UpdateLivyComputeResponse:
        """
        @summary 更新livy compute
        
        @param request: UpdateLivyComputeRequest
        @return: UpdateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_livy_compute_with_options(workspace_biz_id, livy_compute_id, request, headers, runtime)

    async def update_livy_compute_async(
        self,
        workspace_biz_id: str,
        livy_compute_id: str,
        request: emr_serverless_spark_20230808_models.UpdateLivyComputeRequest,
    ) -> emr_serverless_spark_20230808_models.UpdateLivyComputeResponse:
        """
        @summary 更新livy compute
        
        @param request: UpdateLivyComputeRequest
        @return: UpdateLivyComputeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_livy_compute_with_options_async(workspace_biz_id, livy_compute_id, request, headers, runtime)

    def update_process_definition_with_schedule_with_options(
        self,
        biz_id: str,
        code: str,
        tmp_req: emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse:
        """
        @summary Updates the workflow and time-based scheduling configurations.
        
        @param tmp_req: UpdateProcessDefinitionWithScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_state):
            query['releaseState'] = request.release_state
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/process-definition/{OpenApiUtilClient.get_encode_param(code)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_process_definition_with_schedule_with_options_async(
        self,
        biz_id: str,
        code: str,
        tmp_req: emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse:
        """
        @summary Updates the workflow and time-based scheduling configurations.
        
        @param tmp_req: UpdateProcessDefinitionWithScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_params):
            request.global_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_params, 'globalParams', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'schedule', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        if not UtilClient.is_unset(tmp_req.task_definition_json):
            request.task_definition_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_definition_json, 'taskDefinitionJson', 'json')
        if not UtilClient.is_unset(tmp_req.task_relation_json):
            request.task_relation_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_relation_json, 'taskRelationJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_email_address):
            query['alertEmailAddress'] = request.alert_email_address
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.global_params_shrink):
            query['globalParams'] = request.global_params_shrink
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.product_namespace):
            query['productNamespace'] = request.product_namespace
        if not UtilClient.is_unset(request.publish):
            query['publish'] = request.publish
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_state):
            query['releaseState'] = request.release_state
        if not UtilClient.is_unset(request.resource_queue):
            query['resourceQueue'] = request.resource_queue
        if not UtilClient.is_unset(request.retry_times):
            query['retryTimes'] = request.retry_times
        if not UtilClient.is_unset(request.run_as):
            query['runAs'] = request.run_as
        if not UtilClient.is_unset(request.schedule_shrink):
            query['schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_definition_json_shrink):
            query['taskDefinitionJson'] = request.task_definition_json_shrink
        if not UtilClient.is_unset(request.task_parallelism):
            query['taskParallelism'] = request.task_parallelism
        if not UtilClient.is_unset(request.task_relation_json_shrink):
            query['taskRelationJson'] = request.task_relation_json_shrink
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProcessDefinitionWithSchedule',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/projects/{OpenApiUtilClient.get_encode_param(biz_id)}/process-definition/{OpenApiUtilClient.get_encode_param(code)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_process_definition_with_schedule(
        self,
        biz_id: str,
        code: str,
        request: emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleRequest,
    ) -> emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse:
        """
        @summary Updates the workflow and time-based scheduling configurations.
        
        @param request: UpdateProcessDefinitionWithScheduleRequest
        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_process_definition_with_schedule_with_options(biz_id, code, request, headers, runtime)

    async def update_process_definition_with_schedule_async(
        self,
        biz_id: str,
        code: str,
        request: emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleRequest,
    ) -> emr_serverless_spark_20230808_models.UpdateProcessDefinitionWithScheduleResponse:
        """
        @summary Updates the workflow and time-based scheduling configurations.
        
        @param request: UpdateProcessDefinitionWithScheduleRequest
        @return: UpdateProcessDefinitionWithScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_process_definition_with_schedule_with_options_async(biz_id, code, request, headers, runtime)
