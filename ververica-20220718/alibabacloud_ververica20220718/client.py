# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ververica20220718 import models as ververica_20220718_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ververica', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.ApplyScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ApplyScheduledPlanResponse:
        """
        @summary 执行定时计划
        
        @param headers: ApplyScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ApplyScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}%3Aapply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ApplyScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.ApplyScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ApplyScheduledPlanResponse:
        """
        @summary 执行定时计划
        
        @param headers: ApplyScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ApplyScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}%3Aapply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ApplyScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.ApplyScheduledPlanResponse:
        """
        @summary 执行定时计划
        
        @return: ApplyScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ApplyScheduledPlanHeaders()
        return self.apply_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def apply_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.ApplyScheduledPlanResponse:
        """
        @summary 执行定时计划
        
        @return: ApplyScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ApplyScheduledPlanHeaders()
        return await self.apply_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def cancel_sql_preview_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CancelSqlPreviewRequest,
        headers: ververica_20220718_models.CancelSqlPreviewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CancelSqlPreviewResponse:
        """
        @summary 取消调试
        
        @param request: CancelSqlPreviewRequest
        @param headers: CancelSqlPreviewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSqlPreviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['queryId'] = request.query_id
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSqlPreview',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CancelSqlPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_sql_preview_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CancelSqlPreviewRequest,
        headers: ververica_20220718_models.CancelSqlPreviewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CancelSqlPreviewResponse:
        """
        @summary 取消调试
        
        @param request: CancelSqlPreviewRequest
        @param headers: CancelSqlPreviewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSqlPreviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['queryId'] = request.query_id
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSqlPreview',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/cancel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CancelSqlPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_sql_preview(
        self,
        namespace: str,
        request: ververica_20220718_models.CancelSqlPreviewRequest,
    ) -> ververica_20220718_models.CancelSqlPreviewResponse:
        """
        @summary 取消调试
        
        @param request: CancelSqlPreviewRequest
        @return: CancelSqlPreviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CancelSqlPreviewHeaders()
        return self.cancel_sql_preview_with_options(namespace, request, headers, runtime)

    async def cancel_sql_preview_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CancelSqlPreviewRequest,
    ) -> ververica_20220718_models.CancelSqlPreviewResponse:
        """
        @summary 取消调试
        
        @param request: CancelSqlPreviewRequest
        @return: CancelSqlPreviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CancelSqlPreviewHeaders()
        return await self.cancel_sql_preview_with_options_async(namespace, request, headers, runtime)

    def create_deployment_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
        headers: ververica_20220718_models.CreateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary Creates a deployment.
        
        @param request: CreateDeploymentRequest
        @param headers: CreateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
        headers: ververica_20220718_models.CreateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary Creates a deployment.
        
        @param request: CreateDeploymentRequest
        @param headers: CreateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary Creates a deployment.
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentHeaders()
        return self.create_deployment_with_options(namespace, request, headers, runtime)

    async def create_deployment_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentRequest,
    ) -> ververica_20220718_models.CreateDeploymentResponse:
        """
        @summary Creates a deployment.
        
        @param request: CreateDeploymentRequest
        @return: CreateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentHeaders()
        return await self.create_deployment_with_options_async(namespace, request, headers, runtime)

    def create_deployment_draft_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentDraftRequest,
        headers: ververica_20220718_models.CreateDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentDraftResponse:
        """
        @summary create a deploymentDraft
        
        @param request: CreateDeploymentDraftRequest
        @param headers: CreateDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentDraftResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_draft_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentDraftRequest,
        headers: ververica_20220718_models.CreateDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentDraftResponse:
        """
        @summary create a deploymentDraft
        
        @param request: CreateDeploymentDraftRequest
        @param headers: CreateDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentDraftResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_draft(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentDraftRequest,
    ) -> ververica_20220718_models.CreateDeploymentDraftResponse:
        """
        @summary create a deploymentDraft
        
        @param request: CreateDeploymentDraftRequest
        @return: CreateDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentDraftHeaders()
        return self.create_deployment_draft_with_options(namespace, request, headers, runtime)

    async def create_deployment_draft_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentDraftRequest,
    ) -> ververica_20220718_models.CreateDeploymentDraftResponse:
        """
        @summary create a deploymentDraft
        
        @param request: CreateDeploymentDraftRequest
        @return: CreateDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentDraftHeaders()
        return await self.create_deployment_draft_with_options_async(namespace, request, headers, runtime)

    def create_deployment_target_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetRequest,
        headers: ververica_20220718_models.CreateDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentTargetResponse:
        """
        @summary 创建deploymentTarget
        
        @param request: CreateDeploymentTargetRequest
        @param headers: CreateDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_target_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetRequest,
        headers: ververica_20220718_models.CreateDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentTargetResponse:
        """
        @summary 创建deploymentTarget
        
        @param request: CreateDeploymentTargetRequest
        @param headers: CreateDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_target(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetRequest,
    ) -> ververica_20220718_models.CreateDeploymentTargetResponse:
        """
        @summary 创建deploymentTarget
        
        @param request: CreateDeploymentTargetRequest
        @return: CreateDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentTargetHeaders()
        return self.create_deployment_target_with_options(namespace, request, headers, runtime)

    async def create_deployment_target_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetRequest,
    ) -> ververica_20220718_models.CreateDeploymentTargetResponse:
        """
        @summary 创建deploymentTarget
        
        @param request: CreateDeploymentTargetRequest
        @return: CreateDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentTargetHeaders()
        return await self.create_deployment_target_with_options_async(namespace, request, headers, runtime)

    def create_deployment_target_v2with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetV2Request,
        headers: ververica_20220718_models.CreateDeploymentTargetV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentTargetV2Response:
        """
        @summary 创建部署目标V2
        
        @param request: CreateDeploymentTargetV2Request
        @param headers: CreateDeploymentTargetV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentTargetV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentTargetV2',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/support-elastic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentTargetV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_target_v2with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetV2Request,
        headers: ververica_20220718_models.CreateDeploymentTargetV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateDeploymentTargetV2Response:
        """
        @summary 创建部署目标V2
        
        @param request: CreateDeploymentTargetV2Request
        @param headers: CreateDeploymentTargetV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentTargetV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDeploymentTargetV2',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/support-elastic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentTargetV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_target_v2(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetV2Request,
    ) -> ververica_20220718_models.CreateDeploymentTargetV2Response:
        """
        @summary 创建部署目标V2
        
        @param request: CreateDeploymentTargetV2Request
        @return: CreateDeploymentTargetV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentTargetV2Headers()
        return self.create_deployment_target_v2with_options(namespace, request, headers, runtime)

    async def create_deployment_target_v2_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateDeploymentTargetV2Request,
    ) -> ververica_20220718_models.CreateDeploymentTargetV2Response:
        """
        @summary 创建部署目标V2
        
        @param request: CreateDeploymentTargetV2Request
        @return: CreateDeploymentTargetV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentTargetV2Headers()
        return await self.create_deployment_target_v2with_options_async(namespace, request, headers, runtime)

    def create_folder_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateFolderRequest,
        headers: ververica_20220718_models.CreateFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateFolderResponse:
        """
        @summary create a folder
        
        @param request: CreateFolderRequest
        @param headers: CreateFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateFolderRequest,
        headers: ververica_20220718_models.CreateFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateFolderResponse:
        """
        @summary create a folder
        
        @param request: CreateFolderRequest
        @param headers: CreateFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateFolderRequest,
    ) -> ververica_20220718_models.CreateFolderResponse:
        """
        @summary create a folder
        
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateFolderHeaders()
        return self.create_folder_with_options(namespace, request, headers, runtime)

    async def create_folder_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateFolderRequest,
    ) -> ververica_20220718_models.CreateFolderResponse:
        """
        @summary create a folder
        
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateFolderHeaders()
        return await self.create_folder_with_options_async(namespace, request, headers, runtime)

    def create_member_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
        headers: ververica_20220718_models.CreateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary Adds a user to a namespace as a member and grants permissions to the user.
        
        @param request: CreateMemberRequest
        @param headers: CreateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
        headers: ververica_20220718_models.CreateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary Adds a user to a namespace as a member and grants permissions to the user.
        
        @param request: CreateMemberRequest
        @param headers: CreateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary Adds a user to a namespace as a member and grants permissions to the user.
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateMemberHeaders()
        return self.create_member_with_options(namespace, request, headers, runtime)

    async def create_member_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateMemberRequest,
    ) -> ververica_20220718_models.CreateMemberResponse:
        """
        @summary Adds a user to a namespace as a member and grants permissions to the user.
        
        @param request: CreateMemberRequest
        @return: CreateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateMemberHeaders()
        return await self.create_member_with_options_async(namespace, request, headers, runtime)

    def create_savepoint_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
        headers: ververica_20220718_models.CreateSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary Creates a savepoint.
        
        @param request: CreateSavepointRequest
        @param headers: CreateSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavepointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_savepoint_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
        headers: ververica_20220718_models.CreateSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary Creates a savepoint.
        
        @param request: CreateSavepointRequest
        @param headers: CreateSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavepointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_savepoint(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary Creates a savepoint.
        
        @param request: CreateSavepointRequest
        @return: CreateSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSavepointHeaders()
        return self.create_savepoint_with_options(namespace, request, headers, runtime)

    async def create_savepoint_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSavepointRequest,
    ) -> ververica_20220718_models.CreateSavepointResponse:
        """
        @summary Creates a savepoint.
        
        @param request: CreateSavepointRequest
        @return: CreateSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSavepointHeaders()
        return await self.create_savepoint_with_options_async(namespace, request, headers, runtime)

    def create_scheduled_plan_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateScheduledPlanRequest,
        headers: ververica_20220718_models.CreateScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateScheduledPlanResponse:
        """
        @summary 创建定时执行计划
        
        @param request: CreateScheduledPlanRequest
        @param headers: CreateScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateScheduledPlanRequest,
        headers: ververica_20220718_models.CreateScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateScheduledPlanResponse:
        """
        @summary 创建定时执行计划
        
        @param request: CreateScheduledPlanRequest
        @param headers: CreateScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_plan(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateScheduledPlanRequest,
    ) -> ververica_20220718_models.CreateScheduledPlanResponse:
        """
        @summary 创建定时执行计划
        
        @param request: CreateScheduledPlanRequest
        @return: CreateScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateScheduledPlanHeaders()
        return self.create_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def create_scheduled_plan_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateScheduledPlanRequest,
    ) -> ververica_20220718_models.CreateScheduledPlanResponse:
        """
        @summary 创建定时执行计划
        
        @param request: CreateScheduledPlanRequest
        @return: CreateScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateScheduledPlanHeaders()
        return await self.create_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def create_session_cluster_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSessionClusterRequest,
        headers: ververica_20220718_models.CreateSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSessionClusterResponse:
        """
        @summary 创建session集群
        
        @param request: CreateSessionClusterRequest
        @param headers: CreateSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_cluster_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSessionClusterRequest,
        headers: ververica_20220718_models.CreateSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateSessionClusterResponse:
        """
        @summary 创建session集群
        
        @param request: CreateSessionClusterRequest
        @param headers: CreateSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session_cluster(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSessionClusterRequest,
    ) -> ververica_20220718_models.CreateSessionClusterResponse:
        """
        @summary 创建session集群
        
        @param request: CreateSessionClusterRequest
        @return: CreateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSessionClusterHeaders()
        return self.create_session_cluster_with_options(namespace, request, headers, runtime)

    async def create_session_cluster_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateSessionClusterRequest,
    ) -> ververica_20220718_models.CreateSessionClusterResponse:
        """
        @summary 创建session集群
        
        @param request: CreateSessionClusterRequest
        @return: CreateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSessionClusterHeaders()
        return await self.create_session_cluster_with_options_async(namespace, request, headers, runtime)

    def create_udf_artifact_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateUdfArtifactRequest,
        headers: ververica_20220718_models.CreateUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateUdfArtifactResponse:
        """
        @summary Parses all user-defined function (UDF) methods in your JAR or Python file and creates an artifact configuration for a UDF.
        
        @param request: CreateUdfArtifactRequest
        @param headers: CreateUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUdfArtifactResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_udf_artifact_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateUdfArtifactRequest,
        headers: ververica_20220718_models.CreateUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateUdfArtifactResponse:
        """
        @summary Parses all user-defined function (UDF) methods in your JAR or Python file and creates an artifact configuration for a UDF.
        
        @param request: CreateUdfArtifactRequest
        @param headers: CreateUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUdfArtifactResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_udf_artifact(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateUdfArtifactRequest,
    ) -> ververica_20220718_models.CreateUdfArtifactResponse:
        """
        @summary Parses all user-defined function (UDF) methods in your JAR or Python file and creates an artifact configuration for a UDF.
        
        @param request: CreateUdfArtifactRequest
        @return: CreateUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateUdfArtifactHeaders()
        return self.create_udf_artifact_with_options(namespace, request, headers, runtime)

    async def create_udf_artifact_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateUdfArtifactRequest,
    ) -> ververica_20220718_models.CreateUdfArtifactResponse:
        """
        @summary Parses all user-defined function (UDF) methods in your JAR or Python file and creates an artifact configuration for a UDF.
        
        @param request: CreateUdfArtifactRequest
        @return: CreateUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateUdfArtifactHeaders()
        return await self.create_udf_artifact_with_options_async(namespace, request, headers, runtime)

    def create_variable_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
        headers: ververica_20220718_models.CreateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary Creates a variable.
        
        @param request: CreateVariableRequest
        @param headers: CreateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
        headers: ververica_20220718_models.CreateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary Creates a variable.
        
        @param request: CreateVariableRequest
        @param headers: CreateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary Creates a variable.
        
        @param request: CreateVariableRequest
        @return: CreateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateVariableHeaders()
        return self.create_variable_with_options(namespace, request, headers, runtime)

    async def create_variable_async(
        self,
        namespace: str,
        request: ververica_20220718_models.CreateVariableRequest,
    ) -> ververica_20220718_models.CreateVariableResponse:
        """
        @summary Creates a variable.
        
        @param request: CreateVariableRequest
        @return: CreateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateVariableHeaders()
        return await self.create_variable_with_options_async(namespace, request, headers, runtime)

    def delete_custom_connector_with_options(
        self,
        namespace: str,
        connector_name: str,
        headers: ververica_20220718_models.DeleteCustomConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteCustomConnectorResponse:
        """
        @summary Deletes a registered custom connector from a workspace.
        
        @param headers: DeleteCustomConnectorHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomConnectorResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteCustomConnector',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors/{OpenApiUtilClient.get_encode_param(connector_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteCustomConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_connector_with_options_async(
        self,
        namespace: str,
        connector_name: str,
        headers: ververica_20220718_models.DeleteCustomConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteCustomConnectorResponse:
        """
        @summary Deletes a registered custom connector from a workspace.
        
        @param headers: DeleteCustomConnectorHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomConnectorResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteCustomConnector',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors/{OpenApiUtilClient.get_encode_param(connector_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteCustomConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_connector(
        self,
        namespace: str,
        connector_name: str,
    ) -> ververica_20220718_models.DeleteCustomConnectorResponse:
        """
        @summary Deletes a registered custom connector from a workspace.
        
        @return: DeleteCustomConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteCustomConnectorHeaders()
        return self.delete_custom_connector_with_options(namespace, connector_name, headers, runtime)

    async def delete_custom_connector_async(
        self,
        namespace: str,
        connector_name: str,
    ) -> ververica_20220718_models.DeleteCustomConnectorResponse:
        """
        @summary Deletes a registered custom connector from a workspace.
        
        @return: DeleteCustomConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteCustomConnectorHeaders()
        return await self.delete_custom_connector_with_options_async(namespace, connector_name, headers, runtime)

    def delete_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.DeleteDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary Deletes a deployment based on the deployment ID.
        
        @param headers: DeleteDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.DeleteDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary Deletes a deployment based on the deployment ID.
        
        @param headers: DeleteDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary Deletes a deployment based on the deployment ID.
        
        @return: DeleteDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentHeaders()
        return self.delete_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def delete_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentResponse:
        """
        @summary Deletes a deployment based on the deployment ID.
        
        @return: DeleteDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentHeaders()
        return await self.delete_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def delete_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: ververica_20220718_models.DeleteDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentDraftResponse:
        """
        @summary delete a deploymentDraft
        
        @param headers: DeleteDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentDraftResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: ververica_20220718_models.DeleteDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentDraftResponse:
        """
        @summary delete a deploymentDraft
        
        @param headers: DeleteDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentDraftResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentDraftResponse:
        """
        @summary delete a deploymentDraft
        
        @return: DeleteDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentDraftHeaders()
        return self.delete_deployment_draft_with_options(namespace, deployment_draft_id, headers, runtime)

    async def delete_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> ververica_20220718_models.DeleteDeploymentDraftResponse:
        """
        @summary delete a deploymentDraft
        
        @return: DeleteDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentDraftHeaders()
        return await self.delete_deployment_draft_with_options_async(namespace, deployment_draft_id, headers, runtime)

    def delete_deployment_target_with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        headers: ververica_20220718_models.DeleteDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentTargetResponse:
        """
        @summary 删除deploymentTarget
        
        @param headers: DeleteDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentTargetResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_target_with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        headers: ververica_20220718_models.DeleteDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteDeploymentTargetResponse:
        """
        @summary 删除deploymentTarget
        
        @param headers: DeleteDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentTargetResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_target(
        self,
        namespace: str,
        deployment_target_name: str,
    ) -> ververica_20220718_models.DeleteDeploymentTargetResponse:
        """
        @summary 删除deploymentTarget
        
        @return: DeleteDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentTargetHeaders()
        return self.delete_deployment_target_with_options(namespace, deployment_target_name, headers, runtime)

    async def delete_deployment_target_async(
        self,
        namespace: str,
        deployment_target_name: str,
    ) -> ververica_20220718_models.DeleteDeploymentTargetResponse:
        """
        @summary 删除deploymentTarget
        
        @return: DeleteDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentTargetHeaders()
        return await self.delete_deployment_target_with_options_async(namespace, deployment_target_name, headers, runtime)

    def delete_folder_with_options(
        self,
        namespace: str,
        folder_id: str,
        headers: ververica_20220718_models.DeleteFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteFolderResponse:
        """
        @summary delete a folder
        
        @param headers: DeleteFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        namespace: str,
        folder_id: str,
        headers: ververica_20220718_models.DeleteFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteFolderResponse:
        """
        @summary delete a folder
        
        @param headers: DeleteFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        namespace: str,
        folder_id: str,
    ) -> ververica_20220718_models.DeleteFolderResponse:
        """
        @summary delete a folder
        
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteFolderHeaders()
        return self.delete_folder_with_options(namespace, folder_id, headers, runtime)

    async def delete_folder_async(
        self,
        namespace: str,
        folder_id: str,
    ) -> ververica_20220718_models.DeleteFolderResponse:
        """
        @summary delete a folder
        
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteFolderHeaders()
        return await self.delete_folder_with_options_async(namespace, folder_id, headers, runtime)

    def delete_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.DeleteJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary Deletes the information about a job that is not in the running state in a deployment.
        
        @param headers: DeleteJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.DeleteJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary Deletes the information about a job that is not in the running state in a deployment.
        
        @param headers: DeleteJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary Deletes the information about a job that is not in the running state in a deployment.
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteJobHeaders()
        return self.delete_job_with_options(namespace, job_id, headers, runtime)

    async def delete_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.DeleteJobResponse:
        """
        @summary Deletes the information about a job that is not in the running state in a deployment.
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteJobHeaders()
        return await self.delete_job_with_options_async(namespace, job_id, headers, runtime)

    def delete_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.DeleteMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary Revokes the permissions from a member.
        
        @param headers: DeleteMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.DeleteMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary Revokes the permissions from a member.
        
        @param headers: DeleteMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary Revokes the permissions from a member.
        
        @return: DeleteMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteMemberHeaders()
        return self.delete_member_with_options(namespace, member, headers, runtime)

    async def delete_member_async(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.DeleteMemberResponse:
        """
        @summary Revokes the permissions from a member.
        
        @return: DeleteMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteMemberHeaders()
        return await self.delete_member_with_options_async(namespace, member, headers, runtime)

    def delete_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.DeleteSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary Deletes a savepoint.
        
        @param headers: DeleteSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.DeleteSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary Deletes a savepoint.
        
        @param headers: DeleteSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary Deletes a savepoint.
        
        @return: DeleteSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSavepointHeaders()
        return self.delete_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def delete_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.DeleteSavepointResponse:
        """
        @summary Deletes a savepoint.
        
        @return: DeleteSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSavepointHeaders()
        return await self.delete_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def delete_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.DeleteScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteScheduledPlanResponse:
        """
        @summary 删除定时执行计划
        
        @param headers: DeleteScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.DeleteScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteScheduledPlanResponse:
        """
        @summary 删除定时执行计划
        
        @param headers: DeleteScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.DeleteScheduledPlanResponse:
        """
        @summary 删除定时执行计划
        
        @return: DeleteScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteScheduledPlanHeaders()
        return self.delete_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def delete_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.DeleteScheduledPlanResponse:
        """
        @summary 删除定时执行计划
        
        @return: DeleteScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteScheduledPlanHeaders()
        return await self.delete_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def delete_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.DeleteSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSessionClusterResponse:
        """
        @summary 删除session集群
        
        @param headers: DeleteSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.DeleteSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteSessionClusterResponse:
        """
        @summary 删除session集群
        
        @param headers: DeleteSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.DeleteSessionClusterResponse:
        """
        @summary 删除session集群
        
        @return: DeleteSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSessionClusterHeaders()
        return self.delete_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def delete_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.DeleteSessionClusterResponse:
        """
        @summary 删除session集群
        
        @return: DeleteSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSessionClusterHeaders()
        return await self.delete_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def delete_udf_artifact_with_options(
        self,
        namespace: str,
        udf_artifact_name: str,
        headers: ververica_20220718_models.DeleteUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteUdfArtifactResponse:
        """
        @summary 删除UdfArtifact
        
        @param headers: DeleteUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdfArtifactResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/{OpenApiUtilClient.get_encode_param(udf_artifact_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udf_artifact_with_options_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        headers: ververica_20220718_models.DeleteUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteUdfArtifactResponse:
        """
        @summary 删除UdfArtifact
        
        @param headers: DeleteUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdfArtifactResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/{OpenApiUtilClient.get_encode_param(udf_artifact_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udf_artifact(
        self,
        namespace: str,
        udf_artifact_name: str,
    ) -> ververica_20220718_models.DeleteUdfArtifactResponse:
        """
        @summary 删除UdfArtifact
        
        @return: DeleteUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteUdfArtifactHeaders()
        return self.delete_udf_artifact_with_options(namespace, udf_artifact_name, headers, runtime)

    async def delete_udf_artifact_async(
        self,
        namespace: str,
        udf_artifact_name: str,
    ) -> ververica_20220718_models.DeleteUdfArtifactResponse:
        """
        @summary 删除UdfArtifact
        
        @return: DeleteUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteUdfArtifactHeaders()
        return await self.delete_udf_artifact_with_options_async(namespace, udf_artifact_name, headers, runtime)

    def delete_udf_function_with_options(
        self,
        namespace: str,
        function_name: str,
        request: ververica_20220718_models.DeleteUdfFunctionRequest,
        headers: ververica_20220718_models.DeleteUdfFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteUdfFunctionResponse:
        """
        @summary Deletes an existing user-defined function (UDF) from a Realtime Compute for Apache Flink workspace.
        
        @param request: DeleteUdfFunctionRequest
        @param headers: DeleteUdfFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdfFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_name):
            query['className'] = request.class_name
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdfFunction',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/function/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteUdfFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udf_function_with_options_async(
        self,
        namespace: str,
        function_name: str,
        request: ververica_20220718_models.DeleteUdfFunctionRequest,
        headers: ververica_20220718_models.DeleteUdfFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteUdfFunctionResponse:
        """
        @summary Deletes an existing user-defined function (UDF) from a Realtime Compute for Apache Flink workspace.
        
        @param request: DeleteUdfFunctionRequest
        @param headers: DeleteUdfFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUdfFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_name):
            query['className'] = request.class_name
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUdfFunction',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/function/{OpenApiUtilClient.get_encode_param(function_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteUdfFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udf_function(
        self,
        namespace: str,
        function_name: str,
        request: ververica_20220718_models.DeleteUdfFunctionRequest,
    ) -> ververica_20220718_models.DeleteUdfFunctionResponse:
        """
        @summary Deletes an existing user-defined function (UDF) from a Realtime Compute for Apache Flink workspace.
        
        @param request: DeleteUdfFunctionRequest
        @return: DeleteUdfFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteUdfFunctionHeaders()
        return self.delete_udf_function_with_options(namespace, function_name, request, headers, runtime)

    async def delete_udf_function_async(
        self,
        namespace: str,
        function_name: str,
        request: ververica_20220718_models.DeleteUdfFunctionRequest,
    ) -> ververica_20220718_models.DeleteUdfFunctionResponse:
        """
        @summary Deletes an existing user-defined function (UDF) from a Realtime Compute for Apache Flink workspace.
        
        @param request: DeleteUdfFunctionRequest
        @return: DeleteUdfFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteUdfFunctionHeaders()
        return await self.delete_udf_function_with_options_async(namespace, function_name, request, headers, runtime)

    def delete_variable_with_options(
        self,
        namespace: str,
        name: str,
        headers: ververica_20220718_models.DeleteVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary Deletes a variable.
        
        @param headers: DeleteVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVariableResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_with_options_async(
        self,
        namespace: str,
        name: str,
        headers: ververica_20220718_models.DeleteVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary Deletes a variable.
        
        @param headers: DeleteVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVariableResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable(
        self,
        namespace: str,
        name: str,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary Deletes a variable.
        
        @return: DeleteVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteVariableHeaders()
        return self.delete_variable_with_options(namespace, name, headers, runtime)

    async def delete_variable_async(
        self,
        namespace: str,
        name: str,
    ) -> ververica_20220718_models.DeleteVariableResponse:
        """
        @summary Deletes a variable.
        
        @return: DeleteVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteVariableHeaders()
        return await self.delete_variable_with_options_async(namespace, name, headers, runtime)

    def deploy_deployment_draft_async_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.DeployDeploymentDraftAsyncRequest,
        headers: ververica_20220718_models.DeployDeploymentDraftAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeployDeploymentDraftAsyncResponse:
        """
        @summary deploy deploymentDraft async
        
        @param request: DeployDeploymentDraftAsyncRequest
        @param headers: DeployDeploymentDraftAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployDeploymentDraftAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DeployDeploymentDraftAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/async-deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeployDeploymentDraftAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_deployment_draft_async_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.DeployDeploymentDraftAsyncRequest,
        headers: ververica_20220718_models.DeployDeploymentDraftAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.DeployDeploymentDraftAsyncResponse:
        """
        @summary deploy deploymentDraft async
        
        @param request: DeployDeploymentDraftAsyncRequest
        @param headers: DeployDeploymentDraftAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployDeploymentDraftAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DeployDeploymentDraftAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/async-deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeployDeploymentDraftAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_deployment_draft_async(
        self,
        namespace: str,
        request: ververica_20220718_models.DeployDeploymentDraftAsyncRequest,
    ) -> ververica_20220718_models.DeployDeploymentDraftAsyncResponse:
        """
        @summary deploy deploymentDraft async
        
        @param request: DeployDeploymentDraftAsyncRequest
        @return: DeployDeploymentDraftAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeployDeploymentDraftAsyncHeaders()
        return self.deploy_deployment_draft_async_with_options(namespace, request, headers, runtime)

    async def deploy_deployment_draft_async_async(
        self,
        namespace: str,
        request: ververica_20220718_models.DeployDeploymentDraftAsyncRequest,
    ) -> ververica_20220718_models.DeployDeploymentDraftAsyncResponse:
        """
        @summary deploy deploymentDraft async
        
        @param request: DeployDeploymentDraftAsyncRequest
        @return: DeployDeploymentDraftAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeployDeploymentDraftAsyncHeaders()
        return await self.deploy_deployment_draft_async_with_options_async(namespace, request, headers, runtime)

    def execute_sql_statement_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ExecuteSqlStatementRequest,
        headers: ververica_20220718_models.ExecuteSqlStatementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ExecuteSqlStatementResponse:
        """
        @summary 执行sql语句
        
        @param request: ExecuteSqlStatementRequest
        @param headers: ExecuteSqlStatementHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSqlStatementResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ExecuteSqlStatement',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-statement/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ExecuteSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_sql_statement_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ExecuteSqlStatementRequest,
        headers: ververica_20220718_models.ExecuteSqlStatementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ExecuteSqlStatementResponse:
        """
        @summary 执行sql语句
        
        @param request: ExecuteSqlStatementRequest
        @param headers: ExecuteSqlStatementHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSqlStatementResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ExecuteSqlStatement',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-statement/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ExecuteSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_sql_statement(
        self,
        namespace: str,
        request: ververica_20220718_models.ExecuteSqlStatementRequest,
    ) -> ververica_20220718_models.ExecuteSqlStatementResponse:
        """
        @summary 执行sql语句
        
        @param request: ExecuteSqlStatementRequest
        @return: ExecuteSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ExecuteSqlStatementHeaders()
        return self.execute_sql_statement_with_options(namespace, request, headers, runtime)

    async def execute_sql_statement_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ExecuteSqlStatementRequest,
    ) -> ververica_20220718_models.ExecuteSqlStatementResponse:
        """
        @summary 执行sql语句
        
        @param request: ExecuteSqlStatementRequest
        @return: ExecuteSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ExecuteSqlStatementHeaders()
        return await self.execute_sql_statement_with_options_async(namespace, request, headers, runtime)

    def fetch_sql_preview_results_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.FetchSqlPreviewResultsRequest,
        headers: ververica_20220718_models.FetchSqlPreviewResultsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FetchSqlPreviewResultsResponse:
        """
        @summary 获取调试结果
        
        @param request: FetchSqlPreviewResultsRequest
        @param headers: FetchSqlPreviewResultsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchSqlPreviewResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['queryId'] = request.query_id
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchSqlPreviewResults',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/fetchResults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FetchSqlPreviewResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_sql_preview_results_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.FetchSqlPreviewResultsRequest,
        headers: ververica_20220718_models.FetchSqlPreviewResultsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FetchSqlPreviewResultsResponse:
        """
        @summary 获取调试结果
        
        @param request: FetchSqlPreviewResultsRequest
        @param headers: FetchSqlPreviewResultsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchSqlPreviewResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['queryId'] = request.query_id
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchSqlPreviewResults',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/fetchResults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FetchSqlPreviewResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_sql_preview_results(
        self,
        namespace: str,
        request: ververica_20220718_models.FetchSqlPreviewResultsRequest,
    ) -> ververica_20220718_models.FetchSqlPreviewResultsResponse:
        """
        @summary 获取调试结果
        
        @param request: FetchSqlPreviewResultsRequest
        @return: FetchSqlPreviewResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FetchSqlPreviewResultsHeaders()
        return self.fetch_sql_preview_results_with_options(namespace, request, headers, runtime)

    async def fetch_sql_preview_results_async(
        self,
        namespace: str,
        request: ververica_20220718_models.FetchSqlPreviewResultsRequest,
    ) -> ververica_20220718_models.FetchSqlPreviewResultsResponse:
        """
        @summary 获取调试结果
        
        @param request: FetchSqlPreviewResultsRequest
        @return: FetchSqlPreviewResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FetchSqlPreviewResultsHeaders()
        return await self.fetch_sql_preview_results_with_options_async(namespace, request, headers, runtime)

    def flink_api_proxy_with_options(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
        headers: ververica_20220718_models.FlinkApiProxyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary Provides a Flink request proxy.
        
        @param request: FlinkApiProxyRequest
        @param headers: FlinkApiProxyHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlinkApiProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlinkApiProxy',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/flink-ui/v2/proxy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FlinkApiProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def flink_api_proxy_with_options_async(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
        headers: ververica_20220718_models.FlinkApiProxyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary Provides a Flink request proxy.
        
        @param request: FlinkApiProxyRequest
        @param headers: FlinkApiProxyHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlinkApiProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlinkApiProxy',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/flink-ui/v2/proxy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FlinkApiProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flink_api_proxy(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary Provides a Flink request proxy.
        
        @param request: FlinkApiProxyRequest
        @return: FlinkApiProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FlinkApiProxyHeaders()
        return self.flink_api_proxy_with_options(request, headers, runtime)

    async def flink_api_proxy_async(
        self,
        request: ververica_20220718_models.FlinkApiProxyRequest,
    ) -> ververica_20220718_models.FlinkApiProxyResponse:
        """
        @summary Provides a Flink request proxy.
        
        @param request: FlinkApiProxyRequest
        @return: FlinkApiProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FlinkApiProxyHeaders()
        return await self.flink_api_proxy_with_options_async(request, headers, runtime)

    def generate_resource_plan_with_flink_conf_async_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary Submits a ticket that applies for asynchronous generation of the fine-grained resources. This operation returns the ID of the ticket for you to query the asynchronous generation result.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @param headers: GenerateResourcePlanWithFlinkConfAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateResourcePlanWithFlinkConfAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/resource-plan%3AasyncGenerate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_resource_plan_with_flink_conf_async_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary Submits a ticket that applies for asynchronous generation of the fine-grained resources. This operation returns the ID of the ticket for you to query the asynchronous generation result.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @param headers: GenerateResourcePlanWithFlinkConfAsyncHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateResourcePlanWithFlinkConfAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/resource-plan%3AasyncGenerate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_resource_plan_with_flink_conf_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary Submits a ticket that applies for asynchronous generation of the fine-grained resources. This operation returns the ID of the ticket for you to query the asynchronous generation result.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return self.generate_resource_plan_with_flink_conf_async_with_options(namespace, deployment_id, request, headers, runtime)

    async def generate_resource_plan_with_flink_conf_async_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        """
        @summary Submits a ticket that applies for asynchronous generation of the fine-grained resources. This operation returns the ID of the ticket for you to query the asynchronous generation result.
        
        @param request: GenerateResourcePlanWithFlinkConfAsyncRequest
        @return: GenerateResourcePlanWithFlinkConfAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return await self.generate_resource_plan_with_flink_conf_async_with_options_async(namespace, deployment_id, request, headers, runtime)

    def get_applied_scheduled_plan_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetAppliedScheduledPlanRequest,
        headers: ververica_20220718_models.GetAppliedScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetAppliedScheduledPlanResponse:
        """
        @summary 获取应用中的执行定时计划
        
        @param request: GetAppliedScheduledPlanRequest
        @param headers: GetAppliedScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppliedScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans%3AgetExecutedScheduledPlan',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetAppliedScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_applied_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetAppliedScheduledPlanRequest,
        headers: ververica_20220718_models.GetAppliedScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetAppliedScheduledPlanResponse:
        """
        @summary 获取应用中的执行定时计划
        
        @param request: GetAppliedScheduledPlanRequest
        @param headers: GetAppliedScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppliedScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans%3AgetExecutedScheduledPlan',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetAppliedScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_applied_scheduled_plan(
        self,
        namespace: str,
        request: ververica_20220718_models.GetAppliedScheduledPlanRequest,
    ) -> ververica_20220718_models.GetAppliedScheduledPlanResponse:
        """
        @summary 获取应用中的执行定时计划
        
        @param request: GetAppliedScheduledPlanRequest
        @return: GetAppliedScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetAppliedScheduledPlanHeaders()
        return self.get_applied_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def get_applied_scheduled_plan_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetAppliedScheduledPlanRequest,
    ) -> ververica_20220718_models.GetAppliedScheduledPlanResponse:
        """
        @summary 获取应用中的执行定时计划
        
        @param request: GetAppliedScheduledPlanRequest
        @return: GetAppliedScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetAppliedScheduledPlanHeaders()
        return await self.get_applied_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def get_catalogs_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetCatalogsRequest,
        headers: ververica_20220718_models.GetCatalogsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetCatalogsResponse:
        """
        @summary 获取catalog
        
        @param request: GetCatalogsRequest
        @param headers: GetCatalogsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['catalogName'] = request.catalog_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalogs_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetCatalogsRequest,
        headers: ververica_20220718_models.GetCatalogsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetCatalogsResponse:
        """
        @summary 获取catalog
        
        @param request: GetCatalogsRequest
        @param headers: GetCatalogsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['catalogName'] = request.catalog_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalogs(
        self,
        namespace: str,
        request: ververica_20220718_models.GetCatalogsRequest,
    ) -> ververica_20220718_models.GetCatalogsResponse:
        """
        @summary 获取catalog
        
        @param request: GetCatalogsRequest
        @return: GetCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetCatalogsHeaders()
        return self.get_catalogs_with_options(namespace, request, headers, runtime)

    async def get_catalogs_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetCatalogsRequest,
    ) -> ververica_20220718_models.GetCatalogsResponse:
        """
        @summary 获取catalog
        
        @param request: GetCatalogsRequest
        @return: GetCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetCatalogsHeaders()
        return await self.get_catalogs_with_options_async(namespace, request, headers, runtime)

    def get_databases_with_options(
        self,
        namespace: str,
        catalog_name: str,
        request: ververica_20220718_models.GetDatabasesRequest,
        headers: ververica_20220718_models.GetDatabasesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDatabasesResponse:
        """
        @summary 获取database
        
        @param request: GetDatabasesRequest
        @param headers: GetDatabasesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_name):
            query['databaseName'] = request.database_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabases',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs/{OpenApiUtilClient.get_encode_param(catalog_name)}/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_databases_with_options_async(
        self,
        namespace: str,
        catalog_name: str,
        request: ververica_20220718_models.GetDatabasesRequest,
        headers: ververica_20220718_models.GetDatabasesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDatabasesResponse:
        """
        @summary 获取database
        
        @param request: GetDatabasesRequest
        @param headers: GetDatabasesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_name):
            query['databaseName'] = request.database_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabases',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs/{OpenApiUtilClient.get_encode_param(catalog_name)}/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_databases(
        self,
        namespace: str,
        catalog_name: str,
        request: ververica_20220718_models.GetDatabasesRequest,
    ) -> ververica_20220718_models.GetDatabasesResponse:
        """
        @summary 获取database
        
        @param request: GetDatabasesRequest
        @return: GetDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDatabasesHeaders()
        return self.get_databases_with_options(namespace, catalog_name, request, headers, runtime)

    async def get_databases_async(
        self,
        namespace: str,
        catalog_name: str,
        request: ververica_20220718_models.GetDatabasesRequest,
    ) -> ververica_20220718_models.GetDatabasesResponse:
        """
        @summary 获取database
        
        @param request: GetDatabasesRequest
        @return: GetDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDatabasesHeaders()
        return await self.get_databases_with_options_async(namespace, catalog_name, request, headers, runtime)

    def get_deploy_deployment_draft_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetDeployDeploymentDraftResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeployDeploymentDraftResultResponse:
        """
        @summary get deploy deploymentDraft result
        
        @param headers: GetDeployDeploymentDraftResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployDeploymentDraftResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployDeploymentDraftResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/async-deploy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeployDeploymentDraftResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deploy_deployment_draft_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetDeployDeploymentDraftResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeployDeploymentDraftResultResponse:
        """
        @summary get deploy deploymentDraft result
        
        @param headers: GetDeployDeploymentDraftResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployDeploymentDraftResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployDeploymentDraftResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/async-deploy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeployDeploymentDraftResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deploy_deployment_draft_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetDeployDeploymentDraftResultResponse:
        """
        @summary get deploy deploymentDraft result
        
        @return: GetDeployDeploymentDraftResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeployDeploymentDraftResultHeaders()
        return self.get_deploy_deployment_draft_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_deploy_deployment_draft_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetDeployDeploymentDraftResultResponse:
        """
        @summary get deploy deploymentDraft result
        
        @return: GetDeployDeploymentDraftResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeployDeploymentDraftResultHeaders()
        return await self.get_deploy_deployment_draft_result_with_options_async(namespace, ticket_id, headers, runtime)

    def get_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary Obtains the details of a deployment.
        
        @param headers: GetDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary Obtains the details of a deployment.
        
        @param headers: GetDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary Obtains the details of a deployment.
        
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentHeaders()
        return self.get_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def get_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetDeploymentResponse:
        """
        @summary Obtains the details of a deployment.
        
        @return: GetDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentHeaders()
        return await self.get_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def get_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: ververica_20220718_models.GetDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentDraftResponse:
        """
        @summary get a deploymentDraft
        
        @param headers: GetDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentDraftResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: ververica_20220718_models.GetDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentDraftResponse:
        """
        @summary get a deploymentDraft
        
        @param headers: GetDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentDraftResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> ververica_20220718_models.GetDeploymentDraftResponse:
        """
        @summary get a deploymentDraft
        
        @return: GetDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentDraftHeaders()
        return self.get_deployment_draft_with_options(namespace, deployment_draft_id, headers, runtime)

    async def get_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> ververica_20220718_models.GetDeploymentDraftResponse:
        """
        @summary get a deploymentDraft
        
        @return: GetDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentDraftHeaders()
        return await self.get_deployment_draft_with_options_async(namespace, deployment_draft_id, headers, runtime)

    def get_deployment_draft_lock_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetDeploymentDraftLockRequest,
        headers: ververica_20220718_models.GetDeploymentDraftLockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentDraftLockResponse:
        """
        @summary get deploymentDraft lock
        
        @param request: GetDeploymentDraftLockRequest
        @param headers: GetDeploymentDraftLockHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentDraftLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_draft_id):
            query['deploymentDraftId'] = request.deployment_draft_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeploymentDraftLock',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/getLock',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentDraftLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_draft_lock_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetDeploymentDraftLockRequest,
        headers: ververica_20220718_models.GetDeploymentDraftLockHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetDeploymentDraftLockResponse:
        """
        @summary get deploymentDraft lock
        
        @param request: GetDeploymentDraftLockRequest
        @param headers: GetDeploymentDraftLockHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentDraftLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_draft_id):
            query['deploymentDraftId'] = request.deployment_draft_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeploymentDraftLock',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/getLock',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentDraftLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_draft_lock(
        self,
        namespace: str,
        request: ververica_20220718_models.GetDeploymentDraftLockRequest,
    ) -> ververica_20220718_models.GetDeploymentDraftLockResponse:
        """
        @summary get deploymentDraft lock
        
        @param request: GetDeploymentDraftLockRequest
        @return: GetDeploymentDraftLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentDraftLockHeaders()
        return self.get_deployment_draft_lock_with_options(namespace, request, headers, runtime)

    async def get_deployment_draft_lock_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetDeploymentDraftLockRequest,
    ) -> ververica_20220718_models.GetDeploymentDraftLockResponse:
        """
        @summary get deploymentDraft lock
        
        @param request: GetDeploymentDraftLockRequest
        @return: GetDeploymentDraftLockResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentDraftLockHeaders()
        return await self.get_deployment_draft_lock_with_options_async(namespace, request, headers, runtime)

    def get_events_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetEventsRequest,
        headers: ververica_20220718_models.GetEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetEventsResponse:
        """
        @summary 获取运行事件
        
        @param request: GetEventsRequest
        @param headers: GetEventsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEvents',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_events_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetEventsRequest,
        headers: ververica_20220718_models.GetEventsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetEventsResponse:
        """
        @summary 获取运行事件
        
        @param request: GetEventsRequest
        @param headers: GetEventsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEvents',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_events(
        self,
        namespace: str,
        request: ververica_20220718_models.GetEventsRequest,
    ) -> ververica_20220718_models.GetEventsResponse:
        """
        @summary 获取运行事件
        
        @param request: GetEventsRequest
        @return: GetEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetEventsHeaders()
        return self.get_events_with_options(namespace, request, headers, runtime)

    async def get_events_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetEventsRequest,
    ) -> ververica_20220718_models.GetEventsResponse:
        """
        @summary 获取运行事件
        
        @param request: GetEventsRequest
        @return: GetEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetEventsHeaders()
        return await self.get_events_with_options_async(namespace, request, headers, runtime)

    def get_folder_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetFolderRequest,
        headers: ververica_20220718_models.GetFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetFolderResponse:
        """
        @summary get a folder
        
        @param request: GetFolderRequest
        @param headers: GetFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetFolderRequest,
        headers: ververica_20220718_models.GetFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetFolderResponse:
        """
        @summary get a folder
        
        @param request: GetFolderRequest
        @param headers: GetFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        namespace: str,
        request: ververica_20220718_models.GetFolderRequest,
    ) -> ververica_20220718_models.GetFolderResponse:
        """
        @summary get a folder
        
        @param request: GetFolderRequest
        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetFolderHeaders()
        return self.get_folder_with_options(namespace, request, headers, runtime)

    async def get_folder_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetFolderRequest,
    ) -> ververica_20220718_models.GetFolderResponse:
        """
        @summary get a folder
        
        @param request: GetFolderRequest
        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetFolderHeaders()
        return await self.get_folder_with_options_async(namespace, request, headers, runtime)

    def get_generate_resource_plan_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetGenerateResourcePlanResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary Obtains the asynchronous generation result of fine-grained resources based on the ID of the ticket that applies for an asynchronous generation.
        
        @param headers: GetGenerateResourcePlanResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGenerateResourcePlanResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGenerateResourcePlanResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/resource-plan%3AasyncGenerate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetGenerateResourcePlanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generate_resource_plan_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: ververica_20220718_models.GetGenerateResourcePlanResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary Obtains the asynchronous generation result of fine-grained resources based on the ID of the ticket that applies for an asynchronous generation.
        
        @param headers: GetGenerateResourcePlanResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGenerateResourcePlanResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGenerateResourcePlanResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/tickets/{OpenApiUtilClient.get_encode_param(ticket_id)}/resource-plan%3AasyncGenerate',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetGenerateResourcePlanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generate_resource_plan_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary Obtains the asynchronous generation result of fine-grained resources based on the ID of the ticket that applies for an asynchronous generation.
        
        @return: GetGenerateResourcePlanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetGenerateResourcePlanResultHeaders()
        return self.get_generate_resource_plan_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_generate_resource_plan_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> ververica_20220718_models.GetGenerateResourcePlanResultResponse:
        """
        @summary Obtains the asynchronous generation result of fine-grained resources based on the ID of the ticket that applies for an asynchronous generation.
        
        @return: GetGenerateResourcePlanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetGenerateResourcePlanResultHeaders()
        return await self.get_generate_resource_plan_result_with_options_async(namespace, ticket_id, headers, runtime)

    def get_hot_update_job_result_with_options(
        self,
        namespace: str,
        job_hot_update_id: str,
        headers: ververica_20220718_models.GetHotUpdateJobResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetHotUpdateJobResultResponse:
        """
        @summary 查询动态更新结果
        
        @param headers: GetHotUpdateJobResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotUpdateJobResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetHotUpdateJobResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/hot-updates/{OpenApiUtilClient.get_encode_param(job_hot_update_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetHotUpdateJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_update_job_result_with_options_async(
        self,
        namespace: str,
        job_hot_update_id: str,
        headers: ververica_20220718_models.GetHotUpdateJobResultHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetHotUpdateJobResultResponse:
        """
        @summary 查询动态更新结果
        
        @param headers: GetHotUpdateJobResultHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHotUpdateJobResultResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetHotUpdateJobResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/hot-updates/{OpenApiUtilClient.get_encode_param(job_hot_update_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetHotUpdateJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_update_job_result(
        self,
        namespace: str,
        job_hot_update_id: str,
    ) -> ververica_20220718_models.GetHotUpdateJobResultResponse:
        """
        @summary 查询动态更新结果
        
        @return: GetHotUpdateJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetHotUpdateJobResultHeaders()
        return self.get_hot_update_job_result_with_options(namespace, job_hot_update_id, headers, runtime)

    async def get_hot_update_job_result_async(
        self,
        namespace: str,
        job_hot_update_id: str,
    ) -> ververica_20220718_models.GetHotUpdateJobResultResponse:
        """
        @summary 查询动态更新结果
        
        @return: GetHotUpdateJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetHotUpdateJobResultHeaders()
        return await self.get_hot_update_job_result_with_options_async(namespace, job_hot_update_id, headers, runtime)

    def get_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param headers: GetJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param headers: GetJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobHeaders()
        return self.get_job_with_options(namespace, job_id, headers, runtime)

    async def get_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobHeaders()
        return await self.get_job_with_options_async(namespace, job_id, headers, runtime)

    def get_job_diagnosis_with_options(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobDiagnosisHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobDiagnosisResponse:
        """
        @summary 获取作业诊断信息
        
        @param headers: GetJobDiagnosisHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDiagnosisResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJobDiagnosis',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/job-diagnoses/lite',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_diagnosis_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
        headers: ververica_20220718_models.GetJobDiagnosisHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetJobDiagnosisResponse:
        """
        @summary 获取作业诊断信息
        
        @param headers: GetJobDiagnosisHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDiagnosisResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJobDiagnosis',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/job-diagnoses/lite',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_diagnosis(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobDiagnosisResponse:
        """
        @summary 获取作业诊断信息
        
        @return: GetJobDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobDiagnosisHeaders()
        return self.get_job_diagnosis_with_options(namespace, deployment_id, job_id, headers, runtime)

    async def get_job_diagnosis_async(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
    ) -> ververica_20220718_models.GetJobDiagnosisResponse:
        """
        @summary 获取作业诊断信息
        
        @return: GetJobDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobDiagnosisHeaders()
        return await self.get_job_diagnosis_with_options_async(namespace, deployment_id, job_id, headers, runtime)

    def get_latest_job_start_log_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetLatestJobStartLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetLatestJobStartLogResponse:
        """
        @summary Obtains the latest startup logs of a job.
        
        @param headers: GetLatestJobStartLogHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestJobStartLogResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetLatestJobStartLog',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/latest_jobmanager_start_log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetLatestJobStartLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_job_start_log_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: ververica_20220718_models.GetLatestJobStartLogHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetLatestJobStartLogResponse:
        """
        @summary Obtains the latest startup logs of a job.
        
        @param headers: GetLatestJobStartLogHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestJobStartLogResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetLatestJobStartLog',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}/latest_jobmanager_start_log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetLatestJobStartLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_job_start_log(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetLatestJobStartLogResponse:
        """
        @summary Obtains the latest startup logs of a job.
        
        @return: GetLatestJobStartLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetLatestJobStartLogHeaders()
        return self.get_latest_job_start_log_with_options(namespace, deployment_id, headers, runtime)

    async def get_latest_job_start_log_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> ververica_20220718_models.GetLatestJobStartLogResponse:
        """
        @summary Obtains the latest startup logs of a job.
        
        @return: GetLatestJobStartLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetLatestJobStartLogHeaders()
        return await self.get_latest_job_start_log_with_options_async(namespace, deployment_id, headers, runtime)

    def get_lineage_info_with_options(
        self,
        request: ververica_20220718_models.GetLineageInfoRequest,
        headers: ververica_20220718_models.GetLineageInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetLineageInfoResponse:
        """
        @summary Obtains the lineage information of a deployment.
        
        @param request: GetLineageInfoRequest
        @param headers: GetLineageInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLineageInfoResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GetLineageInfo',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/meta/v2/lineage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetLineageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lineage_info_with_options_async(
        self,
        request: ververica_20220718_models.GetLineageInfoRequest,
        headers: ververica_20220718_models.GetLineageInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetLineageInfoResponse:
        """
        @summary Obtains the lineage information of a deployment.
        
        @param request: GetLineageInfoRequest
        @param headers: GetLineageInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLineageInfoResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GetLineageInfo',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/meta/v2/lineage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetLineageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lineage_info(
        self,
        request: ververica_20220718_models.GetLineageInfoRequest,
    ) -> ververica_20220718_models.GetLineageInfoResponse:
        """
        @summary Obtains the lineage information of a deployment.
        
        @param request: GetLineageInfoRequest
        @return: GetLineageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetLineageInfoHeaders()
        return self.get_lineage_info_with_options(request, headers, runtime)

    async def get_lineage_info_async(
        self,
        request: ververica_20220718_models.GetLineageInfoRequest,
    ) -> ververica_20220718_models.GetLineageInfoResponse:
        """
        @summary Obtains the lineage information of a deployment.
        
        @param request: GetLineageInfoRequest
        @return: GetLineageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetLineageInfoHeaders()
        return await self.get_lineage_info_with_options_async(request, headers, runtime)

    def get_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.GetMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary Queries the permissions of a member.
        
        @param headers: GetMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: ververica_20220718_models.GetMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary Queries the permissions of a member.
        
        @param headers: GetMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMemberResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members/{OpenApiUtilClient.get_encode_param(member)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_member(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary Queries the permissions of a member.
        
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetMemberHeaders()
        return self.get_member_with_options(namespace, member, headers, runtime)

    async def get_member_async(
        self,
        namespace: str,
        member: str,
    ) -> ververica_20220718_models.GetMemberResponse:
        """
        @summary Queries the permissions of a member.
        
        @return: GetMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetMemberHeaders()
        return await self.get_member_with_options_async(namespace, member, headers, runtime)

    def get_pre_signed_url_for_put_object_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetPreSignedUrlForPutObjectRequest,
        headers: ververica_20220718_models.GetPreSignedUrlForPutObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetPreSignedUrlForPutObjectResponse:
        """
        @summary 获取上传文件URL
        
        @param request: GetPreSignedUrlForPutObjectRequest
        @param headers: GetPreSignedUrlForPutObjectHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPreSignedUrlForPutObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPreSignedUrlForPutObject',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/artifacts/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/getPreSignedUrlForPutObject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetPreSignedUrlForPutObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pre_signed_url_for_put_object_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetPreSignedUrlForPutObjectRequest,
        headers: ververica_20220718_models.GetPreSignedUrlForPutObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetPreSignedUrlForPutObjectResponse:
        """
        @summary 获取上传文件URL
        
        @param request: GetPreSignedUrlForPutObjectRequest
        @param headers: GetPreSignedUrlForPutObjectHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPreSignedUrlForPutObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPreSignedUrlForPutObject',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/artifacts/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/getPreSignedUrlForPutObject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetPreSignedUrlForPutObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pre_signed_url_for_put_object(
        self,
        namespace: str,
        request: ververica_20220718_models.GetPreSignedUrlForPutObjectRequest,
    ) -> ververica_20220718_models.GetPreSignedUrlForPutObjectResponse:
        """
        @summary 获取上传文件URL
        
        @param request: GetPreSignedUrlForPutObjectRequest
        @return: GetPreSignedUrlForPutObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetPreSignedUrlForPutObjectHeaders()
        return self.get_pre_signed_url_for_put_object_with_options(namespace, request, headers, runtime)

    async def get_pre_signed_url_for_put_object_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetPreSignedUrlForPutObjectRequest,
    ) -> ververica_20220718_models.GetPreSignedUrlForPutObjectResponse:
        """
        @summary 获取上传文件URL
        
        @param request: GetPreSignedUrlForPutObjectRequest
        @return: GetPreSignedUrlForPutObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetPreSignedUrlForPutObjectHeaders()
        return await self.get_pre_signed_url_for_put_object_with_options_async(namespace, request, headers, runtime)

    def get_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.GetSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary Queries details of a savepoint and checkpoint.
        
        @param headers: GetSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: ververica_20220718_models.GetSavepointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary Queries details of a savepoint and checkpoint.
        
        @param headers: GetSavepointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavepointResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints/{OpenApiUtilClient.get_encode_param(savepoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary Queries details of a savepoint and checkpoint.
        
        @return: GetSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSavepointHeaders()
        return self.get_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def get_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> ververica_20220718_models.GetSavepointResponse:
        """
        @summary Queries details of a savepoint and checkpoint.
        
        @return: GetSavepointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSavepointHeaders()
        return await self.get_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def get_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.GetSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSessionClusterResponse:
        """
        @summary 获取session集群
        
        @param headers: GetSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.GetSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetSessionClusterResponse:
        """
        @summary 获取session集群
        
        @param headers: GetSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.GetSessionClusterResponse:
        """
        @summary 获取session集群
        
        @return: GetSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSessionClusterHeaders()
        return self.get_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def get_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.GetSessionClusterResponse:
        """
        @summary 获取session集群
        
        @return: GetSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSessionClusterHeaders()
        return await self.get_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def get_tables_with_options(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: ververica_20220718_models.GetTablesRequest,
        headers: ververica_20220718_models.GetTablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetTablesResponse:
        """
        @summary 获取table
        
        @param request: GetTablesRequest
        @param headers: GetTablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs/{OpenApiUtilClient.get_encode_param(catalog_name)}/databases/{OpenApiUtilClient.get_encode_param(database_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tables_with_options_async(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: ververica_20220718_models.GetTablesRequest,
        headers: ververica_20220718_models.GetTablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetTablesResponse:
        """
        @summary 获取table
        
        @param request: GetTablesRequest
        @param headers: GetTablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/catalogs/{OpenApiUtilClient.get_encode_param(catalog_name)}/databases/{OpenApiUtilClient.get_encode_param(database_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tables(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: ververica_20220718_models.GetTablesRequest,
    ) -> ververica_20220718_models.GetTablesResponse:
        """
        @summary 获取table
        
        @param request: GetTablesRequest
        @return: GetTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetTablesHeaders()
        return self.get_tables_with_options(namespace, catalog_name, database_name, request, headers, runtime)

    async def get_tables_async(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: ververica_20220718_models.GetTablesRequest,
    ) -> ververica_20220718_models.GetTablesResponse:
        """
        @summary 获取table
        
        @param request: GetTablesRequest
        @return: GetTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetTablesHeaders()
        return await self.get_tables_with_options_async(namespace, catalog_name, database_name, request, headers, runtime)

    def get_udf_artifacts_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.GetUdfArtifactsRequest,
        headers: ververica_20220718_models.GetUdfArtifactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetUdfArtifactsResponse:
        """
        @summary Obtains the details of the JAR or Python file that corresponds to the user-defined function (UDF) that you upload and create.
        
        @param request: GetUdfArtifactsRequest
        @param headers: GetUdfArtifactsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUdfArtifactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUdfArtifacts',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetUdfArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_udf_artifacts_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetUdfArtifactsRequest,
        headers: ververica_20220718_models.GetUdfArtifactsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.GetUdfArtifactsResponse:
        """
        @summary Obtains the details of the JAR or Python file that corresponds to the user-defined function (UDF) that you upload and create.
        
        @param request: GetUdfArtifactsRequest
        @param headers: GetUdfArtifactsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUdfArtifactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUdfArtifacts',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetUdfArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_udf_artifacts(
        self,
        namespace: str,
        request: ververica_20220718_models.GetUdfArtifactsRequest,
    ) -> ververica_20220718_models.GetUdfArtifactsResponse:
        """
        @summary Obtains the details of the JAR or Python file that corresponds to the user-defined function (UDF) that you upload and create.
        
        @param request: GetUdfArtifactsRequest
        @return: GetUdfArtifactsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetUdfArtifactsHeaders()
        return self.get_udf_artifacts_with_options(namespace, request, headers, runtime)

    async def get_udf_artifacts_async(
        self,
        namespace: str,
        request: ververica_20220718_models.GetUdfArtifactsRequest,
    ) -> ververica_20220718_models.GetUdfArtifactsResponse:
        """
        @summary Obtains the details of the JAR or Python file that corresponds to the user-defined function (UDF) that you upload and create.
        
        @param request: GetUdfArtifactsRequest
        @return: GetUdfArtifactsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetUdfArtifactsHeaders()
        return await self.get_udf_artifacts_with_options_async(namespace, request, headers, runtime)

    def hot_update_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.HotUpdateJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.HotUpdateJobResponse:
        """
        @summary Dynamically updates parameters or resources of a deployment that is running.
        
        @param headers: HotUpdateJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotUpdateJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='HotUpdateJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3AhotUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.HotUpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def hot_update_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: ververica_20220718_models.HotUpdateJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.HotUpdateJobResponse:
        """
        @summary Dynamically updates parameters or resources of a deployment that is running.
        
        @param headers: HotUpdateJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: HotUpdateJobResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='HotUpdateJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3AhotUpdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.HotUpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hot_update_job(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.HotUpdateJobResponse:
        """
        @summary Dynamically updates parameters or resources of a deployment that is running.
        
        @return: HotUpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.HotUpdateJobHeaders()
        return self.hot_update_job_with_options(namespace, job_id, headers, runtime)

    async def hot_update_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> ververica_20220718_models.HotUpdateJobResponse:
        """
        @summary Dynamically updates parameters or resources of a deployment that is running.
        
        @return: HotUpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.HotUpdateJobHeaders()
        return await self.hot_update_job_with_options_async(namespace, job_id, headers, runtime)

    def list_custom_connectors_with_options(
        self,
        namespace: str,
        headers: ververica_20220718_models.ListCustomConnectorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListCustomConnectorsResponse:
        """
        @summary Obtains a list of existing custom connectors.
        
        @param headers: ListCustomConnectorsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomConnectorsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCustomConnectors',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListCustomConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_connectors_with_options_async(
        self,
        namespace: str,
        headers: ververica_20220718_models.ListCustomConnectorsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListCustomConnectorsResponse:
        """
        @summary Obtains a list of existing custom connectors.
        
        @param headers: ListCustomConnectorsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomConnectorsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListCustomConnectors',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListCustomConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_connectors(
        self,
        namespace: str,
    ) -> ververica_20220718_models.ListCustomConnectorsResponse:
        """
        @summary Obtains a list of existing custom connectors.
        
        @return: ListCustomConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListCustomConnectorsHeaders()
        return self.list_custom_connectors_with_options(namespace, headers, runtime)

    async def list_custom_connectors_async(
        self,
        namespace: str,
    ) -> ververica_20220718_models.ListCustomConnectorsResponse:
        """
        @summary Obtains a list of existing custom connectors.
        
        @return: ListCustomConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListCustomConnectorsHeaders()
        return await self.list_custom_connectors_with_options_async(namespace, headers, runtime)

    def list_deployment_drafts_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentDraftsRequest,
        headers: ververica_20220718_models.ListDeploymentDraftsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentDraftsResponse:
        """
        @summary list deploymentDrafts
        
        @param request: ListDeploymentDraftsRequest
        @param headers: ListDeploymentDraftsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentDraftsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentDrafts',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentDraftsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_drafts_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentDraftsRequest,
        headers: ververica_20220718_models.ListDeploymentDraftsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentDraftsResponse:
        """
        @summary list deploymentDrafts
        
        @param request: ListDeploymentDraftsRequest
        @param headers: ListDeploymentDraftsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentDraftsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentDrafts',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentDraftsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_drafts(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentDraftsRequest,
    ) -> ververica_20220718_models.ListDeploymentDraftsResponse:
        """
        @summary list deploymentDrafts
        
        @param request: ListDeploymentDraftsRequest
        @return: ListDeploymentDraftsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentDraftsHeaders()
        return self.list_deployment_drafts_with_options(namespace, request, headers, runtime)

    async def list_deployment_drafts_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentDraftsRequest,
    ) -> ververica_20220718_models.ListDeploymentDraftsResponse:
        """
        @summary list deploymentDrafts
        
        @param request: ListDeploymentDraftsRequest
        @return: ListDeploymentDraftsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentDraftsHeaders()
        return await self.list_deployment_drafts_with_options_async(namespace, request, headers, runtime)

    def list_deployment_targets_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
        headers: ververica_20220718_models.ListDeploymentTargetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary Obtains a list of clusters in which deployments can be deployed. The cluster can be a session cluster or a per-job cluster.
        
        @param request: ListDeploymentTargetsRequest
        @param headers: ListDeploymentTargetsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentTargets',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_targets_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
        headers: ververica_20220718_models.ListDeploymentTargetsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary Obtains a list of clusters in which deployments can be deployed. The cluster can be a session cluster or a per-job cluster.
        
        @param request: ListDeploymentTargetsRequest
        @param headers: ListDeploymentTargetsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentTargets',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_targets(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary Obtains a list of clusters in which deployments can be deployed. The cluster can be a session cluster or a per-job cluster.
        
        @param request: ListDeploymentTargetsRequest
        @return: ListDeploymentTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentTargetsHeaders()
        return self.list_deployment_targets_with_options(namespace, request, headers, runtime)

    async def list_deployment_targets_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentTargetsRequest,
    ) -> ververica_20220718_models.ListDeploymentTargetsResponse:
        """
        @summary Obtains a list of clusters in which deployments can be deployed. The cluster can be a session cluster or a per-job cluster.
        
        @param request: ListDeploymentTargetsRequest
        @return: ListDeploymentTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentTargetsHeaders()
        return await self.list_deployment_targets_with_options_async(namespace, request, headers, runtime)

    def list_deployments_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
        headers: ververica_20220718_models.ListDeploymentsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary Obtains information about all deployments.
        
        @param request: ListDeploymentsRequest
        @param headers: ListDeploymentsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.label_key):
            query['labelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
        headers: ververica_20220718_models.ListDeploymentsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary Obtains information about all deployments.
        
        @param request: ListDeploymentsRequest
        @param headers: ListDeploymentsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.label_key):
            query['labelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not UtilClient.is_unset(request.modifier):
            query['modifier'] = request.modifier
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary Obtains information about all deployments.
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentsHeaders()
        return self.list_deployments_with_options(namespace, request, headers, runtime)

    async def list_deployments_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListDeploymentsRequest,
    ) -> ververica_20220718_models.ListDeploymentsResponse:
        """
        @summary Obtains information about all deployments.
        
        @param request: ListDeploymentsRequest
        @return: ListDeploymentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentsHeaders()
        return await self.list_deployments_with_options_async(namespace, request, headers, runtime)

    def list_editable_namespace_with_options(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEditableNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEditableNamespace',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/editable',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEditableNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_editable_namespace_with_options_async(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEditableNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEditableNamespace',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/editable',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEditableNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_editable_namespace(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @return: ListEditableNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_editable_namespace_with_options(request, headers, runtime)

    async def list_editable_namespace_async(
        self,
        request: ververica_20220718_models.ListEditableNamespaceRequest,
    ) -> ververica_20220718_models.ListEditableNamespaceResponse:
        """
        @summary 列出有编辑权限的项目空间。
        
        @param request: ListEditableNamespaceRequest
        @return: ListEditableNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_editable_namespace_with_options_async(request, headers, runtime)

    def list_engine_version_metadata_with_options(
        self,
        headers: ververica_20220718_models.ListEngineVersionMetadataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary Obtains a list of engine versions that are supported by Realtime Compute for Apache Flink.
        
        @param headers: ListEngineVersionMetadataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineVersionMetadataResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListEngineVersionMetadata',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/engine-version-meta.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEngineVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_version_metadata_with_options_async(
        self,
        headers: ververica_20220718_models.ListEngineVersionMetadataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary Obtains a list of engine versions that are supported by Realtime Compute for Apache Flink.
        
        @param headers: ListEngineVersionMetadataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineVersionMetadataResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListEngineVersionMetadata',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/engine-version-meta.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEngineVersionMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_version_metadata(self) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary Obtains a list of engine versions that are supported by Realtime Compute for Apache Flink.
        
        @return: ListEngineVersionMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListEngineVersionMetadataHeaders()
        return self.list_engine_version_metadata_with_options(headers, runtime)

    async def list_engine_version_metadata_async(self) -> ververica_20220718_models.ListEngineVersionMetadataResponse:
        """
        @summary Obtains a list of engine versions that are supported by Realtime Compute for Apache Flink.
        
        @return: ListEngineVersionMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListEngineVersionMetadataHeaders()
        return await self.list_engine_version_metadata_with_options_async(headers, runtime)

    def list_jobs_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
        headers: ververica_20220718_models.ListJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary Queries the information about all jobs in a deployment.
        
        @param request: ListJobsRequest
        @param headers: ListJobsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
        headers: ververica_20220718_models.ListJobsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary Queries the information about all jobs in a deployment.
        
        @param request: ListJobsRequest
        @param headers: ListJobsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_name):
            query['sortName'] = request.sort_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary Queries the information about all jobs in a deployment.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListJobsHeaders()
        return self.list_jobs_with_options(namespace, request, headers, runtime)

    async def list_jobs_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListJobsRequest,
    ) -> ververica_20220718_models.ListJobsResponse:
        """
        @summary Queries the information about all jobs in a deployment.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListJobsHeaders()
        return await self.list_jobs_with_options_async(namespace, request, headers, runtime)

    def list_members_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
        headers: ververica_20220718_models.ListMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary Queries the mappings between the ID and permissions of a member in a specific namespace.
        
        @param request: ListMembersRequest
        @param headers: ListMembersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
        headers: ververica_20220718_models.ListMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary Queries the mappings between the ID and permissions of a member in a specific namespace.
        
        @param request: ListMembersRequest
        @param headers: ListMembersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMembers',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary Queries the mappings between the ID and permissions of a member in a specific namespace.
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListMembersHeaders()
        return self.list_members_with_options(namespace, request, headers, runtime)

    async def list_members_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListMembersRequest,
    ) -> ververica_20220718_models.ListMembersResponse:
        """
        @summary Queries the mappings between the ID and permissions of a member in a specific namespace.
        
        @param request: ListMembersRequest
        @return: ListMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListMembersHeaders()
        return await self.list_members_with_options_async(namespace, request, headers, runtime)

    def list_savepoints_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
        headers: ververica_20220718_models.ListSavepointsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary Obtains a list of savepoints or checkpoints.
        
        @param request: ListSavepointsRequest
        @param headers: ListSavepointsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavepointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavepoints',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSavepointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_savepoints_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
        headers: ververica_20220718_models.ListSavepointsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary Obtains a list of savepoints or checkpoints.
        
        @param request: ListSavepointsRequest
        @param headers: ListSavepointsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavepointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavepoints',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/savepoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSavepointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_savepoints(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary Obtains a list of savepoints or checkpoints.
        
        @param request: ListSavepointsRequest
        @return: ListSavepointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSavepointsHeaders()
        return self.list_savepoints_with_options(namespace, request, headers, runtime)

    async def list_savepoints_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListSavepointsRequest,
    ) -> ververica_20220718_models.ListSavepointsResponse:
        """
        @summary Obtains a list of savepoints or checkpoints.
        
        @param request: ListSavepointsRequest
        @return: ListSavepointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSavepointsHeaders()
        return await self.list_savepoints_with_options_async(namespace, request, headers, runtime)

    def list_scheduled_plan_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanRequest,
        headers: ververica_20220718_models.ListScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListScheduledPlanResponse:
        """
        @summary 列表定时执行计划
        
        @param request: ListScheduledPlanRequest
        @param headers: ListScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanRequest,
        headers: ververica_20220718_models.ListScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListScheduledPlanResponse:
        """
        @summary 列表定时执行计划
        
        @param request: ListScheduledPlanRequest
        @param headers: ListScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_plan(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanRequest,
    ) -> ververica_20220718_models.ListScheduledPlanResponse:
        """
        @summary 列表定时执行计划
        
        @param request: ListScheduledPlanRequest
        @return: ListScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListScheduledPlanHeaders()
        return self.list_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def list_scheduled_plan_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanRequest,
    ) -> ververica_20220718_models.ListScheduledPlanResponse:
        """
        @summary 列表定时执行计划
        
        @param request: ListScheduledPlanRequest
        @return: ListScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListScheduledPlanHeaders()
        return await self.list_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def list_scheduled_plan_executed_history_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanExecutedHistoryRequest,
        headers: ververica_20220718_models.ListScheduledPlanExecutedHistoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse:
        """
        @summary 获取作业资源变更历史
        
        @param request: ListScheduledPlanExecutedHistoryRequest
        @param headers: ListScheduledPlanExecutedHistoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPlanExecutedHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPlanExecutedHistory',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/job-resource-upgradings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_plan_executed_history_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanExecutedHistoryRequest,
        headers: ververica_20220718_models.ListScheduledPlanExecutedHistoryHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse:
        """
        @summary 获取作业资源变更历史
        
        @param request: ListScheduledPlanExecutedHistoryRequest
        @param headers: ListScheduledPlanExecutedHistoryHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPlanExecutedHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPlanExecutedHistory',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/job-resource-upgradings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_plan_executed_history(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanExecutedHistoryRequest,
    ) -> ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse:
        """
        @summary 获取作业资源变更历史
        
        @param request: ListScheduledPlanExecutedHistoryRequest
        @return: ListScheduledPlanExecutedHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListScheduledPlanExecutedHistoryHeaders()
        return self.list_scheduled_plan_executed_history_with_options(namespace, request, headers, runtime)

    async def list_scheduled_plan_executed_history_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListScheduledPlanExecutedHistoryRequest,
    ) -> ververica_20220718_models.ListScheduledPlanExecutedHistoryResponse:
        """
        @summary 获取作业资源变更历史
        
        @param request: ListScheduledPlanExecutedHistoryRequest
        @return: ListScheduledPlanExecutedHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListScheduledPlanExecutedHistoryHeaders()
        return await self.list_scheduled_plan_executed_history_with_options_async(namespace, request, headers, runtime)

    def list_session_clusters_with_options(
        self,
        namespace: str,
        headers: ververica_20220718_models.ListSessionClustersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSessionClustersResponse:
        """
        @summary 列举session集群
        
        @param headers: ListSessionClustersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_clusters_with_options_async(
        self,
        namespace: str,
        headers: ververica_20220718_models.ListSessionClustersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListSessionClustersResponse:
        """
        @summary 列举session集群
        
        @param headers: ListSessionClustersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSessionClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_clusters(
        self,
        namespace: str,
    ) -> ververica_20220718_models.ListSessionClustersResponse:
        """
        @summary 列举session集群
        
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSessionClustersHeaders()
        return self.list_session_clusters_with_options(namespace, headers, runtime)

    async def list_session_clusters_async(
        self,
        namespace: str,
    ) -> ververica_20220718_models.ListSessionClustersResponse:
        """
        @summary 列举session集群
        
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSessionClustersHeaders()
        return await self.list_session_clusters_with_options_async(namespace, headers, runtime)

    def list_variables_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
        headers: ververica_20220718_models.ListVariablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary Obtains a list of variables.
        
        @param request: ListVariablesRequest
        @param headers: ListVariablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVariablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variables_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
        headers: ververica_20220718_models.ListVariablesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary Obtains a list of variables.
        
        @param request: ListVariablesRequest
        @param headers: ListVariablesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVariablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListVariablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variables(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary Obtains a list of variables.
        
        @param request: ListVariablesRequest
        @return: ListVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListVariablesHeaders()
        return self.list_variables_with_options(namespace, request, headers, runtime)

    async def list_variables_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ListVariablesRequest,
    ) -> ververica_20220718_models.ListVariablesResponse:
        """
        @summary Obtains a list of variables.
        
        @param request: ListVariablesRequest
        @return: ListVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListVariablesHeaders()
        return await self.list_variables_with_options_async(namespace, request, headers, runtime)

    def register_custom_connector_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterCustomConnectorRequest,
        headers: ververica_20220718_models.RegisterCustomConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.RegisterCustomConnectorResponse:
        """
        @summary Registers a custom connector in a namespace. The registered custom connector can be used in SQL statements.
        
        @param request: RegisterCustomConnectorRequest
        @param headers: RegisterCustomConnectorHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jar_url):
            query['jarUrl'] = request.jar_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomConnector',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors%3Aregister',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.RegisterCustomConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_connector_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterCustomConnectorRequest,
        headers: ververica_20220718_models.RegisterCustomConnectorHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.RegisterCustomConnectorResponse:
        """
        @summary Registers a custom connector in a namespace. The registered custom connector can be used in SQL statements.
        
        @param request: RegisterCustomConnectorRequest
        @param headers: RegisterCustomConnectorHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jar_url):
            query['jarUrl'] = request.jar_url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomConnector',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/connectors%3Aregister',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.RegisterCustomConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_connector(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterCustomConnectorRequest,
    ) -> ververica_20220718_models.RegisterCustomConnectorResponse:
        """
        @summary Registers a custom connector in a namespace. The registered custom connector can be used in SQL statements.
        
        @param request: RegisterCustomConnectorRequest
        @return: RegisterCustomConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.RegisterCustomConnectorHeaders()
        return self.register_custom_connector_with_options(namespace, request, headers, runtime)

    async def register_custom_connector_async(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterCustomConnectorRequest,
    ) -> ververica_20220718_models.RegisterCustomConnectorResponse:
        """
        @summary Registers a custom connector in a namespace. The registered custom connector can be used in SQL statements.
        
        @param request: RegisterCustomConnectorRequest
        @return: RegisterCustomConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.RegisterCustomConnectorHeaders()
        return await self.register_custom_connector_with_options_async(namespace, request, headers, runtime)

    def register_udf_function_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterUdfFunctionRequest,
        headers: ververica_20220718_models.RegisterUdfFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.RegisterUdfFunctionResponse:
        """
        @summary Registers specific or all of the user-defined functions (UDFs) that are parsed from the JAR files. The registered functions can be used in SQL statements.
        
        @param request: RegisterUdfFunctionRequest
        @param headers: RegisterUdfFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterUdfFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_name):
            query['className'] = request.class_name
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterUdfFunction',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/function%3AregisterUdfFunction',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.RegisterUdfFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_udf_function_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterUdfFunctionRequest,
        headers: ververica_20220718_models.RegisterUdfFunctionHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.RegisterUdfFunctionResponse:
        """
        @summary Registers specific or all of the user-defined functions (UDFs) that are parsed from the JAR files. The registered functions can be used in SQL statements.
        
        @param request: RegisterUdfFunctionRequest
        @param headers: RegisterUdfFunctionHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterUdfFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_name):
            query['className'] = request.class_name
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterUdfFunction',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/function%3AregisterUdfFunction',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.RegisterUdfFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_udf_function(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterUdfFunctionRequest,
    ) -> ververica_20220718_models.RegisterUdfFunctionResponse:
        """
        @summary Registers specific or all of the user-defined functions (UDFs) that are parsed from the JAR files. The registered functions can be used in SQL statements.
        
        @param request: RegisterUdfFunctionRequest
        @return: RegisterUdfFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.RegisterUdfFunctionHeaders()
        return self.register_udf_function_with_options(namespace, request, headers, runtime)

    async def register_udf_function_async(
        self,
        namespace: str,
        request: ververica_20220718_models.RegisterUdfFunctionRequest,
    ) -> ververica_20220718_models.RegisterUdfFunctionResponse:
        """
        @summary Registers specific or all of the user-defined functions (UDFs) that are parsed from the JAR files. The registered functions can be used in SQL statements.
        
        @param request: RegisterUdfFunctionRequest
        @return: RegisterUdfFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.RegisterUdfFunctionHeaders()
        return await self.register_udf_function_with_options_async(namespace, request, headers, runtime)

    def start_job_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
        headers: ververica_20220718_models.StartJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary Creates and starts a job.
        
        @param request: StartJobRequest
        @param headers: StartJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
        headers: ververica_20220718_models.StartJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary Creates and starts a job.
        
        @param request: StartJobRequest
        @param headers: StartJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary Creates and starts a job.
        
        @param request: StartJobRequest
        @return: StartJobResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobHeaders()
        return self.start_job_with_options(namespace, request, headers, runtime)

    async def start_job_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobRequest,
    ) -> ververica_20220718_models.StartJobResponse:
        """
        @deprecated OpenAPI StartJob is deprecated
        
        @summary Creates and starts a job.
        
        @param request: StartJobRequest
        @return: StartJobResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobHeaders()
        return await self.start_job_with_options_async(namespace, request, headers, runtime)

    def start_job_with_params_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
        headers: ververica_20220718_models.StartJobWithParamsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary Starts a job.
        
        @param request: StartJobWithParamsRequest
        @param headers: StartJobWithParamsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobWithParamsResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJobWithParams',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobWithParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_params_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
        headers: ververica_20220718_models.StartJobWithParamsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary Starts a job.
        
        @param request: StartJobWithParamsRequest
        @param headers: StartJobWithParamsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobWithParamsResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StartJobWithParams',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobWithParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_with_params(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary Starts a job.
        
        @param request: StartJobWithParamsRequest
        @return: StartJobWithParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobWithParamsHeaders()
        return self.start_job_with_params_with_options(namespace, request, headers, runtime)

    async def start_job_with_params_async(
        self,
        namespace: str,
        request: ververica_20220718_models.StartJobWithParamsRequest,
    ) -> ververica_20220718_models.StartJobWithParamsResponse:
        """
        @summary Starts a job.
        
        @param request: StartJobWithParamsRequest
        @return: StartJobWithParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobWithParamsHeaders()
        return await self.start_job_with_params_with_options_async(namespace, request, headers, runtime)

    def start_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.StartSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartSessionClusterResponse:
        """
        @summary 启动session集群
        
        @param headers: StartSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StartSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.StartSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StartSessionClusterResponse:
        """
        @summary 启动session集群
        
        @param headers: StartSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StartSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}%3Astart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.StartSessionClusterResponse:
        """
        @summary 启动session集群
        
        @return: StartSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartSessionClusterHeaders()
        return self.start_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def start_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.StartSessionClusterResponse:
        """
        @summary 启动session集群
        
        @return: StartSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartSessionClusterHeaders()
        return await self.start_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def stop_apply_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.StopApplyScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopApplyScheduledPlanResponse:
        """
        @summary 停止应用执行定时计划
        
        @param headers: StopApplyScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplyScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StopApplyScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}%3Astop',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopApplyScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_apply_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: ververica_20220718_models.StopApplyScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopApplyScheduledPlanResponse:
        """
        @summary 停止应用执行定时计划
        
        @param headers: StopApplyScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplyScheduledPlanResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StopApplyScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}%3Astop',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopApplyScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_apply_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.StopApplyScheduledPlanResponse:
        """
        @summary 停止应用执行定时计划
        
        @return: StopApplyScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopApplyScheduledPlanHeaders()
        return self.stop_apply_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def stop_apply_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> ververica_20220718_models.StopApplyScheduledPlanResponse:
        """
        @summary 停止应用执行定时计划
        
        @return: StopApplyScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopApplyScheduledPlanHeaders()
        return await self.stop_apply_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def stop_job_with_options(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
        headers: ververica_20220718_models.StopJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary Stops a job.
        
        @param request: StopJobRequest
        @param headers: StopJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
        headers: ververica_20220718_models.StopJobHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary Stops a job.
        
        @param request: StopJobRequest
        @param headers: StopJobHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary Stops a job.
        
        @param request: StopJobRequest
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopJobHeaders()
        return self.stop_job_with_options(namespace, job_id, request, headers, runtime)

    async def stop_job_async(
        self,
        namespace: str,
        job_id: str,
        request: ververica_20220718_models.StopJobRequest,
    ) -> ververica_20220718_models.StopJobResponse:
        """
        @summary Stops a job.
        
        @param request: StopJobRequest
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopJobHeaders()
        return await self.stop_job_with_options_async(namespace, job_id, request, headers, runtime)

    def stop_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.StopSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopSessionClusterResponse:
        """
        @summary 停止session集群
        
        @param headers: StopSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StopSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: ververica_20220718_models.StopSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.StopSessionClusterResponse:
        """
        @summary 停止session集群
        
        @param headers: StopSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSessionClusterResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='StopSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}%3Astop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.StopSessionClusterResponse:
        """
        @summary 停止session集群
        
        @return: StopSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopSessionClusterHeaders()
        return self.stop_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def stop_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> ververica_20220718_models.StopSessionClusterResponse:
        """
        @summary 停止session集群
        
        @return: StopSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopSessionClusterHeaders()
        return await self.stop_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def submit_sql_preview_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.SubmitSqlPreviewRequest,
        headers: ververica_20220718_models.SubmitSqlPreviewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.SubmitSqlPreviewResponse:
        """
        @summary 提交sql调试
        
        @param request: SubmitSqlPreviewRequest
        @param headers: SubmitSqlPreviewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSqlPreviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='SubmitSqlPreview',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.SubmitSqlPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sql_preview_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.SubmitSqlPreviewRequest,
        headers: ververica_20220718_models.SubmitSqlPreviewHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.SubmitSqlPreviewResponse:
        """
        @summary 提交sql调试
        
        @param request: SubmitSqlPreviewRequest
        @param headers: SubmitSqlPreviewHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSqlPreviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='SubmitSqlPreview',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-preview/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.SubmitSqlPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sql_preview(
        self,
        namespace: str,
        request: ververica_20220718_models.SubmitSqlPreviewRequest,
    ) -> ververica_20220718_models.SubmitSqlPreviewResponse:
        """
        @summary 提交sql调试
        
        @param request: SubmitSqlPreviewRequest
        @return: SubmitSqlPreviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.SubmitSqlPreviewHeaders()
        return self.submit_sql_preview_with_options(namespace, request, headers, runtime)

    async def submit_sql_preview_async(
        self,
        namespace: str,
        request: ververica_20220718_models.SubmitSqlPreviewRequest,
    ) -> ververica_20220718_models.SubmitSqlPreviewResponse:
        """
        @summary 提交sql调试
        
        @param request: SubmitSqlPreviewRequest
        @return: SubmitSqlPreviewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.SubmitSqlPreviewHeaders()
        return await self.submit_sql_preview_with_options_async(namespace, request, headers, runtime)

    def update_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
        headers: ververica_20220718_models.UpdateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary Updates information about a deployment.
        
        @param request: UpdateDeploymentRequest
        @param headers: UpdateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
        headers: ververica_20220718_models.UpdateDeploymentHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary Updates information about a deployment.
        
        @param request: UpdateDeploymentRequest
        @param headers: UpdateDeploymentHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployments/{OpenApiUtilClient.get_encode_param(deployment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary Updates information about a deployment.
        
        @param request: UpdateDeploymentRequest
        @return: UpdateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentHeaders()
        return self.update_deployment_with_options(namespace, deployment_id, request, headers, runtime)

    async def update_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
        request: ververica_20220718_models.UpdateDeploymentRequest,
    ) -> ververica_20220718_models.UpdateDeploymentResponse:
        """
        @summary Updates information about a deployment.
        
        @param request: UpdateDeploymentRequest
        @return: UpdateDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentHeaders()
        return await self.update_deployment_with_options_async(namespace, deployment_id, request, headers, runtime)

    def update_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: ververica_20220718_models.UpdateDeploymentDraftRequest,
        headers: ververica_20220718_models.UpdateDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentDraftResponse:
        """
        @summary update a deploymentDraft
        
        @param request: UpdateDeploymentDraftRequest
        @param headers: UpdateDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentDraftResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: ververica_20220718_models.UpdateDeploymentDraftRequest,
        headers: ververica_20220718_models.UpdateDeploymentDraftHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentDraftResponse:
        """
        @summary update a deploymentDraft
        
        @param request: UpdateDeploymentDraftRequest
        @param headers: UpdateDeploymentDraftHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentDraftResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentDraft',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-drafts/{OpenApiUtilClient.get_encode_param(deployment_draft_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: ververica_20220718_models.UpdateDeploymentDraftRequest,
    ) -> ververica_20220718_models.UpdateDeploymentDraftResponse:
        """
        @summary update a deploymentDraft
        
        @param request: UpdateDeploymentDraftRequest
        @return: UpdateDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentDraftHeaders()
        return self.update_deployment_draft_with_options(namespace, deployment_draft_id, request, headers, runtime)

    async def update_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: ververica_20220718_models.UpdateDeploymentDraftRequest,
    ) -> ververica_20220718_models.UpdateDeploymentDraftResponse:
        """
        @summary update a deploymentDraft
        
        @param request: UpdateDeploymentDraftRequest
        @return: UpdateDeploymentDraftResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentDraftHeaders()
        return await self.update_deployment_draft_with_options_async(namespace, deployment_draft_id, request, headers, runtime)

    def update_deployment_target_with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetRequest,
        headers: ververica_20220718_models.UpdateDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentTargetResponse:
        """
        @summary 修改deploymentTarget
        
        @param request: UpdateDeploymentTargetRequest
        @param headers: UpdateDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentTargetResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_target_with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetRequest,
        headers: ververica_20220718_models.UpdateDeploymentTargetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentTargetResponse:
        """
        @summary 修改deploymentTarget
        
        @param request: UpdateDeploymentTargetRequest
        @param headers: UpdateDeploymentTargetHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentTargetResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentTarget',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_target(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetRequest,
    ) -> ververica_20220718_models.UpdateDeploymentTargetResponse:
        """
        @summary 修改deploymentTarget
        
        @param request: UpdateDeploymentTargetRequest
        @return: UpdateDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentTargetHeaders()
        return self.update_deployment_target_with_options(namespace, deployment_target_name, request, headers, runtime)

    async def update_deployment_target_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetRequest,
    ) -> ververica_20220718_models.UpdateDeploymentTargetResponse:
        """
        @summary 修改deploymentTarget
        
        @param request: UpdateDeploymentTargetRequest
        @return: UpdateDeploymentTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentTargetHeaders()
        return await self.update_deployment_target_with_options_async(namespace, deployment_target_name, request, headers, runtime)

    def update_deployment_target_v2with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetV2Request,
        headers: ververica_20220718_models.UpdateDeploymentTargetV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentTargetV2Response:
        """
        @summary 更新部署目标
        
        @param request: UpdateDeploymentTargetV2Request
        @param headers: UpdateDeploymentTargetV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentTargetV2Response
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentTargetV2',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/support-elastic/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentTargetV2Response(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_target_v2with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetV2Request,
        headers: ververica_20220718_models.UpdateDeploymentTargetV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateDeploymentTargetV2Response:
        """
        @summary 更新部署目标
        
        @param request: UpdateDeploymentTargetV2Request
        @param headers: UpdateDeploymentTargetV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentTargetV2Response
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentTargetV2',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/deployment-targets/support-elastic/{OpenApiUtilClient.get_encode_param(deployment_target_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentTargetV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_target_v2(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetV2Request,
    ) -> ververica_20220718_models.UpdateDeploymentTargetV2Response:
        """
        @summary 更新部署目标
        
        @param request: UpdateDeploymentTargetV2Request
        @return: UpdateDeploymentTargetV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentTargetV2Headers()
        return self.update_deployment_target_v2with_options(namespace, deployment_target_name, request, headers, runtime)

    async def update_deployment_target_v2_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: ververica_20220718_models.UpdateDeploymentTargetV2Request,
    ) -> ververica_20220718_models.UpdateDeploymentTargetV2Response:
        """
        @summary 更新部署目标
        
        @param request: UpdateDeploymentTargetV2Request
        @return: UpdateDeploymentTargetV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentTargetV2Headers()
        return await self.update_deployment_target_v2with_options_async(namespace, deployment_target_name, request, headers, runtime)

    def update_folder_with_options(
        self,
        namespace: str,
        folder_id: str,
        request: ververica_20220718_models.UpdateFolderRequest,
        headers: ververica_20220718_models.UpdateFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateFolderResponse:
        """
        @summary update a folder
        
        @param request: UpdateFolderRequest
        @param headers: UpdateFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFolderResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        namespace: str,
        folder_id: str,
        request: ververica_20220718_models.UpdateFolderRequest,
        headers: ververica_20220718_models.UpdateFolderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateFolderResponse:
        """
        @summary update a folder
        
        @param request: UpdateFolderRequest
        @param headers: UpdateFolderHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFolderResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/folder/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        namespace: str,
        folder_id: str,
        request: ververica_20220718_models.UpdateFolderRequest,
    ) -> ververica_20220718_models.UpdateFolderResponse:
        """
        @summary update a folder
        
        @param request: UpdateFolderRequest
        @return: UpdateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateFolderHeaders()
        return self.update_folder_with_options(namespace, folder_id, request, headers, runtime)

    async def update_folder_async(
        self,
        namespace: str,
        folder_id: str,
        request: ververica_20220718_models.UpdateFolderRequest,
    ) -> ververica_20220718_models.UpdateFolderResponse:
        """
        @summary update a folder
        
        @param request: UpdateFolderRequest
        @return: UpdateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateFolderHeaders()
        return await self.update_folder_with_options_async(namespace, folder_id, request, headers, runtime)

    def update_member_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
        headers: ververica_20220718_models.UpdateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary Updates the permissions of one or more members in a specific namespace.
        
        @param request: UpdateMemberRequest
        @param headers: UpdateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
        headers: ververica_20220718_models.UpdateMemberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary Updates the permissions of one or more members in a specific namespace.
        
        @param request: UpdateMemberRequest
        @param headers: UpdateMemberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/gateway/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/members',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary Updates the permissions of one or more members in a specific namespace.
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateMemberHeaders()
        return self.update_member_with_options(namespace, request, headers, runtime)

    async def update_member_async(
        self,
        namespace: str,
        request: ververica_20220718_models.UpdateMemberRequest,
    ) -> ververica_20220718_models.UpdateMemberResponse:
        """
        @summary Updates the permissions of one or more members in a specific namespace.
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateMemberHeaders()
        return await self.update_member_with_options_async(namespace, request, headers, runtime)

    def update_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: ververica_20220718_models.UpdateScheduledPlanRequest,
        headers: ververica_20220718_models.UpdateScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateScheduledPlanResponse:
        """
        @summary 更新定时执行计划
        
        @param request: UpdateScheduledPlanRequest
        @param headers: UpdateScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: ververica_20220718_models.UpdateScheduledPlanRequest,
        headers: ververica_20220718_models.UpdateScheduledPlanHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateScheduledPlanResponse:
        """
        @summary 更新定时执行计划
        
        @param request: UpdateScheduledPlanRequest
        @param headers: UpdateScheduledPlanHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduledPlanResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateScheduledPlan',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/scheduled-plans/{OpenApiUtilClient.get_encode_param(scheduled_plan_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: ververica_20220718_models.UpdateScheduledPlanRequest,
    ) -> ververica_20220718_models.UpdateScheduledPlanResponse:
        """
        @summary 更新定时执行计划
        
        @param request: UpdateScheduledPlanRequest
        @return: UpdateScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateScheduledPlanHeaders()
        return self.update_scheduled_plan_with_options(namespace, scheduled_plan_id, request, headers, runtime)

    async def update_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: ververica_20220718_models.UpdateScheduledPlanRequest,
    ) -> ververica_20220718_models.UpdateScheduledPlanResponse:
        """
        @summary 更新定时执行计划
        
        @param request: UpdateScheduledPlanRequest
        @return: UpdateScheduledPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateScheduledPlanHeaders()
        return await self.update_scheduled_plan_with_options_async(namespace, scheduled_plan_id, request, headers, runtime)

    def update_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        request: ververica_20220718_models.UpdateSessionClusterRequest,
        headers: ververica_20220718_models.UpdateSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateSessionClusterResponse:
        """
        @summary 更新session集群
        
        @param request: UpdateSessionClusterRequest
        @param headers: UpdateSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        request: ververica_20220718_models.UpdateSessionClusterRequest,
        headers: ververica_20220718_models.UpdateSessionClusterHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateSessionClusterResponse:
        """
        @summary 更新session集群
        
        @param request: UpdateSessionClusterRequest
        @param headers: UpdateSessionClusterHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSessionClusterResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSessionCluster',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sessionclusters/{OpenApiUtilClient.get_encode_param(session_cluster_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
        request: ververica_20220718_models.UpdateSessionClusterRequest,
    ) -> ververica_20220718_models.UpdateSessionClusterResponse:
        """
        @summary 更新session集群
        
        @param request: UpdateSessionClusterRequest
        @return: UpdateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateSessionClusterHeaders()
        return self.update_session_cluster_with_options(namespace, session_cluster_name, request, headers, runtime)

    async def update_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
        request: ververica_20220718_models.UpdateSessionClusterRequest,
    ) -> ververica_20220718_models.UpdateSessionClusterResponse:
        """
        @summary 更新session集群
        
        @param request: UpdateSessionClusterRequest
        @return: UpdateSessionClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateSessionClusterHeaders()
        return await self.update_session_cluster_with_options_async(namespace, session_cluster_name, request, headers, runtime)

    def update_udf_artifact_with_options(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: ververica_20220718_models.UpdateUdfArtifactRequest,
        headers: ververica_20220718_models.UpdateUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateUdfArtifactResponse:
        """
        @summary Updates the JAR file of the user-defined function (UDF) that you create.
        
        @param request: UpdateUdfArtifactRequest
        @param headers: UpdateUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUdfArtifactResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/{OpenApiUtilClient.get_encode_param(udf_artifact_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_udf_artifact_with_options_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: ververica_20220718_models.UpdateUdfArtifactRequest,
        headers: ververica_20220718_models.UpdateUdfArtifactHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateUdfArtifactResponse:
        """
        @summary Updates the JAR file of the user-defined function (UDF) that you create.
        
        @param request: UpdateUdfArtifactRequest
        @param headers: UpdateUdfArtifactHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUdfArtifactResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateUdfArtifact',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/udfartifacts/{OpenApiUtilClient.get_encode_param(udf_artifact_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_udf_artifact(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: ververica_20220718_models.UpdateUdfArtifactRequest,
    ) -> ververica_20220718_models.UpdateUdfArtifactResponse:
        """
        @summary Updates the JAR file of the user-defined function (UDF) that you create.
        
        @param request: UpdateUdfArtifactRequest
        @return: UpdateUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateUdfArtifactHeaders()
        return self.update_udf_artifact_with_options(namespace, udf_artifact_name, request, headers, runtime)

    async def update_udf_artifact_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: ververica_20220718_models.UpdateUdfArtifactRequest,
    ) -> ververica_20220718_models.UpdateUdfArtifactResponse:
        """
        @summary Updates the JAR file of the user-defined function (UDF) that you create.
        
        @param request: UpdateUdfArtifactRequest
        @return: UpdateUdfArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateUdfArtifactHeaders()
        return await self.update_udf_artifact_with_options_async(namespace, udf_artifact_name, request, headers, runtime)

    def update_variable_with_options(
        self,
        namespace: str,
        name: str,
        request: ververica_20220718_models.UpdateVariableRequest,
        headers: ververica_20220718_models.UpdateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateVariableResponse:
        """
        @summary 更新秘钥
        
        @param request: UpdateVariableRequest
        @param headers: UpdateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_with_options_async(
        self,
        namespace: str,
        name: str,
        request: ververica_20220718_models.UpdateVariableRequest,
        headers: ververica_20220718_models.UpdateVariableHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.UpdateVariableResponse:
        """
        @summary 更新秘钥
        
        @param request: UpdateVariableRequest
        @param headers: UpdateVariableHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVariableResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/variables/{OpenApiUtilClient.get_encode_param(name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable(
        self,
        namespace: str,
        name: str,
        request: ververica_20220718_models.UpdateVariableRequest,
    ) -> ververica_20220718_models.UpdateVariableResponse:
        """
        @summary 更新秘钥
        
        @param request: UpdateVariableRequest
        @return: UpdateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateVariableHeaders()
        return self.update_variable_with_options(namespace, name, request, headers, runtime)

    async def update_variable_async(
        self,
        namespace: str,
        name: str,
        request: ververica_20220718_models.UpdateVariableRequest,
    ) -> ververica_20220718_models.UpdateVariableResponse:
        """
        @summary 更新秘钥
        
        @param request: UpdateVariableRequest
        @return: UpdateVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateVariableHeaders()
        return await self.update_variable_with_options_async(namespace, name, request, headers, runtime)

    def validate_sql_statement_with_options(
        self,
        namespace: str,
        request: ververica_20220718_models.ValidateSqlStatementRequest,
        headers: ververica_20220718_models.ValidateSqlStatementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ValidateSqlStatementResponse:
        """
        @summary Verifies the code of an SQL deployment.
        
        @param request: ValidateSqlStatementRequest
        @param headers: ValidateSqlStatementHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ValidateSqlStatement',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-statement/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ValidateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_sql_statement_with_options_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ValidateSqlStatementRequest,
        headers: ververica_20220718_models.ValidateSqlStatementHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ververica_20220718_models.ValidateSqlStatementResponse:
        """
        @summary Verifies the code of an SQL deployment.
        
        @param request: ValidateSqlStatementRequest
        @param headers: ValidateSqlStatementHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ValidateSqlStatement',
            version='2022-07-18',
            protocol='HTTPS',
            pathname=f'/api/v2/namespaces/{OpenApiUtilClient.get_encode_param(namespace)}/sql-statement/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ValidateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_sql_statement(
        self,
        namespace: str,
        request: ververica_20220718_models.ValidateSqlStatementRequest,
    ) -> ververica_20220718_models.ValidateSqlStatementResponse:
        """
        @summary Verifies the code of an SQL deployment.
        
        @param request: ValidateSqlStatementRequest
        @return: ValidateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ValidateSqlStatementHeaders()
        return self.validate_sql_statement_with_options(namespace, request, headers, runtime)

    async def validate_sql_statement_async(
        self,
        namespace: str,
        request: ververica_20220718_models.ValidateSqlStatementRequest,
    ) -> ververica_20220718_models.ValidateSqlStatementResponse:
        """
        @summary Verifies the code of an SQL deployment.
        
        @param request: ValidateSqlStatementRequest
        @return: ValidateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ValidateSqlStatementHeaders()
        return await self.validate_sql_statement_with_options_async(namespace, request, headers, runtime)
