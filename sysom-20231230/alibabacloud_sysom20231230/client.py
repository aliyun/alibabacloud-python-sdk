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
