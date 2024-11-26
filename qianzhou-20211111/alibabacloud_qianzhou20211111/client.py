# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qianzhou20211111 import models as qianzhou_20211111_models
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
        self._endpoint = self.get_endpoint('qianzhou', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_icreate_session_message_with_options(
        self,
        request: qianzhou_20211111_models.AICreateSessionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.AICreateSessionMessageResponse:
        """
        @summary ACK AI助手千舟InnerAPI
        
        @param request: AICreateSessionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AICreateSessionMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.employee_id):
            query['employee_id'] = request.employee_id
        body = {}
        if not UtilClient.is_unset(request.context):
            body['context'] = request.context
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AICreateSessionMessage',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/AICreateSessionMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.AICreateSessionMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_icreate_session_message_with_options_async(
        self,
        request: qianzhou_20211111_models.AICreateSessionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.AICreateSessionMessageResponse:
        """
        @summary ACK AI助手千舟InnerAPI
        
        @param request: AICreateSessionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AICreateSessionMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.employee_id):
            query['employee_id'] = request.employee_id
        body = {}
        if not UtilClient.is_unset(request.context):
            body['context'] = request.context
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        if not UtilClient.is_unset(request.message):
            body['message'] = request.message
        if not UtilClient.is_unset(request.session_id):
            body['session_id'] = request.session_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AICreateSessionMessage',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/AICreateSessionMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.AICreateSessionMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_icreate_session_message(
        self,
        request: qianzhou_20211111_models.AICreateSessionMessageRequest,
    ) -> qianzhou_20211111_models.AICreateSessionMessageResponse:
        """
        @summary ACK AI助手千舟InnerAPI
        
        @param request: AICreateSessionMessageRequest
        @return: AICreateSessionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.a_icreate_session_message_with_options(request, headers, runtime)

    async def a_icreate_session_message_async(
        self,
        request: qianzhou_20211111_models.AICreateSessionMessageRequest,
    ) -> qianzhou_20211111_models.AICreateSessionMessageResponse:
        """
        @summary ACK AI助手千舟InnerAPI
        
        @param request: AICreateSessionMessageRequest
        @return: AICreateSessionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.a_icreate_session_message_with_options_async(request, headers, runtime)

    def create_diagnosis_with_options(
        self,
        request: qianzhou_20211111_models.CreateDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.CreateDiagnosisResponse:
        """
        @summary CreateDiagnosis
        
        @param request: CreateDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        if not UtilClient.is_unset(request.diagnosis_type):
            query['diagnosisType'] = request.diagnosis_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateDiagnosis',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/createDiagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.CreateDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnosis_with_options_async(
        self,
        request: qianzhou_20211111_models.CreateDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.CreateDiagnosisResponse:
        """
        @summary CreateDiagnosis
        
        @param request: CreateDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        if not UtilClient.is_unset(request.diagnosis_type):
            query['diagnosisType'] = request.diagnosis_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateDiagnosis',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/createDiagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.CreateDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnosis(
        self,
        request: qianzhou_20211111_models.CreateDiagnosisRequest,
    ) -> qianzhou_20211111_models.CreateDiagnosisResponse:
        """
        @summary CreateDiagnosis
        
        @param request: CreateDiagnosisRequest
        @return: CreateDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_diagnosis_with_options(request, headers, runtime)

    async def create_diagnosis_async(
        self,
        request: qianzhou_20211111_models.CreateDiagnosisRequest,
    ) -> qianzhou_20211111_models.CreateDiagnosisResponse:
        """
        @summary CreateDiagnosis
        
        @param request: CreateDiagnosisRequest
        @return: CreateDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_diagnosis_with_options_async(request, headers, runtime)

    def get_cluster_with_options(
        self,
        request: qianzhou_20211111_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetClusterResponse:
        """
        @summary 获取集群信息
        
        @param request: GetClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getCluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: qianzhou_20211111_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetClusterResponse:
        """
        @summary 获取集群信息
        
        @param request: GetClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getCluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: qianzhou_20211111_models.GetClusterRequest,
    ) -> qianzhou_20211111_models.GetClusterResponse:
        """
        @summary 获取集群信息
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(request, headers, runtime)

    async def get_cluster_async(
        self,
        request: qianzhou_20211111_models.GetClusterRequest,
    ) -> qianzhou_20211111_models.GetClusterResponse:
        """
        @summary 获取集群信息
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_with_options_async(request, headers, runtime)

    def get_cluster_warning_with_options(
        self,
        request: qianzhou_20211111_models.GetClusterWarningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetClusterWarningResponse:
        """
        @summary 单个集群的高危风险项
        
        @param request: GetClusterWarningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterWarningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterWarning',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getKeyClusterWarningList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetClusterWarningResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_warning_with_options_async(
        self,
        request: qianzhou_20211111_models.GetClusterWarningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetClusterWarningResponse:
        """
        @summary 单个集群的高危风险项
        
        @param request: GetClusterWarningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterWarningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterID'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterWarning',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getKeyClusterWarningList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetClusterWarningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_warning(
        self,
        request: qianzhou_20211111_models.GetClusterWarningRequest,
    ) -> qianzhou_20211111_models.GetClusterWarningResponse:
        """
        @summary 单个集群的高危风险项
        
        @param request: GetClusterWarningRequest
        @return: GetClusterWarningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_warning_with_options(request, headers, runtime)

    async def get_cluster_warning_async(
        self,
        request: qianzhou_20211111_models.GetClusterWarningRequest,
    ) -> qianzhou_20211111_models.GetClusterWarningResponse:
        """
        @summary 单个集群的高危风险项
        
        @param request: GetClusterWarningRequest
        @return: GetClusterWarningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_warning_with_options_async(request, headers, runtime)

    def get_diagnosis_result_with_options(
        self,
        request: qianzhou_20211111_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetDiagnosisResultResponse:
        """
        @summary GetDiagnosisResult
        
        @param request: GetDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnosis_id):
            query['diagnosisId'] = request.diagnosis_id
        if not UtilClient.is_unset(request.owner_uid):
            query['ownerUid'] = request.owner_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/GetDiagnosisResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_result_with_options_async(
        self,
        request: qianzhou_20211111_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetDiagnosisResultResponse:
        """
        @summary GetDiagnosisResult
        
        @param request: GetDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnosis_id):
            query['diagnosisId'] = request.diagnosis_id
        if not UtilClient.is_unset(request.owner_uid):
            query['ownerUid'] = request.owner_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/GetDiagnosisResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_result(
        self,
        request: qianzhou_20211111_models.GetDiagnosisResultRequest,
    ) -> qianzhou_20211111_models.GetDiagnosisResultResponse:
        """
        @summary GetDiagnosisResult
        
        @param request: GetDiagnosisResultRequest
        @return: GetDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_diagnosis_result_with_options(request, headers, runtime)

    async def get_diagnosis_result_async(
        self,
        request: qianzhou_20211111_models.GetDiagnosisResultRequest,
    ) -> qianzhou_20211111_models.GetDiagnosisResultResponse:
        """
        @summary GetDiagnosisResult
        
        @param request: GetDiagnosisResultRequest
        @return: GetDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_diagnosis_result_with_options_async(request, headers, runtime)

    def get_user_cluster_warning_with_options(
        self,
        request: qianzhou_20211111_models.GetUserClusterWarningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetUserClusterWarningResponse:
        """
        @summary 单个用户的高危集群
        
        @param request: GetUserClusterWarningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserClusterWarningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userID'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserClusterWarning',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listUserKeyClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetUserClusterWarningResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_cluster_warning_with_options_async(
        self,
        request: qianzhou_20211111_models.GetUserClusterWarningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetUserClusterWarningResponse:
        """
        @summary 单个用户的高危集群
        
        @param request: GetUserClusterWarningRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserClusterWarningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['userID'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserClusterWarning',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listUserKeyClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetUserClusterWarningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_cluster_warning(
        self,
        request: qianzhou_20211111_models.GetUserClusterWarningRequest,
    ) -> qianzhou_20211111_models.GetUserClusterWarningResponse:
        """
        @summary 单个用户的高危集群
        
        @param request: GetUserClusterWarningRequest
        @return: GetUserClusterWarningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_cluster_warning_with_options(request, headers, runtime)

    async def get_user_cluster_warning_async(
        self,
        request: qianzhou_20211111_models.GetUserClusterWarningRequest,
    ) -> qianzhou_20211111_models.GetUserClusterWarningResponse:
        """
        @summary 单个用户的高危集群
        
        @param request: GetUserClusterWarningRequest
        @return: GetUserClusterWarningResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_cluster_warning_with_options_async(request, headers, runtime)

    def get_webshell_token_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetWebshellTokenResponse:
        """
        @deprecated OpenAPI GetWebshellToken is deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebshellTokenResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWebshellToken',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getChorusToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetWebshellTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_webshell_token_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.GetWebshellTokenResponse:
        """
        @deprecated OpenAPI GetWebshellToken is deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebshellTokenResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWebshellToken',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/getChorusToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.GetWebshellTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_webshell_token(self) -> qianzhou_20211111_models.GetWebshellTokenResponse:
        """
        @deprecated OpenAPI GetWebshellToken is deprecated
        
        @return: GetWebshellTokenResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_webshell_token_with_options(headers, runtime)

    async def get_webshell_token_async(self) -> qianzhou_20211111_models.GetWebshellTokenResponse:
        """
        @deprecated OpenAPI GetWebshellToken is deprecated
        
        @return: GetWebshellTokenResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_webshell_token_with_options_async(headers, runtime)

    def hello_with_options(
        self,
        request: qianzhou_20211111_models.HelloRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.HelloResponse:
        """
        @summary 测试接口
        
        @param request: HelloRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HelloResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user):
            query['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Hello',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/hello',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.HelloResponse(),
            self.call_api(params, req, runtime)
        )

    async def hello_with_options_async(
        self,
        request: qianzhou_20211111_models.HelloRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.HelloResponse:
        """
        @summary 测试接口
        
        @param request: HelloRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: HelloResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user):
            query['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Hello',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/hello',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.HelloResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hello(
        self,
        request: qianzhou_20211111_models.HelloRequest,
    ) -> qianzhou_20211111_models.HelloResponse:
        """
        @summary 测试接口
        
        @param request: HelloRequest
        @return: HelloResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.hello_with_options(request, headers, runtime)

    async def hello_async(
        self,
        request: qianzhou_20211111_models.HelloRequest,
    ) -> qianzhou_20211111_models.HelloResponse:
        """
        @summary 测试接口
        
        @param request: HelloRequest
        @return: HelloResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.hello_with_options_async(request, headers, runtime)

    def list_cluster_deprecated_apiwith_options(
        self,
        request: qianzhou_20211111_models.ListClusterDeprecatedAPIRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListClusterDeprecatedAPIResponse:
        """
        @summary 获取某集群废弃api的统计情况
        
        @param request: ListClusterDeprecatedAPIRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterDeprecatedAPIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.target_version):
            query['target_version'] = request.target_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterDeprecatedAPI',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listDeprecatedK8sAPI',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListClusterDeprecatedAPIResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_deprecated_apiwith_options_async(
        self,
        request: qianzhou_20211111_models.ListClusterDeprecatedAPIRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListClusterDeprecatedAPIResponse:
        """
        @summary 获取某集群废弃api的统计情况
        
        @param request: ListClusterDeprecatedAPIRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterDeprecatedAPIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.target_version):
            query['target_version'] = request.target_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterDeprecatedAPI',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listDeprecatedK8sAPI',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListClusterDeprecatedAPIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_deprecated_api(
        self,
        request: qianzhou_20211111_models.ListClusterDeprecatedAPIRequest,
    ) -> qianzhou_20211111_models.ListClusterDeprecatedAPIResponse:
        """
        @summary 获取某集群废弃api的统计情况
        
        @param request: ListClusterDeprecatedAPIRequest
        @return: ListClusterDeprecatedAPIResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_deprecated_apiwith_options(request, headers, runtime)

    async def list_cluster_deprecated_api_async(
        self,
        request: qianzhou_20211111_models.ListClusterDeprecatedAPIRequest,
    ) -> qianzhou_20211111_models.ListClusterDeprecatedAPIResponse:
        """
        @summary 获取某集群废弃api的统计情况
        
        @param request: ListClusterDeprecatedAPIRequest
        @return: ListClusterDeprecatedAPIResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_deprecated_apiwith_options_async(request, headers, runtime)

    def list_cluster_images_with_options(
        self,
        request: qianzhou_20211111_models.ListClusterImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListClusterImagesResponse:
        """
        @summary 获取某集群中的Image列表
        
        @param request: ListClusterImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.image_hash):
            query['image_hash'] = request.image_hash
        if not UtilClient.is_unset(request.image_name):
            query['image_name'] = request.image_name
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterImages',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listClusterPodImages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListClusterImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_images_with_options_async(
        self,
        request: qianzhou_20211111_models.ListClusterImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListClusterImagesResponse:
        """
        @summary 获取某集群中的Image列表
        
        @param request: ListClusterImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.image_hash):
            query['image_hash'] = request.image_hash
        if not UtilClient.is_unset(request.image_name):
            query['image_name'] = request.image_name
        if not UtilClient.is_unset(request.page_no):
            query['page_no'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterImages',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listClusterPodImages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListClusterImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_images(
        self,
        request: qianzhou_20211111_models.ListClusterImagesRequest,
    ) -> qianzhou_20211111_models.ListClusterImagesResponse:
        """
        @summary 获取某集群中的Image列表
        
        @param request: ListClusterImagesRequest
        @return: ListClusterImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_images_with_options(request, headers, runtime)

    async def list_cluster_images_async(
        self,
        request: qianzhou_20211111_models.ListClusterImagesRequest,
    ) -> qianzhou_20211111_models.ListClusterImagesResponse:
        """
        @summary 获取某集群中的Image列表
        
        @param request: ListClusterImagesRequest
        @return: ListClusterImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_images_with_options_async(request, headers, runtime)

    def list_user_clusters_with_options(
        self,
        request: qianzhou_20211111_models.ListUserClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListUserClustersResponse:
        """
        @summary 获取用户下的集群列表
        
        @param request: ListUserClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['userID'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listUserClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListUserClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_clusters_with_options_async(
        self,
        request: qianzhou_20211111_models.ListUserClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.ListUserClustersResponse:
        """
        @summary 获取用户下的集群列表
        
        @param request: ListUserClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['userID'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/listUserClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.ListUserClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_clusters(
        self,
        request: qianzhou_20211111_models.ListUserClustersRequest,
    ) -> qianzhou_20211111_models.ListUserClustersResponse:
        """
        @summary 获取用户下的集群列表
        
        @param request: ListUserClustersRequest
        @return: ListUserClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_clusters_with_options(request, headers, runtime)

    async def list_user_clusters_async(
        self,
        request: qianzhou_20211111_models.ListUserClustersRequest,
    ) -> qianzhou_20211111_models.ListUserClustersResponse:
        """
        @summary 获取用户下的集群列表
        
        @param request: ListUserClustersRequest
        @return: ListUserClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_clusters_with_options_async(request, headers, runtime)

    def query_by_instance_info_with_options(
        self,
        request: qianzhou_20211111_models.QueryByInstanceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.QueryByInstanceInfoResponse:
        """
        @summary 查询节点相关集群、用户信息
        
        @param request: QueryByInstanceInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryByInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryByInstanceInfo',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/queryByInstanceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.QueryByInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_by_instance_info_with_options_async(
        self,
        request: qianzhou_20211111_models.QueryByInstanceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.QueryByInstanceInfoResponse:
        """
        @summary 查询节点相关集群、用户信息
        
        @param request: QueryByInstanceInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryByInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryByInstanceInfo',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/queryByInstanceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.QueryByInstanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_by_instance_info(
        self,
        request: qianzhou_20211111_models.QueryByInstanceInfoRequest,
    ) -> qianzhou_20211111_models.QueryByInstanceInfoResponse:
        """
        @summary 查询节点相关集群、用户信息
        
        @param request: QueryByInstanceInfoRequest
        @return: QueryByInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_by_instance_info_with_options(request, headers, runtime)

    async def query_by_instance_info_async(
        self,
        request: qianzhou_20211111_models.QueryByInstanceInfoRequest,
    ) -> qianzhou_20211111_models.QueryByInstanceInfoResponse:
        """
        @summary 查询节点相关集群、用户信息
        
        @param request: QueryByInstanceInfoRequest
        @return: QueryByInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_by_instance_info_with_options_async(request, headers, runtime)

    def query_node_info_with_options(
        self,
        request: qianzhou_20211111_models.QueryNodeInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.QueryNodeInfoResponse:
        """
        @summary 根据节点instanceId查询集群/用户信息
        
        @param request: QueryNodeInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryNodeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNodeInfo',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/queryByInstanceId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.QueryNodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_node_info_with_options_async(
        self,
        request: qianzhou_20211111_models.QueryNodeInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> qianzhou_20211111_models.QueryNodeInfoResponse:
        """
        @summary 根据节点instanceId查询集群/用户信息
        
        @param request: QueryNodeInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryNodeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryNodeInfo',
            version='2021-11-11',
            protocol='HTTPS',
            pathname=f'/popapi/queryByInstanceId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            qianzhou_20211111_models.QueryNodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_node_info(
        self,
        request: qianzhou_20211111_models.QueryNodeInfoRequest,
    ) -> qianzhou_20211111_models.QueryNodeInfoResponse:
        """
        @summary 根据节点instanceId查询集群/用户信息
        
        @param request: QueryNodeInfoRequest
        @return: QueryNodeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_node_info_with_options(request, headers, runtime)

    async def query_node_info_async(
        self,
        request: qianzhou_20211111_models.QueryNodeInfoRequest,
    ) -> qianzhou_20211111_models.QueryNodeInfoResponse:
        """
        @summary 根据节点instanceId查询集群/用户信息
        
        @param request: QueryNodeInfoRequest
        @return: QueryNodeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_node_info_with_options_async(request, headers, runtime)
