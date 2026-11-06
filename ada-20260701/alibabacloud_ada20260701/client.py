# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_ada20260701 import models as main_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._product_id = 'Ada'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ada', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_agent_session_with_options(
        self,
        tmp_req: main_models.CancelAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CancelAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_agent_session_with_options_async(
        self,
        tmp_req: main_models.CancelAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CancelAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_agent_session(
        self,
        request: main_models.CancelAgentSessionRequest,
    ) -> main_models.CancelAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.cancel_agent_session_with_options(request, runtime)

    async def cancel_agent_session_async(
        self,
        request: main_models.CancelAgentSessionRequest,
    ) -> main_models.CancelAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.cancel_agent_session_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        request: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.knowledge_bases):
            body['KnowledgeBases'] = request.knowledge_bases
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.skills):
            body['Skills'] = request.skills
        if not DaraCore.is_null(request.system_prompt):
            body['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools):
            body['Tools'] = request.tools
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.knowledge_bases):
            body['KnowledgeBases'] = request.knowledge_bases
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.skills):
            body['Skills'] = request.skills
        if not DaraCore.is_null(request.system_prompt):
            body['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools):
            body['Tools'] = request.tools
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def create_agent_session_with_options(
        self,
        tmp_req: main_models.CreateAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_session_with_options_async(
        self,
        tmp_req: main_models.CreateAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_session(
        self,
        request: main_models.CreateAgentSessionRequest,
    ) -> main_models.CreateAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.create_agent_session_with_options(request, runtime)

    async def create_agent_session_async(
        self,
        request: main_models.CreateAgentSessionRequest,
    ) -> main_models.CreateAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_session_with_options_async(request, runtime)

    def create_skill_with_options(
        self,
        request: main_models.CreateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_with_options_async(
        self,
        request: main_models.CreateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill(
        self,
        request: main_models.CreateSkillRequest,
    ) -> main_models.CreateSkillResponse:
        runtime = RuntimeOptions()
        return self.create_skill_with_options(request, runtime)

    async def create_skill_async(
        self,
        request: main_models.CreateSkillRequest,
    ) -> main_models.CreateSkillResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_with_options_async(request, runtime)

    def create_transit_upload_policy_with_options(
        self,
        request: main_models.CreateTransitUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitUploadPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_ms):
            body['ExpireMs'] = request.expire_ms
        if not DaraCore.is_null(request.file_show_name):
            body['FileShowName'] = request.file_show_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.path_prefix):
            body['PathPrefix'] = request.path_prefix
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitUploadPolicy',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_upload_policy_with_options_async(
        self,
        request: main_models.CreateTransitUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitUploadPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_ms):
            body['ExpireMs'] = request.expire_ms
        if not DaraCore.is_null(request.file_show_name):
            body['FileShowName'] = request.file_show_name
        if not DaraCore.is_null(request.network):
            body['Network'] = request.network
        if not DaraCore.is_null(request.path_prefix):
            body['PathPrefix'] = request.path_prefix
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitUploadPolicy',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_upload_policy(
        self,
        request: main_models.CreateTransitUploadPolicyRequest,
    ) -> main_models.CreateTransitUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_transit_upload_policy_with_options(request, runtime)

    async def create_transit_upload_policy_async(
        self,
        request: main_models.CreateTransitUploadPolicyRequest,
    ) -> main_models.CreateTransitUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_upload_policy_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def delete_agent_session_with_options(
        self,
        tmp_req: main_models.DeleteAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSessionResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_session_with_options_async(
        self,
        tmp_req: main_models.DeleteAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentSessionResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent_session(
        self,
        request: main_models.DeleteAgentSessionRequest,
    ) -> main_models.DeleteAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_session_with_options(request, runtime)

    async def delete_agent_session_async(
        self,
        request: main_models.DeleteAgentSessionRequest,
    ) -> main_models.DeleteAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_session_with_options_async(request, runtime)

    def delete_skill_with_options(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_with_options_async(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_with_options(request, runtime)

    async def delete_skill_async(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_agent_session_with_options(
        self,
        tmp_req: main_models.GetAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSessionResponse:
        tmp_req.validate()
        request = main_models.GetAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            query['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_session_with_options_async(
        self,
        tmp_req: main_models.GetAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSessionResponse:
        tmp_req.validate()
        request = main_models.GetAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            query['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_session(
        self,
        request: main_models.GetAgentSessionRequest,
    ) -> main_models.GetAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.get_agent_session_with_options(request, runtime)

    async def get_agent_session_async(
        self,
        request: main_models.GetAgentSessionRequest,
    ) -> main_models.GetAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_session_with_options_async(request, runtime)

    def get_agent_session_model_with_options(
        self,
        tmp_req: main_models.GetAgentSessionModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSessionModelResponse:
        tmp_req.validate()
        request = main_models.GetAgentSessionModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            query['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSessionModel',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSessionModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_session_model_with_options_async(
        self,
        tmp_req: main_models.GetAgentSessionModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentSessionModelResponse:
        tmp_req.validate()
        request = main_models.GetAgentSessionModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            query['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentSessionModel',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentSessionModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_session_model(
        self,
        request: main_models.GetAgentSessionModelRequest,
    ) -> main_models.GetAgentSessionModelResponse:
        runtime = RuntimeOptions()
        return self.get_agent_session_model_with_options(request, runtime)

    async def get_agent_session_model_async(
        self,
        request: main_models.GetAgentSessionModelRequest,
    ) -> main_models.GetAgentSessionModelResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_session_model_with_options_async(request, runtime)

    def get_skill_with_options(
        self,
        request: main_models.GetSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_with_options_async(
        self,
        request: main_models.GetSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        return self.get_skill_with_options(request, runtime)

    async def get_skill_async(
        self,
        request: main_models.GetSkillRequest,
    ) -> main_models.GetSkillResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_with_options_async(request, runtime)

    def get_transit_meta_with_options(
        self,
        request: main_models.GetTransitMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransitMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_ms):
            query['ExpireMs'] = request.expire_ms
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.transit_id):
            query['TransitId'] = request.transit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransitMeta',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransitMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transit_meta_with_options_async(
        self,
        request: main_models.GetTransitMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransitMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_ms):
            query['ExpireMs'] = request.expire_ms
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.transit_id):
            query['TransitId'] = request.transit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransitMeta',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransitMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transit_meta(
        self,
        request: main_models.GetTransitMetaRequest,
    ) -> main_models.GetTransitMetaResponse:
        runtime = RuntimeOptions()
        return self.get_transit_meta_with_options(request, runtime)

    async def get_transit_meta_async(
        self,
        request: main_models.GetTransitMetaRequest,
    ) -> main_models.GetTransitMetaResponse:
        runtime = RuntimeOptions()
        return await self.get_transit_meta_with_options_async(request, runtime)

    def list_agent_sessions_with_options(
        self,
        tmp_req: main_models.ListAgentSessionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSessionsResponse:
        tmp_req.validate()
        request = main_models.ListAgentSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSessions',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_sessions_with_options_async(
        self,
        tmp_req: main_models.ListAgentSessionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentSessionsResponse:
        tmp_req.validate()
        request = main_models.ListAgentSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentSessions',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent_sessions(
        self,
        request: main_models.ListAgentSessionsRequest,
    ) -> main_models.ListAgentSessionsResponse:
        runtime = RuntimeOptions()
        return self.list_agent_sessions_with_options(request, runtime)

    async def list_agent_sessions_async(
        self,
        request: main_models.ListAgentSessionsRequest,
    ) -> main_models.ListAgentSessionsResponse:
        runtime = RuntimeOptions()
        return await self.list_agent_sessions_with_options_async(request, runtime)

    def list_agents_with_options(
        self,
        request: main_models.ListAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.q):
            query['Q'] = request.q
        if not DaraCore.is_null(request.required_runtime):
            query['RequiredRuntime'] = request.required_runtime
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: main_models.ListAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.q):
            query['Q'] = request.q
        if not DaraCore.is_null(request.required_runtime):
            query['RequiredRuntime'] = request.required_runtime
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        return self.list_agents_with_options(request, runtime)

    async def list_agents_async(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        return await self.list_agents_with_options_async(request, runtime)

    def list_models_with_options(
        self,
        request: main_models.ListModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_with_options_async(
        self,
        request: main_models.ListModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModels',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_models(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        return self.list_models_with_options(request, runtime)

    async def list_models_async(
        self,
        request: main_models.ListModelsRequest,
    ) -> main_models.ListModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_models_with_options_async(request, runtime)

    def list_skills_with_options(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.q):
            query['Q'] = request.q
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skills_with_options_async(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.q):
            query['Q'] = request.q
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skills(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return self.list_skills_with_options(request, runtime)

    async def list_skills_async(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return await self.list_skills_with_options_async(request, runtime)

    def load_agent_session_with_sse(
        self,
        tmp_req: main_models.LoadAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.LoadAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.LoadAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.LoadAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def load_agent_session_with_sse_async(
        self,
        tmp_req: main_models.LoadAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.LoadAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.LoadAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.LoadAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def load_agent_session_with_options(
        self,
        tmp_req: main_models.LoadAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadAgentSessionResponse:
        tmp_req.validate()
        request = main_models.LoadAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_agent_session_with_options_async(
        self,
        tmp_req: main_models.LoadAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadAgentSessionResponse:
        tmp_req.validate()
        request = main_models.LoadAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_agent_session(
        self,
        request: main_models.LoadAgentSessionRequest,
    ) -> main_models.LoadAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.load_agent_session_with_options(request, runtime)

    async def load_agent_session_async(
        self,
        request: main_models.LoadAgentSessionRequest,
    ) -> main_models.LoadAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.load_agent_session_with_options_async(request, runtime)

    def prompt_agent_session_with_sse(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.PromptAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PromptAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def prompt_agent_session_with_sse_async(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.PromptAgentSessionResponse, None, None]:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.PromptAgentSessionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def prompt_agent_session_with_options(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromptAgentSessionResponse:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromptAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def prompt_agent_session_with_options_async(
        self,
        tmp_req: main_models.PromptAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromptAgentSessionResponse:
        tmp_req.validate()
        request = main_models.PromptAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PromptAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromptAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prompt_agent_session(
        self,
        request: main_models.PromptAgentSessionRequest,
    ) -> main_models.PromptAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.prompt_agent_session_with_options(request, runtime)

    async def prompt_agent_session_async(
        self,
        request: main_models.PromptAgentSessionRequest,
    ) -> main_models.PromptAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.prompt_agent_session_with_options_async(request, runtime)

    def reply_agent_session_with_options(
        self,
        tmp_req: main_models.ReplyAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplyAgentSessionResponse:
        tmp_req.validate()
        request = main_models.ReplyAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplyAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplyAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reply_agent_session_with_options_async(
        self,
        tmp_req: main_models.ReplyAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplyAgentSessionResponse:
        tmp_req.validate()
        request = main_models.ReplyAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplyAgentSession',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplyAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reply_agent_session(
        self,
        request: main_models.ReplyAgentSessionRequest,
    ) -> main_models.ReplyAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.reply_agent_session_with_options(request, runtime)

    async def reply_agent_session_async(
        self,
        request: main_models.ReplyAgentSessionRequest,
    ) -> main_models.ReplyAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.reply_agent_session_with_options_async(request, runtime)

    def set_agent_session_model_with_options(
        self,
        tmp_req: main_models.SetAgentSessionModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAgentSessionModelResponse:
        tmp_req.validate()
        request = main_models.SetAgentSessionModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetAgentSessionModel',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAgentSessionModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_agent_session_model_with_options_async(
        self,
        tmp_req: main_models.SetAgentSessionModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAgentSessionModelResponse:
        tmp_req.validate()
        request = main_models.SetAgentSessionModelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.jsonrpc):
            body['Jsonrpc'] = request.jsonrpc
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetAgentSessionModel',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAgentSessionModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_agent_session_model(
        self,
        request: main_models.SetAgentSessionModelRequest,
    ) -> main_models.SetAgentSessionModelResponse:
        runtime = RuntimeOptions()
        return self.set_agent_session_model_with_options(request, runtime)

    async def set_agent_session_model_async(
        self,
        request: main_models.SetAgentSessionModelRequest,
    ) -> main_models.SetAgentSessionModelResponse:
        runtime = RuntimeOptions()
        return await self.set_agent_session_model_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        request: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not DaraCore.is_null(request.knowledge_bases):
            body['KnowledgeBases'] = request.knowledge_bases
        if not DaraCore.is_null(request.skills):
            body['Skills'] = request.skills
        if not DaraCore.is_null(request.system_prompt):
            body['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools):
            body['Tools'] = request.tools
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        request: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not DaraCore.is_null(request.knowledge_bases):
            body['KnowledgeBases'] = request.knowledge_bases
        if not DaraCore.is_null(request.skills):
            body['Skills'] = request.skills
        if not DaraCore.is_null(request.system_prompt):
            body['SystemPrompt'] = request.system_prompt
        if not DaraCore.is_null(request.tools):
            body['Tools'] = request.tools
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def update_skill_with_options(
        self,
        request: main_models.UpdateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_with_options_async(
        self,
        request: main_models.UpdateSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not DaraCore.is_null(request.metadata):
            body['Metadata'] = request.metadata
        if not DaraCore.is_null(request.visibility):
            body['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkill',
            version = '2026-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill(
        self,
        request: main_models.UpdateSkillRequest,
    ) -> main_models.UpdateSkillResponse:
        runtime = RuntimeOptions()
        return self.update_skill_with_options(request, runtime)

    async def update_skill_async(
        self,
        request: main_models.UpdateSkillRequest,
    ) -> main_models.UpdateSkillResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_with_options_async(request, runtime)
