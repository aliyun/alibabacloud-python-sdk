# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_ververica20220718 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.ApplyScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}%3Aapply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.ApplyScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}%3Aapply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.ApplyScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.ApplyScheduledPlanHeaders()
        return self.apply_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def apply_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.ApplyScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.ApplyScheduledPlanHeaders()
        return await self.apply_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def cancel_sql_preview_with_options(
        self,
        namespace: str,
        request: main_models.CancelSqlPreviewRequest,
        headers: main_models.CancelSqlPreviewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSqlPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['queryId'] = request.query_id
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelSqlPreview',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/cancel',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSqlPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_sql_preview_with_options_async(
        self,
        namespace: str,
        request: main_models.CancelSqlPreviewRequest,
        headers: main_models.CancelSqlPreviewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSqlPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['queryId'] = request.query_id
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelSqlPreview',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/cancel',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSqlPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_sql_preview(
        self,
        namespace: str,
        request: main_models.CancelSqlPreviewRequest,
    ) -> main_models.CancelSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelSqlPreviewHeaders()
        return self.cancel_sql_preview_with_options(namespace, request, headers, runtime)

    async def cancel_sql_preview_async(
        self,
        namespace: str,
        request: main_models.CancelSqlPreviewRequest,
    ) -> main_models.CancelSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = main_models.CancelSqlPreviewHeaders()
        return await self.cancel_sql_preview_with_options_async(namespace, request, headers, runtime)

    def create_deployment_with_options(
        self,
        namespace: str,
        request: main_models.CreateDeploymentRequest,
        headers: main_models.CreateDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentRequest,
        headers: main_models.CreateDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment(
        self,
        namespace: str,
        request: main_models.CreateDeploymentRequest,
    ) -> main_models.CreateDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentHeaders()
        return self.create_deployment_with_options(namespace, request, headers, runtime)

    async def create_deployment_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentRequest,
    ) -> main_models.CreateDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentHeaders()
        return await self.create_deployment_with_options_async(namespace, request, headers, runtime)

    def create_deployment_draft_with_options(
        self,
        namespace: str,
        request: main_models.CreateDeploymentDraftRequest,
        headers: main_models.CreateDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentDraftResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_draft_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentDraftRequest,
        headers: main_models.CreateDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentDraftResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_draft(
        self,
        namespace: str,
        request: main_models.CreateDeploymentDraftRequest,
    ) -> main_models.CreateDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentDraftHeaders()
        return self.create_deployment_draft_with_options(namespace, request, headers, runtime)

    async def create_deployment_draft_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentDraftRequest,
    ) -> main_models.CreateDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentDraftHeaders()
        return await self.create_deployment_draft_with_options_async(namespace, request, headers, runtime)

    def create_deployment_target_with_options(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetRequest,
        headers: main_models.CreateDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_target_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetRequest,
        headers: main_models.CreateDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_target(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetRequest,
    ) -> main_models.CreateDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentTargetHeaders()
        return self.create_deployment_target_with_options(namespace, request, headers, runtime)

    async def create_deployment_target_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetRequest,
    ) -> main_models.CreateDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentTargetHeaders()
        return await self.create_deployment_target_with_options_async(namespace, request, headers, runtime)

    def create_deployment_target_v2with_options(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetV2Request,
        headers: main_models.CreateDeploymentTargetV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentTargetV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentTargetV2',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/support-elastic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentTargetV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_target_v2with_options_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetV2Request,
        headers: main_models.CreateDeploymentTargetV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentTargetV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_target_name):
            query['deploymentTargetName'] = request.deployment_target_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentTargetV2',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/support-elastic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentTargetV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_target_v2(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetV2Request,
    ) -> main_models.CreateDeploymentTargetV2Response:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentTargetV2Headers()
        return self.create_deployment_target_v2with_options(namespace, request, headers, runtime)

    async def create_deployment_target_v2_async(
        self,
        namespace: str,
        request: main_models.CreateDeploymentTargetV2Request,
    ) -> main_models.CreateDeploymentTargetV2Response:
        runtime = RuntimeOptions()
        headers = main_models.CreateDeploymentTargetV2Headers()
        return await self.create_deployment_target_v2with_options_async(namespace, request, headers, runtime)

    def create_folder_with_options(
        self,
        namespace: str,
        request: main_models.CreateFolderRequest,
        headers: main_models.CreateFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateFolderRequest,
        headers: main_models.CreateFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        namespace: str,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateFolderHeaders()
        return self.create_folder_with_options(namespace, request, headers, runtime)

    async def create_folder_async(
        self,
        namespace: str,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateFolderHeaders()
        return await self.create_folder_with_options_async(namespace, request, headers, runtime)

    def create_member_with_options(
        self,
        namespace: str,
        request: main_models.CreateMemberRequest,
        headers: main_models.CreateMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateMemberRequest,
        headers: main_models.CreateMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member(
        self,
        namespace: str,
        request: main_models.CreateMemberRequest,
    ) -> main_models.CreateMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateMemberHeaders()
        return self.create_member_with_options(namespace, request, headers, runtime)

    async def create_member_async(
        self,
        namespace: str,
        request: main_models.CreateMemberRequest,
    ) -> main_models.CreateMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateMemberHeaders()
        return await self.create_member_with_options_async(namespace, request, headers, runtime)

    def create_savepoint_with_options(
        self,
        namespace: str,
        request: main_models.CreateSavepointRequest,
        headers: main_models.CreateSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavepointResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_savepoint_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateSavepointRequest,
        headers: main_models.CreateSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavepointResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_savepoint(
        self,
        namespace: str,
        request: main_models.CreateSavepointRequest,
    ) -> main_models.CreateSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateSavepointHeaders()
        return self.create_savepoint_with_options(namespace, request, headers, runtime)

    async def create_savepoint_async(
        self,
        namespace: str,
        request: main_models.CreateSavepointRequest,
    ) -> main_models.CreateSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateSavepointHeaders()
        return await self.create_savepoint_with_options_async(namespace, request, headers, runtime)

    def create_scheduled_plan_with_options(
        self,
        namespace: str,
        request: main_models.CreateScheduledPlanRequest,
        headers: main_models.CreateScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledPlanResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateScheduledPlanRequest,
        headers: main_models.CreateScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledPlanResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_plan(
        self,
        namespace: str,
        request: main_models.CreateScheduledPlanRequest,
    ) -> main_models.CreateScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateScheduledPlanHeaders()
        return self.create_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def create_scheduled_plan_async(
        self,
        namespace: str,
        request: main_models.CreateScheduledPlanRequest,
    ) -> main_models.CreateScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateScheduledPlanHeaders()
        return await self.create_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def create_session_cluster_with_options(
        self,
        namespace: str,
        request: main_models.CreateSessionClusterRequest,
        headers: main_models.CreateSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionClusterResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_cluster_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateSessionClusterRequest,
        headers: main_models.CreateSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionClusterResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session_cluster(
        self,
        namespace: str,
        request: main_models.CreateSessionClusterRequest,
    ) -> main_models.CreateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateSessionClusterHeaders()
        return self.create_session_cluster_with_options(namespace, request, headers, runtime)

    async def create_session_cluster_async(
        self,
        namespace: str,
        request: main_models.CreateSessionClusterRequest,
    ) -> main_models.CreateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateSessionClusterHeaders()
        return await self.create_session_cluster_with_options_async(namespace, request, headers, runtime)

    def create_udf_artifact_with_options(
        self,
        namespace: str,
        request: main_models.CreateUdfArtifactRequest,
        headers: main_models.CreateUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfArtifactResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_udf_artifact_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateUdfArtifactRequest,
        headers: main_models.CreateUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfArtifactResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_udf_artifact(
        self,
        namespace: str,
        request: main_models.CreateUdfArtifactRequest,
    ) -> main_models.CreateUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateUdfArtifactHeaders()
        return self.create_udf_artifact_with_options(namespace, request, headers, runtime)

    async def create_udf_artifact_async(
        self,
        namespace: str,
        request: main_models.CreateUdfArtifactRequest,
    ) -> main_models.CreateUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateUdfArtifactHeaders()
        return await self.create_udf_artifact_with_options_async(namespace, request, headers, runtime)

    def create_variable_with_options(
        self,
        namespace: str,
        request: main_models.CreateVariableRequest,
        headers: main_models.CreateVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVariableResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_variable_with_options_async(
        self,
        namespace: str,
        request: main_models.CreateVariableRequest,
        headers: main_models.CreateVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVariableResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_variable(
        self,
        namespace: str,
        request: main_models.CreateVariableRequest,
    ) -> main_models.CreateVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateVariableHeaders()
        return self.create_variable_with_options(namespace, request, headers, runtime)

    async def create_variable_async(
        self,
        namespace: str,
        request: main_models.CreateVariableRequest,
    ) -> main_models.CreateVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateVariableHeaders()
        return await self.create_variable_with_options_async(namespace, request, headers, runtime)

    def delete_custom_connector_with_options(
        self,
        namespace: str,
        connector_name: str,
        headers: main_models.DeleteCustomConnectorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomConnectorResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomConnector',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors/{DaraURL.percent_encode(connector_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_connector_with_options_async(
        self,
        namespace: str,
        connector_name: str,
        headers: main_models.DeleteCustomConnectorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomConnectorResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomConnector',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors/{DaraURL.percent_encode(connector_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_connector(
        self,
        namespace: str,
        connector_name: str,
    ) -> main_models.DeleteCustomConnectorResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCustomConnectorHeaders()
        return self.delete_custom_connector_with_options(namespace, connector_name, headers, runtime)

    async def delete_custom_connector_async(
        self,
        namespace: str,
        connector_name: str,
    ) -> main_models.DeleteCustomConnectorResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteCustomConnectorHeaders()
        return await self.delete_custom_connector_with_options_async(namespace, connector_name, headers, runtime)

    def delete_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.DeleteDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.DeleteDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.DeleteDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentHeaders()
        return self.delete_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def delete_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.DeleteDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentHeaders()
        return await self.delete_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def delete_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: main_models.DeleteDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentDraftResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: main_models.DeleteDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentDraftResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> main_models.DeleteDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentDraftHeaders()
        return self.delete_deployment_draft_with_options(namespace, deployment_draft_id, headers, runtime)

    async def delete_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> main_models.DeleteDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentDraftHeaders()
        return await self.delete_deployment_draft_with_options_async(namespace, deployment_draft_id, headers, runtime)

    def delete_deployment_target_with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        headers: main_models.DeleteDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentTargetResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_target_with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        headers: main_models.DeleteDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentTargetResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_target(
        self,
        namespace: str,
        deployment_target_name: str,
    ) -> main_models.DeleteDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentTargetHeaders()
        return self.delete_deployment_target_with_options(namespace, deployment_target_name, headers, runtime)

    async def delete_deployment_target_async(
        self,
        namespace: str,
        deployment_target_name: str,
    ) -> main_models.DeleteDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteDeploymentTargetHeaders()
        return await self.delete_deployment_target_with_options_async(namespace, deployment_target_name, headers, runtime)

    def delete_folder_with_options(
        self,
        namespace: str,
        folder_id: str,
        headers: main_models.DeleteFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder/{DaraURL.percent_encode(folder_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        namespace: str,
        folder_id: str,
        headers: main_models.DeleteFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder/{DaraURL.percent_encode(folder_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        namespace: str,
        folder_id: str,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteFolderHeaders()
        return self.delete_folder_with_options(namespace, folder_id, headers, runtime)

    async def delete_folder_async(
        self,
        namespace: str,
        folder_id: str,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteFolderHeaders()
        return await self.delete_folder_with_options_async(namespace, folder_id, headers, runtime)

    def delete_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.DeleteJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.DeleteJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteJobHeaders()
        return self.delete_job_with_options(namespace, job_id, headers, runtime)

    async def delete_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteJobHeaders()
        return await self.delete_job_with_options_async(namespace, job_id, headers, runtime)

    def delete_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: main_models.DeleteMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemberResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members/{DaraURL.percent_encode(member)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: main_models.DeleteMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemberResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members/{DaraURL.percent_encode(member)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member(
        self,
        namespace: str,
        member: str,
    ) -> main_models.DeleteMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteMemberHeaders()
        return self.delete_member_with_options(namespace, member, headers, runtime)

    async def delete_member_async(
        self,
        namespace: str,
        member: str,
    ) -> main_models.DeleteMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteMemberHeaders()
        return await self.delete_member_with_options_async(namespace, member, headers, runtime)

    def delete_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: main_models.DeleteSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavepointResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints/{DaraURL.percent_encode(savepoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: main_models.DeleteSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavepointResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints/{DaraURL.percent_encode(savepoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> main_models.DeleteSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSavepointHeaders()
        return self.delete_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def delete_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> main_models.DeleteSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSavepointHeaders()
        return await self.delete_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def delete_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.DeleteScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.DeleteScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.DeleteScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteScheduledPlanHeaders()
        return self.delete_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def delete_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.DeleteScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteScheduledPlanHeaders()
        return await self.delete_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def delete_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.DeleteSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.DeleteSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.DeleteSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSessionClusterHeaders()
        return self.delete_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def delete_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.DeleteSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteSessionClusterHeaders()
        return await self.delete_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def delete_udf_artifact_with_options(
        self,
        namespace: str,
        udf_artifact_name: str,
        headers: main_models.DeleteUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfArtifactResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/{DaraURL.percent_encode(udf_artifact_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udf_artifact_with_options_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        headers: main_models.DeleteUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfArtifactResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/{DaraURL.percent_encode(udf_artifact_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udf_artifact(
        self,
        namespace: str,
        udf_artifact_name: str,
    ) -> main_models.DeleteUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUdfArtifactHeaders()
        return self.delete_udf_artifact_with_options(namespace, udf_artifact_name, headers, runtime)

    async def delete_udf_artifact_async(
        self,
        namespace: str,
        udf_artifact_name: str,
    ) -> main_models.DeleteUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUdfArtifactHeaders()
        return await self.delete_udf_artifact_with_options_async(namespace, udf_artifact_name, headers, runtime)

    def delete_udf_function_with_options(
        self,
        namespace: str,
        function_name: str,
        request: main_models.DeleteUdfFunctionRequest,
        headers: main_models.DeleteUdfFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdfFunction',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/function/{DaraURL.percent_encode(function_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udf_function_with_options_async(
        self,
        namespace: str,
        function_name: str,
        request: main_models.DeleteUdfFunctionRequest,
        headers: main_models.DeleteUdfFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdfFunction',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/function/{DaraURL.percent_encode(function_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udf_function(
        self,
        namespace: str,
        function_name: str,
        request: main_models.DeleteUdfFunctionRequest,
    ) -> main_models.DeleteUdfFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUdfFunctionHeaders()
        return self.delete_udf_function_with_options(namespace, function_name, request, headers, runtime)

    async def delete_udf_function_async(
        self,
        namespace: str,
        function_name: str,
        request: main_models.DeleteUdfFunctionRequest,
    ) -> main_models.DeleteUdfFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUdfFunctionHeaders()
        return await self.delete_udf_function_with_options_async(namespace, function_name, request, headers, runtime)

    def delete_variable_with_options(
        self,
        namespace: str,
        name: str,
        headers: main_models.DeleteVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVariableResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_variable_with_options_async(
        self,
        namespace: str,
        name: str,
        headers: main_models.DeleteVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVariableResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_variable(
        self,
        namespace: str,
        name: str,
    ) -> main_models.DeleteVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteVariableHeaders()
        return self.delete_variable_with_options(namespace, name, headers, runtime)

    async def delete_variable_async(
        self,
        namespace: str,
        name: str,
    ) -> main_models.DeleteVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteVariableHeaders()
        return await self.delete_variable_with_options_async(namespace, name, headers, runtime)

    def deploy_deployment_draft_async_with_options(
        self,
        namespace: str,
        request: main_models.DeployDeploymentDraftAsyncRequest,
        headers: main_models.DeployDeploymentDraftAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeployDeploymentDraftAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DeployDeploymentDraftAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/async-deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployDeploymentDraftAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_deployment_draft_async_with_options_async(
        self,
        namespace: str,
        request: main_models.DeployDeploymentDraftAsyncRequest,
        headers: main_models.DeployDeploymentDraftAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeployDeploymentDraftAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'DeployDeploymentDraftAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/async-deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployDeploymentDraftAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_deployment_draft_async(
        self,
        namespace: str,
        request: main_models.DeployDeploymentDraftAsyncRequest,
    ) -> main_models.DeployDeploymentDraftAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeployDeploymentDraftAsyncHeaders()
        return self.deploy_deployment_draft_async_with_options(namespace, request, headers, runtime)

    async def deploy_deployment_draft_async_async(
        self,
        namespace: str,
        request: main_models.DeployDeploymentDraftAsyncRequest,
    ) -> main_models.DeployDeploymentDraftAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeployDeploymentDraftAsyncHeaders()
        return await self.deploy_deployment_draft_async_with_options_async(namespace, request, headers, runtime)

    def execute_sql_statement_with_options(
        self,
        namespace: str,
        request: main_models.ExecuteSqlStatementRequest,
        headers: main_models.ExecuteSqlStatementHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSqlStatementResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSqlStatement',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-statement/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_sql_statement_with_options_async(
        self,
        namespace: str,
        request: main_models.ExecuteSqlStatementRequest,
        headers: main_models.ExecuteSqlStatementHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSqlStatementResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSqlStatement',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-statement/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_sql_statement(
        self,
        namespace: str,
        request: main_models.ExecuteSqlStatementRequest,
    ) -> main_models.ExecuteSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = main_models.ExecuteSqlStatementHeaders()
        return self.execute_sql_statement_with_options(namespace, request, headers, runtime)

    async def execute_sql_statement_async(
        self,
        namespace: str,
        request: main_models.ExecuteSqlStatementRequest,
    ) -> main_models.ExecuteSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = main_models.ExecuteSqlStatementHeaders()
        return await self.execute_sql_statement_with_options_async(namespace, request, headers, runtime)

    def fetch_sql_preview_results_with_options(
        self,
        namespace: str,
        request: main_models.FetchSqlPreviewResultsRequest,
        headers: main_models.FetchSqlPreviewResultsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FetchSqlPreviewResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['queryId'] = request.query_id
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchSqlPreviewResults',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/fetchResults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchSqlPreviewResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_sql_preview_results_with_options_async(
        self,
        namespace: str,
        request: main_models.FetchSqlPreviewResultsRequest,
        headers: main_models.FetchSqlPreviewResultsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FetchSqlPreviewResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['queryId'] = request.query_id
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FetchSqlPreviewResults',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/fetchResults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchSqlPreviewResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_sql_preview_results(
        self,
        namespace: str,
        request: main_models.FetchSqlPreviewResultsRequest,
    ) -> main_models.FetchSqlPreviewResultsResponse:
        runtime = RuntimeOptions()
        headers = main_models.FetchSqlPreviewResultsHeaders()
        return self.fetch_sql_preview_results_with_options(namespace, request, headers, runtime)

    async def fetch_sql_preview_results_async(
        self,
        namespace: str,
        request: main_models.FetchSqlPreviewResultsRequest,
    ) -> main_models.FetchSqlPreviewResultsResponse:
        runtime = RuntimeOptions()
        headers = main_models.FetchSqlPreviewResultsHeaders()
        return await self.fetch_sql_preview_results_with_options_async(namespace, request, headers, runtime)

    def flink_api_proxy_with_options(
        self,
        request: main_models.FlinkApiProxyRequest,
        headers: main_models.FlinkApiProxyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FlinkApiProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlinkApiProxy',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/flink-ui/v2/proxy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlinkApiProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def flink_api_proxy_with_options_async(
        self,
        request: main_models.FlinkApiProxyRequest,
        headers: main_models.FlinkApiProxyHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.FlinkApiProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlinkApiProxy',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/flink-ui/v2/proxy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlinkApiProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flink_api_proxy(
        self,
        request: main_models.FlinkApiProxyRequest,
    ) -> main_models.FlinkApiProxyResponse:
        runtime = RuntimeOptions()
        headers = main_models.FlinkApiProxyHeaders()
        return self.flink_api_proxy_with_options(request, headers, runtime)

    async def flink_api_proxy_async(
        self,
        request: main_models.FlinkApiProxyRequest,
    ) -> main_models.FlinkApiProxyResponse:
        runtime = RuntimeOptions()
        headers = main_models.FlinkApiProxyHeaders()
        return await self.flink_api_proxy_with_options_async(request, headers, runtime)

    def generate_resource_plan_with_flink_conf_async_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: main_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResourcePlanWithFlinkConfAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/resource-plan%3AasyncGenerate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_resource_plan_with_flink_conf_async_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
        headers: main_models.GenerateResourcePlanWithFlinkConfAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateResourcePlanWithFlinkConfAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/resource-plan%3AasyncGenerate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_resource_plan_with_flink_conf_async(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> main_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return self.generate_resource_plan_with_flink_conf_async_with_options(namespace, deployment_id, request, headers, runtime)

    async def generate_resource_plan_with_flink_conf_async_async(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.GenerateResourcePlanWithFlinkConfAsyncRequest,
    ) -> main_models.GenerateResourcePlanWithFlinkConfAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return await self.generate_resource_plan_with_flink_conf_async_with_options_async(namespace, deployment_id, request, headers, runtime)

    def get_applied_scheduled_plan_with_options(
        self,
        namespace: str,
        request: main_models.GetAppliedScheduledPlanRequest,
        headers: main_models.GetAppliedScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedScheduledPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans%3AgetExecutedScheduledPlan',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_applied_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: main_models.GetAppliedScheduledPlanRequest,
        headers: main_models.GetAppliedScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedScheduledPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans%3AgetExecutedScheduledPlan',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_applied_scheduled_plan(
        self,
        namespace: str,
        request: main_models.GetAppliedScheduledPlanRequest,
    ) -> main_models.GetAppliedScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAppliedScheduledPlanHeaders()
        return self.get_applied_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def get_applied_scheduled_plan_async(
        self,
        namespace: str,
        request: main_models.GetAppliedScheduledPlanRequest,
    ) -> main_models.GetAppliedScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetAppliedScheduledPlanHeaders()
        return await self.get_applied_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def get_catalogs_with_options(
        self,
        namespace: str,
        request: main_models.GetCatalogsRequest,
        headers: main_models.GetCatalogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['catalogName'] = request.catalog_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogs',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalogs_with_options_async(
        self,
        namespace: str,
        request: main_models.GetCatalogsRequest,
        headers: main_models.GetCatalogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['catalogName'] = request.catalog_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogs',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalogs(
        self,
        namespace: str,
        request: main_models.GetCatalogsRequest,
    ) -> main_models.GetCatalogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCatalogsHeaders()
        return self.get_catalogs_with_options(namespace, request, headers, runtime)

    async def get_catalogs_async(
        self,
        namespace: str,
        request: main_models.GetCatalogsRequest,
    ) -> main_models.GetCatalogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetCatalogsHeaders()
        return await self.get_catalogs_with_options_async(namespace, request, headers, runtime)

    def get_databases_with_options(
        self,
        namespace: str,
        catalog_name: str,
        request: main_models.GetDatabasesRequest,
        headers: main_models.GetDatabasesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name):
            query['databaseName'] = request.database_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabases',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs/{DaraURL.percent_encode(catalog_name)}/databases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_databases_with_options_async(
        self,
        namespace: str,
        catalog_name: str,
        request: main_models.GetDatabasesRequest,
        headers: main_models.GetDatabasesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name):
            query['databaseName'] = request.database_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabases',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs/{DaraURL.percent_encode(catalog_name)}/databases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_databases(
        self,
        namespace: str,
        catalog_name: str,
        request: main_models.GetDatabasesRequest,
    ) -> main_models.GetDatabasesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDatabasesHeaders()
        return self.get_databases_with_options(namespace, catalog_name, request, headers, runtime)

    async def get_databases_async(
        self,
        namespace: str,
        catalog_name: str,
        request: main_models.GetDatabasesRequest,
    ) -> main_models.GetDatabasesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDatabasesHeaders()
        return await self.get_databases_with_options_async(namespace, catalog_name, request, headers, runtime)

    def get_deploy_deployment_draft_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetDeployDeploymentDraftResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeployDeploymentDraftResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployDeploymentDraftResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/tickets/{DaraURL.percent_encode(ticket_id)}/async-deploy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeployDeploymentDraftResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deploy_deployment_draft_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetDeployDeploymentDraftResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeployDeploymentDraftResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployDeploymentDraftResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/tickets/{DaraURL.percent_encode(ticket_id)}/async-deploy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeployDeploymentDraftResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deploy_deployment_draft_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetDeployDeploymentDraftResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeployDeploymentDraftResultHeaders()
        return self.get_deploy_deployment_draft_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_deploy_deployment_draft_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetDeployDeploymentDraftResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeployDeploymentDraftResultHeaders()
        return await self.get_deploy_deployment_draft_result_with_options_async(namespace, ticket_id, headers, runtime)

    def get_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.GetDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.GetDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.GetDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentHeaders()
        return self.get_deployment_with_options(namespace, deployment_id, headers, runtime)

    async def get_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.GetDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentHeaders()
        return await self.get_deployment_with_options_async(namespace, deployment_id, headers, runtime)

    def get_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: main_models.GetDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentDraftResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        headers: main_models.GetDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentDraftResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> main_models.GetDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentDraftHeaders()
        return self.get_deployment_draft_with_options(namespace, deployment_draft_id, headers, runtime)

    async def get_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
    ) -> main_models.GetDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentDraftHeaders()
        return await self.get_deployment_draft_with_options_async(namespace, deployment_draft_id, headers, runtime)

    def get_deployment_draft_lock_with_options(
        self,
        namespace: str,
        request: main_models.GetDeploymentDraftLockRequest,
        headers: main_models.GetDeploymentDraftLockHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentDraftLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_draft_id):
            query['deploymentDraftId'] = request.deployment_draft_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentDraftLock',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/getLock',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentDraftLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_draft_lock_with_options_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentDraftLockRequest,
        headers: main_models.GetDeploymentDraftLockHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentDraftLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_draft_id):
            query['deploymentDraftId'] = request.deployment_draft_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentDraftLock',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/getLock',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentDraftLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_draft_lock(
        self,
        namespace: str,
        request: main_models.GetDeploymentDraftLockRequest,
    ) -> main_models.GetDeploymentDraftLockResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentDraftLockHeaders()
        return self.get_deployment_draft_lock_with_options(namespace, request, headers, runtime)

    async def get_deployment_draft_lock_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentDraftLockRequest,
    ) -> main_models.GetDeploymentDraftLockResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentDraftLockHeaders()
        return await self.get_deployment_draft_lock_with_options_async(namespace, request, headers, runtime)

    def get_deployments_by_ip_with_options(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByIpRequest,
        headers: main_models.GetDeploymentsByIpHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_ip):
            query['dstIp'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['dstPort'] = request.dst_port
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        if not DaraCore.is_null(request.src_ip):
            query['srcIp'] = request.src_ip
        if not DaraCore.is_null(request.src_port):
            query['srcPort'] = request.src_port
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByIp',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/getDeployments/byIp',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployments_by_ip_with_options_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByIpRequest,
        headers: main_models.GetDeploymentsByIpHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_ip):
            query['dstIp'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['dstPort'] = request.dst_port
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        if not DaraCore.is_null(request.src_ip):
            query['srcIp'] = request.src_ip
        if not DaraCore.is_null(request.src_port):
            query['srcPort'] = request.src_port
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByIp',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/getDeployments/byIp',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployments_by_ip(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByIpRequest,
    ) -> main_models.GetDeploymentsByIpResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByIpHeaders()
        return self.get_deployments_by_ip_with_options(namespace, request, headers, runtime)

    async def get_deployments_by_ip_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByIpRequest,
    ) -> main_models.GetDeploymentsByIpResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByIpHeaders()
        return await self.get_deployments_by_ip_with_options_async(namespace, request, headers, runtime)

    def get_deployments_by_label_with_options(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByLabelRequest,
        headers: main_models.GetDeploymentsByLabelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        if not DaraCore.is_null(request.label_key):
            query['labelKey'] = request.label_key
        if not DaraCore.is_null(request.label_value):
            query['labelValue'] = request.label_value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByLabel',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/getDeployments/byLabel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployments_by_label_with_options_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByLabelRequest,
        headers: main_models.GetDeploymentsByLabelHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        if not DaraCore.is_null(request.label_key):
            query['labelKey'] = request.label_key
        if not DaraCore.is_null(request.label_value):
            query['labelValue'] = request.label_value
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByLabel',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/getDeployments/byLabel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployments_by_label(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByLabelRequest,
    ) -> main_models.GetDeploymentsByLabelResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByLabelHeaders()
        return self.get_deployments_by_label_with_options(namespace, request, headers, runtime)

    async def get_deployments_by_label_async(
        self,
        namespace: str,
        request: main_models.GetDeploymentsByLabelRequest,
    ) -> main_models.GetDeploymentsByLabelResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByLabelHeaders()
        return await self.get_deployments_by_label_with_options_async(namespace, request, headers, runtime)

    def get_deployments_by_name_with_options(
        self,
        namespace: str,
        deployment_name: str,
        request: main_models.GetDeploymentsByNameRequest,
        headers: main_models.GetDeploymentsByNameHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByName',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/name/{DaraURL.percent_encode(deployment_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployments_by_name_with_options_async(
        self,
        namespace: str,
        deployment_name: str,
        request: main_models.GetDeploymentsByNameRequest,
        headers: main_models.GetDeploymentsByNameHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentsByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignore_job_summary):
            query['ignoreJobSummary'] = request.ignore_job_summary
        if not DaraCore.is_null(request.ignore_resource_setting):
            query['ignoreResourceSetting'] = request.ignore_resource_setting
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeploymentsByName',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/name/{DaraURL.percent_encode(deployment_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentsByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployments_by_name(
        self,
        namespace: str,
        deployment_name: str,
        request: main_models.GetDeploymentsByNameRequest,
    ) -> main_models.GetDeploymentsByNameResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByNameHeaders()
        return self.get_deployments_by_name_with_options(namespace, deployment_name, request, headers, runtime)

    async def get_deployments_by_name_async(
        self,
        namespace: str,
        deployment_name: str,
        request: main_models.GetDeploymentsByNameRequest,
    ) -> main_models.GetDeploymentsByNameResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetDeploymentsByNameHeaders()
        return await self.get_deployments_by_name_with_options_async(namespace, deployment_name, request, headers, runtime)

    def get_events_with_options(
        self,
        namespace: str,
        request: main_models.GetEventsRequest,
        headers: main_models.GetEventsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.deployment_name):
            query['deploymentName'] = request.deployment_name
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvents',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_events_with_options_async(
        self,
        namespace: str,
        request: main_models.GetEventsRequest,
        headers: main_models.GetEventsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.deployment_name):
            query['deploymentName'] = request.deployment_name
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEvents',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_events(
        self,
        namespace: str,
        request: main_models.GetEventsRequest,
    ) -> main_models.GetEventsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetEventsHeaders()
        return self.get_events_with_options(namespace, request, headers, runtime)

    async def get_events_async(
        self,
        namespace: str,
        request: main_models.GetEventsRequest,
    ) -> main_models.GetEventsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetEventsHeaders()
        return await self.get_events_with_options_async(namespace, request, headers, runtime)

    def get_folder_with_options(
        self,
        namespace: str,
        request: main_models.GetFolderRequest,
        headers: main_models.GetFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.root_type):
            query['rootType'] = request.root_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        namespace: str,
        request: main_models.GetFolderRequest,
        headers: main_models.GetFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['folderId'] = request.folder_id
        if not DaraCore.is_null(request.root_type):
            query['rootType'] = request.root_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        namespace: str,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetFolderHeaders()
        return self.get_folder_with_options(namespace, request, headers, runtime)

    async def get_folder_async(
        self,
        namespace: str,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetFolderHeaders()
        return await self.get_folder_with_options_async(namespace, request, headers, runtime)

    def get_generate_resource_plan_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetGenerateResourcePlanResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetGenerateResourcePlanResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetGenerateResourcePlanResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/tickets/{DaraURL.percent_encode(ticket_id)}/resource-plan%3AasyncGenerate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGenerateResourcePlanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generate_resource_plan_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetGenerateResourcePlanResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetGenerateResourcePlanResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetGenerateResourcePlanResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/tickets/{DaraURL.percent_encode(ticket_id)}/resource-plan%3AasyncGenerate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGenerateResourcePlanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generate_resource_plan_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetGenerateResourcePlanResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetGenerateResourcePlanResultHeaders()
        return self.get_generate_resource_plan_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_generate_resource_plan_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetGenerateResourcePlanResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetGenerateResourcePlanResultHeaders()
        return await self.get_generate_resource_plan_result_with_options_async(namespace, ticket_id, headers, runtime)

    def get_hot_update_job_result_with_options(
        self,
        namespace: str,
        job_hot_update_id: str,
        headers: main_models.GetHotUpdateJobResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotUpdateJobResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetHotUpdateJobResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/hot-updates/{DaraURL.percent_encode(job_hot_update_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotUpdateJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_update_job_result_with_options_async(
        self,
        namespace: str,
        job_hot_update_id: str,
        headers: main_models.GetHotUpdateJobResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotUpdateJobResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetHotUpdateJobResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/hot-updates/{DaraURL.percent_encode(job_hot_update_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotUpdateJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_update_job_result(
        self,
        namespace: str,
        job_hot_update_id: str,
    ) -> main_models.GetHotUpdateJobResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotUpdateJobResultHeaders()
        return self.get_hot_update_job_result_with_options(namespace, job_hot_update_id, headers, runtime)

    async def get_hot_update_job_result_async(
        self,
        namespace: str,
        job_hot_update_id: str,
    ) -> main_models.GetHotUpdateJobResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetHotUpdateJobResultHeaders()
        return await self.get_hot_update_job_result_with_options_async(namespace, job_hot_update_id, headers, runtime)

    def get_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.GetJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.GetJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJobHeaders()
        return self.get_job_with_options(namespace, job_id, headers, runtime)

    async def get_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJobHeaders()
        return await self.get_job_with_options_async(namespace, job_id, headers, runtime)

    def get_job_diagnosis_with_options(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
        headers: main_models.GetJobDiagnosisHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDiagnosisResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobDiagnosis',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/jobs/{DaraURL.percent_encode(job_id)}/job-diagnoses/lite',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_diagnosis_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
        headers: main_models.GetJobDiagnosisHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDiagnosisResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobDiagnosis',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/jobs/{DaraURL.percent_encode(job_id)}/job-diagnoses/lite',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_diagnosis(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
    ) -> main_models.GetJobDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJobDiagnosisHeaders()
        return self.get_job_diagnosis_with_options(namespace, deployment_id, job_id, headers, runtime)

    async def get_job_diagnosis_async(
        self,
        namespace: str,
        deployment_id: str,
        job_id: str,
    ) -> main_models.GetJobDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetJobDiagnosisHeaders()
        return await self.get_job_diagnosis_with_options_async(namespace, deployment_id, job_id, headers, runtime)

    def get_latest_job_start_log_with_options(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.GetLatestJobStartLogHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetLatestJobStartLogResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetLatestJobStartLog',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/latest_jobmanager_start_log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLatestJobStartLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_job_start_log_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        headers: main_models.GetLatestJobStartLogHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetLatestJobStartLogResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetLatestJobStartLog',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}/latest_jobmanager_start_log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLatestJobStartLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_job_start_log(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.GetLatestJobStartLogResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetLatestJobStartLogHeaders()
        return self.get_latest_job_start_log_with_options(namespace, deployment_id, headers, runtime)

    async def get_latest_job_start_log_async(
        self,
        namespace: str,
        deployment_id: str,
    ) -> main_models.GetLatestJobStartLogResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetLatestJobStartLogHeaders()
        return await self.get_latest_job_start_log_with_options_async(namespace, deployment_id, headers, runtime)

    def get_lineage_info_with_options(
        self,
        request: main_models.GetLineageInfoRequest,
        headers: main_models.GetLineageInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetLineageInfoResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetLineageInfo',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/meta/v2/lineage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLineageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lineage_info_with_options_async(
        self,
        request: main_models.GetLineageInfoRequest,
        headers: main_models.GetLineageInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetLineageInfoResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetLineageInfo',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/meta/v2/lineage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLineageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lineage_info(
        self,
        request: main_models.GetLineageInfoRequest,
    ) -> main_models.GetLineageInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetLineageInfoHeaders()
        return self.get_lineage_info_with_options(request, headers, runtime)

    async def get_lineage_info_async(
        self,
        request: main_models.GetLineageInfoRequest,
    ) -> main_models.GetLineageInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetLineageInfoHeaders()
        return await self.get_lineage_info_with_options_async(request, headers, runtime)

    def get_member_with_options(
        self,
        namespace: str,
        member: str,
        headers: main_models.GetMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetMemberResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members/{DaraURL.percent_encode(member)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_member_with_options_async(
        self,
        namespace: str,
        member: str,
        headers: main_models.GetMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetMemberResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members/{DaraURL.percent_encode(member)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_member(
        self,
        namespace: str,
        member: str,
    ) -> main_models.GetMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetMemberHeaders()
        return self.get_member_with_options(namespace, member, headers, runtime)

    async def get_member_async(
        self,
        namespace: str,
        member: str,
    ) -> main_models.GetMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetMemberHeaders()
        return await self.get_member_with_options_async(namespace, member, headers, runtime)

    def get_pre_signed_url_for_put_object_with_options(
        self,
        namespace: str,
        request: main_models.GetPreSignedUrlForPutObjectRequest,
        headers: main_models.GetPreSignedUrlForPutObjectHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPreSignedUrlForPutObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPreSignedUrlForPutObject',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/artifacts/v2/namespaces/{DaraURL.percent_encode(namespace)}/getPreSignedUrlForPutObject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPreSignedUrlForPutObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pre_signed_url_for_put_object_with_options_async(
        self,
        namespace: str,
        request: main_models.GetPreSignedUrlForPutObjectRequest,
        headers: main_models.GetPreSignedUrlForPutObjectHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPreSignedUrlForPutObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPreSignedUrlForPutObject',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/artifacts/v2/namespaces/{DaraURL.percent_encode(namespace)}/getPreSignedUrlForPutObject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPreSignedUrlForPutObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pre_signed_url_for_put_object(
        self,
        namespace: str,
        request: main_models.GetPreSignedUrlForPutObjectRequest,
    ) -> main_models.GetPreSignedUrlForPutObjectResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPreSignedUrlForPutObjectHeaders()
        return self.get_pre_signed_url_for_put_object_with_options(namespace, request, headers, runtime)

    async def get_pre_signed_url_for_put_object_async(
        self,
        namespace: str,
        request: main_models.GetPreSignedUrlForPutObjectRequest,
    ) -> main_models.GetPreSignedUrlForPutObjectResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPreSignedUrlForPutObjectHeaders()
        return await self.get_pre_signed_url_for_put_object_with_options_async(namespace, request, headers, runtime)

    def get_savepoint_with_options(
        self,
        namespace: str,
        savepoint_id: str,
        headers: main_models.GetSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavepointResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints/{DaraURL.percent_encode(savepoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_savepoint_with_options_async(
        self,
        namespace: str,
        savepoint_id: str,
        headers: main_models.GetSavepointHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavepointResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetSavepoint',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints/{DaraURL.percent_encode(savepoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavepointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_savepoint(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> main_models.GetSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetSavepointHeaders()
        return self.get_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    async def get_savepoint_async(
        self,
        namespace: str,
        savepoint_id: str,
    ) -> main_models.GetSavepointResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetSavepointHeaders()
        return await self.get_savepoint_with_options_async(namespace, savepoint_id, headers, runtime)

    def get_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.GetSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.GetSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.GetSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetSessionClusterHeaders()
        return self.get_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def get_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.GetSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetSessionClusterHeaders()
        return await self.get_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def get_tables_with_options(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: main_models.GetTablesRequest,
        headers: main_models.GetTablesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.table_name):
            query['tableName'] = request.table_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTables',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs/{DaraURL.percent_encode(catalog_name)}/databases/{DaraURL.percent_encode(database_name)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tables_with_options_async(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: main_models.GetTablesRequest,
        headers: main_models.GetTablesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.table_name):
            query['tableName'] = request.table_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTables',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/catalogs/{DaraURL.percent_encode(catalog_name)}/databases/{DaraURL.percent_encode(database_name)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tables(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: main_models.GetTablesRequest,
    ) -> main_models.GetTablesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetTablesHeaders()
        return self.get_tables_with_options(namespace, catalog_name, database_name, request, headers, runtime)

    async def get_tables_async(
        self,
        namespace: str,
        catalog_name: str,
        database_name: str,
        request: main_models.GetTablesRequest,
    ) -> main_models.GetTablesResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetTablesHeaders()
        return await self.get_tables_with_options_async(namespace, catalog_name, database_name, request, headers, runtime)

    def get_udf_artifacts_with_options(
        self,
        namespace: str,
        request: main_models.GetUdfArtifactsRequest,
        headers: main_models.GetUdfArtifactsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdfArtifacts',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_udf_artifacts_with_options_async(
        self,
        namespace: str,
        request: main_models.GetUdfArtifactsRequest,
        headers: main_models.GetUdfArtifactsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdfArtifacts',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_udf_artifacts(
        self,
        namespace: str,
        request: main_models.GetUdfArtifactsRequest,
    ) -> main_models.GetUdfArtifactsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUdfArtifactsHeaders()
        return self.get_udf_artifacts_with_options(namespace, request, headers, runtime)

    async def get_udf_artifacts_async(
        self,
        namespace: str,
        request: main_models.GetUdfArtifactsRequest,
    ) -> main_models.GetUdfArtifactsResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUdfArtifactsHeaders()
        return await self.get_udf_artifacts_with_options_async(namespace, request, headers, runtime)

    def get_validate_deployment_draft_result_with_options(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetValidateDeploymentDraftResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateDeploymentDraftResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetValidateDeploymentDraftResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/tickets/{DaraURL.percent_encode(ticket_id)}/async-validate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateDeploymentDraftResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_validate_deployment_draft_result_with_options_async(
        self,
        namespace: str,
        ticket_id: str,
        headers: main_models.GetValidateDeploymentDraftResultHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetValidateDeploymentDraftResultResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetValidateDeploymentDraftResult',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/tickets/{DaraURL.percent_encode(ticket_id)}/async-validate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetValidateDeploymentDraftResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_validate_deployment_draft_result(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetValidateDeploymentDraftResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetValidateDeploymentDraftResultHeaders()
        return self.get_validate_deployment_draft_result_with_options(namespace, ticket_id, headers, runtime)

    async def get_validate_deployment_draft_result_async(
        self,
        namespace: str,
        ticket_id: str,
    ) -> main_models.GetValidateDeploymentDraftResultResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetValidateDeploymentDraftResultHeaders()
        return await self.get_validate_deployment_draft_result_with_options_async(namespace, ticket_id, headers, runtime)

    def hot_update_job_with_options(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.HotUpdateJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.HotUpdateJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'HotUpdateJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}%3AhotUpdate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotUpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def hot_update_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        headers: main_models.HotUpdateJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.HotUpdateJobResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'HotUpdateJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}%3AhotUpdate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HotUpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hot_update_job(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.HotUpdateJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.HotUpdateJobHeaders()
        return self.hot_update_job_with_options(namespace, job_id, headers, runtime)

    async def hot_update_job_async(
        self,
        namespace: str,
        job_id: str,
    ) -> main_models.HotUpdateJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.HotUpdateJobHeaders()
        return await self.hot_update_job_with_options_async(namespace, job_id, headers, runtime)

    def list_custom_connectors_with_options(
        self,
        namespace: str,
        headers: main_models.ListCustomConnectorsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomConnectorsResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListCustomConnectors',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_connectors_with_options_async(
        self,
        namespace: str,
        headers: main_models.ListCustomConnectorsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomConnectorsResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListCustomConnectors',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_connectors(
        self,
        namespace: str,
    ) -> main_models.ListCustomConnectorsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCustomConnectorsHeaders()
        return self.list_custom_connectors_with_options(namespace, headers, runtime)

    async def list_custom_connectors_async(
        self,
        namespace: str,
    ) -> main_models.ListCustomConnectorsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListCustomConnectorsHeaders()
        return await self.list_custom_connectors_with_options_async(namespace, headers, runtime)

    def list_deployment_drafts_with_options(
        self,
        namespace: str,
        request: main_models.ListDeploymentDraftsRequest,
        headers: main_models.ListDeploymentDraftsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentDraftsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentDrafts',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentDraftsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_drafts_with_options_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentDraftsRequest,
        headers: main_models.ListDeploymentDraftsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentDraftsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentDrafts',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentDraftsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_drafts(
        self,
        namespace: str,
        request: main_models.ListDeploymentDraftsRequest,
    ) -> main_models.ListDeploymentDraftsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentDraftsHeaders()
        return self.list_deployment_drafts_with_options(namespace, request, headers, runtime)

    async def list_deployment_drafts_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentDraftsRequest,
    ) -> main_models.ListDeploymentDraftsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentDraftsHeaders()
        return await self.list_deployment_drafts_with_options_async(namespace, request, headers, runtime)

    def list_deployment_targets_with_options(
        self,
        namespace: str,
        request: main_models.ListDeploymentTargetsRequest,
        headers: main_models.ListDeploymentTargetsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentTargets',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_targets_with_options_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentTargetsRequest,
        headers: main_models.ListDeploymentTargetsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentTargets',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_targets(
        self,
        namespace: str,
        request: main_models.ListDeploymentTargetsRequest,
    ) -> main_models.ListDeploymentTargetsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentTargetsHeaders()
        return self.list_deployment_targets_with_options(namespace, request, headers, runtime)

    async def list_deployment_targets_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentTargetsRequest,
    ) -> main_models.ListDeploymentTargetsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentTargetsHeaders()
        return await self.list_deployment_targets_with_options_async(namespace, request, headers, runtime)

    def list_deployments_with_options(
        self,
        namespace: str,
        request: main_models.ListDeploymentsRequest,
        headers: main_models.ListDeploymentsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['creator'] = request.creator
        if not DaraCore.is_null(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not DaraCore.is_null(request.label_key):
            query['labelKey'] = request.label_key
        if not DaraCore.is_null(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not DaraCore.is_null(request.modifier):
            query['modifier'] = request.modifier
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_name):
            query['sortName'] = request.sort_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployments',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentsRequest,
        headers: main_models.ListDeploymentsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['creator'] = request.creator
        if not DaraCore.is_null(request.execution_mode):
            query['executionMode'] = request.execution_mode
        if not DaraCore.is_null(request.label_key):
            query['labelKey'] = request.label_key
        if not DaraCore.is_null(request.label_value_array):
            query['labelValueArray'] = request.label_value_array
        if not DaraCore.is_null(request.modifier):
            query['modifier'] = request.modifier
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_name):
            query['sortName'] = request.sort_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployments',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        namespace: str,
        request: main_models.ListDeploymentsRequest,
    ) -> main_models.ListDeploymentsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentsHeaders()
        return self.list_deployments_with_options(namespace, request, headers, runtime)

    async def list_deployments_async(
        self,
        namespace: str,
        request: main_models.ListDeploymentsRequest,
    ) -> main_models.ListDeploymentsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListDeploymentsHeaders()
        return await self.list_deployments_with_options_async(namespace, request, headers, runtime)

    def list_editable_namespace_with_options(
        self,
        request: main_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEditableNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEditableNamespace',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/editable',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEditableNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_editable_namespace_with_options_async(
        self,
        request: main_models.ListEditableNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEditableNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEditableNamespace',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/editable',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEditableNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_editable_namespace(
        self,
        request: main_models.ListEditableNamespaceRequest,
    ) -> main_models.ListEditableNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_editable_namespace_with_options(request, headers, runtime)

    async def list_editable_namespace_async(
        self,
        request: main_models.ListEditableNamespaceRequest,
    ) -> main_models.ListEditableNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_editable_namespace_with_options_async(request, headers, runtime)

    def list_engine_version_metadata_with_options(
        self,
        headers: main_models.ListEngineVersionMetadataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineVersionMetadataResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListEngineVersionMetadata',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/engine-version-meta.json',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_version_metadata_with_options_async(
        self,
        headers: main_models.ListEngineVersionMetadataHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineVersionMetadataResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListEngineVersionMetadata',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/engine-version-meta.json',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineVersionMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_version_metadata(self) -> main_models.ListEngineVersionMetadataResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListEngineVersionMetadataHeaders()
        return self.list_engine_version_metadata_with_options(headers, runtime)

    async def list_engine_version_metadata_async(self) -> main_models.ListEngineVersionMetadataResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListEngineVersionMetadataHeaders()
        return await self.list_engine_version_metadata_with_options_async(headers, runtime)

    def list_jobs_with_options(
        self,
        namespace: str,
        request: main_models.ListJobsRequest,
        headers: main_models.ListJobsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_name):
            query['sortName'] = request.sort_name
        if not DaraCore.is_null(request.sort_order):
            query['sortOrder'] = request.sort_order
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        namespace: str,
        request: main_models.ListJobsRequest,
        headers: main_models.ListJobsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_name):
            query['sortName'] = request.sort_name
        if not DaraCore.is_null(request.sort_order):
            query['sortOrder'] = request.sort_order
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        namespace: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListJobsHeaders()
        return self.list_jobs_with_options(namespace, request, headers, runtime)

    async def list_jobs_async(
        self,
        namespace: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListJobsHeaders()
        return await self.list_jobs_with_options_async(namespace, request, headers, runtime)

    def list_members_with_options(
        self,
        namespace: str,
        request: main_models.ListMembersRequest,
        headers: main_models.ListMembersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_members_with_options_async(
        self,
        namespace: str,
        request: main_models.ListMembersRequest,
        headers: main_models.ListMembersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMembers',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_members(
        self,
        namespace: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListMembersHeaders()
        return self.list_members_with_options(namespace, request, headers, runtime)

    async def list_members_async(
        self,
        namespace: str,
        request: main_models.ListMembersRequest,
    ) -> main_models.ListMembersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListMembersHeaders()
        return await self.list_members_with_options_async(namespace, request, headers, runtime)

    def list_savepoints_with_options(
        self,
        namespace: str,
        request: main_models.ListSavepointsRequest,
        headers: main_models.ListSavepointsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSavepointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavepoints',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavepointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_savepoints_with_options_async(
        self,
        namespace: str,
        request: main_models.ListSavepointsRequest,
        headers: main_models.ListSavepointsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSavepointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavepoints',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/savepoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavepointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_savepoints(
        self,
        namespace: str,
        request: main_models.ListSavepointsRequest,
    ) -> main_models.ListSavepointsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSavepointsHeaders()
        return self.list_savepoints_with_options(namespace, request, headers, runtime)

    async def list_savepoints_async(
        self,
        namespace: str,
        request: main_models.ListSavepointsRequest,
    ) -> main_models.ListSavepointsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSavepointsHeaders()
        return await self.list_savepoints_with_options_async(namespace, request, headers, runtime)

    def list_scheduled_plan_with_options(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanRequest,
        headers: main_models.ListScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_plan_with_options_async(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanRequest,
        headers: main_models.ListScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_plan(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanRequest,
    ) -> main_models.ListScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListScheduledPlanHeaders()
        return self.list_scheduled_plan_with_options(namespace, request, headers, runtime)

    async def list_scheduled_plan_async(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanRequest,
    ) -> main_models.ListScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListScheduledPlanHeaders()
        return await self.list_scheduled_plan_with_options_async(namespace, request, headers, runtime)

    def list_scheduled_plan_executed_history_with_options(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanExecutedHistoryRequest,
        headers: main_models.ListScheduledPlanExecutedHistoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledPlanExecutedHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledPlanExecutedHistory',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/job-resource-upgradings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledPlanExecutedHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_plan_executed_history_with_options_async(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanExecutedHistoryRequest,
        headers: main_models.ListScheduledPlanExecutedHistoryHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledPlanExecutedHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledPlanExecutedHistory',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/job-resource-upgradings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledPlanExecutedHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_plan_executed_history(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanExecutedHistoryRequest,
    ) -> main_models.ListScheduledPlanExecutedHistoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListScheduledPlanExecutedHistoryHeaders()
        return self.list_scheduled_plan_executed_history_with_options(namespace, request, headers, runtime)

    async def list_scheduled_plan_executed_history_async(
        self,
        namespace: str,
        request: main_models.ListScheduledPlanExecutedHistoryRequest,
    ) -> main_models.ListScheduledPlanExecutedHistoryResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListScheduledPlanExecutedHistoryHeaders()
        return await self.list_scheduled_plan_executed_history_with_options_async(namespace, request, headers, runtime)

    def list_session_clusters_with_options(
        self,
        namespace: str,
        headers: main_models.ListSessionClustersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionClustersResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListSessionClusters',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_clusters_with_options_async(
        self,
        namespace: str,
        headers: main_models.ListSessionClustersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionClustersResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListSessionClusters',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_clusters(
        self,
        namespace: str,
    ) -> main_models.ListSessionClustersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSessionClustersHeaders()
        return self.list_session_clusters_with_options(namespace, headers, runtime)

    async def list_session_clusters_async(
        self,
        namespace: str,
    ) -> main_models.ListSessionClustersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListSessionClustersHeaders()
        return await self.list_session_clusters_with_options_async(namespace, headers, runtime)

    def list_variables_with_options(
        self,
        namespace: str,
        request: main_models.ListVariablesRequest,
        headers: main_models.ListVariablesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVariables',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_variables_with_options_async(
        self,
        namespace: str,
        request: main_models.ListVariablesRequest,
        headers: main_models.ListVariablesHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListVariablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVariables',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVariablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_variables(
        self,
        namespace: str,
        request: main_models.ListVariablesRequest,
    ) -> main_models.ListVariablesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListVariablesHeaders()
        return self.list_variables_with_options(namespace, request, headers, runtime)

    async def list_variables_async(
        self,
        namespace: str,
        request: main_models.ListVariablesRequest,
    ) -> main_models.ListVariablesResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListVariablesHeaders()
        return await self.list_variables_with_options_async(namespace, request, headers, runtime)

    def register_custom_connector_with_options(
        self,
        namespace: str,
        request: main_models.RegisterCustomConnectorRequest,
        headers: main_models.RegisterCustomConnectorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jar_url):
            query['jarUrl'] = request.jar_url
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomConnector',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors%3Aregister',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_connector_with_options_async(
        self,
        namespace: str,
        request: main_models.RegisterCustomConnectorRequest,
        headers: main_models.RegisterCustomConnectorHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jar_url):
            query['jarUrl'] = request.jar_url
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomConnector',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/connectors%3Aregister',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_connector(
        self,
        namespace: str,
        request: main_models.RegisterCustomConnectorRequest,
    ) -> main_models.RegisterCustomConnectorResponse:
        runtime = RuntimeOptions()
        headers = main_models.RegisterCustomConnectorHeaders()
        return self.register_custom_connector_with_options(namespace, request, headers, runtime)

    async def register_custom_connector_async(
        self,
        namespace: str,
        request: main_models.RegisterCustomConnectorRequest,
    ) -> main_models.RegisterCustomConnectorResponse:
        runtime = RuntimeOptions()
        headers = main_models.RegisterCustomConnectorHeaders()
        return await self.register_custom_connector_with_options_async(namespace, request, headers, runtime)

    def register_udf_function_with_options(
        self,
        namespace: str,
        request: main_models.RegisterUdfFunctionRequest,
        headers: main_models.RegisterUdfFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterUdfFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterUdfFunction',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/function%3AregisterUdfFunction',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterUdfFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_udf_function_with_options_async(
        self,
        namespace: str,
        request: main_models.RegisterUdfFunctionRequest,
        headers: main_models.RegisterUdfFunctionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterUdfFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.function_name):
            query['functionName'] = request.function_name
        if not DaraCore.is_null(request.udf_artifact_name):
            query['udfArtifactName'] = request.udf_artifact_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterUdfFunction',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/function%3AregisterUdfFunction',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterUdfFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_udf_function(
        self,
        namespace: str,
        request: main_models.RegisterUdfFunctionRequest,
    ) -> main_models.RegisterUdfFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.RegisterUdfFunctionHeaders()
        return self.register_udf_function_with_options(namespace, request, headers, runtime)

    async def register_udf_function_async(
        self,
        namespace: str,
        request: main_models.RegisterUdfFunctionRequest,
    ) -> main_models.RegisterUdfFunctionResponse:
        runtime = RuntimeOptions()
        headers = main_models.RegisterUdfFunctionHeaders()
        return await self.register_udf_function_with_options_async(namespace, request, headers, runtime)

    def start_job_with_options(
        self,
        namespace: str,
        request: main_models.StartJobRequest,
        headers: main_models.StartJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StartJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_options_async(
        self,
        namespace: str,
        request: main_models.StartJobRequest,
        headers: main_models.StartJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StartJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job(
        self,
        namespace: str,
        request: main_models.StartJobRequest,
    ) -> main_models.StartJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartJobHeaders()
        return self.start_job_with_options(namespace, request, headers, runtime)

    async def start_job_async(
        self,
        namespace: str,
        request: main_models.StartJobRequest,
    ) -> main_models.StartJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartJobHeaders()
        return await self.start_job_with_options_async(namespace, request, headers, runtime)

    def start_job_with_params_with_options(
        self,
        namespace: str,
        request: main_models.StartJobWithParamsRequest,
        headers: main_models.StartJobWithParamsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobWithParamsResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StartJobWithParams',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs%3Astart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobWithParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_with_params_with_options_async(
        self,
        namespace: str,
        request: main_models.StartJobWithParamsRequest,
        headers: main_models.StartJobWithParamsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartJobWithParamsResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StartJobWithParams',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs%3Astart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartJobWithParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_with_params(
        self,
        namespace: str,
        request: main_models.StartJobWithParamsRequest,
    ) -> main_models.StartJobWithParamsResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartJobWithParamsHeaders()
        return self.start_job_with_params_with_options(namespace, request, headers, runtime)

    async def start_job_with_params_async(
        self,
        namespace: str,
        request: main_models.StartJobWithParamsRequest,
    ) -> main_models.StartJobWithParamsResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartJobWithParamsHeaders()
        return await self.start_job_with_params_with_options_async(namespace, request, headers, runtime)

    def start_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.StartSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StartSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}%3Astart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.StartSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StartSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StartSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}%3Astart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.StartSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartSessionClusterHeaders()
        return self.start_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def start_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.StartSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.StartSessionClusterHeaders()
        return await self.start_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def stop_apply_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.StopApplyScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopApplyScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StopApplyScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}%3Astop',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplyScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_apply_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        headers: main_models.StopApplyScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopApplyScheduledPlanResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StopApplyScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}%3Astop',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplyScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_apply_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.StopApplyScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopApplyScheduledPlanHeaders()
        return self.stop_apply_scheduled_plan_with_options(namespace, scheduled_plan_id, headers, runtime)

    async def stop_apply_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
    ) -> main_models.StopApplyScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopApplyScheduledPlanHeaders()
        return await self.stop_apply_scheduled_plan_with_options_async(namespace, scheduled_plan_id, headers, runtime)

    def stop_job_with_options(
        self,
        namespace: str,
        job_id: str,
        request: main_models.StopJobRequest,
        headers: main_models.StopJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopJobResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StopJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}%3Astop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        namespace: str,
        job_id: str,
        request: main_models.StopJobRequest,
        headers: main_models.StopJobHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopJobResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'StopJob',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/jobs/{DaraURL.percent_encode(job_id)}%3Astop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        namespace: str,
        job_id: str,
        request: main_models.StopJobRequest,
    ) -> main_models.StopJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopJobHeaders()
        return self.stop_job_with_options(namespace, job_id, request, headers, runtime)

    async def stop_job_async(
        self,
        namespace: str,
        job_id: str,
        request: main_models.StopJobRequest,
    ) -> main_models.StopJobResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopJobHeaders()
        return await self.stop_job_with_options_async(namespace, job_id, request, headers, runtime)

    def stop_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.StopSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StopSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}%3Astop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        headers: main_models.StopSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.StopSessionClusterResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'StopSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}%3Astop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.StopSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopSessionClusterHeaders()
        return self.stop_session_cluster_with_options(namespace, session_cluster_name, headers, runtime)

    async def stop_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
    ) -> main_models.StopSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.StopSessionClusterHeaders()
        return await self.stop_session_cluster_with_options_async(namespace, session_cluster_name, headers, runtime)

    def submit_sql_preview_with_options(
        self,
        namespace: str,
        request: main_models.SubmitSqlPreviewRequest,
        headers: main_models.SubmitSqlPreviewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSqlPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSqlPreview',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSqlPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sql_preview_with_options_async(
        self,
        namespace: str,
        request: main_models.SubmitSqlPreviewRequest,
        headers: main_models.SubmitSqlPreviewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSqlPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_cluster_name):
            query['sessionClusterName'] = request.session_cluster_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSqlPreview',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-preview/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSqlPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sql_preview(
        self,
        namespace: str,
        request: main_models.SubmitSqlPreviewRequest,
    ) -> main_models.SubmitSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitSqlPreviewHeaders()
        return self.submit_sql_preview_with_options(namespace, request, headers, runtime)

    async def submit_sql_preview_async(
        self,
        namespace: str,
        request: main_models.SubmitSqlPreviewRequest,
    ) -> main_models.SubmitSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitSqlPreviewHeaders()
        return await self.submit_sql_preview_with_options_async(namespace, request, headers, runtime)

    def update_deployment_with_options(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.UpdateDeploymentRequest,
        headers: main_models.UpdateDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_with_options_async(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.UpdateDeploymentRequest,
        headers: main_models.UpdateDeploymentHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeployment',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployments/{DaraURL.percent_encode(deployment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.UpdateDeploymentRequest,
    ) -> main_models.UpdateDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentHeaders()
        return self.update_deployment_with_options(namespace, deployment_id, request, headers, runtime)

    async def update_deployment_async(
        self,
        namespace: str,
        deployment_id: str,
        request: main_models.UpdateDeploymentRequest,
    ) -> main_models.UpdateDeploymentResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentHeaders()
        return await self.update_deployment_with_options_async(namespace, deployment_id, request, headers, runtime)

    def update_deployment_draft_with_options(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: main_models.UpdateDeploymentDraftRequest,
        headers: main_models.UpdateDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentDraftResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_draft_with_options_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: main_models.UpdateDeploymentDraftRequest,
        headers: main_models.UpdateDeploymentDraftHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentDraftResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentDraft',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/{DaraURL.percent_encode(deployment_draft_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_draft(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: main_models.UpdateDeploymentDraftRequest,
    ) -> main_models.UpdateDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentDraftHeaders()
        return self.update_deployment_draft_with_options(namespace, deployment_draft_id, request, headers, runtime)

    async def update_deployment_draft_async(
        self,
        namespace: str,
        deployment_draft_id: str,
        request: main_models.UpdateDeploymentDraftRequest,
    ) -> main_models.UpdateDeploymentDraftResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentDraftHeaders()
        return await self.update_deployment_draft_with_options_async(namespace, deployment_draft_id, request, headers, runtime)

    def update_deployment_target_with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetRequest,
        headers: main_models.UpdateDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentTargetResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_target_with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetRequest,
        headers: main_models.UpdateDeploymentTargetHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentTargetResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentTarget',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_target(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetRequest,
    ) -> main_models.UpdateDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentTargetHeaders()
        return self.update_deployment_target_with_options(namespace, deployment_target_name, request, headers, runtime)

    async def update_deployment_target_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetRequest,
    ) -> main_models.UpdateDeploymentTargetResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentTargetHeaders()
        return await self.update_deployment_target_with_options_async(namespace, deployment_target_name, request, headers, runtime)

    def update_deployment_target_v2with_options(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetV2Request,
        headers: main_models.UpdateDeploymentTargetV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentTargetV2Response:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentTargetV2',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/support-elastic/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentTargetV2Response(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_target_v2with_options_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetV2Request,
        headers: main_models.UpdateDeploymentTargetV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentTargetV2Response:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentTargetV2',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-targets/support-elastic/{DaraURL.percent_encode(deployment_target_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentTargetV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_target_v2(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetV2Request,
    ) -> main_models.UpdateDeploymentTargetV2Response:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentTargetV2Headers()
        return self.update_deployment_target_v2with_options(namespace, deployment_target_name, request, headers, runtime)

    async def update_deployment_target_v2_async(
        self,
        namespace: str,
        deployment_target_name: str,
        request: main_models.UpdateDeploymentTargetV2Request,
    ) -> main_models.UpdateDeploymentTargetV2Response:
        runtime = RuntimeOptions()
        headers = main_models.UpdateDeploymentTargetV2Headers()
        return await self.update_deployment_target_v2with_options_async(namespace, deployment_target_name, request, headers, runtime)

    def update_folder_with_options(
        self,
        namespace: str,
        folder_id: str,
        request: main_models.UpdateFolderRequest,
        headers: main_models.UpdateFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder/{DaraURL.percent_encode(folder_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        namespace: str,
        folder_id: str,
        request: main_models.UpdateFolderRequest,
        headers: main_models.UpdateFolderHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/folder/{DaraURL.percent_encode(folder_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        namespace: str,
        folder_id: str,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateFolderHeaders()
        return self.update_folder_with_options(namespace, folder_id, request, headers, runtime)

    async def update_folder_async(
        self,
        namespace: str,
        folder_id: str,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateFolderHeaders()
        return await self.update_folder_with_options_async(namespace, folder_id, request, headers, runtime)

    def update_member_with_options(
        self,
        namespace: str,
        request: main_models.UpdateMemberRequest,
        headers: main_models.UpdateMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemberResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_with_options_async(
        self,
        namespace: str,
        request: main_models.UpdateMemberRequest,
        headers: main_models.UpdateMemberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemberResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMember',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/gateway/v2/namespaces/{DaraURL.percent_encode(namespace)}/members',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member(
        self,
        namespace: str,
        request: main_models.UpdateMemberRequest,
    ) -> main_models.UpdateMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateMemberHeaders()
        return self.update_member_with_options(namespace, request, headers, runtime)

    async def update_member_async(
        self,
        namespace: str,
        request: main_models.UpdateMemberRequest,
    ) -> main_models.UpdateMemberResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateMemberHeaders()
        return await self.update_member_with_options_async(namespace, request, headers, runtime)

    def update_scheduled_plan_with_options(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: main_models.UpdateScheduledPlanRequest,
        headers: main_models.UpdateScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledPlanResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheduled_plan_with_options_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: main_models.UpdateScheduledPlanRequest,
        headers: main_models.UpdateScheduledPlanHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledPlanResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledPlan',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/scheduled-plans/{DaraURL.percent_encode(scheduled_plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheduled_plan(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: main_models.UpdateScheduledPlanRequest,
    ) -> main_models.UpdateScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateScheduledPlanHeaders()
        return self.update_scheduled_plan_with_options(namespace, scheduled_plan_id, request, headers, runtime)

    async def update_scheduled_plan_async(
        self,
        namespace: str,
        scheduled_plan_id: str,
        request: main_models.UpdateScheduledPlanRequest,
    ) -> main_models.UpdateScheduledPlanResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateScheduledPlanHeaders()
        return await self.update_scheduled_plan_with_options_async(namespace, scheduled_plan_id, request, headers, runtime)

    def update_session_cluster_with_options(
        self,
        namespace: str,
        session_cluster_name: str,
        request: main_models.UpdateSessionClusterRequest,
        headers: main_models.UpdateSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionClusterResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSessionClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_session_cluster_with_options_async(
        self,
        namespace: str,
        session_cluster_name: str,
        request: main_models.UpdateSessionClusterRequest,
        headers: main_models.UpdateSessionClusterHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSessionClusterResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSessionCluster',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sessionclusters/{DaraURL.percent_encode(session_cluster_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSessionClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_session_cluster(
        self,
        namespace: str,
        session_cluster_name: str,
        request: main_models.UpdateSessionClusterRequest,
    ) -> main_models.UpdateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateSessionClusterHeaders()
        return self.update_session_cluster_with_options(namespace, session_cluster_name, request, headers, runtime)

    async def update_session_cluster_async(
        self,
        namespace: str,
        session_cluster_name: str,
        request: main_models.UpdateSessionClusterRequest,
    ) -> main_models.UpdateSessionClusterResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateSessionClusterHeaders()
        return await self.update_session_cluster_with_options_async(namespace, session_cluster_name, request, headers, runtime)

    def update_udf_artifact_with_options(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: main_models.UpdateUdfArtifactRequest,
        headers: main_models.UpdateUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfArtifactResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/{DaraURL.percent_encode(udf_artifact_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_udf_artifact_with_options_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: main_models.UpdateUdfArtifactRequest,
        headers: main_models.UpdateUdfArtifactHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfArtifactResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdfArtifact',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/udfartifacts/{DaraURL.percent_encode(udf_artifact_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_udf_artifact(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: main_models.UpdateUdfArtifactRequest,
    ) -> main_models.UpdateUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateUdfArtifactHeaders()
        return self.update_udf_artifact_with_options(namespace, udf_artifact_name, request, headers, runtime)

    async def update_udf_artifact_async(
        self,
        namespace: str,
        udf_artifact_name: str,
        request: main_models.UpdateUdfArtifactRequest,
    ) -> main_models.UpdateUdfArtifactResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateUdfArtifactHeaders()
        return await self.update_udf_artifact_with_options_async(namespace, udf_artifact_name, request, headers, runtime)

    def update_variable_with_options(
        self,
        namespace: str,
        name: str,
        request: main_models.UpdateVariableRequest,
        headers: main_models.UpdateVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVariableResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_variable_with_options_async(
        self,
        namespace: str,
        name: str,
        request: main_models.UpdateVariableRequest,
        headers: main_models.UpdateVariableHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVariableResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVariable',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/variables/{DaraURL.percent_encode(name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_variable(
        self,
        namespace: str,
        name: str,
        request: main_models.UpdateVariableRequest,
    ) -> main_models.UpdateVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateVariableHeaders()
        return self.update_variable_with_options(namespace, name, request, headers, runtime)

    async def update_variable_async(
        self,
        namespace: str,
        name: str,
        request: main_models.UpdateVariableRequest,
    ) -> main_models.UpdateVariableResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateVariableHeaders()
        return await self.update_variable_with_options_async(namespace, name, request, headers, runtime)

    def validate_deployment_draft_async_with_options(
        self,
        namespace: str,
        request: main_models.ValidateDeploymentDraftAsyncRequest,
        headers: main_models.ValidateDeploymentDraftAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDeploymentDraftAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDeploymentDraftAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/async-validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDeploymentDraftAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_deployment_draft_async_with_options_async(
        self,
        namespace: str,
        request: main_models.ValidateDeploymentDraftAsyncRequest,
        headers: main_models.ValidateDeploymentDraftAsyncHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDeploymentDraftAsyncResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDeploymentDraftAsync',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/deployment-drafts/async-validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDeploymentDraftAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_deployment_draft_async(
        self,
        namespace: str,
        request: main_models.ValidateDeploymentDraftAsyncRequest,
    ) -> main_models.ValidateDeploymentDraftAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.ValidateDeploymentDraftAsyncHeaders()
        return self.validate_deployment_draft_async_with_options(namespace, request, headers, runtime)

    async def validate_deployment_draft_async_async(
        self,
        namespace: str,
        request: main_models.ValidateDeploymentDraftAsyncRequest,
    ) -> main_models.ValidateDeploymentDraftAsyncResponse:
        runtime = RuntimeOptions()
        headers = main_models.ValidateDeploymentDraftAsyncHeaders()
        return await self.validate_deployment_draft_async_with_options_async(namespace, request, headers, runtime)

    def validate_sql_statement_with_options(
        self,
        namespace: str,
        request: main_models.ValidateSqlStatementRequest,
        headers: main_models.ValidateSqlStatementHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateSqlStatementResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateSqlStatement',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-statement/validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_sql_statement_with_options_async(
        self,
        namespace: str,
        request: main_models.ValidateSqlStatementRequest,
        headers: main_models.ValidateSqlStatementHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateSqlStatementResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.workspace):
            real_headers['workspace'] = str(headers.workspace)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateSqlStatement',
            version = '2022-07-18',
            protocol = 'HTTPS',
            pathname = f'/api/v2/namespaces/{DaraURL.percent_encode(namespace)}/sql-statement/validate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_sql_statement(
        self,
        namespace: str,
        request: main_models.ValidateSqlStatementRequest,
    ) -> main_models.ValidateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = main_models.ValidateSqlStatementHeaders()
        return self.validate_sql_statement_with_options(namespace, request, headers, runtime)

    async def validate_sql_statement_async(
        self,
        namespace: str,
        request: main_models.ValidateSqlStatementRequest,
    ) -> main_models.ValidateSqlStatementResponse:
        runtime = RuntimeOptions()
        headers = main_models.ValidateSqlStatementHeaders()
        return await self.validate_sql_statement_with_options_async(namespace, request, headers, runtime)
