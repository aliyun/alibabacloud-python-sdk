# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_serverless20210924 import models as serverless_20210924_models
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
        self._endpoint = self.get_endpoint('serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_task(
        self,
        name: str,
    ) -> serverless_20210924_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(name, headers, runtime)

    async def cancel_task_async(
        self,
        name: str,
    ) -> serverless_20210924_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(name, headers, runtime)

    def cancel_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CancelTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CancelTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: serverless_20210924_models.CreateApplicationRequest,
    ) -> serverless_20210924_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    async def create_application_async(
        self,
        request: serverless_20210924_models.CreateApplicationRequest,
    ) -> serverless_20210924_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_with_options_async(request, headers, runtime)

    def create_application_with_options(
        self,
        request: serverless_20210924_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_deploy):
            body['autoDeploy'] = request.auto_deploy
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.env_vars):
            body['envVars'] = request.env_vars
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.repo_source):
            body['repoSource'] = request.repo_source
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.trigger):
            body['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: serverless_20210924_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_deploy):
            body['autoDeploy'] = request.auto_deploy
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.env_vars):
            body['envVars'] = request.env_vars
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.repo_source):
            body['repoSource'] = request.repo_source
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.trigger):
            body['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        request: serverless_20210924_models.CreatePipelineRequest,
    ) -> serverless_20210924_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(request, headers, runtime)

    async def create_pipeline_async(
        self,
        request: serverless_20210924_models.CreatePipelineRequest,
    ) -> serverless_20210924_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_with_options_async(request, headers, runtime)

    def create_pipeline_with_options(
        self,
        request: serverless_20210924_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        request: serverless_20210924_models.CreatePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_template(
        self,
        request: serverless_20210924_models.CreatePipelineTemplateRequest,
    ) -> serverless_20210924_models.CreatePipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_template_with_options(request, headers, runtime)

    async def create_pipeline_template_async(
        self,
        request: serverless_20210924_models.CreatePipelineTemplateRequest,
    ) -> serverless_20210924_models.CreatePipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_pipeline_template_with_options_async(request, headers, runtime)

    def create_pipeline_template_with_options(
        self,
        request: serverless_20210924_models.CreatePipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreatePipelineTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_template_with_options_async(
        self,
        request: serverless_20210924_models.CreatePipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreatePipelineTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_release(
        self,
        app_name: str,
        request: serverless_20210924_models.CreateReleaseRequest,
    ) -> serverless_20210924_models.CreateReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_release_with_options(app_name, request, headers, runtime)

    async def create_release_async(
        self,
        app_name: str,
        request: serverless_20210924_models.CreateReleaseRequest,
    ) -> serverless_20210924_models.CreateReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_release_with_options_async(app_name, request, headers, runtime)

    def create_release_with_options(
        self,
        app_name: str,
        request: serverless_20210924_models.CreateReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(app_name)}/releases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_release_with_options_async(
        self,
        app_name: str,
        request: serverless_20210924_models.CreateReleaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(app_name)}/releases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: serverless_20210924_models.CreateTaskRequest,
    ) -> serverless_20210924_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: serverless_20210924_models.CreateTaskRequest,
    ) -> serverless_20210924_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: serverless_20210924_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: serverless_20210924_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_template(
        self,
        request: serverless_20210924_models.CreateTaskTemplateRequest,
    ) -> serverless_20210924_models.CreateTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_template_with_options(request, headers, runtime)

    async def create_task_template_async(
        self,
        request: serverless_20210924_models.CreateTaskTemplateRequest,
    ) -> serverless_20210924_models.CreateTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_template_with_options_async(request, headers, runtime)

    def create_task_template_with_options(
        self,
        request: serverless_20210924_models.CreateTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateTaskTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_template_with_options_async(
        self,
        request: serverless_20210924_models.CreateTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.CreateTaskTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(name, headers, runtime)

    async def delete_application_async(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(name, headers, runtime)

    def delete_application_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteApplicationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteApplicationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(name, headers, runtime)

    async def delete_environment_async(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(name, headers, runtime)

    def delete_environment_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline_template(
        self,
        name: str,
    ) -> serverless_20210924_models.DeletePipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_template_with_options(name, headers, runtime)

    async def delete_pipeline_template_async(
        self,
        name: str,
    ) -> serverless_20210924_models.DeletePipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_pipeline_template_with_options_async(name, headers, runtime)

    def delete_pipeline_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeletePipelineTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeletePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeletePipelineTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeletePipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task_template(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_template_with_options(name, headers, runtime)

    async def delete_task_template_async(
        self,
        name: str,
    ) -> serverless_20210924_models.DeleteTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_task_template_with_options_async(name, headers, runtime)

    def delete_task_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteTaskTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteTaskTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        name: str,
        request: serverless_20210924_models.DeleteTemplateRequest,
    ) -> serverless_20210924_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(name, request, headers, runtime)

    async def delete_template_async(
        self,
        name: str,
        request: serverless_20210924_models.DeleteTemplateRequest,
    ) -> serverless_20210924_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(name, request, headers, runtime)

    def delete_template_with_options(
        self,
        name: str,
        request: serverless_20210924_models.DeleteTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.DeleteTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        name: str,
    ) -> serverless_20210924_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_application_with_options(name, headers, runtime)

    async def get_application_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(name, headers, runtime)

    def get_application_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetApplicationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetApplicationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        name: str,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(name, headers, runtime)

    async def get_environment_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(name, headers, runtime)

    def get_environment_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        name: str,
    ) -> serverless_20210924_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(name, headers, runtime)

    async def get_pipeline_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_with_options_async(name, headers, runtime)

    def get_pipeline_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_template(
        self,
        name: str,
    ) -> serverless_20210924_models.GetPipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_template_with_options(name, headers, runtime)

    async def get_pipeline_template_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetPipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pipeline_template_with_options_async(name, headers, runtime)

    def get_pipeline_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetPipelineTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetPipelineTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_release(
        self,
        app_name: str,
        version_id: str,
    ) -> serverless_20210924_models.GetReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_release_with_options(app_name, version_id, headers, runtime)

    async def get_release_async(
        self,
        app_name: str,
        version_id: str,
    ) -> serverless_20210924_models.GetReleaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_release_with_options_async(app_name, version_id, headers, runtime)

    def get_release_with_options(
        self,
        app_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetReleaseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(app_name)}/releases/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_release_with_options_async(
        self,
        app_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetReleaseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(app_name)}/releases/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        name: str,
    ) -> serverless_20210924_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(name, headers, runtime)

    async def get_service_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(name, headers, runtime)

    def get_service_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        name: str,
    ) -> serverless_20210924_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(name, headers, runtime)

    async def get_task_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(name, headers, runtime)

    def get_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_template(
        self,
        name: str,
    ) -> serverless_20210924_models.GetTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(name, headers, runtime)

    async def get_task_template_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_template_with_options_async(name, headers, runtime)

    def get_task_template_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTaskTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_template_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTaskTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        name: str,
        request: serverless_20210924_models.GetTemplateRequest,
    ) -> serverless_20210924_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(name, request, headers, runtime)

    async def get_template_async(
        self,
        name: str,
        request: serverless_20210924_models.GetTemplateRequest,
    ) -> serverless_20210924_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(name, request, headers, runtime)

    def get_template_with_options(
        self,
        name: str,
        request: serverless_20210924_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_revisions(
        self,
        request: serverless_20210924_models.ListEnvironmentRevisionsRequest,
    ) -> serverless_20210924_models.ListEnvironmentRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_revisions_with_options(request, headers, runtime)

    async def list_environment_revisions_async(
        self,
        request: serverless_20210924_models.ListEnvironmentRevisionsRequest,
    ) -> serverless_20210924_models.ListEnvironmentRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environment_revisions_with_options_async(request, headers, runtime)

    def list_environment_revisions_with_options(
        self,
        request: serverless_20210924_models.ListEnvironmentRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_name):
            query['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environmentrevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_revisions_with_options_async(
        self,
        request: serverless_20210924_models.ListEnvironmentRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_name):
            query['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environmentrevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentRevisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(self) -> serverless_20210924_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(headers, runtime)

    async def list_environments_async(self) -> serverless_20210924_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(headers, runtime)

    def list_environments_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_templates(
        self,
        request: serverless_20210924_models.ListPipelineTemplatesRequest,
    ) -> serverless_20210924_models.ListPipelineTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_templates_with_options(request, headers, runtime)

    async def list_pipeline_templates_async(
        self,
        request: serverless_20210924_models.ListPipelineTemplatesRequest,
    ) -> serverless_20210924_models.ListPipelineTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipeline_templates_with_options_async(request, headers, runtime)

    def list_pipeline_templates_with_options(
        self,
        tmp_req: serverless_20210924_models.ListPipelineTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListPipelineTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelineTemplatesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelineTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_templates_with_options_async(
        self,
        tmp_req: serverless_20210924_models.ListPipelineTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListPipelineTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelineTemplatesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelineTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        request: serverless_20210924_models.ListPipelinesRequest,
    ) -> serverless_20210924_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(request, headers, runtime)

    async def list_pipelines_async(
        self,
        request: serverless_20210924_models.ListPipelinesRequest,
    ) -> serverless_20210924_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pipelines_with_options_async(request, headers, runtime)

    def list_pipelines_with_options(
        self,
        tmp_req: serverless_20210924_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListPipelinesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelinesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        tmp_req: serverless_20210924_models.ListPipelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListPipelinesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelinesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_revisions(
        self,
        request: serverless_20210924_models.ListServiceRevisionsRequest,
    ) -> serverless_20210924_models.ListServiceRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_revisions_with_options(request, headers, runtime)

    async def list_service_revisions_async(
        self,
        request: serverless_20210924_models.ListServiceRevisionsRequest,
    ) -> serverless_20210924_models.ListServiceRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_revisions_with_options_async(request, headers, runtime)

    def list_service_revisions_with_options(
        self,
        request: serverless_20210924_models.ListServiceRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServiceRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/servicerevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServiceRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_revisions_with_options_async(
        self,
        request: serverless_20210924_models.ListServiceRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServiceRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/servicerevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServiceRevisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(self) -> serverless_20210924_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(headers, runtime)

    async def list_services_async(self) -> serverless_20210924_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(headers, runtime)

    def list_services_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_templates(
        self,
        request: serverless_20210924_models.ListTaskTemplatesRequest,
    ) -> serverless_20210924_models.ListTaskTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_templates_with_options(request, headers, runtime)

    async def list_task_templates_async(
        self,
        request: serverless_20210924_models.ListTaskTemplatesRequest,
    ) -> serverless_20210924_models.ListTaskTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_templates_with_options_async(request, headers, runtime)

    def list_task_templates_with_options(
        self,
        tmp_req: serverless_20210924_models.ListTaskTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTaskTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTaskTemplatesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTaskTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_templates_with_options_async(
        self,
        tmp_req: serverless_20210924_models.ListTaskTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTaskTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTaskTemplatesShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTaskTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: serverless_20210924_models.ListTasksRequest,
    ) -> serverless_20210924_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: serverless_20210924_models.ListTasksRequest,
    ) -> serverless_20210924_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: serverless_20210924_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTasksShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: serverless_20210924_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTasksShrinkRequest()
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_revisions(
        self,
        request: serverless_20210924_models.ListTemplateRevisionsRequest,
    ) -> serverless_20210924_models.ListTemplateRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_template_revisions_with_options(request, headers, runtime)

    async def list_template_revisions_async(
        self,
        request: serverless_20210924_models.ListTemplateRevisionsRequest,
    ) -> serverless_20210924_models.ListTemplateRevisionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_template_revisions_with_options_async(request, headers, runtime)

    def list_template_revisions_with_options(
        self,
        request: serverless_20210924_models.ListTemplateRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTemplateRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['templateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templaterevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplateRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_revisions_with_options_async(
        self,
        request: serverless_20210924_models.ListTemplateRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTemplateRevisionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['templateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templaterevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplateRevisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: serverless_20210924_models.ListTemplatesRequest,
    ) -> serverless_20210924_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: serverless_20210924_models.ListTemplatesRequest,
    ) -> serverless_20210924_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: serverless_20210924_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: serverless_20210924_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_environment(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_with_options(name, request, headers, runtime)

    async def put_environment_async(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_environment_with_options_async(name, request, headers, runtime)

    def put_environment_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_environment_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_pipeline_status(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineStatusRequest,
    ) -> serverless_20210924_models.PutPipelineStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_status_with_options(name, request, headers, runtime)

    async def put_pipeline_status_async(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineStatusRequest,
    ) -> serverless_20210924_models.PutPipelineStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_pipeline_status_with_options_async(name, request, headers, runtime)

    def put_pipeline_status_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutPipelineStatusResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_pipeline_status_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutPipelineStatusResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_pipeline_template(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineTemplateRequest,
    ) -> serverless_20210924_models.PutPipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_template_with_options(name, request, headers, runtime)

    async def put_pipeline_template_async(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineTemplateRequest,
    ) -> serverless_20210924_models.PutPipelineTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_pipeline_template_with_options_async(name, request, headers, runtime)

    def put_pipeline_template_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutPipelineTemplateResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_pipeline_template_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutPipelineTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutPipelineTemplateResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelinetemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_service(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
    ) -> serverless_20210924_models.PutServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_service_with_options(name, request, headers, runtime)

    async def put_service_async(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
    ) -> serverless_20210924_models.PutServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_service_with_options_async(name, request, headers, runtime)

    def put_service_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_service_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_task_status(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskStatusRequest,
    ) -> serverless_20210924_models.PutTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_status_with_options(name, request, headers, runtime)

    async def put_task_status_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskStatusRequest,
    ) -> serverless_20210924_models.PutTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_task_status_with_options_async(name, request, headers, runtime)

    def put_task_status_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTaskStatusResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_task_status_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTaskStatusResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_task_template(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskTemplateRequest,
    ) -> serverless_20210924_models.PutTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_template_with_options(name, request, headers, runtime)

    async def put_task_template_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskTemplateRequest,
    ) -> serverless_20210924_models.PutTaskTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_task_template_with_options_async(name, request, headers, runtime)

    def put_task_template_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTaskTemplateResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_task_template_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTaskTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTaskTemplateResponse:
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
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasktemplates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_template(
        self,
        name: str,
        request: serverless_20210924_models.PutTemplateRequest,
    ) -> serverless_20210924_models.PutTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_template_with_options(name, request, headers, runtime)

    async def put_template_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTemplateRequest,
    ) -> serverless_20210924_models.PutTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_template_with_options_async(name, request, headers, runtime)

    def put_template_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_template_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/templates/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task(
        self,
        name: str,
    ) -> serverless_20210924_models.ResumeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(name, headers, runtime)

    async def resume_task_async(
        self,
        name: str,
    ) -> serverless_20210924_models.ResumeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_task_with_options_async(name, headers, runtime)

    def resume_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ResumeTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ResumeTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/resume',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ResumeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pipeline(
        self,
        name: str,
    ) -> serverless_20210924_models.StartPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_with_options(name, headers, runtime)

    async def start_pipeline_async(
        self,
        name: str,
    ) -> serverless_20210924_models.StartPipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_pipeline_with_options_async(name, headers, runtime)

    def start_pipeline_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.StartPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pipeline_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.StartPipelineResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/pipelines/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task(
        self,
        name: str,
    ) -> serverless_20210924_models.StartTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_task_with_options(name, headers, runtime)

    async def start_task_async(
        self,
        name: str,
    ) -> serverless_20210924_models.StartTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_task_with_options_async(name, headers, runtime)

    def start_task_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.StartTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.StartTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/tasks/{OpenApiUtilClient.get_encode_param(name)}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        name: str,
        request: serverless_20210924_models.UpdateApplicationRequest,
    ) -> serverless_20210924_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_with_options(name, request, headers, runtime)

    async def update_application_async(
        self,
        name: str,
        request: serverless_20210924_models.UpdateApplicationRequest,
    ) -> serverless_20210924_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_with_options_async(name, request, headers, runtime)

    def update_application_with_options(
        self,
        name: str,
        request: serverless_20210924_models.UpdateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.UpdateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/applications/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )
