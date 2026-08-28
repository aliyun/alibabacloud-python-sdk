# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        self._endpoint = self.get_endpoint('agentcore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_delete_models_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchDeleteModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteModelsResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/actions/batch-delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_models_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchDeleteModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteModelsResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/actions/batch-delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_models(
        self,
        workspace_id: str,
        request: main_models.BatchDeleteModelsRequest,
    ) -> main_models.BatchDeleteModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_models_with_options(workspace_id, request, headers, runtime)

    async def batch_delete_models_async(
        self,
        workspace_id: str,
        request: main_models.BatchDeleteModelsRequest,
    ) -> main_models.BatchDeleteModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_models_with_options_async(workspace_id, request, headers, runtime)

    def batch_upload_skills_via_oss_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchUploadSkillsViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUploadSkillsViaOssResponse:
        tmp_req.validate()
        request = main_models.BatchUploadSkillsViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUploadSkillsViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/batch-upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUploadSkillsViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_upload_skills_via_oss_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.BatchUploadSkillsViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUploadSkillsViaOssResponse:
        tmp_req.validate()
        request = main_models.BatchUploadSkillsViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUploadSkillsViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/batch-upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUploadSkillsViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_upload_skills_via_oss(
        self,
        workspace_id: str,
        request: main_models.BatchUploadSkillsViaOssRequest,
    ) -> main_models.BatchUploadSkillsViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_upload_skills_via_oss_with_options(workspace_id, request, headers, runtime)

    async def batch_upload_skills_via_oss_async(
        self,
        workspace_id: str,
        request: main_models.BatchUploadSkillsViaOssRequest,
    ) -> main_models.BatchUploadSkillsViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_upload_skills_via_oss_with_options_async(workspace_id, request, headers, runtime)

    def create_agent_imchannel_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.CreateAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentIMChannelResponse:
        tmp_req.validate()
        request = main_models.CreateAgentIMChannelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentIMChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_imchannel_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.CreateAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentIMChannelResponse:
        tmp_req.validate()
        request = main_models.CreateAgentIMChannelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentIMChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_imchannel(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateAgentIMChannelRequest,
    ) -> main_models.CreateAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_imchannel_with_options(workspace_id, agent_id, request, headers, runtime)

    async def create_agent_imchannel_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateAgentIMChannelRequest,
    ) -> main_models.CreateAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_imchannel_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def create_agent_spec_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpecResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_spec_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpecResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_spec(
        self,
        workspace_id: str,
        request: main_models.CreateAgentSpecRequest,
    ) -> main_models.CreateAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_spec_with_options(workspace_id, request, headers, runtime)

    async def create_agent_spec_async(
        self,
        workspace_id: str,
        request: main_models.CreateAgentSpecRequest,
    ) -> main_models.CreateAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_spec_with_options_async(workspace_id, request, headers, runtime)

    def create_agent_spec_version_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        tmp_req: main_models.CreateAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpecVersionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSpecVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpecVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_spec_version_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        tmp_req: main_models.CreateAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSpecVersionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSpecVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSpecVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_spec_version(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.CreateAgentSpecVersionRequest,
    ) -> main_models.CreateAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_spec_version_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def create_agent_spec_version_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.CreateAgentSpecVersionRequest,
    ) -> main_models.CreateAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_spec_version_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def create_credential_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_credential_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCredentialResponse:
        tmp_req.validate()
        request = main_models.CreateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_credential(
        self,
        workspace_id: str,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_credential_with_options(workspace_id, request, headers, runtime)

    async def create_credential_async(
        self,
        workspace_id: str,
        request: main_models.CreateCredentialRequest,
    ) -> main_models.CreateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_credential_with_options_async(workspace_id, request, headers, runtime)

    def create_external_agent_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalAgentResponse:
        tmp_req.validate()
        request = main_models.CreateExternalAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_external_agent_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalAgentResponse:
        tmp_req.validate()
        request = main_models.CreateExternalAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_external_agent(
        self,
        workspace_id: str,
        request: main_models.CreateExternalAgentRequest,
    ) -> main_models.CreateExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_external_agent_with_options(workspace_id, request, headers, runtime)

    async def create_external_agent_async(
        self,
        workspace_id: str,
        request: main_models.CreateExternalAgentRequest,
    ) -> main_models.CreateExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_external_agent_with_options_async(workspace_id, request, headers, runtime)

    def create_external_agent_bootstrap_token_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateExternalAgentBootstrapTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalAgentBootstrapTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_type):
            query['networkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalAgentBootstrapToken',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}/bootstrap/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalAgentBootstrapTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_external_agent_bootstrap_token_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateExternalAgentBootstrapTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalAgentBootstrapTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_type):
            query['networkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalAgentBootstrapToken',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}/bootstrap/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalAgentBootstrapTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_external_agent_bootstrap_token(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateExternalAgentBootstrapTokenRequest,
    ) -> main_models.CreateExternalAgentBootstrapTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_external_agent_bootstrap_token_with_options(workspace_id, agent_id, request, headers, runtime)

    async def create_external_agent_bootstrap_token_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.CreateExternalAgentBootstrapTokenRequest,
    ) -> main_models.CreateExternalAgentBootstrapTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_external_agent_bootstrap_token_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def create_identity_provider_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.CreateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider(
        self,
        workspace_id: str,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_identity_provider_with_options(workspace_id, request, headers, runtime)

    async def create_identity_provider_async(
        self,
        workspace_id: str,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_identity_provider_with_options_async(workspace_id, request, headers, runtime)

    def create_managed_agent_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.CreateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_managed_agent_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.CreateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_managed_agent(
        self,
        workspace_id: str,
        request: main_models.CreateManagedAgentRequest,
    ) -> main_models.CreateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_managed_agent_with_options(workspace_id, request, headers, runtime)

    async def create_managed_agent_async(
        self,
        workspace_id: str,
        request: main_models.CreateManagedAgentRequest,
    ) -> main_models.CreateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_managed_agent_with_options_async(workspace_id, request, headers, runtime)

    def create_mcp_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpResponse:
        tmp_req.validate()
        request = main_models.CreateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcp_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpResponse:
        tmp_req.validate()
        request = main_models.CreateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcp(
        self,
        workspace_id: str,
        request: main_models.CreateMcpRequest,
    ) -> main_models.CreateMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mcp_with_options(workspace_id, request, headers, runtime)

    async def create_mcp_async(
        self,
        workspace_id: str,
        request: main_models.CreateMcpRequest,
    ) -> main_models.CreateMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mcp_with_options_async(workspace_id, request, headers, runtime)

    def create_model_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelResponse:
        tmp_req.validate()
        request = main_models.CreateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        workspace_id: str,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_with_options(workspace_id, request, headers, runtime)

    async def create_model_async(
        self,
        workspace_id: str,
        request: main_models.CreateModelRequest,
    ) -> main_models.CreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_with_options_async(workspace_id, request, headers, runtime)

    def create_model_connection_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_connection_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_connection(
        self,
        workspace_id: str,
        request: main_models.CreateModelConnectionRequest,
    ) -> main_models.CreateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_connection_with_options(workspace_id, request, headers, runtime)

    async def create_model_connection_async(
        self,
        workspace_id: str,
        request: main_models.CreateModelConnectionRequest,
    ) -> main_models.CreateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_connection_with_options_async(workspace_id, request, headers, runtime)

    def create_skill_draft_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateSkillDraftRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillDraftResponse:
        tmp_req.validate()
        request = main_models.CreateSkillDraftShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillDraft',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_draft_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateSkillDraftRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillDraftResponse:
        tmp_req.validate()
        request = main_models.CreateSkillDraftShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillDraft',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_draft(
        self,
        workspace_id: str,
        request: main_models.CreateSkillDraftRequest,
    ) -> main_models.CreateSkillDraftResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_skill_draft_with_options(workspace_id, request, headers, runtime)

    async def create_skill_draft_async(
        self,
        workspace_id: str,
        request: main_models.CreateSkillDraftRequest,
    ) -> main_models.CreateSkillDraftResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_skill_draft_with_options_async(workspace_id, request, headers, runtime)

    def create_team_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_team_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        tmp_req.validate()
        request = main_models.CreateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_team(
        self,
        workspace_id: str,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_team_with_options(workspace_id, request, headers, runtime)

    async def create_team_async(
        self,
        workspace_id: str,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_team_with_options_async(workspace_id, request, headers, runtime)

    def create_user_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        tmp_req.validate()
        request = main_models.CreateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        workspace_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(workspace_id, request, headers, runtime)

    async def create_user_async(
        self,
        workspace_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(workspace_id, request, headers, runtime)

    def create_workspace_with_options(
        self,
        tmp_req: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        tmp_req: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def debug_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.DebugModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugModelResponse:
        tmp_req.validate()
        request = main_models.DebugModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}/actions/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.DebugModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugModelResponse:
        tmp_req.validate()
        request = main_models.DebugModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}/actions/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DebugModelRequest,
    ) -> main_models.DebugModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.debug_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def debug_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DebugModelRequest,
    ) -> main_models.DebugModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.debug_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def delete_agent_imchannel_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.DeleteAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentIMChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentIMChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_imchannel_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.DeleteAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentIMChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentIMChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_imchannel(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.DeleteAgentIMChannelRequest,
    ) -> main_models.DeleteAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_imchannel_with_options(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    async def delete_agent_imchannel_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.DeleteAgentIMChannelRequest,
    ) -> main_models.DeleteAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_imchannel_with_options_async(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    def delete_agent_spec_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpecResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_spec_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpecResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_spec(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecRequest,
    ) -> main_models.DeleteAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_spec_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def delete_agent_spec_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecRequest,
    ) -> main_models.DeleteAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_spec_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def delete_agent_spec_version_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpecVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/draft',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpecVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_spec_version_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSpecVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/draft',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSpecVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_spec_version(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecVersionRequest,
    ) -> main_models.DeleteAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_spec_version_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def delete_agent_spec_version_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DeleteAgentSpecVersionRequest,
    ) -> main_models.DeleteAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_spec_version_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def delete_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def delete_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.DeleteCredentialRequest,
    ) -> main_models.DeleteCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def delete_external_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExternalAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_external_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExternalAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_external_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteExternalAgentRequest,
    ) -> main_models.DeleteExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_external_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def delete_external_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteExternalAgentRequest,
    ) -> main_models.DeleteExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_external_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def delete_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def delete_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def delete_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
    ) -> main_models.DeleteManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def delete_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.DeleteManagedAgentRequest,
    ) -> main_models.DeleteManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def delete_mcp_with_options(
        self,
        mcp_server_id: str,
        workspace_id: str,
        request: main_models.DeleteMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcp_with_options_async(
        self,
        mcp_server_id: str,
        workspace_id: str,
        request: main_models.DeleteMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcp(
        self,
        mcp_server_id: str,
        workspace_id: str,
        request: main_models.DeleteMcpRequest,
    ) -> main_models.DeleteMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mcp_with_options(mcp_server_id, workspace_id, request, headers, runtime)

    async def delete_mcp_async(
        self,
        mcp_server_id: str,
        workspace_id: str,
        request: main_models.DeleteMcpRequest,
    ) -> main_models.DeleteMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mcp_with_options_async(mcp_server_id, workspace_id, request, headers, runtime)

    def delete_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def delete_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.DeleteModelRequest,
    ) -> main_models.DeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def delete_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
    ) -> main_models.DeleteModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def delete_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.DeleteModelConnectionRequest,
    ) -> main_models.DeleteModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def delete_skill_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_skill_with_options(workspace_id, skill_name, request, headers, runtime)

    async def delete_skill_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_skill_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def delete_skill_draft_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillDraftRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillDraftResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillDraft',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/draft',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_draft_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillDraftRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillDraftResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillDraft',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/draft',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_draft(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillDraftRequest,
    ) -> main_models.DeleteSkillDraftResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_skill_draft_with_options(workspace_id, skill_name, request, headers, runtime)

    async def delete_skill_draft_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.DeleteSkillDraftRequest,
    ) -> main_models.DeleteSkillDraftResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_skill_draft_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def delete_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def delete_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def delete_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def delete_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_id, request, headers, runtime)

    def download_agent_spec_via_oss_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DownloadAgentSpecViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadAgentSpecViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_spec_version):
            query['agentSpecVersion'] = request.agent_spec_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadAgentSpecViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/actions/download-via-oss',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadAgentSpecViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_agent_spec_via_oss_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DownloadAgentSpecViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadAgentSpecViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_spec_version):
            query['agentSpecVersion'] = request.agent_spec_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadAgentSpecViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/actions/download-via-oss',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadAgentSpecViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_agent_spec_via_oss(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DownloadAgentSpecViaOssRequest,
    ) -> main_models.DownloadAgentSpecViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.download_agent_spec_via_oss_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def download_agent_spec_via_oss_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.DownloadAgentSpecViaOssRequest,
    ) -> main_models.DownloadAgentSpecViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.download_agent_spec_via_oss_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def download_skill_version_via_oss_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.DownloadSkillVersionViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DownloadSkillVersionViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/download-via-oss',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSkillVersionViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_skill_version_via_oss_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.DownloadSkillVersionViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DownloadSkillVersionViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/download-via-oss',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSkillVersionViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_skill_version_via_oss(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.DownloadSkillVersionViaOssRequest,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.download_skill_version_via_oss_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def download_skill_version_via_oss_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.DownloadSkillVersionViaOssRequest,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.download_skill_version_via_oss_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def force_publish_skill_version_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.ForcePublishSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ForcePublishSkillVersionResponse:
        tmp_req.validate()
        request = main_models.ForcePublishSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ForcePublishSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/force-publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForcePublishSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def force_publish_skill_version_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.ForcePublishSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ForcePublishSkillVersionResponse:
        tmp_req.validate()
        request = main_models.ForcePublishSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ForcePublishSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/force-publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForcePublishSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def force_publish_skill_version(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.ForcePublishSkillVersionRequest,
    ) -> main_models.ForcePublishSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.force_publish_skill_version_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def force_publish_skill_version_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.ForcePublishSkillVersionRequest,
    ) -> main_models.ForcePublishSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.force_publish_skill_version_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def get_agent_imchannel_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.GetAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentIMChannelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentIMChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_imchannel_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.GetAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentIMChannelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentIMChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_imchannel(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.GetAgentIMChannelRequest,
    ) -> main_models.GetAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_imchannel_with_options(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    async def get_agent_imchannel_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.GetAgentIMChannelRequest,
    ) -> main_models.GetAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_imchannel_with_options_async(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    def get_agent_spec_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_spec_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_spec(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecRequest,
    ) -> main_models.GetAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_spec_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def get_agent_spec_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecRequest,
    ) -> main_models.GetAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_spec_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def get_agent_spec_import_file_url_with_options(
        self,
        workspace_id: str,
        request: main_models.GetAgentSpecImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['contentType'] = request.content_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecImportFileUrl',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-spec-actions/get-import-file-url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_spec_import_file_url_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetAgentSpecImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['contentType'] = request.content_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecImportFileUrl',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-spec-actions/get-import-file-url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_spec_import_file_url(
        self,
        workspace_id: str,
        request: main_models.GetAgentSpecImportFileUrlRequest,
    ) -> main_models.GetAgentSpecImportFileUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_spec_import_file_url_with_options(workspace_id, request, headers, runtime)

    async def get_agent_spec_import_file_url_async(
        self,
        workspace_id: str,
        request: main_models.GetAgentSpecImportFileUrlRequest,
    ) -> main_models.GetAgentSpecImportFileUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_spec_import_file_url_with_options_async(workspace_id, request, headers, runtime)

    def get_agent_spec_latest_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecLatestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecLatestResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecLatest',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/latest',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecLatestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_spec_latest_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecLatestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecLatestResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecLatest',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/latest',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecLatestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_spec_latest(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecLatestRequest,
    ) -> main_models.GetAgentSpecLatestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_spec_latest_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def get_agent_spec_latest_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.GetAgentSpecLatestRequest,
    ) -> main_models.GetAgentSpecLatestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_spec_latest_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def get_agent_spec_version_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.GetAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions/{DaraURL.percent_encode(agent_spec_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_spec_version_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.GetAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSpecVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions/{DaraURL.percent_encode(agent_spec_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSpecVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_spec_version(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.GetAgentSpecVersionRequest,
    ) -> main_models.GetAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_spec_version_with_options(workspace_id, agent_spec_name, agent_spec_version, request, headers, runtime)

    async def get_agent_spec_version_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.GetAgentSpecVersionRequest,
    ) -> main_models.GetAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_spec_version_with_options_async(workspace_id, agent_spec_name, agent_spec_version, request, headers, runtime)

    def get_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def get_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.GetCredentialRequest,
    ) -> main_models.GetCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def get_external_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentRequest,
    ) -> main_models.GetExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_external_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def get_external_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentRequest,
    ) -> main_models.GetExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_external_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def get_external_agent_bootstrap_options_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentBootstrapOptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalAgentBootstrapOptionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExternalAgentBootstrapOptions',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}/bootstrap/options',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalAgentBootstrapOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_agent_bootstrap_options_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentBootstrapOptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalAgentBootstrapOptionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExternalAgentBootstrapOptions',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}/bootstrap/options',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalAgentBootstrapOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_agent_bootstrap_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentBootstrapOptionsRequest,
    ) -> main_models.GetExternalAgentBootstrapOptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_external_agent_bootstrap_options_with_options(workspace_id, agent_id, request, headers, runtime)

    async def get_external_agent_bootstrap_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetExternalAgentBootstrapOptionsRequest,
    ) -> main_models.GetExternalAgentBootstrapOptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_external_agent_bootstrap_options_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def get_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def get_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def get_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedAgentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
    ) -> main_models.GetManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def get_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.GetManagedAgentRequest,
    ) -> main_models.GetManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def get_mcp_with_options(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.GetMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcp_with_options_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.GetMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcp(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.GetMcpRequest,
    ) -> main_models.GetMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mcp_with_options(workspace_id, mcp_server_id, request, headers, runtime)

    async def get_mcp_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.GetMcpRequest,
    ) -> main_models.GetMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mcp_with_options_async(workspace_id, mcp_server_id, request, headers, runtime)

    def get_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def get_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.GetModelRequest,
    ) -> main_models.GetModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def get_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelConnectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelConnectionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
    ) -> main_models.GetModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def get_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.GetModelConnectionRequest,
    ) -> main_models.GetModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def get_service_endpoint_with_options(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpoint',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints/{DaraURL.percent_encode(service_endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_endpoint_with_options_async(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpoint',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints/{DaraURL.percent_encode(service_endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_endpoint(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointRequest,
    ) -> main_models.GetServiceEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_endpoint_with_options(workspace_id, service_endpoint_id, request, headers, runtime)

    async def get_service_endpoint_async(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointRequest,
    ) -> main_models.GetServiceEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_endpoint_with_options_async(workspace_id, service_endpoint_id, request, headers, runtime)

    def get_service_endpoint_api_key_with_options(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpointApiKey',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints/{DaraURL.percent_encode(service_endpoint_id)}/api-key/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_endpoint_api_key_with_options_async(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEndpointApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEndpointApiKey',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints/{DaraURL.percent_encode(service_endpoint_id)}/api-key/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEndpointApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_endpoint_api_key(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointApiKeyRequest,
    ) -> main_models.GetServiceEndpointApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_endpoint_api_key_with_options(workspace_id, service_endpoint_id, request, headers, runtime)

    async def get_service_endpoint_api_key_async(
        self,
        workspace_id: str,
        service_endpoint_id: str,
        request: main_models.GetServiceEndpointApiKeyRequest,
    ) -> main_models.GetServiceEndpointApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_endpoint_api_key_with_options_async(workspace_id, service_endpoint_id, request, headers, runtime)

    def get_skill_detail_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.GetSkillDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillDetail',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_detail_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.GetSkillDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillDetail',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_detail(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.GetSkillDetailRequest,
    ) -> main_models.GetSkillDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_detail_with_options(workspace_id, skill_name, request, headers, runtime)

    async def get_skill_detail_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.GetSkillDetailRequest,
    ) -> main_models.GetSkillDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_detail_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def get_skill_import_file_url_with_options(
        self,
        workspace_id: str,
        request: main_models.GetSkillImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['contentType'] = request.content_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillImportFileUrl',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/get-import-file-url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_import_file_url_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetSkillImportFileUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['contentType'] = request.content_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillImportFileUrl',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/get-import-file-url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_import_file_url(
        self,
        workspace_id: str,
        request: main_models.GetSkillImportFileUrlRequest,
    ) -> main_models.GetSkillImportFileUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_import_file_url_with_options(workspace_id, request, headers, runtime)

    async def get_skill_import_file_url_async(
        self,
        workspace_id: str,
        request: main_models.GetSkillImportFileUrlRequest,
    ) -> main_models.GetSkillImportFileUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_import_file_url_with_options_async(workspace_id, request, headers, runtime)

    def get_skill_version_detail_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.GetSkillVersionDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillVersionDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillVersionDetail',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_version_detail_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.GetSkillVersionDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillVersionDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillVersionDetail',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_version_detail(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.GetSkillVersionDetailRequest,
    ) -> main_models.GetSkillVersionDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_version_detail_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def get_skill_version_detail_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.GetSkillVersionDetailRequest,
    ) -> main_models.GetSkillVersionDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_version_detail_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def get_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def get_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def get_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def get_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, request, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
        request: main_models.GetWorkspaceRequest,
    ) -> main_models.GetWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_id, request, headers, runtime)

    def get_workspace_plugin_with_options(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.GetWorkspacePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspacePluginResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspacePlugin',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/plugins/{DaraURL.percent_encode(plugin_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspacePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_plugin_with_options_async(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.GetWorkspacePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspacePluginResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspacePlugin',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/plugins/{DaraURL.percent_encode(plugin_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspacePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace_plugin(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.GetWorkspacePluginRequest,
    ) -> main_models.GetWorkspacePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_workspace_plugin_with_options(workspace_id, plugin_name, request, headers, runtime)

    async def get_workspace_plugin_async(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.GetWorkspacePluginRequest,
    ) -> main_models.GetWorkspacePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_workspace_plugin_with_options_async(workspace_id, plugin_name, request, headers, runtime)

    def install_workspace_plugin_with_options(
        self,
        workspace_id: str,
        plugin_name: str,
        tmp_req: main_models.InstallWorkspacePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallWorkspacePluginResponse:
        tmp_req.validate()
        request = main_models.InstallWorkspacePluginShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallWorkspacePlugin',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/plugins/{DaraURL.percent_encode(plugin_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallWorkspacePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_workspace_plugin_with_options_async(
        self,
        workspace_id: str,
        plugin_name: str,
        tmp_req: main_models.InstallWorkspacePluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallWorkspacePluginResponse:
        tmp_req.validate()
        request = main_models.InstallWorkspacePluginShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallWorkspacePlugin',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/plugins/{DaraURL.percent_encode(plugin_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallWorkspacePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_workspace_plugin(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.InstallWorkspacePluginRequest,
    ) -> main_models.InstallWorkspacePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_workspace_plugin_with_options(workspace_id, plugin_name, request, headers, runtime)

    async def install_workspace_plugin_async(
        self,
        workspace_id: str,
        plugin_name: str,
        request: main_models.InstallWorkspacePluginRequest,
    ) -> main_models.InstallWorkspacePluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_workspace_plugin_with_options_async(workspace_id, plugin_name, request, headers, runtime)

    def list_agent_imchannels_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.ListAgentIMChannelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentIMChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['channelType'] = request.channel_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentIMChannels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentIMChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_imchannels_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.ListAgentIMChannelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentIMChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['channelType'] = request.channel_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentIMChannels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentIMChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_imchannels(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.ListAgentIMChannelsRequest,
    ) -> main_models.ListAgentIMChannelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_imchannels_with_options(workspace_id, agent_id, request, headers, runtime)

    async def list_agent_imchannels_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.ListAgentIMChannelsRequest,
    ) -> main_models.ListAgentIMChannelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_imchannels_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def list_agent_specs_with_options(
        self,
        workspace_id: str,
        request: main_models.ListAgentSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_spec_name):
            query['agentSpecName'] = request.agent_spec_name
        if not DaraCore.is_null(request.biz_tag):
            query['bizTag'] = request.biz_tag
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.with_capabilities):
            query['withCapabilities'] = request.with_capabilities
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpecs',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_specs_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListAgentSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_spec_name):
            query['agentSpecName'] = request.agent_spec_name
        if not DaraCore.is_null(request.biz_tag):
            query['bizTag'] = request.biz_tag
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.with_capabilities):
            query['withCapabilities'] = request.with_capabilities
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSpecs',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_specs(
        self,
        workspace_id: str,
        request: main_models.ListAgentSpecsRequest,
    ) -> main_models.ListAgentSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_specs_with_options(workspace_id, request, headers, runtime)

    async def list_agent_specs_async(
        self,
        workspace_id: str,
        request: main_models.ListAgentSpecsRequest,
    ) -> main_models.ListAgentSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_specs_with_options_async(workspace_id, request, headers, runtime)

    def list_agent_teams_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ListAgentTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentTeamsResponse:
        tmp_req.validate()
        request = main_models.ListAgentTeamsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-team-memberships',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_teams_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ListAgentTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentTeamsResponse:
        tmp_req.validate()
        request = main_models.ListAgentTeamsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-team-memberships',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_teams(
        self,
        workspace_id: str,
        request: main_models.ListAgentTeamsRequest,
    ) -> main_models.ListAgentTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_teams_with_options(workspace_id, request, headers, runtime)

    async def list_agent_teams_async(
        self,
        workspace_id: str,
        request: main_models.ListAgentTeamsRequest,
    ) -> main_models.ListAgentTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_teams_with_options_async(workspace_id, request, headers, runtime)

    def list_credentials_with_options(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['credentialType'] = request.credential_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_credentials_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['credentialType'] = request.credential_type
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCredentials',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_credentials(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_credentials_with_options(workspace_id, request, headers, runtime)

    async def list_credentials_async(
        self,
        workspace_id: str,
        request: main_models.ListCredentialsRequest,
    ) -> main_models.ListCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_credentials_with_options_async(workspace_id, request, headers, runtime)

    def list_external_agents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListExternalAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_agents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListExternalAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_agents(
        self,
        workspace_id: str,
        request: main_models.ListExternalAgentsRequest,
    ) -> main_models.ListExternalAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_external_agents_with_options(workspace_id, request, headers, runtime)

    async def list_external_agents_async(
        self,
        workspace_id: str,
        request: main_models.ListExternalAgentsRequest,
    ) -> main_models.ListExternalAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_external_agents_with_options_async(workspace_id, request, headers, runtime)

    def list_identity_providers_with_options(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_identity_providers_with_options(workspace_id, request, headers, runtime)

    async def list_identity_providers_async(
        self,
        workspace_id: str,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_identity_providers_with_options_async(workspace_id, request, headers, runtime)

    def list_managed_agents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListManagedAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_managed_agents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListManagedAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListManagedAgents',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListManagedAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_managed_agents(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
    ) -> main_models.ListManagedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_managed_agents_with_options(workspace_id, request, headers, runtime)

    async def list_managed_agents_async(
        self,
        workspace_id: str,
        request: main_models.ListManagedAgentsRequest,
    ) -> main_models.ListManagedAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_managed_agents_with_options_async(workspace_id, request, headers, runtime)

    def list_mcp_tools_with_options(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.ListMcpToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpTools',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/tools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcp_tools_with_options_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.ListMcpToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpTools',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/tools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcp_tools(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.ListMcpToolsRequest,
    ) -> main_models.ListMcpToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mcp_tools_with_options(workspace_id, mcp_server_id, request, headers, runtime)

    async def list_mcp_tools_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.ListMcpToolsRequest,
    ) -> main_models.ListMcpToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mcp_tools_with_options_async(workspace_id, mcp_server_id, request, headers, runtime)

    def list_mcps_with_options(
        self,
        workspace_id: str,
        request: main_models.ListMcpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcps',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcps_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListMcpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcps',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcps(
        self,
        workspace_id: str,
        request: main_models.ListMcpsRequest,
    ) -> main_models.ListMcpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mcps_with_options(workspace_id, request, headers, runtime)

    async def list_mcps_async(
        self,
        workspace_id: str,
        request: main_models.ListMcpsRequest,
    ) -> main_models.ListMcpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mcps_with_options_async(workspace_id, request, headers, runtime)

    def list_model_connections_with_options(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_models):
            query['includeModels'] = request.include_models
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol):
            query['protocol'] = request.protocol
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelConnections',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_connections_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_models):
            query['includeModels'] = request.include_models
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol):
            query['protocol'] = request.protocol
        if not DaraCore.is_null(request.provider_type):
            query['providerType'] = request.provider_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelConnections',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_connections(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
    ) -> main_models.ListModelConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_connections_with_options(workspace_id, request, headers, runtime)

    async def list_model_connections_async(
        self,
        workspace_id: str,
        request: main_models.ListModelConnectionsRequest,
    ) -> main_models.ListModelConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_connections_with_options_async(workspace_id, request, headers, runtime)

    def list_models_with_options(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_id):
            query['connectionId'] = request.connection_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_id):
            query['connectionId'] = request.connection_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_name):
            query['modelName'] = request.model_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_models_with_options(workspace_id, request, headers, runtime)

    async def list_models_async(
        self,
        workspace_id: str,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_models_with_options_async(workspace_id, request, headers, runtime)

    def list_predefined_model_providers_with_options(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModelProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_model_providers_with_options_async(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModelProviders',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_model_providers(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_predefined_model_providers_with_options(request, headers, runtime)

    async def list_predefined_model_providers_async(
        self,
        request: main_models.ListPredefinedModelProvidersRequest,
    ) -> main_models.ListPredefinedModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_predefined_model_providers_with_options_async(request, headers, runtime)

    def list_predefined_models_with_options(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers/{DaraURL.percent_encode(provider_type)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_models_with_options_async(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedModelsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedModels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/model-catalog/providers/{DaraURL.percent_encode(provider_type)}/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_models(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
    ) -> main_models.ListPredefinedModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_predefined_models_with_options(provider_type, request, headers, runtime)

    async def list_predefined_models_async(
        self,
        provider_type: str,
        request: main_models.ListPredefinedModelsRequest,
    ) -> main_models.ListPredefinedModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_predefined_models_with_options_async(provider_type, request, headers, runtime)

    def list_service_endpoints_with_options(
        self,
        workspace_id: str,
        request: main_models.ListServiceEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            query['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.collaboration_component):
            query['collaborationComponent'] = request.collaboration_component
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_binding_id):
            query['resourceBindingId'] = request.resource_binding_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceEndpoints',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_endpoints_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListServiceEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_version):
            query['agentVersion'] = request.agent_version
        if not DaraCore.is_null(request.collaboration_component):
            query['collaborationComponent'] = request.collaboration_component
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_binding_id):
            query['resourceBindingId'] = request.resource_binding_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceEndpoints',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/service-endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_endpoints(
        self,
        workspace_id: str,
        request: main_models.ListServiceEndpointsRequest,
    ) -> main_models.ListServiceEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_endpoints_with_options(workspace_id, request, headers, runtime)

    async def list_service_endpoints_async(
        self,
        workspace_id: str,
        request: main_models.ListServiceEndpointsRequest,
    ) -> main_models.ListServiceEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_endpoints_with_options_async(workspace_id, request, headers, runtime)

    def list_skills_with_options(
        self,
        workspace_id: str,
        request: main_models.ListSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skills_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skills(
        self,
        workspace_id: str,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_skills_with_options(workspace_id, request, headers, runtime)

    async def list_skills_async(
        self,
        workspace_id: str,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_skills_with_options_async(workspace_id, request, headers, runtime)

    def list_teams_with_options(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_teams_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_teams(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_teams_with_options(workspace_id, request, headers, runtime)

    async def list_teams_async(
        self,
        workspace_id: str,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_teams_with_options_async(workspace_id, request, headers, runtime)

    def list_users_with_options(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(workspace_id, request, headers, runtime)

    async def list_users_async(
        self,
        workspace_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def offline_skill_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.OfflineSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineSkillResponse:
        tmp_req.validate()
        request = main_models.OfflineSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/actions/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_skill_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.OfflineSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineSkillResponse:
        tmp_req.validate()
        request = main_models.OfflineSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/actions/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_skill(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.OfflineSkillRequest,
    ) -> main_models.OfflineSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_skill_with_options(workspace_id, skill_name, request, headers, runtime)

    async def offline_skill_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.OfflineSkillRequest,
    ) -> main_models.OfflineSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_skill_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def online_skill_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.OnlineSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineSkillResponse:
        tmp_req.validate()
        request = main_models.OnlineSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/actions/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_skill_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.OnlineSkillRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineSkillResponse:
        tmp_req.validate()
        request = main_models.OnlineSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineSkill',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/actions/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_skill(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.OnlineSkillRequest,
    ) -> main_models.OnlineSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.online_skill_with_options(workspace_id, skill_name, request, headers, runtime)

    async def online_skill_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.OnlineSkillRequest,
    ) -> main_models.OnlineSkillResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.online_skill_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def precheck_skill_upload_via_oss_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.PrecheckSkillUploadViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckSkillUploadViaOssResponse:
        tmp_req.validate()
        request = main_models.PrecheckSkillUploadViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckSkillUploadViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/precheck-upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckSkillUploadViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def precheck_skill_upload_via_oss_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.PrecheckSkillUploadViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckSkillUploadViaOssResponse:
        tmp_req.validate()
        request = main_models.PrecheckSkillUploadViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckSkillUploadViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/precheck-upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckSkillUploadViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def precheck_skill_upload_via_oss(
        self,
        workspace_id: str,
        request: main_models.PrecheckSkillUploadViaOssRequest,
    ) -> main_models.PrecheckSkillUploadViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.precheck_skill_upload_via_oss_with_options(workspace_id, request, headers, runtime)

    async def precheck_skill_upload_via_oss_async(
        self,
        workspace_id: str,
        request: main_models.PrecheckSkillUploadViaOssRequest,
    ) -> main_models.PrecheckSkillUploadViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.precheck_skill_upload_via_oss_with_options_async(workspace_id, request, headers, runtime)

    def publish_skill_version_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.PublishSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishSkillVersionResponse:
        tmp_req.validate()
        request = main_models.PublishSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_skill_version_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.PublishSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishSkillVersionResponse:
        tmp_req.validate()
        request = main_models.PublishSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_skill_version(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.PublishSkillVersionRequest,
    ) -> main_models.PublishSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_skill_version_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def publish_skill_version_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.PublishSkillVersionRequest,
    ) -> main_models.PublishSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_skill_version_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def redraft_skill_version_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.RedraftSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RedraftSkillVersionResponse:
        tmp_req.validate()
        request = main_models.RedraftSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RedraftSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/redraft',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedraftSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def redraft_skill_version_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.RedraftSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RedraftSkillVersionResponse:
        tmp_req.validate()
        request = main_models.RedraftSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RedraftSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/redraft',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedraftSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def redraft_skill_version(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.RedraftSkillVersionRequest,
    ) -> main_models.RedraftSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.redraft_skill_version_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def redraft_skill_version_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.RedraftSkillVersionRequest,
    ) -> main_models.RedraftSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.redraft_skill_version_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def reset_user_password_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ResetUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        tmp_req.validate()
        request = main_models.ResetUserPasswordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/actions/reset-password',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ResetUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        tmp_req.validate()
        request = main_models.ResetUserPasswordShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/actions/reset-password',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        workspace_id: str,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_user_password_with_options(workspace_id, request, headers, runtime)

    async def reset_user_password_async(
        self,
        workspace_id: str,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_user_password_with_options_async(workspace_id, request, headers, runtime)

    def submit_agent_spec_version_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        tmp_req: main_models.SubmitAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAgentSpecVersionResponse:
        tmp_req.validate()
        request = main_models.SubmitAgentSpecVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions/{DaraURL.percent_encode(agent_spec_version)}/actions/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAgentSpecVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_agent_spec_version_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        tmp_req: main_models.SubmitAgentSpecVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAgentSpecVersionResponse:
        tmp_req.validate()
        request = main_models.SubmitAgentSpecVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAgentSpecVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}/versions/{DaraURL.percent_encode(agent_spec_version)}/actions/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAgentSpecVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_agent_spec_version(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.SubmitAgentSpecVersionRequest,
    ) -> main_models.SubmitAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_agent_spec_version_with_options(workspace_id, agent_spec_name, agent_spec_version, request, headers, runtime)

    async def submit_agent_spec_version_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        agent_spec_version: str,
        request: main_models.SubmitAgentSpecVersionRequest,
    ) -> main_models.SubmitAgentSpecVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_agent_spec_version_with_options_async(workspace_id, agent_spec_name, agent_spec_version, request, headers, runtime)

    def submit_skill_version_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.SubmitSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSkillVersionResponse:
        tmp_req.validate()
        request = main_models.SubmitSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_skill_version_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        tmp_req: main_models.SubmitSkillVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSkillVersionResponse:
        tmp_req.validate()
        request = main_models.SubmitSkillVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSkillVersion',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/versions/{DaraURL.percent_encode(skill_version)}/actions/submit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_skill_version(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.SubmitSkillVersionRequest,
    ) -> main_models.SubmitSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_skill_version_with_options(workspace_id, skill_name, skill_version, request, headers, runtime)

    async def submit_skill_version_async(
        self,
        workspace_id: str,
        skill_name: str,
        skill_version: str,
        request: main_models.SubmitSkillVersionRequest,
    ) -> main_models.SubmitSkillVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_skill_version_with_options_async(workspace_id, skill_name, skill_version, request, headers, runtime)

    def update_agent_imchannel_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        tmp_req: main_models.UpdateAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentIMChannelResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentIMChannelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentIMChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_imchannel_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        tmp_req: main_models.UpdateAgentIMChannelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentIMChannelResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentIMChannelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentIMChannel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentIMChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_imchannel(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.UpdateAgentIMChannelRequest,
    ) -> main_models.UpdateAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_imchannel_with_options(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    async def update_agent_imchannel_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.UpdateAgentIMChannelRequest,
    ) -> main_models.UpdateAgentIMChannelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_imchannel_with_options_async(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    def update_agent_imchannel_credential_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        tmp_req: main_models.UpdateAgentIMChannelCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentIMChannelCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentIMChannelCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentIMChannelCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}/actions/update-credential',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentIMChannelCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_imchannel_credential_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        tmp_req: main_models.UpdateAgentIMChannelCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentIMChannelCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentIMChannelCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentIMChannelCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agents/{DaraURL.percent_encode(agent_id)}/im-channels/{DaraURL.percent_encode(im_channel_id)}/actions/update-credential',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentIMChannelCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_imchannel_credential(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.UpdateAgentIMChannelCredentialRequest,
    ) -> main_models.UpdateAgentIMChannelCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_imchannel_credential_with_options(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    async def update_agent_imchannel_credential_async(
        self,
        workspace_id: str,
        agent_id: str,
        im_channel_id: str,
        request: main_models.UpdateAgentIMChannelCredentialRequest,
    ) -> main_models.UpdateAgentIMChannelCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_imchannel_credential_with_options_async(workspace_id, agent_id, im_channel_id, request, headers, runtime)

    def update_agent_spec_with_options(
        self,
        workspace_id: str,
        agent_spec_name: str,
        tmp_req: main_models.UpdateAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpecResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_spec_with_options_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        tmp_req: main_models.UpdateAgentSpecRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentSpecResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentSpec',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-specs/{DaraURL.percent_encode(agent_spec_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent_spec(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.UpdateAgentSpecRequest,
    ) -> main_models.UpdateAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_spec_with_options(workspace_id, agent_spec_name, request, headers, runtime)

    async def update_agent_spec_async(
        self,
        workspace_id: str,
        agent_spec_name: str,
        request: main_models.UpdateAgentSpecRequest,
    ) -> main_models.UpdateAgentSpecResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_spec_with_options_async(workspace_id, agent_spec_name, request, headers, runtime)

    def update_credential_with_options(
        self,
        workspace_id: str,
        credential_id: str,
        tmp_req: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_credential_with_options_async(
        self,
        workspace_id: str,
        credential_id: str,
        tmp_req: main_models.UpdateCredentialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCredentialResponse:
        tmp_req.validate()
        request = main_models.UpdateCredentialShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCredential',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/credentials/{DaraURL.percent_encode(credential_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_credential(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_credential_with_options(workspace_id, credential_id, request, headers, runtime)

    async def update_credential_async(
        self,
        workspace_id: str,
        credential_id: str,
        request: main_models.UpdateCredentialRequest,
    ) -> main_models.UpdateCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_credential_with_options_async(workspace_id, credential_id, request, headers, runtime)

    def update_external_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExternalAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateExternalAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_external_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExternalAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateExternalAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExternalAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/external-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_external_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateExternalAgentRequest,
    ) -> main_models.UpdateExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_external_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def update_external_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateExternalAgentRequest,
    ) -> main_models.UpdateExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_external_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def update_identity_provider_with_options(
        self,
        workspace_id: str,
        identity_provider_type: str,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_identity_provider_with_options_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        tmp_req: main_models.UpdateIdentityProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        tmp_req.validate()
        request = main_models.UpdateIdentityProviderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/identity-providers/{DaraURL.percent_encode(identity_provider_type)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_identity_provider(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_identity_provider_with_options(workspace_id, identity_provider_type, request, headers, runtime)

    async def update_identity_provider_async(
        self,
        workspace_id: str,
        identity_provider_type: str,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_identity_provider_with_options_async(workspace_id, identity_provider_type, request, headers, runtime)

    def update_managed_agent_with_options(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateManagedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_managed_agent_with_options_async(
        self,
        workspace_id: str,
        agent_id: str,
        tmp_req: main_models.UpdateManagedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateManagedAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateManagedAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateManagedAgent',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/managed-agents/{DaraURL.percent_encode(agent_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateManagedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_managed_agent(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateManagedAgentRequest,
    ) -> main_models.UpdateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_managed_agent_with_options(workspace_id, agent_id, request, headers, runtime)

    async def update_managed_agent_async(
        self,
        workspace_id: str,
        agent_id: str,
        request: main_models.UpdateManagedAgentRequest,
    ) -> main_models.UpdateManagedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_managed_agent_with_options_async(workspace_id, agent_id, request, headers, runtime)

    def update_mcp_with_options(
        self,
        workspace_id: str,
        mcp_server_id: str,
        tmp_req: main_models.UpdateMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpResponse:
        tmp_req.validate()
        request = main_models.UpdateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcp_with_options_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        tmp_req: main_models.UpdateMcpRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpResponse:
        tmp_req.validate()
        request = main_models.UpdateMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcp',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcp(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.UpdateMcpRequest,
    ) -> main_models.UpdateMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_mcp_with_options(workspace_id, mcp_server_id, request, headers, runtime)

    async def update_mcp_async(
        self,
        workspace_id: str,
        mcp_server_id: str,
        request: main_models.UpdateMcpRequest,
    ) -> main_models.UpdateMcpResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_mcp_with_options_async(workspace_id, mcp_server_id, request, headers, runtime)

    def update_model_with_options(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        tmp_req.validate()
        request = main_models.UpdateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        workspace_id: str,
        model_id: str,
        tmp_req: main_models.UpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelResponse:
        tmp_req.validate()
        request = main_models.UpdateModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModel',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/models/{DaraURL.percent_encode(model_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_with_options(workspace_id, model_id, request, headers, runtime)

    async def update_model_async(
        self,
        workspace_id: str,
        model_id: str,
        request: main_models.UpdateModelRequest,
    ) -> main_models.UpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_with_options_async(workspace_id, model_id, request, headers, runtime)

    def update_model_connection_with_options(
        self,
        workspace_id: str,
        connection_id: str,
        tmp_req: main_models.UpdateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_connection_with_options_async(
        self,
        workspace_id: str,
        connection_id: str,
        tmp_req: main_models.UpdateModelConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateModelConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelConnection',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/model-connections/{DaraURL.percent_encode(connection_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_connection(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.UpdateModelConnectionRequest,
    ) -> main_models.UpdateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_connection_with_options(workspace_id, connection_id, request, headers, runtime)

    async def update_model_connection_async(
        self,
        workspace_id: str,
        connection_id: str,
        request: main_models.UpdateModelConnectionRequest,
    ) -> main_models.UpdateModelConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_connection_with_options_async(workspace_id, connection_id, request, headers, runtime)

    def update_skill_biz_tags_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillBizTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillBizTagsResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillBizTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillBizTags',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/biz-tags',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillBizTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_biz_tags_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillBizTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillBizTagsResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillBizTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillBizTags',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/biz-tags',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillBizTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_biz_tags(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillBizTagsRequest,
    ) -> main_models.UpdateSkillBizTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_skill_biz_tags_with_options(workspace_id, skill_name, request, headers, runtime)

    async def update_skill_biz_tags_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillBizTagsRequest,
    ) -> main_models.UpdateSkillBizTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_skill_biz_tags_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def update_skill_labels_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillLabelsResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillLabelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillLabels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_labels_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillLabelsResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillLabelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillLabels',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/labels',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_labels(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillLabelsRequest,
    ) -> main_models.UpdateSkillLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_skill_labels_with_options(workspace_id, skill_name, request, headers, runtime)

    async def update_skill_labels_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillLabelsRequest,
    ) -> main_models.UpdateSkillLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_skill_labels_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def update_skill_scope_with_options(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillScopeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillScopeResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillScope',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/scope',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_scope_with_options_async(
        self,
        workspace_id: str,
        skill_name: str,
        tmp_req: main_models.UpdateSkillScopeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillScopeResponse:
        tmp_req.validate()
        request = main_models.UpdateSkillScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillScope',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skills/{DaraURL.percent_encode(skill_name)}/scope',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_scope(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillScopeRequest,
    ) -> main_models.UpdateSkillScopeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_skill_scope_with_options(workspace_id, skill_name, request, headers, runtime)

    async def update_skill_scope_async(
        self,
        workspace_id: str,
        skill_name: str,
        request: main_models.UpdateSkillScopeRequest,
    ) -> main_models.UpdateSkillScopeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_skill_scope_with_options_async(workspace_id, skill_name, request, headers, runtime)

    def update_team_with_options(
        self,
        workspace_id: str,
        team_id: str,
        tmp_req: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_team_with_options_async(
        self,
        workspace_id: str,
        team_id: str,
        tmp_req: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        tmp_req.validate()
        request = main_models.UpdateTeamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_team(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_team_with_options(workspace_id, team_id, request, headers, runtime)

    async def update_team_async(
        self,
        workspace_id: str,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_team_with_options_async(workspace_id, team_id, request, headers, runtime)

    def update_user_with_options(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        tmp_req: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        tmp_req.validate()
        request = main_models.UpdateUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/users/{DaraURL.percent_encode(agent_core_user_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_with_options(workspace_id, agent_core_user_id, request, headers, runtime)

    async def update_user_async(
        self,
        workspace_id: str,
        agent_core_user_id: str,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(workspace_id, agent_core_user_id, request, headers, runtime)

    def update_workspace_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.UpdateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceResponse:
        tmp_req.validate()
        request = main_models.UpdateWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspace',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_workspace_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_async(
        self,
        workspace_id: str,
        request: main_models.UpdateWorkspaceRequest,
    ) -> main_models.UpdateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_workspace_with_options_async(workspace_id, request, headers, runtime)

    def upload_agent_spec_via_oss_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.UploadAgentSpecViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadAgentSpecViaOssResponse:
        tmp_req.validate()
        request = main_models.UploadAgentSpecViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadAgentSpecViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-spec-actions/upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAgentSpecViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_agent_spec_via_oss_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.UploadAgentSpecViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadAgentSpecViaOssResponse:
        tmp_req.validate()
        request = main_models.UploadAgentSpecViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadAgentSpecViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/agent-spec-actions/upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAgentSpecViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_agent_spec_via_oss(
        self,
        workspace_id: str,
        request: main_models.UploadAgentSpecViaOssRequest,
    ) -> main_models.UploadAgentSpecViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_agent_spec_via_oss_with_options(workspace_id, request, headers, runtime)

    async def upload_agent_spec_via_oss_async(
        self,
        workspace_id: str,
        request: main_models.UploadAgentSpecViaOssRequest,
    ) -> main_models.UploadAgentSpecViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_agent_spec_via_oss_with_options_async(workspace_id, request, headers, runtime)

    def upload_skill_via_oss_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.UploadSkillViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadSkillViaOssResponse:
        tmp_req.validate()
        request = main_models.UploadSkillViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadSkillViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadSkillViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_skill_via_oss_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.UploadSkillViaOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadSkillViaOssResponse:
        tmp_req.validate()
        request = main_models.UploadSkillViaOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadSkillViaOss',
            version = '2026-08-04',
            protocol = 'HTTPS',
            pathname = f'/workspaces/{DaraURL.percent_encode(workspace_id)}/skill-actions/upload-via-oss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadSkillViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_skill_via_oss(
        self,
        workspace_id: str,
        request: main_models.UploadSkillViaOssRequest,
    ) -> main_models.UploadSkillViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_skill_via_oss_with_options(workspace_id, request, headers, runtime)

    async def upload_skill_via_oss_async(
        self,
        workspace_id: str,
        request: main_models.UploadSkillViaOssRequest,
    ) -> main_models.UploadSkillViaOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_skill_via_oss_with_options_async(workspace_id, request, headers, runtime)
