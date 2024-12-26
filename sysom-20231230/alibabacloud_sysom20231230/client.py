# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sysom20231230 import models as sys_om20231230_models
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
        self._endpoint = self.get_endpoint('sysom', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def auth_diagnosis_with_options(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        """
        @summary 授权 SysOM 对某个机器进行诊断
        
        @param request: AuthDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_role):
            body['autoCreateRole'] = request.auto_create_role
        if not UtilClient.is_unset(request.auto_install_agent):
            body['autoInstallAgent'] = request.auto_install_agent
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/auth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.AuthDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        """
        @summary 授权 SysOM 对某个机器进行诊断
        
        @param request: AuthDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_role):
            body['autoCreateRole'] = request.auto_create_role
        if not UtilClient.is_unset(request.auto_install_agent):
            body['autoInstallAgent'] = request.auto_install_agent
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/auth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.AuthDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_diagnosis(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        """
        @summary 授权 SysOM 对某个机器进行诊断
        
        @param request: AuthDiagnosisRequest
        @return: AuthDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.auth_diagnosis_with_options(request, headers, runtime)

    async def auth_diagnosis_async(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        """
        @summary 授权 SysOM 对某个机器进行诊断
        
        @param request: AuthDiagnosisRequest
        @return: AuthDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.auth_diagnosis_with_options_async(request, headers, runtime)

    def generate_copilot_response_with_options(
        self,
        request: sys_om20231230_models.GenerateCopilotResponseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GenerateCopilotResponseResponse:
        """
        @summary 获取copilot服务的返回结果
        
        @param request: GenerateCopilotResponseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCopilotResponseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCopilotResponse',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/generate_copilot_response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GenerateCopilotResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_copilot_response_with_options_async(
        self,
        request: sys_om20231230_models.GenerateCopilotResponseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GenerateCopilotResponseResponse:
        """
        @summary 获取copilot服务的返回结果
        
        @param request: GenerateCopilotResponseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCopilotResponseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.llm_param_string):
            body['llmParamString'] = request.llm_param_string
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateCopilotResponse',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/generate_copilot_response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GenerateCopilotResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_copilot_response(
        self,
        request: sys_om20231230_models.GenerateCopilotResponseRequest,
    ) -> sys_om20231230_models.GenerateCopilotResponseResponse:
        """
        @summary 获取copilot服务的返回结果
        
        @param request: GenerateCopilotResponseRequest
        @return: GenerateCopilotResponseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_copilot_response_with_options(request, headers, runtime)

    async def generate_copilot_response_async(
        self,
        request: sys_om20231230_models.GenerateCopilotResponseRequest,
    ) -> sys_om20231230_models.GenerateCopilotResponseResponse:
        """
        @summary 获取copilot服务的返回结果
        
        @param request: GenerateCopilotResponseRequest
        @return: GenerateCopilotResponseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_copilot_response_with_options_async(request, headers, runtime)

    def get_aiquery_result_with_options(
        self,
        request: sys_om20231230_models.GetAIQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAIQueryResultResponse:
        """
        @summary 查看AI Infra分析结果
        
        @param request: GetAIQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAIQueryResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_id):
            body['analysisId'] = request.analysis_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAIQueryResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/app_observ/aiAnalysis/query_result',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAIQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiquery_result_with_options_async(
        self,
        request: sys_om20231230_models.GetAIQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAIQueryResultResponse:
        """
        @summary 查看AI Infra分析结果
        
        @param request: GetAIQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAIQueryResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.analysis_id):
            body['analysisId'] = request.analysis_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAIQueryResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/app_observ/aiAnalysis/query_result',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAIQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiquery_result(
        self,
        request: sys_om20231230_models.GetAIQueryResultRequest,
    ) -> sys_om20231230_models.GetAIQueryResultResponse:
        """
        @summary 查看AI Infra分析结果
        
        @param request: GetAIQueryResultRequest
        @return: GetAIQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aiquery_result_with_options(request, headers, runtime)

    async def get_aiquery_result_async(
        self,
        request: sys_om20231230_models.GetAIQueryResultRequest,
    ) -> sys_om20231230_models.GetAIQueryResultResponse:
        """
        @summary 查看AI Infra分析结果
        
        @param request: GetAIQueryResultRequest
        @return: GetAIQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aiquery_result_with_options_async(request, headers, runtime)

    def get_abnormal_events_count_with_options(
        self,
        request: sys_om20231230_models.GetAbnormalEventsCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAbnormalEventsCountResponse:
        """
        @summary 获取节点/Pod不同等级异常事件的数量
        
        @param request: GetAbnormalEventsCountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAbnormalEventsCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod):
            query['pod'] = request.pod
        if not UtilClient.is_unset(request.show_pod):
            query['showPod'] = request.show_pod
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAbnormalEventsCount',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/abnormaly_events_count',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAbnormalEventsCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abnormal_events_count_with_options_async(
        self,
        request: sys_om20231230_models.GetAbnormalEventsCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAbnormalEventsCountResponse:
        """
        @summary 获取节点/Pod不同等级异常事件的数量
        
        @param request: GetAbnormalEventsCountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAbnormalEventsCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod):
            query['pod'] = request.pod
        if not UtilClient.is_unset(request.show_pod):
            query['showPod'] = request.show_pod
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAbnormalEventsCount',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/abnormaly_events_count',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAbnormalEventsCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abnormal_events_count(
        self,
        request: sys_om20231230_models.GetAbnormalEventsCountRequest,
    ) -> sys_om20231230_models.GetAbnormalEventsCountResponse:
        """
        @summary 获取节点/Pod不同等级异常事件的数量
        
        @param request: GetAbnormalEventsCountRequest
        @return: GetAbnormalEventsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_abnormal_events_count_with_options(request, headers, runtime)

    async def get_abnormal_events_count_async(
        self,
        request: sys_om20231230_models.GetAbnormalEventsCountRequest,
    ) -> sys_om20231230_models.GetAbnormalEventsCountResponse:
        """
        @summary 获取节点/Pod不同等级异常事件的数量
        
        @param request: GetAbnormalEventsCountRequest
        @return: GetAbnormalEventsCountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_abnormal_events_count_with_options_async(request, headers, runtime)

    def get_agent_with_options(
        self,
        request: sys_om20231230_models.GetAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAgentResponse:
        """
        @summary 获取某个组件的详情
        
        @param request: GetAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['agent_id'] = request.agent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/get_agent',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: sys_om20231230_models.GetAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAgentResponse:
        """
        @summary 获取某个组件的详情
        
        @param request: GetAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['agent_id'] = request.agent_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/get_agent',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent(
        self,
        request: sys_om20231230_models.GetAgentRequest,
    ) -> sys_om20231230_models.GetAgentResponse:
        """
        @summary 获取某个组件的详情
        
        @param request: GetAgentRequest
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_with_options(request, headers, runtime)

    async def get_agent_async(
        self,
        request: sys_om20231230_models.GetAgentRequest,
    ) -> sys_om20231230_models.GetAgentResponse:
        """
        @summary 获取某个组件的详情
        
        @param request: GetAgentRequest
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_with_options_async(request, headers, runtime)

    def get_agent_task_with_options(
        self,
        request: sys_om20231230_models.GetAgentTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAgentTaskResponse:
        """
        @summary 获取Agent安装任务执行状态
        
        @param request: GetAgentTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentTask',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/get_agent_task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAgentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_task_with_options_async(
        self,
        request: sys_om20231230_models.GetAgentTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetAgentTaskResponse:
        """
        @summary 获取Agent安装任务执行状态
        
        @param request: GetAgentTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentTask',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/get_agent_task',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetAgentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_task(
        self,
        request: sys_om20231230_models.GetAgentTaskRequest,
    ) -> sys_om20231230_models.GetAgentTaskResponse:
        """
        @summary 获取Agent安装任务执行状态
        
        @param request: GetAgentTaskRequest
        @return: GetAgentTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_task_with_options(request, headers, runtime)

    async def get_agent_task_async(
        self,
        request: sys_om20231230_models.GetAgentTaskRequest,
    ) -> sys_om20231230_models.GetAgentTaskResponse:
        """
        @summary 获取Agent安装任务执行状态
        
        @param request: GetAgentTaskRequest
        @return: GetAgentTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_task_with_options_async(request, headers, runtime)

    def get_diagnosis_result_with_options(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        """
        @summary 获取诊断结果
        
        @param request: GetDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_result_with_options_async(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        """
        @summary 获取诊断结果
        
        @param request: GetDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_result(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        """
        @summary 获取诊断结果
        
        @param request: GetDiagnosisResultRequest
        @return: GetDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_diagnosis_result_with_options(request, headers, runtime)

    async def get_diagnosis_result_async(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        """
        @summary 获取诊断结果
        
        @param request: GetDiagnosisResultRequest
        @return: GetDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_diagnosis_result_with_options_async(request, headers, runtime)

    def get_health_percentage_with_options(
        self,
        request: sys_om20231230_models.GetHealthPercentageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHealthPercentageResponse:
        """
        @summary 获取一段时间的节点/pod健康度比例
        
        @param request: GetHealthPercentageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHealthPercentageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthPercentage',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/health_percentage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHealthPercentageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_percentage_with_options_async(
        self,
        request: sys_om20231230_models.GetHealthPercentageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHealthPercentageResponse:
        """
        @summary 获取一段时间的节点/pod健康度比例
        
        @param request: GetHealthPercentageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHealthPercentageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthPercentage',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/health_percentage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHealthPercentageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_percentage(
        self,
        request: sys_om20231230_models.GetHealthPercentageRequest,
    ) -> sys_om20231230_models.GetHealthPercentageResponse:
        """
        @summary 获取一段时间的节点/pod健康度比例
        
        @param request: GetHealthPercentageRequest
        @return: GetHealthPercentageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_health_percentage_with_options(request, headers, runtime)

    async def get_health_percentage_async(
        self,
        request: sys_om20231230_models.GetHealthPercentageRequest,
    ) -> sys_om20231230_models.GetHealthPercentageResponse:
        """
        @summary 获取一段时间的节点/pod健康度比例
        
        @param request: GetHealthPercentageRequest
        @return: GetHealthPercentageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_health_percentage_with_options_async(request, headers, runtime)

    def get_host_count_with_options(
        self,
        request: sys_om20231230_models.GetHostCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHostCountResponse:
        """
        @summary 获取集群节点数量
        
        @param request: GetHostCountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostCount',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/host_count',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHostCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_count_with_options_async(
        self,
        request: sys_om20231230_models.GetHostCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHostCountResponse:
        """
        @summary 获取集群节点数量
        
        @param request: GetHostCountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostCount',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/host_count',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHostCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_count(
        self,
        request: sys_om20231230_models.GetHostCountRequest,
    ) -> sys_om20231230_models.GetHostCountResponse:
        """
        @summary 获取集群节点数量
        
        @param request: GetHostCountRequest
        @return: GetHostCountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_count_with_options(request, headers, runtime)

    async def get_host_count_async(
        self,
        request: sys_om20231230_models.GetHostCountRequest,
    ) -> sys_om20231230_models.GetHostCountResponse:
        """
        @summary 获取集群节点数量
        
        @param request: GetHostCountRequest
        @return: GetHostCountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_host_count_with_options_async(request, headers, runtime)

    def get_hotspot_analysis_with_options(
        self,
        request: sys_om20231230_models.GetHotspotAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotAnalysisResponse:
        """
        @summary 获取热定分析结果
        
        @param request: GetHotspotAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['appType'] = request.app_type
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.pid):
            body['pid'] = request.pid
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_analysis_with_options_async(
        self,
        request: sys_om20231230_models.GetHotspotAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotAnalysisResponse:
        """
        @summary 获取热定分析结果
        
        @param request: GetHotspotAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['appType'] = request.app_type
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.pid):
            body['pid'] = request.pid
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_analysis(
        self,
        request: sys_om20231230_models.GetHotspotAnalysisRequest,
    ) -> sys_om20231230_models.GetHotspotAnalysisResponse:
        """
        @summary 获取热定分析结果
        
        @param request: GetHotspotAnalysisRequest
        @return: GetHotspotAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hotspot_analysis_with_options(request, headers, runtime)

    async def get_hotspot_analysis_async(
        self,
        request: sys_om20231230_models.GetHotspotAnalysisRequest,
    ) -> sys_om20231230_models.GetHotspotAnalysisResponse:
        """
        @summary 获取热定分析结果
        
        @param request: GetHotspotAnalysisRequest
        @return: GetHotspotAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hotspot_analysis_with_options_async(request, headers, runtime)

    def get_hotspot_instance_list_with_options(
        self,
        request: sys_om20231230_models.GetHotspotInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotInstanceListResponse:
        """
        @summary 获取热点实例列表
        
        @param request: GetHotspotInstanceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotInstanceListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotInstanceList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_instance_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_instance_list_with_options_async(
        self,
        request: sys_om20231230_models.GetHotspotInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotInstanceListResponse:
        """
        @summary 获取热点实例列表
        
        @param request: GetHotspotInstanceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotInstanceListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotInstanceList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_instance_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_instance_list(
        self,
        request: sys_om20231230_models.GetHotspotInstanceListRequest,
    ) -> sys_om20231230_models.GetHotspotInstanceListResponse:
        """
        @summary 获取热点实例列表
        
        @param request: GetHotspotInstanceListRequest
        @return: GetHotspotInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hotspot_instance_list_with_options(request, headers, runtime)

    async def get_hotspot_instance_list_async(
        self,
        request: sys_om20231230_models.GetHotspotInstanceListRequest,
    ) -> sys_om20231230_models.GetHotspotInstanceListResponse:
        """
        @summary 获取热点实例列表
        
        @param request: GetHotspotInstanceListRequest
        @return: GetHotspotInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hotspot_instance_list_with_options_async(request, headers, runtime)

    def get_hotspot_pid_list_with_options(
        self,
        request: sys_om20231230_models.GetHotspotPidListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotPidListResponse:
        """
        @summary 获取某个实例的pid列表
        
        @param request: GetHotspotPidListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotPidListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotPidList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_pid_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotPidListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_pid_list_with_options_async(
        self,
        request: sys_om20231230_models.GetHotspotPidListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotPidListResponse:
        """
        @summary 获取某个实例的pid列表
        
        @param request: GetHotspotPidListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotPidListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotPidList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_pid_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotPidListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_pid_list(
        self,
        request: sys_om20231230_models.GetHotspotPidListRequest,
    ) -> sys_om20231230_models.GetHotspotPidListResponse:
        """
        @summary 获取某个实例的pid列表
        
        @param request: GetHotspotPidListRequest
        @return: GetHotspotPidListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hotspot_pid_list_with_options(request, headers, runtime)

    async def get_hotspot_pid_list_async(
        self,
        request: sys_om20231230_models.GetHotspotPidListRequest,
    ) -> sys_om20231230_models.GetHotspotPidListResponse:
        """
        @summary 获取某个实例的pid列表
        
        @param request: GetHotspotPidListRequest
        @return: GetHotspotPidListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hotspot_pid_list_with_options_async(request, headers, runtime)

    def get_list_record_with_options(
        self,
        request: sys_om20231230_models.GetListRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetListRecordResponse:
        """
        @summary AI Infra获取分析记录列表
        
        @param request: GetListRecordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListRecord',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/app_observ/aiAnalysis/list_record',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetListRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_list_record_with_options_async(
        self,
        request: sys_om20231230_models.GetListRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetListRecordResponse:
        """
        @summary AI Infra获取分析记录列表
        
        @param request: GetListRecordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListRecord',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/app_observ/aiAnalysis/list_record',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetListRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_list_record(
        self,
        request: sys_om20231230_models.GetListRecordRequest,
    ) -> sys_om20231230_models.GetListRecordResponse:
        """
        @summary AI Infra获取分析记录列表
        
        @param request: GetListRecordRequest
        @return: GetListRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_list_record_with_options(request, headers, runtime)

    async def get_list_record_async(
        self,
        request: sys_om20231230_models.GetListRecordRequest,
    ) -> sys_om20231230_models.GetListRecordResponse:
        """
        @summary AI Infra获取分析记录列表
        
        @param request: GetListRecordRequest
        @return: GetListRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_list_record_with_options_async(request, headers, runtime)

    def get_problem_percentage_with_options(
        self,
        request: sys_om20231230_models.GetProblemPercentageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetProblemPercentageResponse:
        """
        @summary 获取一定时间内集群中节点/节点中pod异常问题占比
        
        @param request: GetProblemPercentageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProblemPercentageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProblemPercentage',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/problem_percentage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetProblemPercentageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_percentage_with_options_async(
        self,
        request: sys_om20231230_models.GetProblemPercentageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetProblemPercentageResponse:
        """
        @summary 获取一定时间内集群中节点/节点中pod异常问题占比
        
        @param request: GetProblemPercentageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProblemPercentageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProblemPercentage',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/problem_percentage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetProblemPercentageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem_percentage(
        self,
        request: sys_om20231230_models.GetProblemPercentageRequest,
    ) -> sys_om20231230_models.GetProblemPercentageResponse:
        """
        @summary 获取一定时间内集群中节点/节点中pod异常问题占比
        
        @param request: GetProblemPercentageRequest
        @return: GetProblemPercentageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_percentage_with_options(request, headers, runtime)

    async def get_problem_percentage_async(
        self,
        request: sys_om20231230_models.GetProblemPercentageRequest,
    ) -> sys_om20231230_models.GetProblemPercentageResponse:
        """
        @summary 获取一定时间内集群中节点/节点中pod异常问题占比
        
        @param request: GetProblemPercentageRequest
        @return: GetProblemPercentageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_problem_percentage_with_options_async(request, headers, runtime)

    def get_range_score_with_options(
        self,
        request: sys_om20231230_models.GetRangeScoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetRangeScoreResponse:
        """
        @summary 获取健康分趋势
        
        @param request: GetRangeScoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRangeScoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRangeScore',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/score',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetRangeScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_range_score_with_options_async(
        self,
        request: sys_om20231230_models.GetRangeScoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetRangeScoreResponse:
        """
        @summary 获取健康分趋势
        
        @param request: GetRangeScoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRangeScoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRangeScore',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/score',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetRangeScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_range_score(
        self,
        request: sys_om20231230_models.GetRangeScoreRequest,
    ) -> sys_om20231230_models.GetRangeScoreResponse:
        """
        @summary 获取健康分趋势
        
        @param request: GetRangeScoreRequest
        @return: GetRangeScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_range_score_with_options(request, headers, runtime)

    async def get_range_score_async(
        self,
        request: sys_om20231230_models.GetRangeScoreRequest,
    ) -> sys_om20231230_models.GetRangeScoreResponse:
        """
        @summary 获取健康分趋势
        
        @param request: GetRangeScoreRequest
        @return: GetRangeScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_range_score_with_options_async(request, headers, runtime)

    def get_resources_with_options(
        self,
        request: sys_om20231230_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetResourcesResponse:
        """
        @summary 获取集群/节点资源实时使用情况
        
        @param request: GetResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResources',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/instant/resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resources_with_options_async(
        self,
        request: sys_om20231230_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetResourcesResponse:
        """
        @summary 获取集群/节点资源实时使用情况
        
        @param request: GetResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResources',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/instant/resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resources(
        self,
        request: sys_om20231230_models.GetResourcesRequest,
    ) -> sys_om20231230_models.GetResourcesResponse:
        """
        @summary 获取集群/节点资源实时使用情况
        
        @param request: GetResourcesRequest
        @return: GetResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resources_with_options(request, headers, runtime)

    async def get_resources_async(
        self,
        request: sys_om20231230_models.GetResourcesRequest,
    ) -> sys_om20231230_models.GetResourcesResponse:
        """
        @summary 获取集群/节点资源实时使用情况
        
        @param request: GetResourcesRequest
        @return: GetResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resources_with_options_async(request, headers, runtime)

    def install_agent_with_options(
        self,
        request: sys_om20231230_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InstallAgentResponse:
        """
        @summary 在指定的实例上安装 Agent
        
        @param request: InstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.install_type):
            body['install_type'] = request.install_type
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/install_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_with_options_async(
        self,
        request: sys_om20231230_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InstallAgentResponse:
        """
        @summary 在指定的实例上安装 Agent
        
        @param request: InstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.install_type):
            body['install_type'] = request.install_type
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/install_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent(
        self,
        request: sys_om20231230_models.InstallAgentRequest,
    ) -> sys_om20231230_models.InstallAgentResponse:
        """
        @summary 在指定的实例上安装 Agent
        
        @param request: InstallAgentRequest
        @return: InstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_agent_with_options(request, headers, runtime)

    async def install_agent_async(
        self,
        request: sys_om20231230_models.InstallAgentRequest,
    ) -> sys_om20231230_models.InstallAgentResponse:
        """
        @summary 在指定的实例上安装 Agent
        
        @param request: InstallAgentRequest
        @return: InstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_agent_with_options_async(request, headers, runtime)

    def invoke_anomaly_diagnosis_with_options(
        self,
        request: sys_om20231230_models.InvokeAnomalyDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeAnomalyDiagnosisResponse:
        """
        @summary 异常项诊断跳转
        
        @param request: InvokeAnomalyDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeAnomalyDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeAnomalyDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/diagnosis/invoke_anomaly_diagnose',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeAnomalyDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_anomaly_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.InvokeAnomalyDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeAnomalyDiagnosisResponse:
        """
        @summary 异常项诊断跳转
        
        @param request: InvokeAnomalyDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeAnomalyDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeAnomalyDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/diagnosis/invoke_anomaly_diagnose',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeAnomalyDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_anomaly_diagnosis(
        self,
        request: sys_om20231230_models.InvokeAnomalyDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeAnomalyDiagnosisResponse:
        """
        @summary 异常项诊断跳转
        
        @param request: InvokeAnomalyDiagnosisRequest
        @return: InvokeAnomalyDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.invoke_anomaly_diagnosis_with_options(request, headers, runtime)

    async def invoke_anomaly_diagnosis_async(
        self,
        request: sys_om20231230_models.InvokeAnomalyDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeAnomalyDiagnosisResponse:
        """
        @summary 异常项诊断跳转
        
        @param request: InvokeAnomalyDiagnosisRequest
        @return: InvokeAnomalyDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.invoke_anomaly_diagnosis_with_options_async(request, headers, runtime)

    def invoke_diagnosis_with_options(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        """
        @summary 发起诊断
        
        @param request: InvokeDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        """
        @summary 发起诊断
        
        @param request: InvokeDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_diagnosis(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        """
        @summary 发起诊断
        
        @param request: InvokeDiagnosisRequest
        @return: InvokeDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.invoke_diagnosis_with_options(request, headers, runtime)

    async def invoke_diagnosis_async(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        """
        @summary 发起诊断
        
        @param request: InvokeDiagnosisRequest
        @return: InvokeDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.invoke_diagnosis_with_options_async(request, headers, runtime)

    def list_abnormaly_events_with_options(
        self,
        request: sys_om20231230_models.ListAbnormalyEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAbnormalyEventsResponse:
        """
        @summary 获取一定时间段内的异常事件
        
        @param request: ListAbnormalyEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAbnormalyEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod):
            query['pod'] = request.pod
        if not UtilClient.is_unset(request.show_pod):
            query['showPod'] = request.show_pod
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAbnormalyEvents',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/abnormaly_events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAbnormalyEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abnormaly_events_with_options_async(
        self,
        request: sys_om20231230_models.ListAbnormalyEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAbnormalyEventsResponse:
        """
        @summary 获取一定时间段内的异常事件
        
        @param request: ListAbnormalyEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAbnormalyEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod):
            query['pod'] = request.pod
        if not UtilClient.is_unset(request.show_pod):
            query['showPod'] = request.show_pod
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAbnormalyEvents',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/abnormaly_events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAbnormalyEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abnormaly_events(
        self,
        request: sys_om20231230_models.ListAbnormalyEventsRequest,
    ) -> sys_om20231230_models.ListAbnormalyEventsResponse:
        """
        @summary 获取一定时间段内的异常事件
        
        @param request: ListAbnormalyEventsRequest
        @return: ListAbnormalyEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abnormaly_events_with_options(request, headers, runtime)

    async def list_abnormaly_events_async(
        self,
        request: sys_om20231230_models.ListAbnormalyEventsRequest,
    ) -> sys_om20231230_models.ListAbnormalyEventsResponse:
        """
        @summary 获取一定时间段内的异常事件
        
        @param request: ListAbnormalyEventsRequest
        @return: ListAbnormalyEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abnormaly_events_with_options_async(request, headers, runtime)

    def list_agent_install_records_with_options(
        self,
        request: sys_om20231230_models.ListAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAgentInstallRecordsResponse:
        """
        @summary 列出 Agent 的安装记录
        
        @param request: ListAgentInstallRecordsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentInstallRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentInstallRecords',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_agent_install_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAgentInstallRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_install_records_with_options_async(
        self,
        request: sys_om20231230_models.ListAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAgentInstallRecordsResponse:
        """
        @summary 列出 Agent 的安装记录
        
        @param request: ListAgentInstallRecordsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentInstallRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentInstallRecords',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_agent_install_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAgentInstallRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_install_records(
        self,
        request: sys_om20231230_models.ListAgentInstallRecordsRequest,
    ) -> sys_om20231230_models.ListAgentInstallRecordsResponse:
        """
        @summary 列出 Agent 的安装记录
        
        @param request: ListAgentInstallRecordsRequest
        @return: ListAgentInstallRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agent_install_records_with_options(request, headers, runtime)

    async def list_agent_install_records_async(
        self,
        request: sys_om20231230_models.ListAgentInstallRecordsRequest,
    ) -> sys_om20231230_models.ListAgentInstallRecordsResponse:
        """
        @summary 列出 Agent 的安装记录
        
        @param request: ListAgentInstallRecordsRequest
        @return: ListAgentInstallRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agent_install_records_with_options_async(request, headers, runtime)

    def list_agents_with_options(
        self,
        request: sys_om20231230_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAgentsResponse:
        """
        @summary 获取 Agent 列表
        
        @param request: ListAgentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgents',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_agents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: sys_om20231230_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListAgentsResponse:
        """
        @summary 获取 Agent 列表
        
        @param request: ListAgentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgents',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_agents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: sys_om20231230_models.ListAgentsRequest,
    ) -> sys_om20231230_models.ListAgentsResponse:
        """
        @summary 获取 Agent 列表
        
        @param request: ListAgentsRequest
        @return: ListAgentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agents_with_options(request, headers, runtime)

    async def list_agents_async(
        self,
        request: sys_om20231230_models.ListAgentsRequest,
    ) -> sys_om20231230_models.ListAgentsResponse:
        """
        @summary 获取 Agent 列表
        
        @param request: ListAgentsRequest
        @return: ListAgentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agents_with_options_async(request, headers, runtime)

    def list_instance_health_with_options(
        self,
        request: sys_om20231230_models.ListInstanceHealthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstanceHealthResponse:
        """
        @summary 获取一定时间内集群节点/Pod健康度列表
        
        @param request: ListInstanceHealthRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceHealth',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/instance_health_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_health_with_options_async(
        self,
        request: sys_om20231230_models.ListInstanceHealthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstanceHealthResponse:
        """
        @summary 获取一定时间内集群节点/Pod健康度列表
        
        @param request: ListInstanceHealthRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceHealth',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/range/instance_health_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstanceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_health(
        self,
        request: sys_om20231230_models.ListInstanceHealthRequest,
    ) -> sys_om20231230_models.ListInstanceHealthResponse:
        """
        @summary 获取一定时间内集群节点/Pod健康度列表
        
        @param request: ListInstanceHealthRequest
        @return: ListInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_health_with_options(request, headers, runtime)

    async def list_instance_health_async(
        self,
        request: sys_om20231230_models.ListInstanceHealthRequest,
    ) -> sys_om20231230_models.ListInstanceHealthResponse:
        """
        @summary 获取一定时间内集群节点/Pod健康度列表
        
        @param request: ListInstanceHealthRequest
        @return: ListInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_health_with_options_async(request, headers, runtime)

    def start_aianalysis_with_options(
        self,
        request: sys_om20231230_models.StartAIAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.StartAIAnalysisResponse:
        """
        @summary 启动AI作业分析
        
        @param request: StartAIAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAIAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.comms):
            body['comms'] = request.comms
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.pids):
            body['pids'] = request.pids
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAIAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/start_ai_analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.StartAIAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aianalysis_with_options_async(
        self,
        request: sys_om20231230_models.StartAIAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.StartAIAnalysisResponse:
        """
        @summary 启动AI作业分析
        
        @param request: StartAIAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAIAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.comms):
            body['comms'] = request.comms
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.pids):
            body['pids'] = request.pids
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAIAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/start_ai_analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.StartAIAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aianalysis(
        self,
        request: sys_om20231230_models.StartAIAnalysisRequest,
    ) -> sys_om20231230_models.StartAIAnalysisResponse:
        """
        @summary 启动AI作业分析
        
        @param request: StartAIAnalysisRequest
        @return: StartAIAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_aianalysis_with_options(request, headers, runtime)

    async def start_aianalysis_async(
        self,
        request: sys_om20231230_models.StartAIAnalysisRequest,
    ) -> sys_om20231230_models.StartAIAnalysisResponse:
        """
        @summary 启动AI作业分析
        
        @param request: StartAIAnalysisRequest
        @return: StartAIAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_aianalysis_with_options_async(request, headers, runtime)

    def uninstall_agent_with_options(
        self,
        request: sys_om20231230_models.UninstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UninstallAgentResponse:
        """
        @summary 卸载 SysOM Agent
        
        @param request: UninstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UninstallAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/uninstall_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UninstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_agent_with_options_async(
        self,
        request: sys_om20231230_models.UninstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UninstallAgentResponse:
        """
        @summary 卸载 SysOM Agent
        
        @param request: UninstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UninstallAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/uninstall_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UninstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_agent(
        self,
        request: sys_om20231230_models.UninstallAgentRequest,
    ) -> sys_om20231230_models.UninstallAgentResponse:
        """
        @summary 卸载 SysOM Agent
        
        @param request: UninstallAgentRequest
        @return: UninstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_agent_with_options(request, headers, runtime)

    async def uninstall_agent_async(
        self,
        request: sys_om20231230_models.UninstallAgentRequest,
    ) -> sys_om20231230_models.UninstallAgentResponse:
        """
        @summary 卸载 SysOM Agent
        
        @param request: UninstallAgentRequest
        @return: UninstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_agent_with_options_async(request, headers, runtime)

    def upgrade_agent_with_options(
        self,
        request: sys_om20231230_models.UpgradeAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpgradeAgentResponse:
        """
        @summary 更新 SysOM Agent
        
        @param request: UpgradeAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/upgrade_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpgradeAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_agent_with_options_async(
        self,
        request: sys_om20231230_models.UpgradeAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpgradeAgentResponse:
        """
        @summary 更新 SysOM Agent
        
        @param request: UpgradeAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAgentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeAgent',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/upgrade_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpgradeAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_agent(
        self,
        request: sys_om20231230_models.UpgradeAgentRequest,
    ) -> sys_om20231230_models.UpgradeAgentResponse:
        """
        @summary 更新 SysOM Agent
        
        @param request: UpgradeAgentRequest
        @return: UpgradeAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_agent_with_options(request, headers, runtime)

    async def upgrade_agent_async(
        self,
        request: sys_om20231230_models.UpgradeAgentRequest,
    ) -> sys_om20231230_models.UpgradeAgentResponse:
        """
        @summary 更新 SysOM Agent
        
        @param request: UpgradeAgentRequest
        @return: UpgradeAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_agent_with_options_async(request, headers, runtime)
