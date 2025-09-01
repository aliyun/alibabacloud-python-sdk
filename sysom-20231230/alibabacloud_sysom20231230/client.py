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

    def check_instance_support_with_options(
        self,
        request: sys_om20231230_models.CheckInstanceSupportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.CheckInstanceSupportResponse:
        """
        @summary 检查目标实例是否被 SysOM 支持
        
        @param request: CheckInstanceSupportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceSupportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceSupport',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/supportInstanceList/checkInstanceSupport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.CheckInstanceSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_support_with_options_async(
        self,
        request: sys_om20231230_models.CheckInstanceSupportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.CheckInstanceSupportResponse:
        """
        @summary 检查目标实例是否被 SysOM 支持
        
        @param request: CheckInstanceSupportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceSupportResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceSupport',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/supportInstanceList/checkInstanceSupport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.CheckInstanceSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_support(
        self,
        request: sys_om20231230_models.CheckInstanceSupportRequest,
    ) -> sys_om20231230_models.CheckInstanceSupportResponse:
        """
        @summary 检查目标实例是否被 SysOM 支持
        
        @param request: CheckInstanceSupportRequest
        @return: CheckInstanceSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_support_with_options(request, headers, runtime)

    async def check_instance_support_async(
        self,
        request: sys_om20231230_models.CheckInstanceSupportRequest,
    ) -> sys_om20231230_models.CheckInstanceSupportResponse:
        """
        @summary 检查目标实例是否被 SysOM 支持
        
        @param request: CheckInstanceSupportRequest
        @return: CheckInstanceSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_support_with_options_async(request, headers, runtime)

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

    def generate_copilot_stream_response_with_options(
        self,
        request: sys_om20231230_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GenerateCopilotStreamResponseResponse:
        """
        @summary 流式copilot服务接口
        
        @param request: GenerateCopilotStreamResponseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCopilotStreamResponseResponse
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
            action='GenerateCopilotStreamResponse',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/generate_copilot_stream_response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GenerateCopilotStreamResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_copilot_stream_response_with_options_async(
        self,
        request: sys_om20231230_models.GenerateCopilotStreamResponseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GenerateCopilotStreamResponseResponse:
        """
        @summary 流式copilot服务接口
        
        @param request: GenerateCopilotStreamResponseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCopilotStreamResponseResponse
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
            action='GenerateCopilotStreamResponse',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/generate_copilot_stream_response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GenerateCopilotStreamResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_copilot_stream_response(
        self,
        request: sys_om20231230_models.GenerateCopilotStreamResponseRequest,
    ) -> sys_om20231230_models.GenerateCopilotStreamResponseResponse:
        """
        @summary 流式copilot服务接口
        
        @param request: GenerateCopilotStreamResponseRequest
        @return: GenerateCopilotStreamResponseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_copilot_stream_response_with_options(request, headers, runtime)

    async def generate_copilot_stream_response_async(
        self,
        request: sys_om20231230_models.GenerateCopilotStreamResponseRequest,
    ) -> sys_om20231230_models.GenerateCopilotStreamResponseResponse:
        """
        @summary 流式copilot服务接口
        
        @param request: GenerateCopilotStreamResponseRequest
        @return: GenerateCopilotStreamResponseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_copilot_stream_response_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
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
        if not UtilClient.is_unset(request.level):
            query['level'] = request.level
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

    def get_copilot_history_with_options(
        self,
        request: sys_om20231230_models.GetCopilotHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetCopilotHistoryResponse:
        """
        @summary 获取copilot历史聊天记录
        
        @param request: GetCopilotHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCopilotHistoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCopilotHistory',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/get_copilot_history',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetCopilotHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_copilot_history_with_options_async(
        self,
        request: sys_om20231230_models.GetCopilotHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetCopilotHistoryResponse:
        """
        @summary 获取copilot历史聊天记录
        
        @param request: GetCopilotHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCopilotHistoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCopilotHistory',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/copilot/get_copilot_history',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetCopilotHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_copilot_history(
        self,
        request: sys_om20231230_models.GetCopilotHistoryRequest,
    ) -> sys_om20231230_models.GetCopilotHistoryResponse:
        """
        @summary 获取copilot历史聊天记录
        
        @param request: GetCopilotHistoryRequest
        @return: GetCopilotHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_copilot_history_with_options(request, headers, runtime)

    async def get_copilot_history_async(
        self,
        request: sys_om20231230_models.GetCopilotHistoryRequest,
    ) -> sys_om20231230_models.GetCopilotHistoryResponse:
        """
        @summary 获取copilot历史聊天记录
        
        @param request: GetCopilotHistoryRequest
        @return: GetCopilotHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_copilot_history_with_options_async(request, headers, runtime)

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

    def get_hot_spot_uniq_list_with_options(
        self,
        request: sys_om20231230_models.GetHotSpotUniqListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotSpotUniqListResponse:
        """
        @summary 获取实例下的某个字段列表
        
        @param request: GetHotSpotUniqListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotSpotUniqListResponse
        """
        UtilClient.validate_model(request)
        body = {}
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
        if not UtilClient.is_unset(request.uniq):
            body['uniq'] = request.uniq
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotSpotUniqList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/livetrace_proxy/hotspot_uniq_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotSpotUniqListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_spot_uniq_list_with_options_async(
        self,
        request: sys_om20231230_models.GetHotSpotUniqListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotSpotUniqListResponse:
        """
        @summary 获取实例下的某个字段列表
        
        @param request: GetHotSpotUniqListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotSpotUniqListResponse
        """
        UtilClient.validate_model(request)
        body = {}
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
        if not UtilClient.is_unset(request.uniq):
            body['uniq'] = request.uniq
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotSpotUniqList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/livetrace_proxy/hotspot_uniq_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotSpotUniqListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_spot_uniq_list(
        self,
        request: sys_om20231230_models.GetHotSpotUniqListRequest,
    ) -> sys_om20231230_models.GetHotSpotUniqListResponse:
        """
        @summary 获取实例下的某个字段列表
        
        @param request: GetHotSpotUniqListRequest
        @return: GetHotSpotUniqListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hot_spot_uniq_list_with_options(request, headers, runtime)

    async def get_hot_spot_uniq_list_async(
        self,
        request: sys_om20231230_models.GetHotSpotUniqListRequest,
    ) -> sys_om20231230_models.GetHotSpotUniqListResponse:
        """
        @summary 获取实例下的某个字段列表
        
        @param request: GetHotSpotUniqListRequest
        @return: GetHotSpotUniqListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hot_spot_uniq_list_with_options_async(request, headers, runtime)

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

    def get_hotspot_compare_with_options(
        self,
        request: sys_om20231230_models.GetHotspotCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotCompareResponse:
        """
        @summary 热点对比
        
        @param request: GetHotspotCompareRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotCompareResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_1end):
            body['beg1_end'] = request.beg_1end
        if not UtilClient.is_unset(request.beg_1start):
            body['beg1_start'] = request.beg_1start
        if not UtilClient.is_unset(request.beg_2end):
            body['beg2_end'] = request.beg_2end
        if not UtilClient.is_unset(request.beg_2start):
            body['beg2_start'] = request.beg_2start
        if not UtilClient.is_unset(request.hot_type):
            body['hot_type'] = request.hot_type
        if not UtilClient.is_unset(request.instance_1):
            body['instance1'] = request.instance_1
        if not UtilClient.is_unset(request.instance_2):
            body['instance2'] = request.instance_2
        if not UtilClient.is_unset(request.pid_1):
            body['pid1'] = request.pid_1
        if not UtilClient.is_unset(request.pid_2):
            body['pid2'] = request.pid_2
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotCompare',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_compare_with_options_async(
        self,
        request: sys_om20231230_models.GetHotspotCompareRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotCompareResponse:
        """
        @summary 热点对比
        
        @param request: GetHotspotCompareRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotCompareResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_1end):
            body['beg1_end'] = request.beg_1end
        if not UtilClient.is_unset(request.beg_1start):
            body['beg1_start'] = request.beg_1start
        if not UtilClient.is_unset(request.beg_2end):
            body['beg2_end'] = request.beg_2end
        if not UtilClient.is_unset(request.beg_2start):
            body['beg2_start'] = request.beg_2start
        if not UtilClient.is_unset(request.hot_type):
            body['hot_type'] = request.hot_type
        if not UtilClient.is_unset(request.instance_1):
            body['instance1'] = request.instance_1
        if not UtilClient.is_unset(request.instance_2):
            body['instance2'] = request.instance_2
        if not UtilClient.is_unset(request.pid_1):
            body['pid1'] = request.pid_1
        if not UtilClient.is_unset(request.pid_2):
            body['pid2'] = request.pid_2
        if not UtilClient.is_unset(request.table):
            body['table'] = request.table
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHotspotCompare',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_compare(
        self,
        request: sys_om20231230_models.GetHotspotCompareRequest,
    ) -> sys_om20231230_models.GetHotspotCompareResponse:
        """
        @summary 热点对比
        
        @param request: GetHotspotCompareRequest
        @return: GetHotspotCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hotspot_compare_with_options(request, headers, runtime)

    async def get_hotspot_compare_async(
        self,
        request: sys_om20231230_models.GetHotspotCompareRequest,
    ) -> sys_om20231230_models.GetHotspotCompareResponse:
        """
        @summary 热点对比
        
        @param request: GetHotspotCompareRequest
        @return: GetHotspotCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hotspot_compare_with_options_async(request, headers, runtime)

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

    def get_hotspot_tracking_with_options(
        self,
        request: sys_om20231230_models.GetHotspotTrackingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotTrackingResponse:
        """
        @summary 发起热点追踪
        
        @param request: GetHotspotTrackingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotTrackingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.hot_type):
            body['hot_type'] = request.hot_type
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
            action='GetHotspotTracking',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_tracking',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotTrackingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_tracking_with_options_async(
        self,
        request: sys_om20231230_models.GetHotspotTrackingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetHotspotTrackingResponse:
        """
        @summary 发起热点追踪
        
        @param request: GetHotspotTrackingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotspotTrackingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.beg_end):
            body['beg_end'] = request.beg_end
        if not UtilClient.is_unset(request.beg_start):
            body['beg_start'] = request.beg_start
        if not UtilClient.is_unset(request.hot_type):
            body['hot_type'] = request.hot_type
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
            action='GetHotspotTracking',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/livetrace_hotspot_tracking',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetHotspotTrackingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_tracking(
        self,
        request: sys_om20231230_models.GetHotspotTrackingRequest,
    ) -> sys_om20231230_models.GetHotspotTrackingResponse:
        """
        @summary 发起热点追踪
        
        @param request: GetHotspotTrackingRequest
        @return: GetHotspotTrackingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hotspot_tracking_with_options(request, headers, runtime)

    async def get_hotspot_tracking_async(
        self,
        request: sys_om20231230_models.GetHotspotTrackingRequest,
    ) -> sys_om20231230_models.GetHotspotTrackingResponse:
        """
        @summary 发起热点追踪
        
        @param request: GetHotspotTrackingRequest
        @return: GetHotspotTrackingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hotspot_tracking_with_options_async(request, headers, runtime)

    def get_instant_score_with_options(
        self,
        request: sys_om20231230_models.GetInstantScoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetInstantScoreResponse:
        """
        @summary 获取实时集群/节点健康度分数
        
        @param request: GetInstantScoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstantScoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstantScore',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/instant/score',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetInstantScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instant_score_with_options_async(
        self,
        request: sys_om20231230_models.GetInstantScoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetInstantScoreResponse:
        """
        @summary 获取实时集群/节点健康度分数
        
        @param request: GetInstantScoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstantScoreResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster):
            query['cluster'] = request.cluster
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstantScore',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/cluster_health/instant/score',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetInstantScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instant_score(
        self,
        request: sys_om20231230_models.GetInstantScoreRequest,
    ) -> sys_om20231230_models.GetInstantScoreResponse:
        """
        @summary 获取实时集群/节点健康度分数
        
        @param request: GetInstantScoreRequest
        @return: GetInstantScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instant_score_with_options(request, headers, runtime)

    async def get_instant_score_async(
        self,
        request: sys_om20231230_models.GetInstantScoreRequest,
    ) -> sys_om20231230_models.GetInstantScoreResponse:
        """
        @summary 获取实时集群/节点健康度分数
        
        @param request: GetInstantScoreRequest
        @return: GetInstantScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instant_score_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
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
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
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

    def get_service_func_status_with_options(
        self,
        tmp_req: sys_om20231230_models.GetServiceFuncStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetServiceFuncStatusResponse:
        """
        @summary 获取功能模块配置
        
        @param tmp_req: GetServiceFuncStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceFuncStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.GetServiceFuncStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.params_shrink):
            query['params'] = request.params_shrink
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceFuncStatus',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/func-switch/get-service-func-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetServiceFuncStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_func_status_with_options_async(
        self,
        tmp_req: sys_om20231230_models.GetServiceFuncStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetServiceFuncStatusResponse:
        """
        @summary 获取功能模块配置
        
        @param tmp_req: GetServiceFuncStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceFuncStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.GetServiceFuncStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.params_shrink):
            query['params'] = request.params_shrink
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceFuncStatus',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/func-switch/get-service-func-status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetServiceFuncStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_func_status(
        self,
        request: sys_om20231230_models.GetServiceFuncStatusRequest,
    ) -> sys_om20231230_models.GetServiceFuncStatusResponse:
        """
        @summary 获取功能模块配置
        
        @param request: GetServiceFuncStatusRequest
        @return: GetServiceFuncStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_func_status_with_options(request, headers, runtime)

    async def get_service_func_status_async(
        self,
        request: sys_om20231230_models.GetServiceFuncStatusRequest,
    ) -> sys_om20231230_models.GetServiceFuncStatusResponse:
        """
        @summary 获取功能模块配置
        
        @param request: GetServiceFuncStatusRequest
        @return: GetServiceFuncStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_func_status_with_options_async(request, headers, runtime)

    def initial_sysom_with_options(
        self,
        request: sys_om20231230_models.InitialSysomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InitialSysomResponse:
        """
        @summary 初始化SysOM，确保角色存在
        
        @param request: InitialSysomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitialSysomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_only):
            body['check_only'] = request.check_only
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitialSysom',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/initial',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InitialSysomResponse(),
            self.call_api(params, req, runtime)
        )

    async def initial_sysom_with_options_async(
        self,
        request: sys_om20231230_models.InitialSysomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InitialSysomResponse:
        """
        @summary 初始化SysOM，确保角色存在
        
        @param request: InitialSysomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitialSysomResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_only):
            body['check_only'] = request.check_only
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitialSysom',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/initial',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InitialSysomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initial_sysom(
        self,
        request: sys_om20231230_models.InitialSysomRequest,
    ) -> sys_om20231230_models.InitialSysomResponse:
        """
        @summary 初始化SysOM，确保角色存在
        
        @param request: InitialSysomRequest
        @return: InitialSysomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initial_sysom_with_options(request, headers, runtime)

    async def initial_sysom_async(
        self,
        request: sys_om20231230_models.InitialSysomRequest,
    ) -> sys_om20231230_models.InitialSysomResponse:
        """
        @summary 初始化SysOM，确保角色存在
        
        @param request: InitialSysomRequest
        @return: InitialSysomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.initial_sysom_with_options_async(request, headers, runtime)

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

    def install_agent_for_cluster_with_options(
        self,
        request: sys_om20231230_models.InstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InstallAgentForClusterResponse:
        """
        @summary 给集群安装组件
        
        @param request: InstallAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.config_id):
            body['config_id'] = request.config_id
        if not UtilClient.is_unset(request.grayscale_config):
            body['grayscale_config'] = request.grayscale_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/install_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InstallAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_for_cluster_with_options_async(
        self,
        request: sys_om20231230_models.InstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InstallAgentForClusterResponse:
        """
        @summary 给集群安装组件
        
        @param request: InstallAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.config_id):
            body['config_id'] = request.config_id
        if not UtilClient.is_unset(request.grayscale_config):
            body['grayscale_config'] = request.grayscale_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/install_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InstallAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent_for_cluster(
        self,
        request: sys_om20231230_models.InstallAgentForClusterRequest,
    ) -> sys_om20231230_models.InstallAgentForClusterResponse:
        """
        @summary 给集群安装组件
        
        @param request: InstallAgentForClusterRequest
        @return: InstallAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_agent_for_cluster_with_options(request, headers, runtime)

    async def install_agent_for_cluster_async(
        self,
        request: sys_om20231230_models.InstallAgentForClusterRequest,
    ) -> sys_om20231230_models.InstallAgentForClusterResponse:
        """
        @summary 给集群安装组件
        
        @param request: InstallAgentForClusterRequest
        @return: InstallAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_agent_for_cluster_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.event):
            query['event'] = request.event
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
        if not UtilClient.is_unset(request.event):
            query['event'] = request.event
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
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
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
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
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

    def list_cluster_agent_install_records_with_options(
        self,
        request: sys_om20231230_models.ListClusterAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListClusterAgentInstallRecordsResponse:
        """
        @summary 获取集群组件安装记录
        
        @param request: ListClusterAgentInstallRecordsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterAgentInstallRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_config_id):
            query['agent_config_id'] = request.agent_config_id
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterAgentInstallRecords',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_cluster_agent_install_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListClusterAgentInstallRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_agent_install_records_with_options_async(
        self,
        request: sys_om20231230_models.ListClusterAgentInstallRecordsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListClusterAgentInstallRecordsResponse:
        """
        @summary 获取集群组件安装记录
        
        @param request: ListClusterAgentInstallRecordsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterAgentInstallRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_config_id):
            query['agent_config_id'] = request.agent_config_id
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_version):
            query['plugin_version'] = request.plugin_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterAgentInstallRecords',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/list_cluster_agent_install_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListClusterAgentInstallRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_agent_install_records(
        self,
        request: sys_om20231230_models.ListClusterAgentInstallRecordsRequest,
    ) -> sys_om20231230_models.ListClusterAgentInstallRecordsResponse:
        """
        @summary 获取集群组件安装记录
        
        @param request: ListClusterAgentInstallRecordsRequest
        @return: ListClusterAgentInstallRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_agent_install_records_with_options(request, headers, runtime)

    async def list_cluster_agent_install_records_async(
        self,
        request: sys_om20231230_models.ListClusterAgentInstallRecordsRequest,
    ) -> sys_om20231230_models.ListClusterAgentInstallRecordsResponse:
        """
        @summary 获取集群组件安装记录
        
        @param request: ListClusterAgentInstallRecordsRequest
        @return: ListClusterAgentInstallRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_agent_install_records_with_options_async(request, headers, runtime)

    def list_clusters_with_options(
        self,
        request: sys_om20231230_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListClustersResponse:
        """
        @summary 获取当前用户的所有集群
        
        @param request: ListClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_status):
            query['cluster_status'] = request.cluster_status
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/cluster/list_clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: sys_om20231230_models.ListClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListClustersResponse:
        """
        @summary 获取当前用户的所有集群
        
        @param request: ListClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_status):
            query['cluster_status'] = request.cluster_status
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/cluster/list_clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: sys_om20231230_models.ListClustersRequest,
    ) -> sys_om20231230_models.ListClustersResponse:
        """
        @summary 获取当前用户的所有集群
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_clusters_with_options(request, headers, runtime)

    async def list_clusters_async(
        self,
        request: sys_om20231230_models.ListClustersRequest,
    ) -> sys_om20231230_models.ListClustersResponse:
        """
        @summary 获取当前用户的所有集群
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_clusters_with_options_async(request, headers, runtime)

    def list_diagnosis_with_options(
        self,
        request: sys_om20231230_models.ListDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListDiagnosisResponse:
        """
        @summary 获取诊断历史记录列表
        
        @param request: ListDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/list_diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.ListDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListDiagnosisResponse:
        """
        @summary 获取诊断历史记录列表
        
        @param request: ListDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/list_diagnosis',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnosis(
        self,
        request: sys_om20231230_models.ListDiagnosisRequest,
    ) -> sys_om20231230_models.ListDiagnosisResponse:
        """
        @summary 获取诊断历史记录列表
        
        @param request: ListDiagnosisRequest
        @return: ListDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnosis_with_options(request, headers, runtime)

    async def list_diagnosis_async(
        self,
        request: sys_om20231230_models.ListDiagnosisRequest,
    ) -> sys_om20231230_models.ListDiagnosisResponse:
        """
        @summary 获取诊断历史记录列表
        
        @param request: ListDiagnosisRequest
        @return: ListDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_diagnosis_with_options_async(request, headers, runtime)

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

    def list_instance_status_with_options(
        self,
        request: sys_om20231230_models.ListInstanceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstanceStatusResponse:
        """
        @summary 获取实例状态
        
        @param request: ListInstanceStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatus',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_instance_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_status_with_options_async(
        self,
        request: sys_om20231230_models.ListInstanceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstanceStatusResponse:
        """
        @summary 获取实例状态
        
        @param request: ListInstanceStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatus',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_instance_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_status(
        self,
        request: sys_om20231230_models.ListInstanceStatusRequest,
    ) -> sys_om20231230_models.ListInstanceStatusResponse:
        """
        @summary 获取实例状态
        
        @param request: ListInstanceStatusRequest
        @return: ListInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_status_with_options(request, headers, runtime)

    async def list_instance_status_async(
        self,
        request: sys_om20231230_models.ListInstanceStatusRequest,
    ) -> sys_om20231230_models.ListInstanceStatusResponse:
        """
        @summary 获取实例状态
        
        @param request: ListInstanceStatusRequest
        @return: ListInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_status_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: sys_om20231230_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: sys_om20231230_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: sys_om20231230_models.ListInstancesRequest,
    ) -> sys_om20231230_models.ListInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: sys_om20231230_models.ListInstancesRequest,
    ) -> sys_om20231230_models.ListInstancesResponse:
        """
        @summary 获取实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_ecs_info_list_with_options(
        self,
        request: sys_om20231230_models.ListInstancesEcsInfoListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesEcsInfoListResponse:
        """
        @summary 获取ecs信息的列表，如标签列表，公网ip列表等
        
        @param request: ListInstancesEcsInfoListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesEcsInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info_type):
            query['info_type'] = request.info_type
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.managed_type):
            query['managed_type'] = request.managed_type
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesEcsInfoList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/listInstancesEcsInfoList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesEcsInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_ecs_info_list_with_options_async(
        self,
        request: sys_om20231230_models.ListInstancesEcsInfoListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesEcsInfoListResponse:
        """
        @summary 获取ecs信息的列表，如标签列表，公网ip列表等
        
        @param request: ListInstancesEcsInfoListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesEcsInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info_type):
            query['info_type'] = request.info_type
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.managed_type):
            query['managed_type'] = request.managed_type
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesEcsInfoList',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/listInstancesEcsInfoList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesEcsInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_ecs_info_list(
        self,
        request: sys_om20231230_models.ListInstancesEcsInfoListRequest,
    ) -> sys_om20231230_models.ListInstancesEcsInfoListResponse:
        """
        @summary 获取ecs信息的列表，如标签列表，公网ip列表等
        
        @param request: ListInstancesEcsInfoListRequest
        @return: ListInstancesEcsInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_ecs_info_list_with_options(request, headers, runtime)

    async def list_instances_ecs_info_list_async(
        self,
        request: sys_om20231230_models.ListInstancesEcsInfoListRequest,
    ) -> sys_om20231230_models.ListInstancesEcsInfoListResponse:
        """
        @summary 获取ecs信息的列表，如标签列表，公网ip列表等
        
        @param request: ListInstancesEcsInfoListRequest
        @return: ListInstancesEcsInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_ecs_info_list_with_options_async(request, headers, runtime)

    def list_instances_with_ecs_info_with_options(
        self,
        tmp_req: sys_om20231230_models.ListInstancesWithEcsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesWithEcsInfoResponse:
        """
        @summary 获取已纳管/未纳管实例信息，信息中包含ECS信息
        
        @param tmp_req: ListInstancesWithEcsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesWithEcsInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.ListInstancesWithEcsInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_tag):
            request.instance_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_tag, 'instance_tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.health_status):
            query['health_status'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.instance_tag_shrink):
            query['instance_tag'] = request.instance_tag_shrink
        if not UtilClient.is_unset(request.is_managed):
            query['is_managed'] = request.is_managed
        if not UtilClient.is_unset(request.os_name):
            query['os_name'] = request.os_name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['private_ip'] = request.private_ip
        if not UtilClient.is_unset(request.public_ip):
            query['public_ip'] = request.public_ip
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id_name):
            query['resource_group_id_name'] = request.resource_group_id_name
        if not UtilClient.is_unset(request.resource_group_name):
            query['resource_group_name'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesWithEcsInfo',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/listInstancesWithEcsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesWithEcsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_ecs_info_with_options_async(
        self,
        tmp_req: sys_om20231230_models.ListInstancesWithEcsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListInstancesWithEcsInfoResponse:
        """
        @summary 获取已纳管/未纳管实例信息，信息中包含ECS信息
        
        @param tmp_req: ListInstancesWithEcsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesWithEcsInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.ListInstancesWithEcsInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_tag):
            request.instance_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_tag, 'instance_tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.health_status):
            query['health_status'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.instance_tag_shrink):
            query['instance_tag'] = request.instance_tag_shrink
        if not UtilClient.is_unset(request.is_managed):
            query['is_managed'] = request.is_managed
        if not UtilClient.is_unset(request.os_name):
            query['os_name'] = request.os_name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['private_ip'] = request.private_ip
        if not UtilClient.is_unset(request.public_ip):
            query['public_ip'] = request.public_ip
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id_name):
            query['resource_group_id_name'] = request.resource_group_id_name
        if not UtilClient.is_unset(request.resource_group_name):
            query['resource_group_name'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesWithEcsInfo',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/listInstancesWithEcsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListInstancesWithEcsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_with_ecs_info(
        self,
        request: sys_om20231230_models.ListInstancesWithEcsInfoRequest,
    ) -> sys_om20231230_models.ListInstancesWithEcsInfoResponse:
        """
        @summary 获取已纳管/未纳管实例信息，信息中包含ECS信息
        
        @param request: ListInstancesWithEcsInfoRequest
        @return: ListInstancesWithEcsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_ecs_info_with_options(request, headers, runtime)

    async def list_instances_with_ecs_info_async(
        self,
        request: sys_om20231230_models.ListInstancesWithEcsInfoRequest,
    ) -> sys_om20231230_models.ListInstancesWithEcsInfoResponse:
        """
        @summary 获取已纳管/未纳管实例信息，信息中包含ECS信息
        
        @param request: ListInstancesWithEcsInfoRequest
        @return: ListInstancesWithEcsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_ecs_info_with_options_async(request, headers, runtime)

    def list_plugins_instances_with_options(
        self,
        request: sys_om20231230_models.ListPluginsInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListPluginsInstancesResponse:
        """
        @summary 获取插件的安装/更新/卸载实例列表
        
        @param request: ListPluginsInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not UtilClient.is_unset(request.instance_tag):
            query['instance_tag'] = request.instance_tag
        if not UtilClient.is_unset(request.operation_type):
            query['operation_type'] = request.operation_type
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPluginsInstances',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/listPluginsInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListPluginsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_instances_with_options_async(
        self,
        request: sys_om20231230_models.ListPluginsInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListPluginsInstancesResponse:
        """
        @summary 获取插件的安装/更新/卸载实例列表
        
        @param request: ListPluginsInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPluginsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance_id_name):
            query['instance_id_name'] = request.instance_id_name
        if not UtilClient.is_unset(request.instance_tag):
            query['instance_tag'] = request.instance_tag
        if not UtilClient.is_unset(request.operation_type):
            query['operation_type'] = request.operation_type
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['plugin_id'] = request.plugin_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPluginsInstances',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/listPluginsInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListPluginsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins_instances(
        self,
        request: sys_om20231230_models.ListPluginsInstancesRequest,
    ) -> sys_om20231230_models.ListPluginsInstancesResponse:
        """
        @summary 获取插件的安装/更新/卸载实例列表
        
        @param request: ListPluginsInstancesRequest
        @return: ListPluginsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugins_instances_with_options(request, headers, runtime)

    async def list_plugins_instances_async(
        self,
        request: sys_om20231230_models.ListPluginsInstancesRequest,
    ) -> sys_om20231230_models.ListPluginsInstancesResponse:
        """
        @summary 获取插件的安装/更新/卸载实例列表
        
        @param request: ListPluginsInstancesRequest
        @return: ListPluginsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_plugins_instances_with_options_async(request, headers, runtime)

    def list_pods_of_instance_with_options(
        self,
        request: sys_om20231230_models.ListPodsOfInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListPodsOfInstanceResponse:
        """
        @summary 获取实例中的pod列表
        
        @param request: ListPodsOfInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPodsOfInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPodsOfInstance',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_pod_of_instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListPodsOfInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pods_of_instance_with_options_async(
        self,
        request: sys_om20231230_models.ListPodsOfInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListPodsOfInstanceResponse:
        """
        @summary 获取实例中的pod列表
        
        @param request: ListPodsOfInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPodsOfInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.instance):
            query['instance'] = request.instance
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPodsOfInstance',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_pod_of_instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListPodsOfInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pods_of_instance(
        self,
        request: sys_om20231230_models.ListPodsOfInstanceRequest,
    ) -> sys_om20231230_models.ListPodsOfInstanceResponse:
        """
        @summary 获取实例中的pod列表
        
        @param request: ListPodsOfInstanceRequest
        @return: ListPodsOfInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pods_of_instance_with_options(request, headers, runtime)

    async def list_pods_of_instance_async(
        self,
        request: sys_om20231230_models.ListPodsOfInstanceRequest,
    ) -> sys_om20231230_models.ListPodsOfInstanceResponse:
        """
        @summary 获取实例中的pod列表
        
        @param request: ListPodsOfInstanceRequest
        @return: ListPodsOfInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pods_of_instance_with_options_async(request, headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListRegionsResponse:
        """
        @summary 列出所有纳管了机器的区域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.ListRegionsResponse:
        """
        @summary 列出所有纳管了机器的区域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/instance/list_regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> sys_om20231230_models.ListRegionsResponse:
        """
        @summary 列出所有纳管了机器的区域
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> sys_om20231230_models.ListRegionsResponse:
        """
        @summary 列出所有纳管了机器的区域
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

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
        if not UtilClient.is_unset(request.analysis_tool):
            body['analysisTool'] = request.analysis_tool
        if not UtilClient.is_unset(request.analysis_params):
            body['analysis_params'] = request.analysis_params
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.comms):
            body['comms'] = request.comms
        if not UtilClient.is_unset(request.created_by):
            body['created_by'] = request.created_by
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.instance_type):
            body['instance_type'] = request.instance_type
        if not UtilClient.is_unset(request.iteration_func):
            body['iteration_func'] = request.iteration_func
        if not UtilClient.is_unset(request.iteration_mod):
            body['iteration_mod'] = request.iteration_mod
        if not UtilClient.is_unset(request.iteration_range):
            body['iteration_range'] = request.iteration_range
        if not UtilClient.is_unset(request.pids):
            body['pids'] = request.pids
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
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
        if not UtilClient.is_unset(request.analysis_tool):
            body['analysisTool'] = request.analysis_tool
        if not UtilClient.is_unset(request.analysis_params):
            body['analysis_params'] = request.analysis_params
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.comms):
            body['comms'] = request.comms
        if not UtilClient.is_unset(request.created_by):
            body['created_by'] = request.created_by
        if not UtilClient.is_unset(request.instance):
            body['instance'] = request.instance
        if not UtilClient.is_unset(request.instance_type):
            body['instance_type'] = request.instance_type
        if not UtilClient.is_unset(request.iteration_func):
            body['iteration_func'] = request.iteration_func
        if not UtilClient.is_unset(request.iteration_mod):
            body['iteration_mod'] = request.iteration_mod
        if not UtilClient.is_unset(request.iteration_range):
            body['iteration_range'] = request.iteration_range
        if not UtilClient.is_unset(request.pids):
            body['pids'] = request.pids
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
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

    def start_aidiff_analysis_with_options(
        self,
        request: sys_om20231230_models.StartAIDiffAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.StartAIDiffAnalysisResponse:
        """
        @summary 查看AI Infra差分分析结果
        
        @param request: StartAIDiffAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAIDiffAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_1):
            body['task1'] = request.task_1
        if not UtilClient.is_unset(request.task_2):
            body['task2'] = request.task_2
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAIDiffAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/appObserv/aiAnalysis/diffAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.StartAIDiffAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aidiff_analysis_with_options_async(
        self,
        request: sys_om20231230_models.StartAIDiffAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.StartAIDiffAnalysisResponse:
        """
        @summary 查看AI Infra差分分析结果
        
        @param request: StartAIDiffAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAIDiffAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_1):
            body['task1'] = request.task_1
        if not UtilClient.is_unset(request.task_2):
            body['task2'] = request.task_2
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAIDiffAnalysis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/appObserv/aiAnalysis/diffAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.StartAIDiffAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aidiff_analysis(
        self,
        request: sys_om20231230_models.StartAIDiffAnalysisRequest,
    ) -> sys_om20231230_models.StartAIDiffAnalysisResponse:
        """
        @summary 查看AI Infra差分分析结果
        
        @param request: StartAIDiffAnalysisRequest
        @return: StartAIDiffAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_aidiff_analysis_with_options(request, headers, runtime)

    async def start_aidiff_analysis_async(
        self,
        request: sys_om20231230_models.StartAIDiffAnalysisRequest,
    ) -> sys_om20231230_models.StartAIDiffAnalysisResponse:
        """
        @summary 查看AI Infra差分分析结果
        
        @param request: StartAIDiffAnalysisRequest
        @return: StartAIDiffAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_aidiff_analysis_with_options_async(request, headers, runtime)

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

    def uninstall_agent_for_cluster_with_options(
        self,
        request: sys_om20231230_models.UninstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UninstallAgentForClusterResponse:
        """
        @summary 给集群卸载组件
        
        @param request: UninstallAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UninstallAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/uninstall_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UninstallAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_agent_for_cluster_with_options_async(
        self,
        request: sys_om20231230_models.UninstallAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UninstallAgentForClusterResponse:
        """
        @summary 给集群卸载组件
        
        @param request: UninstallAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UninstallAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/uninstall_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UninstallAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_agent_for_cluster(
        self,
        request: sys_om20231230_models.UninstallAgentForClusterRequest,
    ) -> sys_om20231230_models.UninstallAgentForClusterResponse:
        """
        @summary 给集群卸载组件
        
        @param request: UninstallAgentForClusterRequest
        @return: UninstallAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_agent_for_cluster_with_options(request, headers, runtime)

    async def uninstall_agent_for_cluster_async(
        self,
        request: sys_om20231230_models.UninstallAgentForClusterRequest,
    ) -> sys_om20231230_models.UninstallAgentForClusterResponse:
        """
        @summary 给集群卸载组件
        
        @param request: UninstallAgentForClusterRequest
        @return: UninstallAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.uninstall_agent_for_cluster_with_options_async(request, headers, runtime)

    def update_events_attention_with_options(
        self,
        request: sys_om20231230_models.UpdateEventsAttentionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpdateEventsAttentionResponse:
        """
        @summary 异常项关注度更新
        
        @param request: UpdateEventsAttentionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventsAttentionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.range):
            body['range'] = request.range
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventsAttention',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/cluster_update_events_attention',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpdateEventsAttentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_events_attention_with_options_async(
        self,
        request: sys_om20231230_models.UpdateEventsAttentionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpdateEventsAttentionResponse:
        """
        @summary 异常项关注度更新
        
        @param request: UpdateEventsAttentionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventsAttentionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.range):
            body['range'] = request.range
        if not UtilClient.is_unset(request.uuid):
            body['uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventsAttention',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/proxy/post/cluster_update_events_attention',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpdateEventsAttentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_events_attention(
        self,
        request: sys_om20231230_models.UpdateEventsAttentionRequest,
    ) -> sys_om20231230_models.UpdateEventsAttentionResponse:
        """
        @summary 异常项关注度更新
        
        @param request: UpdateEventsAttentionRequest
        @return: UpdateEventsAttentionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_events_attention_with_options(request, headers, runtime)

    async def update_events_attention_async(
        self,
        request: sys_om20231230_models.UpdateEventsAttentionRequest,
    ) -> sys_om20231230_models.UpdateEventsAttentionResponse:
        """
        @summary 异常项关注度更新
        
        @param request: UpdateEventsAttentionRequest
        @return: UpdateEventsAttentionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_events_attention_with_options_async(request, headers, runtime)

    def update_func_switch_record_with_options(
        self,
        tmp_req: sys_om20231230_models.UpdateFuncSwitchRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpdateFuncSwitchRecordResponse:
        """
        @summary 获取功能模块配置
        
        @param tmp_req: UpdateFuncSwitchRecordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFuncSwitchRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.UpdateFuncSwitchRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.params_shrink):
            query['params'] = request.params_shrink
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFuncSwitchRecord',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/func-switch/update-service-func-switch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpdateFuncSwitchRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_func_switch_record_with_options_async(
        self,
        tmp_req: sys_om20231230_models.UpdateFuncSwitchRecordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpdateFuncSwitchRecordResponse:
        """
        @summary 获取功能模块配置
        
        @param tmp_req: UpdateFuncSwitchRecordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFuncSwitchRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sys_om20231230_models.UpdateFuncSwitchRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'params', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.params_shrink):
            query['params'] = request.params_shrink
        if not UtilClient.is_unset(request.service_name):
            query['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFuncSwitchRecord',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/func-switch/update-service-func-switch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpdateFuncSwitchRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_func_switch_record(
        self,
        request: sys_om20231230_models.UpdateFuncSwitchRecordRequest,
    ) -> sys_om20231230_models.UpdateFuncSwitchRecordResponse:
        """
        @summary 获取功能模块配置
        
        @param request: UpdateFuncSwitchRecordRequest
        @return: UpdateFuncSwitchRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_func_switch_record_with_options(request, headers, runtime)

    async def update_func_switch_record_async(
        self,
        request: sys_om20231230_models.UpdateFuncSwitchRecordRequest,
    ) -> sys_om20231230_models.UpdateFuncSwitchRecordResponse:
        """
        @summary 获取功能模块配置
        
        @param request: UpdateFuncSwitchRecordRequest
        @return: UpdateFuncSwitchRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_func_switch_record_with_options_async(request, headers, runtime)

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

    def upgrade_agent_for_cluster_with_options(
        self,
        request: sys_om20231230_models.UpgradeAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpgradeAgentForClusterResponse:
        """
        @summary 给集群更新组件
        
        @param request: UpgradeAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/upgrade_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpgradeAgentForClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_agent_for_cluster_with_options_async(
        self,
        request: sys_om20231230_models.UpgradeAgentForClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.UpgradeAgentForClusterResponse:
        """
        @summary 给集群更新组件
        
        @param request: UpgradeAgentForClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeAgentForClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_id):
            body['agent_id'] = request.agent_id
        if not UtilClient.is_unset(request.agent_version):
            body['agent_version'] = request.agent_version
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeAgentForCluster',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/am/agent/upgrade_agent_by_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.UpgradeAgentForClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_agent_for_cluster(
        self,
        request: sys_om20231230_models.UpgradeAgentForClusterRequest,
    ) -> sys_om20231230_models.UpgradeAgentForClusterResponse:
        """
        @summary 给集群更新组件
        
        @param request: UpgradeAgentForClusterRequest
        @return: UpgradeAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_agent_for_cluster_with_options(request, headers, runtime)

    async def upgrade_agent_for_cluster_async(
        self,
        request: sys_om20231230_models.UpgradeAgentForClusterRequest,
    ) -> sys_om20231230_models.UpgradeAgentForClusterResponse:
        """
        @summary 给集群更新组件
        
        @param request: UpgradeAgentForClusterRequest
        @return: UpgradeAgentForClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_agent_for_cluster_with_options_async(request, headers, runtime)
