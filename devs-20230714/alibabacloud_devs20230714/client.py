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

    def create_connection_with_options(
        self,
        request: devs_20230714_models.CreateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateConnectionResponse:
        """
        @summary 创建身份绑定
        
        @param request: CreateConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnectionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_connection_with_options_async(
        self,
        request: devs_20230714_models.CreateConnectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateConnectionResponse:
        """
        @summary 创建身份绑定
        
        @param request: CreateConnectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnectionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_connection(
        self,
        request: devs_20230714_models.CreateConnectionRequest,
    ) -> devs_20230714_models.CreateConnectionResponse:
        """
        @summary 创建身份绑定
        
        @param request: CreateConnectionRequest
        @return: CreateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_connection_with_options(request, headers, runtime)

    async def create_connection_async(
        self,
        request: devs_20230714_models.CreateConnectionRequest,
    ) -> devs_20230714_models.CreateConnectionResponse:
        """
        @summary 创建身份绑定
        
        @param request: CreateConnectionRequest
        @return: CreateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_connection_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments',
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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments',
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
        project: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(project, request, headers, runtime)

    async def create_environment_async(
        self,
        project: str,
        request: devs_20230714_models.CreateEnvironmentRequest,
    ) -> devs_20230714_models.CreateEnvironmentResponse:
        """
        @summary 创建环境
        
        @param request: CreateEnvironmentRequest
        @return: CreateEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(project, request, headers, runtime)

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

    def create_pipeline_template_with_options(
        self,
        request: devs_20230714_models.CreatePipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTemplateResponse:
        """
        @summary 创建流水线模板
        
        @param request: CreatePipelineTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_template_with_options_async(
        self,
        request: devs_20230714_models.CreatePipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTemplateResponse:
        """
        @summary 创建流水线模板
        
        @param request: CreatePipelineTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_template(
        self,
        request: devs_20230714_models.CreatePipelineTemplateRequest,
    ) -> devs_20230714_models.CreatePipelineTemplateResponse:
        """
        @summary 创建流水线模板
        
        @param request: CreatePipelineTemplateRequest
        @return: CreatePipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_template_with_options(request, headers, runtime)

    async def create_pipeline_template_async(
        self,
        request: devs_20230714_models.CreatePipelineTemplateRequest,
    ) -> devs_20230714_models.CreatePipelineTemplateResponse:
        """
        @summary 创建流水线模板
        
        @param request: CreatePipelineTemplateRequest
        @return: CreatePipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_template_with_options_async(request, headers, runtime)

    def create_pipeline_trigger_with_options(
        self,
        request: devs_20230714_models.CreatePipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTriggerResponse:
        """
        @summary 创建流水线触发器
        
        @param request: CreatePipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_trigger_with_options_async(
        self,
        request: devs_20230714_models.CreatePipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTriggerResponse:
        """
        @summary 创建流水线触发器
        
        @param request: CreatePipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_trigger(
        self,
        request: devs_20230714_models.CreatePipelineTriggerRequest,
    ) -> devs_20230714_models.CreatePipelineTriggerResponse:
        """
        @summary 创建流水线触发器
        
        @param request: CreatePipelineTriggerRequest
        @return: CreatePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_trigger_with_options(request, headers, runtime)

    async def create_pipeline_trigger_async(
        self,
        request: devs_20230714_models.CreatePipelineTriggerRequest,
    ) -> devs_20230714_models.CreatePipelineTriggerResponse:
        """
        @summary 创建流水线触发器
        
        @param request: CreatePipelineTriggerRequest
        @return: CreatePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_trigger_with_options_async(request, headers, runtime)

    def create_pipeline_trigger_event_with_options(
        self,
        request: devs_20230714_models.CreatePipelineTriggerEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTriggerEventResponse:
        """
        @summary 创建流水线触发历史
        
        @param request: CreatePipelineTriggerEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTriggerEventResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTriggerEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_trigger_event_with_options_async(
        self,
        request: devs_20230714_models.CreatePipelineTriggerEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreatePipelineTriggerEventResponse:
        """
        @summary 创建流水线触发历史
        
        @param request: CreatePipelineTriggerEventRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineTriggerEventResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreatePipelineTriggerEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_trigger_event(
        self,
        request: devs_20230714_models.CreatePipelineTriggerEventRequest,
    ) -> devs_20230714_models.CreatePipelineTriggerEventResponse:
        """
        @summary 创建流水线触发历史
        
        @param request: CreatePipelineTriggerEventRequest
        @return: CreatePipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_trigger_event_with_options(request, headers, runtime)

    async def create_pipeline_trigger_event_async(
        self,
        request: devs_20230714_models.CreatePipelineTriggerEventRequest,
    ) -> devs_20230714_models.CreatePipelineTriggerEventResponse:
        """
        @summary 创建流水线触发历史
        
        @param request: CreatePipelineTriggerEventRequest
        @return: CreatePipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_trigger_event_with_options_async(request, headers, runtime)

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

    def create_repository_with_options(
        self,
        request: devs_20230714_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateRepositoryResponse:
        """
        @summary 创建仓库绑定
        
        @param request: CreateRepositoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRepositoryResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: devs_20230714_models.CreateRepositoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateRepositoryResponse:
        """
        @summary 创建仓库绑定
        
        @param request: CreateRepositoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRepositoryResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository(
        self,
        request: devs_20230714_models.CreateRepositoryRequest,
    ) -> devs_20230714_models.CreateRepositoryResponse:
        """
        @summary 创建仓库绑定
        
        @param request: CreateRepositoryRequest
        @return: CreateRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repository_with_options(request, headers, runtime)

    async def create_repository_async(
        self,
        request: devs_20230714_models.CreateRepositoryRequest,
    ) -> devs_20230714_models.CreateRepositoryResponse:
        """
        @summary 创建仓库绑定
        
        @param request: CreateRepositoryRequest
        @return: CreateRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_repository_with_options_async(request, headers, runtime)

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

    def create_task_template_with_options(
        self,
        request: devs_20230714_models.CreateTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateTaskTemplateResponse:
        """
        @summary 创建任务模板
        
        @param request: CreateTaskTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_template_with_options_async(
        self,
        request: devs_20230714_models.CreateTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.CreateTaskTemplateResponse:
        """
        @summary 创建任务模板
        
        @param request: CreateTaskTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskTemplateResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.CreateTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_template(
        self,
        request: devs_20230714_models.CreateTaskTemplateRequest,
    ) -> devs_20230714_models.CreateTaskTemplateResponse:
        """
        @summary 创建任务模板
        
        @param request: CreateTaskTemplateRequest
        @return: CreateTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_template_with_options(request, headers, runtime)

    async def create_task_template_async(
        self,
        request: devs_20230714_models.CreateTaskTemplateRequest,
    ) -> devs_20230714_models.CreateTaskTemplateResponse:
        """
        @summary 创建任务模板
        
        @param request: CreateTaskTemplateRequest
        @return: CreateTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_template_with_options_async(request, headers, runtime)

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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
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
        project: str,
        name: str,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(project, name, headers, runtime)

    async def delete_environment_async(
        self,
        project: str,
        name: str,
    ) -> devs_20230714_models.DeleteEnvironmentResponse:
        """
        @summary 删除环境
        
        @return: DeleteEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(project, name, headers, runtime)

    def delete_pipeline_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTemplateResponse:
        """
        @summary 删除流水线模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTemplateResponse:
        """
        @summary 删除流水线模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_template(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTemplateResponse:
        """
        @summary 删除流水线模板
        
        @return: DeletePipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_template_with_options(name, headers, runtime)

    async def delete_pipeline_template_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTemplateResponse:
        """
        @summary 删除流水线模板
        
        @return: DeletePipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_template_with_options_async(name, headers, runtime)

    def delete_pipeline_trigger_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTriggerResponse:
        """
        @summary 删除流水线触发器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_trigger_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTriggerResponse:
        """
        @summary 删除流水线触发器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_trigger(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTriggerResponse:
        """
        @summary 删除流水线触发器
        
        @return: DeletePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_trigger_with_options(name, headers, runtime)

    async def delete_pipeline_trigger_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTriggerResponse:
        """
        @summary 删除流水线触发器
        
        @return: DeletePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_trigger_with_options_async(name, headers, runtime)

    def delete_pipeline_trigger_event_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTriggerEventResponse:
        """
        @summary 删除流水线触发历史
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTriggerEventResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTriggerEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_trigger_event_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeletePipelineTriggerEventResponse:
        """
        @summary 删除流水线触发历史
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineTriggerEventResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeletePipelineTriggerEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_trigger_event(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTriggerEventResponse:
        """
        @summary 删除流水线触发历史
        
        @return: DeletePipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_trigger_event_with_options(name, headers, runtime)

    async def delete_pipeline_trigger_event_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeletePipelineTriggerEventResponse:
        """
        @summary 删除流水线触发历史
        
        @return: DeletePipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_trigger_event_with_options_async(name, headers, runtime)

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
            body_type='json'
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
            body_type='json'
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

    def delete_repository_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteRepositoryResponse:
        """
        @summary 删除仓库绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRepositoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteRepositoryResponse:
        """
        @summary 删除仓库绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRepositoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteRepositoryResponse:
        """
        @summary 删除仓库绑定
        
        @return: DeleteRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repository_with_options(name, headers, runtime)

    async def delete_repository_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteRepositoryResponse:
        """
        @summary 删除仓库绑定
        
        @return: DeleteRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_repository_with_options_async(name, headers, runtime)

    def delete_task_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteTaskTemplateResponse:
        """
        @summary 删除任务模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.DeleteTaskTemplateResponse:
        """
        @summary 删除任务模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.DeleteTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task_template(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteTaskTemplateResponse:
        """
        @summary 删除任务模板
        
        @return: DeleteTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_template_with_options(name, headers, runtime)

    async def delete_task_template_async(
        self,
        name: str,
    ) -> devs_20230714_models.DeleteTaskTemplateResponse:
        """
        @summary 删除任务模板
        
        @return: DeleteTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_task_template_with_options_async(name, headers, runtime)

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

    def fetch_repository_checkout_with_options(
        self,
        name: str,
        request: devs_20230714_models.FetchRepositoryCheckoutRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchRepositoryCheckoutResponse:
        """
        @summary 查询仓库代码拉取所需信息
        
        @param request: FetchRepositoryCheckoutRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchRepositoryCheckoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.branch):
            query['branch'] = request.branch
        if not UtilClient.is_unset(request.commit):
            query['commit'] = request.commit
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchRepositoryCheckout',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}/fetchCheckout',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchRepositoryCheckoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_repository_checkout_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.FetchRepositoryCheckoutRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.FetchRepositoryCheckoutResponse:
        """
        @summary 查询仓库代码拉取所需信息
        
        @param request: FetchRepositoryCheckoutRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchRepositoryCheckoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.branch):
            query['branch'] = request.branch
        if not UtilClient.is_unset(request.commit):
            query['commit'] = request.commit
        if not UtilClient.is_unset(request.tag):
            query['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchRepositoryCheckout',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories/{OpenApiUtilClient.get_encode_param(name)}/fetchCheckout',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.FetchRepositoryCheckoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_repository_checkout(
        self,
        name: str,
        request: devs_20230714_models.FetchRepositoryCheckoutRequest,
    ) -> devs_20230714_models.FetchRepositoryCheckoutResponse:
        """
        @summary 查询仓库代码拉取所需信息
        
        @param request: FetchRepositoryCheckoutRequest
        @return: FetchRepositoryCheckoutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fetch_repository_checkout_with_options(name, request, headers, runtime)

    async def fetch_repository_checkout_async(
        self,
        name: str,
        request: devs_20230714_models.FetchRepositoryCheckoutRequest,
    ) -> devs_20230714_models.FetchRepositoryCheckoutResponse:
        """
        @summary 查询仓库代码拉取所需信息
        
        @param request: FetchRepositoryCheckoutRequest
        @return: FetchRepositoryCheckoutResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.fetch_repository_checkout_with_options_async(name, request, headers, runtime)

    def get_connection_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetConnectionResponse:
        """
        @summary 查询身份绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetConnectionResponse:
        """
        @summary 查询身份绑定
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection(
        self,
        name: str,
    ) -> devs_20230714_models.GetConnectionResponse:
        """
        @summary 查询身份绑定
        
        @return: GetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_connection_with_options(name, headers, runtime)

    async def get_connection_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetConnectionResponse:
        """
        @summary 查询身份绑定
        
        @return: GetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_connection_with_options_async(name, headers, runtime)

    def get_environment_with_options(
        self,
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
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
        project: str,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(project, name, headers, runtime)

    async def get_environment_async(
        self,
        project: str,
        name: str,
    ) -> devs_20230714_models.GetEnvironmentResponse:
        """
        @summary 获取环境信息
        
        @return: GetEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(project, name, headers, runtime)

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

    def get_pipeline_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTemplateResponse:
        """
        @summary 查询流水线模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTemplateResponse:
        """
        @summary 查询流水线模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_template(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTemplateResponse:
        """
        @summary 查询流水线模板
        
        @return: GetPipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_template_with_options(name, headers, runtime)

    async def get_pipeline_template_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTemplateResponse:
        """
        @summary 查询流水线模板
        
        @return: GetPipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_template_with_options_async(name, headers, runtime)

    def get_pipeline_trigger_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTriggerResponse:
        """
        @summary 查询流水线触发器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_trigger_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTriggerResponse:
        """
        @summary 查询流水线触发器
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_trigger(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTriggerResponse:
        """
        @summary 查询流水线触发器
        
        @return: GetPipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_trigger_with_options(name, headers, runtime)

    async def get_pipeline_trigger_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTriggerResponse:
        """
        @summary 查询流水线触发器
        
        @return: GetPipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_trigger_with_options_async(name, headers, runtime)

    def get_pipeline_trigger_event_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTriggerEventResponse:
        """
        @summary 查询流水线触发历史
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTriggerEventResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTriggerEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_trigger_event_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetPipelineTriggerEventResponse:
        """
        @summary 查询流水线触发历史
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPipelineTriggerEventResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTriggerEvent',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetPipelineTriggerEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_trigger_event(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTriggerEventResponse:
        """
        @summary 查询流水线触发历史
        
        @return: GetPipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_trigger_event_with_options(name, headers, runtime)

    async def get_pipeline_trigger_event_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetPipelineTriggerEventResponse:
        """
        @summary 查询流水线触发历史
        
        @return: GetPipelineTriggerEventResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_trigger_event_with_options_async(name, headers, runtime)

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

    def get_task_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetTaskTemplateResponse:
        """
        @summary 查询任务模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.GetTaskTemplateResponse:
        """
        @summary 查询任务模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.GetTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template(
        self,
        name: str,
    ) -> devs_20230714_models.GetTaskTemplateResponse:
        """
        @summary 查询任务模板
        
        @return: GetTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(name, headers, runtime)

    async def get_task_template_async(
        self,
        name: str,
    ) -> devs_20230714_models.GetTaskTemplateResponse:
        """
        @summary 查询任务模板
        
        @return: GetTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_template_with_options_async(name, headers, runtime)

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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/',
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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/',
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
        project: str,
        request: devs_20230714_models.ListEnvironmentsRequest,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(project, request, headers, runtime)

    async def list_environments_async(
        self,
        project: str,
        request: devs_20230714_models.ListEnvironmentsRequest,
    ) -> devs_20230714_models.ListEnvironmentsResponse:
        """
        @summary 查询环境列表
        
        @param request: ListEnvironmentsRequest
        @return: ListEnvironmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(project, request, headers, runtime)

    def list_pipeline_templates_with_options(
        self,
        tmp_req: devs_20230714_models.ListPipelineTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTemplatesResponse:
        """
        @summary 批量查询流水线模板
        
        @param tmp_req: ListPipelineTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTemplatesShrinkRequest()
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
            action='ListPipelineTemplates',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_templates_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListPipelineTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTemplatesResponse:
        """
        @summary 批量查询流水线模板
        
        @param tmp_req: ListPipelineTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTemplatesShrinkRequest()
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
            action='ListPipelineTemplates',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_templates(
        self,
        request: devs_20230714_models.ListPipelineTemplatesRequest,
    ) -> devs_20230714_models.ListPipelineTemplatesResponse:
        """
        @summary 批量查询流水线模板
        
        @param request: ListPipelineTemplatesRequest
        @return: ListPipelineTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_templates_with_options(request, headers, runtime)

    async def list_pipeline_templates_async(
        self,
        request: devs_20230714_models.ListPipelineTemplatesRequest,
    ) -> devs_20230714_models.ListPipelineTemplatesResponse:
        """
        @summary 批量查询流水线模板
        
        @param request: ListPipelineTemplatesRequest
        @return: ListPipelineTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_templates_with_options_async(request, headers, runtime)

    def list_pipeline_trigger_events_with_options(
        self,
        tmp_req: devs_20230714_models.ListPipelineTriggerEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTriggerEventsResponse:
        """
        @summary 批量查询流水线触发历史
        
        @param tmp_req: ListPipelineTriggerEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTriggerEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTriggerEventsShrinkRequest()
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
            action='ListPipelineTriggerEvents',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTriggerEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_trigger_events_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListPipelineTriggerEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTriggerEventsResponse:
        """
        @summary 批量查询流水线触发历史
        
        @param tmp_req: ListPipelineTriggerEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTriggerEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTriggerEventsShrinkRequest()
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
            action='ListPipelineTriggerEvents',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggerevents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTriggerEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_trigger_events(
        self,
        request: devs_20230714_models.ListPipelineTriggerEventsRequest,
    ) -> devs_20230714_models.ListPipelineTriggerEventsResponse:
        """
        @summary 批量查询流水线触发历史
        
        @param request: ListPipelineTriggerEventsRequest
        @return: ListPipelineTriggerEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_trigger_events_with_options(request, headers, runtime)

    async def list_pipeline_trigger_events_async(
        self,
        request: devs_20230714_models.ListPipelineTriggerEventsRequest,
    ) -> devs_20230714_models.ListPipelineTriggerEventsResponse:
        """
        @summary 批量查询流水线触发历史
        
        @param request: ListPipelineTriggerEventsRequest
        @return: ListPipelineTriggerEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_trigger_events_with_options_async(request, headers, runtime)

    def list_pipeline_triggers_with_options(
        self,
        tmp_req: devs_20230714_models.ListPipelineTriggersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTriggersResponse:
        """
        @summary 批量查询流水线触发器
        
        @param tmp_req: ListPipelineTriggersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTriggersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTriggersShrinkRequest()
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
            action='ListPipelineTriggers',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_triggers_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListPipelineTriggersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListPipelineTriggersResponse:
        """
        @summary 批量查询流水线触发器
        
        @param tmp_req: ListPipelineTriggersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPipelineTriggersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListPipelineTriggersShrinkRequest()
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
            action='ListPipelineTriggers',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListPipelineTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_triggers(
        self,
        request: devs_20230714_models.ListPipelineTriggersRequest,
    ) -> devs_20230714_models.ListPipelineTriggersResponse:
        """
        @summary 批量查询流水线触发器
        
        @param request: ListPipelineTriggersRequest
        @return: ListPipelineTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_triggers_with_options(request, headers, runtime)

    async def list_pipeline_triggers_async(
        self,
        request: devs_20230714_models.ListPipelineTriggersRequest,
    ) -> devs_20230714_models.ListPipelineTriggersResponse:
        """
        @summary 批量查询流水线触发器
        
        @param request: ListPipelineTriggersRequest
        @return: ListPipelineTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_triggers_with_options_async(request, headers, runtime)

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

    def list_repositories_with_options(
        self,
        tmp_req: devs_20230714_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListRepositoriesResponse:
        """
        @summary 批量查询仓库绑定
        
        @param tmp_req: ListRepositoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRepositoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListRepositoriesShrinkRequest()
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
            action='ListRepositories',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repositories_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListRepositoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListRepositoriesResponse:
        """
        @summary 批量查询仓库绑定
        
        @param tmp_req: ListRepositoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRepositoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListRepositoriesShrinkRequest()
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
            action='ListRepositories',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/repositories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repositories(
        self,
        request: devs_20230714_models.ListRepositoriesRequest,
    ) -> devs_20230714_models.ListRepositoriesResponse:
        """
        @summary 批量查询仓库绑定
        
        @param request: ListRepositoriesRequest
        @return: ListRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_repositories_with_options(request, headers, runtime)

    async def list_repositories_async(
        self,
        request: devs_20230714_models.ListRepositoriesRequest,
    ) -> devs_20230714_models.ListRepositoriesResponse:
        """
        @summary 批量查询仓库绑定
        
        @param request: ListRepositoriesRequest
        @return: ListRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_repositories_with_options_async(request, headers, runtime)

    def list_task_templates_with_options(
        self,
        tmp_req: devs_20230714_models.ListTaskTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListTaskTemplatesResponse:
        """
        @summary 批量查询任务模板
        
        @param tmp_req: ListTaskTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListTaskTemplatesShrinkRequest()
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
            action='ListTaskTemplates',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListTaskTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_templates_with_options_async(
        self,
        tmp_req: devs_20230714_models.ListTaskTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.ListTaskTemplatesResponse:
        """
        @summary 批量查询任务模板
        
        @param tmp_req: ListTaskTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = devs_20230714_models.ListTaskTemplatesShrinkRequest()
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
            action='ListTaskTemplates',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            devs_20230714_models.ListTaskTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_templates(
        self,
        request: devs_20230714_models.ListTaskTemplatesRequest,
    ) -> devs_20230714_models.ListTaskTemplatesResponse:
        """
        @summary 批量查询任务模板
        
        @param request: ListTaskTemplatesRequest
        @return: ListTaskTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_templates_with_options(request, headers, runtime)

    async def list_task_templates_async(
        self,
        request: devs_20230714_models.ListTaskTemplatesRequest,
    ) -> devs_20230714_models.ListTaskTemplatesResponse:
        """
        @summary 批量查询任务模板
        
        @param request: ListTaskTemplatesRequest
        @return: ListTaskTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_templates_with_options_async(request, headers, runtime)

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

    def put_environment_with_options(
        self,
        project: str,
        name: str,
        request: devs_20230714_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutEnvironmentResponse:
        """
        @summary 更新环境（全局更新）
        
        @param request: PutEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnvironmentResponse
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
            action='PutEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_environment_with_options_async(
        self,
        project: str,
        name: str,
        request: devs_20230714_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutEnvironmentResponse:
        """
        @summary 更新环境（全局更新）
        
        @param request: PutEnvironmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnvironmentResponse
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
            action='PutEnvironment',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_environment(
        self,
        project: str,
        name: str,
        request: devs_20230714_models.PutEnvironmentRequest,
    ) -> devs_20230714_models.PutEnvironmentResponse:
        """
        @summary 更新环境（全局更新）
        
        @param request: PutEnvironmentRequest
        @return: PutEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_with_options(project, name, request, headers, runtime)

    async def put_environment_async(
        self,
        project: str,
        name: str,
        request: devs_20230714_models.PutEnvironmentRequest,
    ) -> devs_20230714_models.PutEnvironmentResponse:
        """
        @summary 更新环境（全局更新）
        
        @param request: PutEnvironmentRequest
        @return: PutEnvironmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_environment_with_options_async(project, name, request, headers, runtime)

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

    def put_pipeline_template_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineTemplateResponse:
        """
        @summary 更新替换流水线模板
        
        @param request: PutPipelineTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineTemplateResponse
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
            action='PutPipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_pipeline_template_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineTemplateResponse:
        """
        @summary 更新替换流水线模板
        
        @param request: PutPipelineTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineTemplateResponse
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
            action='PutPipelineTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_pipeline_template(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTemplateRequest,
    ) -> devs_20230714_models.PutPipelineTemplateResponse:
        """
        @summary 更新替换流水线模板
        
        @param request: PutPipelineTemplateRequest
        @return: PutPipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_template_with_options(name, request, headers, runtime)

    async def put_pipeline_template_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTemplateRequest,
    ) -> devs_20230714_models.PutPipelineTemplateResponse:
        """
        @summary 更新替换流水线模板
        
        @param request: PutPipelineTemplateRequest
        @return: PutPipelineTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_pipeline_template_with_options_async(name, request, headers, runtime)

    def put_pipeline_trigger_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineTriggerResponse:
        """
        @summary 更新替换流水线触发器
        
        @param request: PutPipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineTriggerResponse
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
            action='PutPipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_pipeline_trigger_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutPipelineTriggerResponse:
        """
        @summary 更新替换流水线触发器
        
        @param request: PutPipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutPipelineTriggerResponse
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
            action='PutPipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutPipelineTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_pipeline_trigger(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTriggerRequest,
    ) -> devs_20230714_models.PutPipelineTriggerResponse:
        """
        @summary 更新替换流水线触发器
        
        @param request: PutPipelineTriggerRequest
        @return: PutPipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_trigger_with_options(name, request, headers, runtime)

    async def put_pipeline_trigger_async(
        self,
        name: str,
        request: devs_20230714_models.PutPipelineTriggerRequest,
    ) -> devs_20230714_models.PutPipelineTriggerResponse:
        """
        @summary 更新替换流水线触发器
        
        @param request: PutPipelineTriggerRequest
        @return: PutPipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_pipeline_trigger_with_options_async(name, request, headers, runtime)

    def put_project_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: PutProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProjectResponse
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
            action='PutProject',
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
            devs_20230714_models.PutProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_project_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: PutProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProjectResponse
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
            action='PutProject',
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
            devs_20230714_models.PutProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_project(
        self,
        name: str,
        request: devs_20230714_models.PutProjectRequest,
    ) -> devs_20230714_models.PutProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: PutProjectRequest
        @return: PutProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_with_options(name, request, headers, runtime)

    async def put_project_async(
        self,
        name: str,
        request: devs_20230714_models.PutProjectRequest,
    ) -> devs_20230714_models.PutProjectResponse:
        """
        @summary 更新替换应用
        
        @param request: PutProjectRequest
        @return: PutProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_project_with_options_async(name, request, headers, runtime)

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

    def put_task_template_with_options(
        self,
        name: str,
        request: devs_20230714_models.PutTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutTaskTemplateResponse:
        """
        @summary 更新替换任务模板
        
        @param request: PutTaskTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTaskTemplateResponse
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
            action='PutTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_task_template_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.PutTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.PutTaskTemplateResponse:
        """
        @summary 更新替换任务模板
        
        @param request: PutTaskTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTaskTemplateResponse
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
            action='PutTaskTemplate',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.PutTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_task_template(
        self,
        name: str,
        request: devs_20230714_models.PutTaskTemplateRequest,
    ) -> devs_20230714_models.PutTaskTemplateResponse:
        """
        @summary 更新替换任务模板
        
        @param request: PutTaskTemplateRequest
        @return: PutTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_template_with_options(name, request, headers, runtime)

    async def put_task_template_async(
        self,
        name: str,
        request: devs_20230714_models.PutTaskTemplateRequest,
    ) -> devs_20230714_models.PutTaskTemplateResponse:
        """
        @summary 更新替换任务模板
        
        @param request: PutTaskTemplateRequest
        @return: PutTaskTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_task_template_with_options_async(name, request, headers, runtime)

    def refresh_connection_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RefreshConnectionResponse:
        """
        @summary 检查并刷新身份绑定中的凭证和账号信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshConnectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefreshConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/refresh',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RefreshConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_connection_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.RefreshConnectionResponse:
        """
        @summary 检查并刷新身份绑定中的凭证和账号信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshConnectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefreshConnection',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/connections/{OpenApiUtilClient.get_encode_param(name)}/refresh',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.RefreshConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_connection(
        self,
        name: str,
    ) -> devs_20230714_models.RefreshConnectionResponse:
        """
        @summary 检查并刷新身份绑定中的凭证和账号信息
        
        @return: RefreshConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_connection_with_options(name, headers, runtime)

    async def refresh_connection_async(
        self,
        name: str,
    ) -> devs_20230714_models.RefreshConnectionResponse:
        """
        @summary 检查并刷新身份绑定中的凭证和账号信息
        
        @return: RefreshConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refresh_connection_with_options_async(name, headers, runtime)

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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
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
        project: str,
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
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(project)}/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
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
        project: str,
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
        return self.update_environment_with_options(project, name, request, headers, runtime)

    async def update_environment_async(
        self,
        project: str,
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
        return await self.update_environment_with_options_async(project, name, request, headers, runtime)

    def update_pipeline_trigger_with_options(
        self,
        name: str,
        request: devs_20230714_models.UpdatePipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdatePipelineTriggerResponse:
        """
        @summary 更新流水线触发器
        
        @param request: UpdatePipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePipelineTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdatePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdatePipelineTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_trigger_with_options_async(
        self,
        name: str,
        request: devs_20230714_models.UpdatePipelineTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> devs_20230714_models.UpdatePipelineTriggerResponse:
        """
        @summary 更新流水线触发器
        
        @param request: UpdatePipelineTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePipelineTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdatePipelineTrigger',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/pipelinetriggers/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devs_20230714_models.UpdatePipelineTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_trigger(
        self,
        name: str,
        request: devs_20230714_models.UpdatePipelineTriggerRequest,
    ) -> devs_20230714_models.UpdatePipelineTriggerResponse:
        """
        @summary 更新流水线触发器
        
        @param request: UpdatePipelineTriggerRequest
        @return: UpdatePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_trigger_with_options(name, request, headers, runtime)

    async def update_pipeline_trigger_async(
        self,
        name: str,
        request: devs_20230714_models.UpdatePipelineTriggerRequest,
    ) -> devs_20230714_models.UpdatePipelineTriggerResponse:
        """
        @summary 更新流水线触发器
        
        @param request: UpdatePipelineTriggerRequest
        @return: UpdatePipelineTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_pipeline_trigger_with_options_async(name, request, headers, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
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
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-07-14',
            protocol='HTTPS',
            pathname=f'/2023-07-14/projects/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
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
