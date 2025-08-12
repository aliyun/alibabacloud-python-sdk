# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paillmtrace20240311 import models as pai_llmtrace_20240311_models
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
        self._endpoint = self.get_endpoint('paillmtrace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_online_eval_task_with_options(
        self,
        tmp_req: pai_llmtrace_20240311_models.CreateOnlineEvalTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse:
        """
        @summary Creates a trace evaluation task. The system will sample some data from the user\\"s trace data based on the task\\"s configuration. Then, an LLM is used to evaluate the performance of these traces, and the evaluation results are recorded.
        
        @param tmp_req: CreateOnlineEvalTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOnlineEvalTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.CreateOnlineEvalTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_online_eval_task_with_options_async(
        self,
        tmp_req: pai_llmtrace_20240311_models.CreateOnlineEvalTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse:
        """
        @summary Creates a trace evaluation task. The system will sample some data from the user\\"s trace data based on the task\\"s configuration. Then, an LLM is used to evaluate the performance of these traces, and the evaluation results are recorded.
        
        @param tmp_req: CreateOnlineEvalTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOnlineEvalTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.CreateOnlineEvalTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.body_shrink):
            query['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_online_eval_task(
        self,
        request: pai_llmtrace_20240311_models.CreateOnlineEvalTaskRequest,
    ) -> pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse:
        """
        @summary Creates a trace evaluation task. The system will sample some data from the user\\"s trace data based on the task\\"s configuration. Then, an LLM is used to evaluate the performance of these traces, and the evaluation results are recorded.
        
        @param request: CreateOnlineEvalTaskRequest
        @return: CreateOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_online_eval_task_with_options(request, headers, runtime)

    async def create_online_eval_task_async(
        self,
        request: pai_llmtrace_20240311_models.CreateOnlineEvalTaskRequest,
    ) -> pai_llmtrace_20240311_models.CreateOnlineEvalTaskResponse:
        """
        @summary Creates a trace evaluation task. The system will sample some data from the user\\"s trace data based on the task\\"s configuration. Then, an LLM is used to evaluate the performance of these traces, and the evaluation results are recorded.
        
        @param request: CreateOnlineEvalTaskRequest
        @return: CreateOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_online_eval_task_with_options_async(request, headers, runtime)

    def create_service_identity_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse:
        """
        @summary Creates a service-linked role required for the PaiLLMTrace service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/ServiceIdentityRole',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_identity_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse:
        """
        @summary Creates a service-linked role required for the PaiLLMTrace service.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/ServiceIdentityRole',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_identity_role(self) -> pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse:
        """
        @summary Creates a service-linked role required for the PaiLLMTrace service.
        
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(headers, runtime)

    async def create_service_identity_role_async(self) -> pai_llmtrace_20240311_models.CreateServiceIdentityRoleResponse:
        """
        @summary Creates a service-linked role required for the PaiLLMTrace service.
        
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_identity_role_with_options_async(headers, runtime)

    def delete_online_eval_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse:
        """
        @summary Delete an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_online_eval_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse:
        """
        @summary Delete an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_online_eval_task(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse:
        """
        @summary Delete an online evaluation task
        
        @return: DeleteOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_online_eval_task_with_options(task_id, headers, runtime)

    async def delete_online_eval_task_async(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.DeleteOnlineEvalTaskResponse:
        """
        @summary Delete an online evaluation task
        
        @return: DeleteOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_online_eval_task_with_options_async(task_id, headers, runtime)

    def evaluate_trace_with_options(
        self,
        trace_id: str,
        request: pai_llmtrace_20240311_models.EvaluateTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.EvaluateTraceResponse:
        """
        @summary Evaluates a specified piece of trace data.
        
        @param request: EvaluateTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.evaluation_config):
            body['EvaluationConfig'] = request.evaluation_config
        if not UtilClient.is_unset(request.evaluation_id):
            body['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.max_time):
            body['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_time):
            body['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EvaluateTrace',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/trace/{OpenApiUtilClient.get_encode_param(trace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.EvaluateTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_trace_with_options_async(
        self,
        trace_id: str,
        request: pai_llmtrace_20240311_models.EvaluateTraceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.EvaluateTraceResponse:
        """
        @summary Evaluates a specified piece of trace data.
        
        @param request: EvaluateTraceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateTraceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.evaluation_config):
            body['EvaluationConfig'] = request.evaluation_config
        if not UtilClient.is_unset(request.evaluation_id):
            body['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.max_time):
            body['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_time):
            body['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EvaluateTrace',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/trace/{OpenApiUtilClient.get_encode_param(trace_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.EvaluateTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_trace(
        self,
        trace_id: str,
        request: pai_llmtrace_20240311_models.EvaluateTraceRequest,
    ) -> pai_llmtrace_20240311_models.EvaluateTraceResponse:
        """
        @summary Evaluates a specified piece of trace data.
        
        @param request: EvaluateTraceRequest
        @return: EvaluateTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.evaluate_trace_with_options(trace_id, request, headers, runtime)

    async def evaluate_trace_async(
        self,
        trace_id: str,
        request: pai_llmtrace_20240311_models.EvaluateTraceRequest,
    ) -> pai_llmtrace_20240311_models.EvaluateTraceResponse:
        """
        @summary Evaluates a specified piece of trace data.
        
        @param request: EvaluateTraceRequest
        @return: EvaluateTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.evaluate_trace_with_options_async(trace_id, request, headers, runtime)

    def get_evaluation_templates_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse:
        """
        @summary Get the content of prompt templates used for evaluation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEvaluationTemplatesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEvaluationTemplates',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_evaluation_templates_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse:
        """
        @summary Get the content of prompt templates used for evaluation
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEvaluationTemplatesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEvaluationTemplates',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_evaluation_templates(self) -> pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse:
        """
        @summary Get the content of prompt templates used for evaluation
        
        @return: GetEvaluationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_evaluation_templates_with_options(headers, runtime)

    async def get_evaluation_templates_async(self) -> pai_llmtrace_20240311_models.GetEvaluationTemplatesResponse:
        """
        @summary Get the content of prompt templates used for evaluation
        
        @return: GetEvaluationTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_evaluation_templates_with_options_async(headers, runtime)

    def get_online_eval_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse:
        """
        @summary Get the details of an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_online_eval_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse:
        """
        @summary Get the details of an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_online_eval_task(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse:
        """
        @summary Get the details of an online evaluation task
        
        @return: GetOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_online_eval_task_with_options(task_id, headers, runtime)

    async def get_online_eval_task_async(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.GetOnlineEvalTaskResponse:
        """
        @summary Get the details of an online evaluation task
        
        @return: GetOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_online_eval_task_with_options_async(task_id, headers, runtime)

    def get_service_identity_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse:
        """
        @summary Obtains the information related to the service-linked role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/ServiceIdentityRole',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_identity_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse:
        """
        @summary Obtains the information related to the service-linked role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/ServiceIdentityRole',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_identity_role(self) -> pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse:
        """
        @summary Obtains the information related to the service-linked role.
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(headers, runtime)

    async def get_service_identity_role_async(self) -> pai_llmtrace_20240311_models.GetServiceIdentityRoleResponse:
        """
        @summary Obtains the information related to the service-linked role.
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_identity_role_with_options_async(headers, runtime)

    def get_xtrace_token_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetXtraceTokenResponse:
        """
        @summary Obtains the token used in the Xtrace service and the endpoint required for uploading trace data.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXtraceTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetXtraceToken',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/XtraceToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetXtraceTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_xtrace_token_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.GetXtraceTokenResponse:
        """
        @summary Obtains the token used in the Xtrace service and the endpoint required for uploading trace data.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXtraceTokenResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetXtraceToken',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/XtraceToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.GetXtraceTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_xtrace_token(self) -> pai_llmtrace_20240311_models.GetXtraceTokenResponse:
        """
        @summary Obtains the token used in the Xtrace service and the endpoint required for uploading trace data.
        
        @return: GetXtraceTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_xtrace_token_with_options(headers, runtime)

    async def get_xtrace_token_async(self) -> pai_llmtrace_20240311_models.GetXtraceTokenResponse:
        """
        @summary Obtains the token used in the Xtrace service and the endpoint required for uploading trace data.
        
        @return: GetXtraceTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_xtrace_token_with_options_async(headers, runtime)

    def list_eval_results_with_options(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListEvalResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListEvalResultsResponse:
        """
        @summary Obtains the list of results for trace evaluation. This API is used together with EvaluateTrace. EvaluateTrace starts the evaluation. ListEvalResults obtains the results.
        
        @param tmp_req: ListEvalResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvalResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListEvalResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_ids):
            request.record_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_ids, 'RecordIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.evaluation_id):
            query['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_ids_shrink):
            query['RecordIds'] = request.record_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvalResults',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListEvalResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eval_results_with_options_async(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListEvalResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListEvalResultsResponse:
        """
        @summary Obtains the list of results for trace evaluation. This API is used together with EvaluateTrace. EvaluateTrace starts the evaluation. ListEvalResults obtains the results.
        
        @param tmp_req: ListEvalResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvalResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListEvalResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_ids):
            request.record_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_ids, 'RecordIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.evaluation_id):
            query['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_ids_shrink):
            query['RecordIds'] = request.record_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvalResults',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/eval/results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListEvalResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eval_results(
        self,
        request: pai_llmtrace_20240311_models.ListEvalResultsRequest,
    ) -> pai_llmtrace_20240311_models.ListEvalResultsResponse:
        """
        @summary Obtains the list of results for trace evaluation. This API is used together with EvaluateTrace. EvaluateTrace starts the evaluation. ListEvalResults obtains the results.
        
        @param request: ListEvalResultsRequest
        @return: ListEvalResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_eval_results_with_options(request, headers, runtime)

    async def list_eval_results_async(
        self,
        request: pai_llmtrace_20240311_models.ListEvalResultsRequest,
    ) -> pai_llmtrace_20240311_models.ListEvalResultsResponse:
        """
        @summary Obtains the list of results for trace evaluation. This API is used together with EvaluateTrace. EvaluateTrace starts the evaluation. ListEvalResults obtains the results.
        
        @param request: ListEvalResultsRequest
        @return: ListEvalResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_eval_results_with_options_async(request, headers, runtime)

    def list_online_eval_task_results_with_options(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse:
        """
        @summary List the results of online evaluation tasks that meet the criteria
        
        @param tmp_req: ListOnlineEvalTaskResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineEvalTaskResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.trace_ids):
            request.trace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trace_ids, 'TraceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.evaluation_id):
            query['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.most_recent_results_only):
            query['MostRecentResultsOnly'] = request.most_recent_results_only
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.trace_ids_shrink):
            query['TraceIds'] = request.trace_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineEvalTaskResults',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltaskresults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_online_eval_task_results_with_options_async(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse:
        """
        @summary List the results of online evaluation tasks that meet the criteria
        
        @param tmp_req: ListOnlineEvalTaskResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineEvalTaskResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.trace_ids):
            request.trace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trace_ids, 'TraceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.evaluation_id):
            query['EvaluationId'] = request.evaluation_id
        if not UtilClient.is_unset(request.most_recent_results_only):
            query['MostRecentResultsOnly'] = request.most_recent_results_only
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.trace_ids_shrink):
            query['TraceIds'] = request.trace_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineEvalTaskResults',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltaskresults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_online_eval_task_results(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsRequest,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse:
        """
        @summary List the results of online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTaskResultsRequest
        @return: ListOnlineEvalTaskResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_online_eval_task_results_with_options(request, headers, runtime)

    async def list_online_eval_task_results_async(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsRequest,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTaskResultsResponse:
        """
        @summary List the results of online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTaskResultsRequest
        @return: ListOnlineEvalTaskResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_online_eval_task_results_with_options_async(request, headers, runtime)

    def list_online_eval_tasks_with_options(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse:
        """
        @summary View online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineEvalTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sampling_method):
            query['SamplingMethod'] = request.sampling_method
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineEvalTasks',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_online_eval_tasks_with_options_async(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse:
        """
        @summary View online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineEvalTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sampling_method):
            query['SamplingMethod'] = request.sampling_method
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineEvalTasks',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_online_eval_tasks(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTasksRequest,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse:
        """
        @summary View online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTasksRequest
        @return: ListOnlineEvalTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_online_eval_tasks_with_options(request, headers, runtime)

    async def list_online_eval_tasks_async(
        self,
        request: pai_llmtrace_20240311_models.ListOnlineEvalTasksRequest,
    ) -> pai_llmtrace_20240311_models.ListOnlineEvalTasksResponse:
        """
        @summary View online evaluation tasks that meet the criteria
        
        @param request: ListOnlineEvalTasksRequest
        @return: ListOnlineEvalTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_online_eval_tasks_with_options_async(request, headers, runtime)

    def list_traces_datas_with_options(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListTracesDatasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListTracesDatasResponse:
        """
        @summary Obtains a list of trace data based on specified criteria.
        
        @param tmp_req: ListTracesDatasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTracesDatasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListTracesDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        if not UtilClient.is_unset(tmp_req.span_ids):
            request.span_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.span_ids, 'SpanIds', 'simple')
        if not UtilClient.is_unset(tmp_req.trace_ids):
            request.trace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trace_ids, 'TraceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not UtilClient.is_unset(request.has_events):
            query['HasEvents'] = request.has_events
        if not UtilClient.is_unset(request.has_status_message):
            query['HasStatusMessage'] = request.has_status_message
        if not UtilClient.is_unset(request.llm_app_name):
            query['LlmAppName'] = request.llm_app_name
        if not UtilClient.is_unset(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.opentelemetry_compatible):
            query['OpentelemetryCompatible'] = request.opentelemetry_compatible
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_sub_id):
            query['OwnerSubId'] = request.owner_sub_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.span_ids_shrink):
            query['SpanIds'] = request.span_ids_shrink
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.trace_ids_shrink):
            query['TraceIds'] = request.trace_ids_shrink
        if not UtilClient.is_unset(request.trace_reduce_method):
            query['TraceReduceMethod'] = request.trace_reduce_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTracesDatas',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/TracesDatas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListTracesDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traces_datas_with_options_async(
        self,
        tmp_req: pai_llmtrace_20240311_models.ListTracesDatasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.ListTracesDatasResponse:
        """
        @summary Obtains a list of trace data based on specified criteria.
        
        @param tmp_req: ListTracesDatasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTracesDatasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_llmtrace_20240311_models.ListTracesDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        if not UtilClient.is_unset(tmp_req.span_ids):
            request.span_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.span_ids, 'SpanIds', 'simple')
        if not UtilClient.is_unset(tmp_req.trace_ids):
            request.trace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trace_ids, 'TraceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not UtilClient.is_unset(request.has_events):
            query['HasEvents'] = request.has_events
        if not UtilClient.is_unset(request.has_status_message):
            query['HasStatusMessage'] = request.has_status_message
        if not UtilClient.is_unset(request.llm_app_name):
            query['LlmAppName'] = request.llm_app_name
        if not UtilClient.is_unset(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.opentelemetry_compatible):
            query['OpentelemetryCompatible'] = request.opentelemetry_compatible
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_sub_id):
            query['OwnerSubId'] = request.owner_sub_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.span_ids_shrink):
            query['SpanIds'] = request.span_ids_shrink
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.trace_ids_shrink):
            query['TraceIds'] = request.trace_ids_shrink
        if not UtilClient.is_unset(request.trace_reduce_method):
            query['TraceReduceMethod'] = request.trace_reduce_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTracesDatas',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/TracesDatas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.ListTracesDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traces_datas(
        self,
        request: pai_llmtrace_20240311_models.ListTracesDatasRequest,
    ) -> pai_llmtrace_20240311_models.ListTracesDatasResponse:
        """
        @summary Obtains a list of trace data based on specified criteria.
        
        @param request: ListTracesDatasRequest
        @return: ListTracesDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_traces_datas_with_options(request, headers, runtime)

    async def list_traces_datas_async(
        self,
        request: pai_llmtrace_20240311_models.ListTracesDatasRequest,
    ) -> pai_llmtrace_20240311_models.ListTracesDatasResponse:
        """
        @summary Obtains a list of trace data based on specified criteria.
        
        @param request: ListTracesDatasRequest
        @return: ListTracesDatasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_traces_datas_with_options_async(request, headers, runtime)

    def stop_online_eval_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse:
        """
        @summary Stop the execution of an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_online_eval_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse:
        """
        @summary Stop the execution of an online evaluation task
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopOnlineEvalTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_online_eval_task(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse:
        """
        @summary Stop the execution of an online evaluation task
        
        @return: StopOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_online_eval_task_with_options(task_id, headers, runtime)

    async def stop_online_eval_task_async(
        self,
        task_id: str,
    ) -> pai_llmtrace_20240311_models.StopOnlineEvalTaskResponse:
        """
        @summary Stop the execution of an online evaluation task
        
        @return: StopOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_online_eval_task_with_options_async(task_id, headers, runtime)

    def update_online_eval_task_with_options(
        self,
        task_id: str,
        request: pai_llmtrace_20240311_models.UpdateOnlineEvalTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse:
        """
        @summary Changes the configuration of a trace evaluation task.
        
        @param request: UpdateOnlineEvalTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOnlineEvalTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_config):
            body['EvaluationConfig'] = request.evaluation_config
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.sampling_frequency_minutes):
            body['SamplingFrequencyMinutes'] = request.sampling_frequency_minutes
        if not UtilClient.is_unset(request.sampling_ratio):
            body['SamplingRatio'] = request.sampling_ratio
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_online_eval_task_with_options_async(
        self,
        task_id: str,
        request: pai_llmtrace_20240311_models.UpdateOnlineEvalTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse:
        """
        @summary Changes the configuration of a trace evaluation task.
        
        @param request: UpdateOnlineEvalTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOnlineEvalTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evaluation_config):
            body['EvaluationConfig'] = request.evaluation_config
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.model_config):
            body['ModelConfig'] = request.model_config
        if not UtilClient.is_unset(request.sampling_frequency_minutes):
            body['SamplingFrequencyMinutes'] = request.sampling_frequency_minutes
        if not UtilClient.is_unset(request.sampling_ratio):
            body['SamplingRatio'] = request.sampling_ratio
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOnlineEvalTask',
            version='2024-03-11',
            protocol='HTTPS',
            pathname=f'/api/v1/PAILLMTrace/onlineevaltasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_online_eval_task(
        self,
        task_id: str,
        request: pai_llmtrace_20240311_models.UpdateOnlineEvalTaskRequest,
    ) -> pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse:
        """
        @summary Changes the configuration of a trace evaluation task.
        
        @param request: UpdateOnlineEvalTaskRequest
        @return: UpdateOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_online_eval_task_with_options(task_id, request, headers, runtime)

    async def update_online_eval_task_async(
        self,
        task_id: str,
        request: pai_llmtrace_20240311_models.UpdateOnlineEvalTaskRequest,
    ) -> pai_llmtrace_20240311_models.UpdateOnlineEvalTaskResponse:
        """
        @summary Changes the configuration of a trace evaluation task.
        
        @param request: UpdateOnlineEvalTaskRequest
        @return: UpdateOnlineEvalTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_online_eval_task_with_options_async(task_id, request, headers, runtime)
