# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devs20230714 import models as devs_20230714_models
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
        self._endpoint = self.get_endpoint('devs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_connection_with_options(
        self,
        name: str,
        request: devs_20230714_models.ActivateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ActivateConnectionResponse:
        """
        @summary 激活身份绑定,完成OAuth授权
        
        @param request: ActivateConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['account'] = request.account
        if not UtilClient.is_unset(request.credential):
            body['credential'] = request.credential
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/activate',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ActivateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_connection_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.ActivateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ActivateConnectionResponse:
        """
        @summary 激活身份绑定,完成OAuth授权
        
        @param request: ActivateConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['account'] = request.account
        if not UtilClient.is_unset(request.credential):
            body['credential'] = request.credential
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/activate',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ActivateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_connection(
        self,
        name: str,
        request: devs_20230714_models.ActivateConnectionRequest,
    ) -> devs_20230714_models.ActivateConnectionResponse:
        """
        @summary 激活身份绑定,完成OAuth授权
        
        @param request: ActivateConnectionRequest
        @return: ActivateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.activate_connection_with_options(name, request, headers, runtime)

    async def activate_connection_async(
        self,
        name: str,
        request: devs_20230714_models.ActivateConnectionRequest,
    ) -> devs_20230714_models.ActivateConnectionResponse:
        """
        @summary 激活身份绑定,完成OAuth授权
        
        @param request: ActivateConnectionRequest
        @return: ActivateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.activate_connection_with_options_async(name, request, headers, runtime)

    def cancel_pipeline_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CancelPipelineResponse:
        """
        @summary 取消流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CancelPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_pipeline_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CancelPipelineResponse:
        """
        @summary 取消流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CancelPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_pipeline(
        self,
        name: str,
    ) -> devs_20230714_models.CancelPipelineResponse:
        """
        @summary 取消流水线
        
        @return: CancelPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_pipeline_with_options(name, headers, runtime)

    async def cancel_pipeline_async(
        self,
        name: str,
    ) -> devs_20230714_models.CancelPipelineResponse:
        """
        @summary 取消流水线
        
        @return: CancelPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_pipeline_with_options_async(name, headers, runtime)

    def cancel_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CancelTaskResponse:
        """
        @summary 取消任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CancelTaskResponse:
        """
        @summary 取消任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        name: str,
    ) -> devs_20230714_models.CancelTaskResponse:
        """
        @summary 取消任务
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(name, headers, runtime)

    async def cancel_task_async(
        self,
        name: str,
    ) -> devs_20230714_models.CancelTaskResponse:
        """
        @summary 取消任务
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(name, headers, runtime)

    def create_artifact_with_options(
        self,
        request: devs_20230714_models.CreateArtifactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateArtifactResponse:
        """
        @summary 创建交付物存储
        
        @param request: CreateArtifactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_with_options_async(
        self,
        request: devs_20230714_models.CreateArtifactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateArtifactResponse:
        """
        @summary 创建交付物存储
        
        @param request: CreateArtifactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact(
        self,
        request: devs_20230714_models.CreateArtifactRequest,
    ) -> devs_20230714_models.CreateArtifactResponse:
        """
        @summary 创建交付物存储
        
        @param request: CreateArtifactRequest
        @return: CreateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_artifact_with_options(request, headers, runtime)

    async def create_artifact_async(
        self,
        request: devs_20230714_models.CreateArtifactRequest,
    ) -> devs_20230714_models.CreateArtifactResponse:
        """
        @summary 创建交付物存储
        
        @param request: CreateArtifactRequest
        @return: CreateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_artifact_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        project_name: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        project_name: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        project_name: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(project_name, request, headers, runtime)

    async def create_environment_async(
        self,
        project_name: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(project_name, request, headers, runtime)

    def create_pipeline_with_options(
        self,
        request: devs_20230714_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineResponse:
        """
        @summary 创建流水线
        
        @param request: CreatePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        request: devs_20230714_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineResponse:
        """
        @summary 创建流水线
        
        @param request: CreatePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        request: devs_20230714_models.CreatePipelineRequest,
    ) -> devs_20230714_models.CreatePipelineResponse:
        """
        @summary 创建流水线
        
        @param request: CreatePipelineRequest
        @return: CreatePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(request, headers, runtime)

    async def create_pipeline_async(
        self,
        request: devs_20230714_models.CreatePipelineRequest,
    ) -> devs_20230714_models.CreatePipelineResponse:
        """
        @summary 创建流水线
        
        @param request: CreatePipelineRequest
        @return: CreatePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: devs_20230714_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: devs_20230714_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: devs_20230714_models.CreateProjectRequest,
    ) -> devs_20230714_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: devs_20230714_models.CreateProjectRequest,
    ) -> devs_20230714_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: devs_20230714_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: devs_20230714_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: devs_20230714_models.CreateTaskRequest,
    ) -> devs_20230714_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: devs_20230714_models.CreateTaskRequest,
    ) -> devs_20230714_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def create_toolset_with_options(
        self,
        request: devs_20230714_models.CreateToolsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateToolsetResponse:
        """
        @summary 创建工具集
        
        @param request: CreateToolsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateToolsetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateToolsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_toolset_with_options_async(
        self,
        request: devs_20230714_models.CreateToolsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateToolsetResponse:
        """
        @summary 创建工具集
        
        @param request: CreateToolsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateToolsetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateToolsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_toolset(
        self,
        request: devs_20230714_models.CreateToolsetRequest,
    ) -> devs_20230714_models.CreateToolsetResponse:
        """
        @summary 创建工具集
        
        @param request: CreateToolsetRequest
        @return: CreateToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_toolset_with_options(request, headers, runtime)

    async def create_toolset_async(
        self,
        request: devs_20230714_models.CreateToolsetRequest,
    ) -> devs_20230714_models.CreateToolsetResponse:
        """
        @summary 创建工具集
        
        @param request: CreateToolsetRequest
        @return: CreateToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_toolset_with_options_async(request, headers, runtime)

    def delete_artifact_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteArtifactResponse:
        """
        @summary 删除交付物
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteArtifactResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_artifact_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteArtifactResponse:
        """
        @summary 删除交付物
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteArtifactResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_artifact(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteArtifactResponse:
        """
        @summary 删除交付物
        
        @return: DeleteArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_artifact_with_options(name, headers, runtime)

    async def delete_artifact_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteArtifactResponse:
        """
        @summary 删除交付物
        
        @return: DeleteArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_artifact_with_options_async(name, headers, runtime)

    def delete_connection_with_options(
        self,
        name: str,
        request: devs_20230714_models.DeleteConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteConnectionResponse:
        """
        @summary 删除身份绑定
        
        @param request: DeleteConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_connection_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.DeleteConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteConnectionResponse:
        """
        @summary 删除身份绑定
        
        @param request: DeleteConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_connection(
        self,
        name: str,
        request: devs_20230714_models.DeleteConnectionRequest,
    ) -> devs_20230714_models.DeleteConnectionResponse:
        """
        @summary 删除身份绑定
        
        @param request: DeleteConnectionRequest
        @return: DeleteConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_connection_with_options(name, request, headers, runtime)

    async def delete_connection_async(
        self,
        name: str,
        request: devs_20230714_models.DeleteConnectionRequest,
    ) -> devs_20230714_models.DeleteConnectionResponse:
        """
        @summary 删除身份绑定
        
        @param request: DeleteConnectionRequest
        @return: DeleteConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_connection_with_options_async(name, request, headers, runtime)

    def delete_environment_with_options(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(project_name, name, headers, runtime)

    async def delete_environment_async(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(project_name, name, headers, runtime)

    def delete_project_with_options(
        self,
        name: str,
        request: devs_20230714_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        name: str,
        request: devs_20230714_models.DeleteProjectRequest,
    ) -> devs_20230714_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(name, request, headers, runtime)

    async def delete_project_async(
        self,
        name: str,
        request: devs_20230714_models.DeleteProjectRequest,
    ) -> devs_20230714_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(name, request, headers, runtime)

    def delete_toolset_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteToolsetResponse:
        """
        @summary 删除工具集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteToolsetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteToolsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_toolset_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteToolsetResponse:
        """
        @summary 删除工具集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteToolsetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteToolsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_toolset(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteToolsetResponse:
        """
        @summary 删除工具集
        
        @return: DeleteToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_toolset_with_options(name, headers, runtime)

    async def delete_toolset_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteToolsetResponse:
        """
        @summary 删除工具集
        
        @return: DeleteToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_toolset_with_options_async(name, headers, runtime)

    def deploy_environment_with_options(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.DeployEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeployEnvironmentResponse:
        """
        @summary 手动触发环境部署
        
        @param request: DeployEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DeployEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}/deploy',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeployEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_environment_with_options_async(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.DeployEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeployEnvironmentResponse:
        """
        @summary 手动触发环境部署
        
        @param request: DeployEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DeployEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}/deploy',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeployEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_environment(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.DeployEnvironmentRequest,
    ) -> devs_20230714_models.DeployEnvironmentResponse:
        """
        @summary 手动触发环境部署
        
        @param request: DeployEnvironmentRequest
        @return: DeployEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_environment_with_options(project_name, name, request, headers, runtime)

    async def deploy_environment_async(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.DeployEnvironmentRequest,
    ) -> devs_20230714_models.DeployEnvironmentResponse:
        """
        @summary 手动触发环境部署
        
        @param request: DeployEnvironmentRequest
        @return: DeployEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_environment_with_options_async(project_name, name, request, headers, runtime)

    def fetch_artifact_download_url_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchArtifactDownloadUrlResponse:
        """
        @summary 获取交付物的zip包临时下载地址url
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchArtifactDownloadUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchArtifactDownloadUrl',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}/fetchCode',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchArtifactDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_artifact_download_url_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchArtifactDownloadUrlResponse:
        """
        @summary 获取交付物的zip包临时下载地址url
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchArtifactDownloadUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchArtifactDownloadUrl',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}/fetchCode',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchArtifactDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_artifact_download_url(
        self,
        name: str,
    ) -> devs_20230714_models.FetchArtifactDownloadUrlResponse:
        """
        @summary 获取交付物的zip包临时下载地址url
        
        @return: FetchArtifactDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fetch_artifact_download_url_with_options(name, headers, runtime)

    async def fetch_artifact_download_url_async(
        self,
        name: str,
    ) -> devs_20230714_models.FetchArtifactDownloadUrlResponse:
        """
        @summary 获取交付物的zip包临时下载地址url
        
        @return: FetchArtifactDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.fetch_artifact_download_url_with_options_async(name, headers, runtime)

    def fetch_artifact_temp_bucket_token_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchArtifactTempBucketTokenResponse:
        """
        @summary 获取交付物临时上传的bucket、object和临时sts
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchArtifactTempBucketTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchArtifactTempBucketToken',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/action/fetchTempBucketToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchArtifactTempBucketTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_artifact_temp_bucket_token_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchArtifactTempBucketTokenResponse:
        """
        @summary 获取交付物临时上传的bucket、object和临时sts
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchArtifactTempBucketTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchArtifactTempBucketToken',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/action/fetchTempBucketToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchArtifactTempBucketTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_artifact_temp_bucket_token(self) -> devs_20230714_models.FetchArtifactTempBucketTokenResponse:
        """
        @summary 获取交付物临时上传的bucket、object和临时sts
        
        @return: FetchArtifactTempBucketTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fetch_artifact_temp_bucket_token_with_options(headers, runtime)

    async def fetch_artifact_temp_bucket_token_async(self) -> devs_20230714_models.FetchArtifactTempBucketTokenResponse:
        """
        @summary 获取交付物临时上传的bucket、object和临时sts
        
        @return: FetchArtifactTempBucketTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.fetch_artifact_temp_bucket_token_with_options_async(headers, runtime)

    def fetch_connection_credential_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchConnectionCredentialResponse:
        """
        @summary 查询身份绑定中的凭证信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchConnectionCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchConnectionCredential',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/fetchCredential',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchConnectionCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_connection_credential_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchConnectionCredentialResponse:
        """
        @summary 查询身份绑定中的凭证信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchConnectionCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FetchConnectionCredential',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/fetchCredential',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchConnectionCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_connection_credential(
        self,
        name: str,
    ) -> devs_20230714_models.FetchConnectionCredentialResponse:
        """
        @summary 查询身份绑定中的凭证信息
        
        @return: FetchConnectionCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fetch_connection_credential_with_options(name, headers, runtime)

    async def fetch_connection_credential_async(
        self,
        name: str,
    ) -> devs_20230714_models.FetchConnectionCredentialResponse:
        """
        @summary 查询身份绑定中的凭证信息
        
        @return: FetchConnectionCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.fetch_connection_credential_with_options_async(name, headers, runtime)

    def get_artifact_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetArtifactResponse:
        """
        @summary 查询交付物
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetArtifactResponse:
        """
        @summary 查询交付物
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact(
        self,
        name: str,
    ) -> devs_20230714_models.GetArtifactResponse:
        """
        @summary 查询交付物
        
        @return: GetArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_artifact_with_options(name, headers, runtime)

    async def get_artifact_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetArtifactResponse:
        """
        @summary 查询交付物
        
        @return: GetArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_artifact_with_options_async(name, headers, runtime)

    def get_environment_with_options(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(project_name, name, headers, runtime)

    async def get_environment_async(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(project_name, name, headers, runtime)

    def get_environment_deployment_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetEnvironmentDeploymentResponse:
        """
        @summary 查询环境部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentDeploymentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentDeployment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/environmentdeployments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetEnvironmentDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_deployment_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetEnvironmentDeploymentResponse:
        """
        @summary 查询环境部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnvironmentDeploymentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentDeployment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/environmentdeployments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetEnvironmentDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment_deployment(
        self,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentDeploymentResponse:
        """
        @summary 查询环境部署信息
        
        @return: GetEnvironmentDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_deployment_with_options(name, headers, runtime)

    async def get_environment_deployment_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentDeploymentResponse:
        """
        @summary 查询环境部署信息
        
        @return: GetEnvironmentDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_deployment_with_options_async(name, headers, runtime)

    def get_pipeline_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineResponse:
        """
        @summary 查询流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineResponse:
        """
        @summary 查询流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineResponse:
        """
        @summary 查询流水线
        
        @return: GetPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(name, headers, runtime)

    async def get_pipeline_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineResponse:
        """
        @summary 查询流水线
        
        @return: GetPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(name, headers, runtime)

    def get_project_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        name: str,
    ) -> devs_20230714_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(name, headers, runtime)

    async def get_project_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(name, headers, runtime)

    def get_repository_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetRepositoryResponse:
        """
        @summary 查询仓库绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRepositoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetRepositoryResponse:
        """
        @summary 查询仓库绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRepositoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository(
        self,
        name: str,
    ) -> devs_20230714_models.GetRepositoryResponse:
        """
        @summary 查询仓库绑定
        
        @return: GetRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repository_with_options(name, headers, runtime)

    async def get_repository_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetRepositoryResponse:
        """
        @summary 查询仓库绑定
        
        @return: GetRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_repository_with_options_async(name, headers, runtime)

    def get_service_deployment_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetServiceDeploymentResponse:
        """
        @summary 查询服务部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDeploymentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceDeployment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/servicedeployments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetServiceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_deployment_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetServiceDeploymentResponse:
        """
        @summary 查询服务部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDeploymentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceDeployment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/servicedeployments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetServiceDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_deployment(
        self,
        name: str,
    ) -> devs_20230714_models.GetServiceDeploymentResponse:
        """
        @summary 查询服务部署信息
        
        @return: GetServiceDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_deployment_with_options(name, headers, runtime)

    async def get_service_deployment_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetServiceDeploymentResponse:
        """
        @summary 查询服务部署信息
        
        @return: GetServiceDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_deployment_with_options_async(name, headers, runtime)

    def get_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetTaskResponse:
        """
        @summary 查询任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetTaskResponse:
        """
        @summary 查询任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        name: str,
    ) -> devs_20230714_models.GetTaskResponse:
        """
        @summary 查询任务
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(name, headers, runtime)

    async def get_task_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetTaskResponse:
        """
        @summary 查询任务
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(name, headers, runtime)

    def get_toolset_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetToolsetResponse:
        """
        @summary 查询工具集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetToolsetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetToolsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_toolset_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetToolsetResponse:
        """
        @summary 查询工具集
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetToolsetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetToolsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_toolset(
        self,
        name: str,
    ) -> devs_20230714_models.GetToolsetResponse:
        """
        @summary 查询工具集
        
        @return: GetToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_toolset_with_options(name, headers, runtime)

    async def get_toolset_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetToolsetResponse:
        """
        @summary 查询工具集
        
        @return: GetToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_toolset_with_options_async(name, headers, runtime)

    def list_connections_with_options(
        self,
        tmp_req: devs_20230714_models.ListConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListConnectionsResponse:
        """
        @summary 批量查询身份绑定
        
        @param tmp_req: ListConnectionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListConnectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnections',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connections_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListConnectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListConnectionsResponse:
        """
        @summary 批量查询身份绑定
        
        @param tmp_req: ListConnectionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListConnectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnections',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connections(
        self,
        request: devs_20230714_models.ListConnectionsRequest,
    ) -> devs_20230714_models.ListConnectionsResponse:
        """
        @summary 批量查询身份绑定
        
        @param request: ListConnectionsRequest
        @return: ListConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_connections_with_options(request, headers, runtime)

    async def list_connections_async(
        self,
        request: devs_20230714_models.ListConnectionsRequest,
    ) -> devs_20230714_models.ListConnectionsResponse:
        """
        @summary 批量查询身份绑定
        
        @param request: ListConnectionsRequest
        @return: ListConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_connections_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        project_name: str,
        tmp_req: devs_20230714_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param tmp_req: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        project_name: str,
        tmp_req: devs_20230714_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param tmp_req: ListEnvironmentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnvironmentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        project_name: str,
        request: devs_20230714_models.ListEnvironmentsRequest,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(project_name, request, headers, runtime)

    async def list_environments_async(
        self,
        project_name: str,
        request: devs_20230714_models.ListEnvironmentsRequest,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(project_name, request, headers, runtime)

    def list_pipelines_with_options(
        self,
        tmp_req: devs_20230714_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelinesResponse:
        """
        @summary 批量查询流水线
        
        @param tmp_req: ListPipelinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelinesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelinesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelinesResponse:
        """
        @summary 批量查询流水线
        
        @param tmp_req: ListPipelinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelinesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelinesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        request: devs_20230714_models.ListPipelinesRequest,
    ) -> devs_20230714_models.ListPipelinesResponse:
        """
        @summary 批量查询流水线
        
        @param request: ListPipelinesRequest
        @return: ListPipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(request, headers, runtime)

    async def list_pipelines_async(
        self,
        request: devs_20230714_models.ListPipelinesRequest,
    ) -> devs_20230714_models.ListPipelinesResponse:
        """
        @summary 批量查询流水线
        
        @param request: ListPipelinesRequest
        @return: ListPipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(request, headers, runtime)

    def list_projects_with_options(
        self,
        tmp_req: devs_20230714_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListProjectsResponse:
        """
        @summary 批量查询项目
        
        @param tmp_req: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListProjectsResponse:
        """
        @summary 批量查询项目
        
        @param tmp_req: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: devs_20230714_models.ListProjectsRequest,
    ) -> devs_20230714_models.ListProjectsResponse:
        """
        @summary 批量查询项目
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: devs_20230714_models.ListProjectsRequest,
    ) -> devs_20230714_models.ListProjectsResponse:
        """
        @summary 批量查询项目
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_service_deployments_with_options(
        self,
        tmp_req: devs_20230714_models.ListServiceDeploymentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListServiceDeploymentsResponse:
        """
        @summary 批量查询服务部署信息
        
        @param tmp_req: ListServiceDeploymentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceDeploymentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListServiceDeploymentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceDeployments',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/servicedeployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListServiceDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_deployments_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListServiceDeploymentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListServiceDeploymentsResponse:
        """
        @summary 批量查询服务部署信息
        
        @param tmp_req: ListServiceDeploymentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceDeploymentsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListServiceDeploymentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceDeployments',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/servicedeployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListServiceDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_deployments(
        self,
        request: devs_20230714_models.ListServiceDeploymentsRequest,
    ) -> devs_20230714_models.ListServiceDeploymentsResponse:
        """
        @summary 批量查询服务部署信息
        
        @param request: ListServiceDeploymentsRequest
        @return: ListServiceDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_deployments_with_options(request, headers, runtime)

    async def list_service_deployments_async(
        self,
        request: devs_20230714_models.ListServiceDeploymentsRequest,
    ) -> devs_20230714_models.ListServiceDeploymentsResponse:
        """
        @summary 批量查询服务部署信息
        
        @param request: ListServiceDeploymentsRequest
        @return: ListServiceDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_deployments_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: devs_20230714_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListTasksResponse:
        """
        @summary 批量查询任务
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListTasksResponse:
        """
        @summary 批量查询任务
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: devs_20230714_models.ListTasksRequest,
    ) -> devs_20230714_models.ListTasksResponse:
        """
        @summary 批量查询任务
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: devs_20230714_models.ListTasksRequest,
    ) -> devs_20230714_models.ListTasksResponse:
        """
        @summary 批量查询任务
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_toolsets_with_options(
        self,
        tmp_req: devs_20230714_models.ListToolsetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListToolsetsResponse:
        """
        @summary 批量查询工具集
        
        @param tmp_req: ListToolsetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListToolsetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListToolsetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListToolsets',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListToolsetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_toolsets_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListToolsetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListToolsetsResponse:
        """
        @summary 批量查询工具集
        
        @param tmp_req: ListToolsetsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListToolsetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListToolsetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListToolsets',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListToolsetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_toolsets(
        self,
        request: devs_20230714_models.ListToolsetsRequest,
    ) -> devs_20230714_models.ListToolsetsResponse:
        """
        @summary 批量查询工具集
        
        @param request: ListToolsetsRequest
        @return: ListToolsetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_toolsets_with_options(request, headers, runtime)

    async def list_toolsets_async(
        self,
        request: devs_20230714_models.ListToolsetsRequest,
    ) -> devs_20230714_models.ListToolsetsResponse:
        """
        @summary 批量查询工具集
        
        @param request: ListToolsetsRequest
        @return: ListToolsetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_toolsets_with_options_async(request, headers, runtime)

    def preview_environment_with_options(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PreviewEnvironmentResponse:
        """
        @summary 预览环境变更信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PreviewEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}/preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PreviewEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_environment_with_options_async(
        self,
        project_name: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PreviewEnvironmentResponse:
        """
        @summary 预览环境变更信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewEnvironmentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PreviewEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}/preview',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PreviewEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_environment(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.PreviewEnvironmentResponse:
        """
        @summary 预览环境变更信息
        
        @return: PreviewEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_environment_with_options(project_name, name, headers, runtime)

    async def preview_environment_async(
        self,
        project_name: str,
        name: str,
    ) -> devs_20230714_models.PreviewEnvironmentResponse:
        """
        @summary 预览环境变更信息
        
        @return: PreviewEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.preview_environment_with_options_async(project_name, name, headers, runtime)

    def put_artifact_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutArtifactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutArtifactResponse:
        """
        @summary 更新交付物
        
        @param request: PutArtifactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_artifact_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutArtifactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutArtifactResponse:
        """
        @summary 更新交付物
        
        @param request: PutArtifactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutArtifact',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/artifacts/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_artifact(
        self,
        name: str,
        request: devs_20230714_models.PutArtifactRequest,
    ) -> devs_20230714_models.PutArtifactResponse:
        """
        @summary 更新交付物
        
        @param request: PutArtifactRequest
        @return: PutArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_artifact_with_options(name, request, headers, runtime)

    async def put_artifact_async(
        self,
        name: str,
        request: devs_20230714_models.PutArtifactRequest,
    ) -> devs_20230714_models.PutArtifactResponse:
        """
        @summary 更新交付物
        
        @param request: PutArtifactRequest
        @return: PutArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_artifact_with_options_async(name, request, headers, runtime)

    def put_pipeline_status_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineStatusResponse:
        """
        @summary 更新流水线状态
        
        @param request: PutPipelineStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutPipelineStatus',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_pipeline_status_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineStatusResponse:
        """
        @summary 更新流水线状态
        
        @param request: PutPipelineStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutPipelineStatus',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_pipeline_status(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineStatusRequest,
    ) -> devs_20230714_models.PutPipelineStatusResponse:
        """
        @summary 更新流水线状态
        
        @param request: PutPipelineStatusRequest
        @return: PutPipelineStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_status_with_options(name, request, headers, runtime)

    async def put_pipeline_status_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineStatusRequest,
    ) -> devs_20230714_models.PutPipelineStatusResponse:
        """
        @summary 更新流水线状态
        
        @param request: PutPipelineStatusRequest
        @return: PutPipelineStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_pipeline_status_with_options_async(name, request, headers, runtime)

    def put_task_status_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutTaskStatusResponse:
        """
        @summary 更新替换任务状态
        
        @param request: PutTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutTaskStatus',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_task_status_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutTaskStatusResponse:
        """
        @summary 更新替换任务状态
        
        @param request: PutTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutTaskStatus',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_task_status(
        self,
        name: str,
        request: devs_20230714_models.PutTaskStatusRequest,
    ) -> devs_20230714_models.PutTaskStatusResponse:
        """
        @summary 更新替换任务状态
        
        @param request: PutTaskStatusRequest
        @return: PutTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_status_with_options(name, request, headers, runtime)

    async def put_task_status_async(
        self,
        name: str,
        request: devs_20230714_models.PutTaskStatusRequest,
    ) -> devs_20230714_models.PutTaskStatusResponse:
        """
        @summary 更新替换任务状态
        
        @param request: PutTaskStatusRequest
        @return: PutTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_task_status_with_options_async(name, request, headers, runtime)

    def render_services_by_template_with_options(
        self,
        request: devs_20230714_models.RenderServicesByTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RenderServicesByTemplateResponse:
        """
        @summary 解析模板中的服务、变量配置
        
        @param request: RenderServicesByTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderServicesByTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.service_name_changes):
            body['serviceNameChanges'] = request.service_name_changes
        if not UtilClient.is_unset(request.template_name):
            body['templateName'] = request.template_name
        if not UtilClient.is_unset(request.variable_values):
            body['variableValues'] = request.variable_values
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenderServicesByTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/templates/action/renderServices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RenderServicesByTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_services_by_template_with_options_async(
        self,
        request: devs_20230714_models.RenderServicesByTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RenderServicesByTemplateResponse:
        """
        @summary 解析模板中的服务、变量配置
        
        @param request: RenderServicesByTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderServicesByTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.service_name_changes):
            body['serviceNameChanges'] = request.service_name_changes
        if not UtilClient.is_unset(request.template_name):
            body['templateName'] = request.template_name
        if not UtilClient.is_unset(request.variable_values):
            body['variableValues'] = request.variable_values
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenderServicesByTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/templates/action/renderServices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RenderServicesByTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_services_by_template(
        self,
        request: devs_20230714_models.RenderServicesByTemplateRequest,
    ) -> devs_20230714_models.RenderServicesByTemplateResponse:
        """
        @summary 解析模板中的服务、变量配置
        
        @param request: RenderServicesByTemplateRequest
        @return: RenderServicesByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.render_services_by_template_with_options(request, headers, runtime)

    async def render_services_by_template_async(
        self,
        request: devs_20230714_models.RenderServicesByTemplateRequest,
    ) -> devs_20230714_models.RenderServicesByTemplateResponse:
        """
        @summary 解析模板中的服务、变量配置
        
        @param request: RenderServicesByTemplateRequest
        @return: RenderServicesByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.render_services_by_template_with_options_async(request, headers, runtime)

    def resume_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ResumeTaskResponse:
        """
        @summary 确认并继续执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ResumeTaskResponse:
        """
        @summary 确认并继续执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ResumeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task(
        self,
        name: str,
    ) -> devs_20230714_models.ResumeTaskResponse:
        """
        @summary 确认并继续执行任务
        
        @return: ResumeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(name, headers, runtime)

    async def resume_task_async(
        self,
        name: str,
    ) -> devs_20230714_models.ResumeTaskResponse:
        """
        @summary 确认并继续执行任务
        
        @return: ResumeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_task_with_options_async(name, headers, runtime)

    def retry_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RetryTaskResponse:
        """
        @summary 重试执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RetryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RetryTaskResponse:
        """
        @summary 重试执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/retry',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RetryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_task(
        self,
        name: str,
    ) -> devs_20230714_models.RetryTaskResponse:
        """
        @summary 重试执行任务
        
        @return: RetryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_task_with_options(name, headers, runtime)

    async def retry_task_async(
        self,
        name: str,
    ) -> devs_20230714_models.RetryTaskResponse:
        """
        @summary 重试执行任务
        
        @return: RetryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_task_with_options_async(name, headers, runtime)

    def start_pipeline_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.StartPipelineResponse:
        """
        @summary 开始执行流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.StartPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.StartPipelineResponse:
        """
        @summary 开始执行流水线
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipeline',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelines/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.StartPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline(
        self,
        name: str,
    ) -> devs_20230714_models.StartPipelineResponse:
        """
        @summary 开始执行流水线
        
        @return: StartPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_with_options(name, headers, runtime)

    async def start_pipeline_async(
        self,
        name: str,
    ) -> devs_20230714_models.StartPipelineResponse:
        """
        @summary 开始执行流水线
        
        @return: StartPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_with_options_async(name, headers, runtime)

    def start_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.StartTaskResponse:
        """
        @summary 开始执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.StartTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.StartTaskResponse:
        """
        @summary 开始执行任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasks/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.StartTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task(
        self,
        name: str,
    ) -> devs_20230714_models.StartTaskResponse:
        """
        @summary 开始执行任务
        
        @return: StartTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_task_with_options(name, headers, runtime)

    async def start_task_async(
        self,
        name: str,
    ) -> devs_20230714_models.StartTaskResponse:
        """
        @summary 开始执行任务
        
        @return: StartTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_task_with_options_async(name, headers, runtime)

    def update_environment_with_options(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateEnvironmentResponse:
        """
        @summary 更新环境（局部更新）
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateEnvironmentResponse:
        """
        @summary 更新环境（局部更新）
        
        @param request: UpdateEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEnvironmentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project_name)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.UpdateEnvironmentRequest,
    ) -> devs_20230714_models.UpdateEnvironmentResponse:
        """
        @summary 更新环境（局部更新）
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(project_name, name, request, headers, runtime)

    async def update_environment_async(
        self,
        project_name: str,
        name: str,
        request: devs_20230714_models.UpdateEnvironmentRequest,
    ) -> devs_20230714_models.UpdateEnvironmentResponse:
        """
        @summary 更新环境（局部更新）
        
        @param request: UpdateEnvironmentRequest
        @return: UpdateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(project_name, name, request, headers, runtime)

    def update_project_with_options(
        self,
        name: str,
        request: devs_20230714_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        name: str,
        request: devs_20230714_models.UpdateProjectRequest,
    ) -> devs_20230714_models.UpdateProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(name, request, headers, runtime)

    async def update_project_async(
        self,
        name: str,
        request: devs_20230714_models.UpdateProjectRequest,
    ) -> devs_20230714_models.UpdateProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(name, request, headers, runtime)

    def update_toolset_with_options(
        self,
        name: str,
        request: devs_20230714_models.UpdateToolsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateToolsetResponse:
        """
        @summary 更新工具集
        
        @param request: UpdateToolsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateToolsetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateToolsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_toolset_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.UpdateToolsetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdateToolsetResponse:
        """
        @summary 更新工具集
        
        @param request: UpdateToolsetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateToolsetResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateToolset',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/toolsets/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdateToolsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_toolset(
        self,
        name: str,
        request: devs_20230714_models.UpdateToolsetRequest,
    ) -> devs_20230714_models.UpdateToolsetResponse:
        """
        @summary 更新工具集
        
        @param request: UpdateToolsetRequest
        @return: UpdateToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_toolset_with_options(name, request, headers, runtime)

    async def update_toolset_async(
        self,
        name: str,
        request: devs_20230714_models.UpdateToolsetRequest,
    ) -> devs_20230714_models.UpdateToolsetResponse:
        """
        @summary 更新工具集
        
        @param request: UpdateToolsetRequest
        @return: UpdateToolsetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_toolset_with_options_async(name, request, headers, runtime)
