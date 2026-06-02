# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_appflow20230904 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('appflow', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_flow_with_options(
        self,
        request: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.launch_status):
            query['LaunchStatus'] = request.launch_status
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.launch_status):
            query['LaunchStatus'] = request.launch_status
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_user_auth_config_with_options(
        self,
        request: main_models.CreateUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config):
            query['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_config_name):
            query['AuthConfigName'] = request.auth_config_name
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_auth_config_with_options_async(
        self,
        request: main_models.CreateUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config):
            query['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_config_name):
            query['AuthConfigName'] = request.auth_config_name
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_auth_config(
        self,
        request: main_models.CreateUserAuthConfigRequest,
    ) -> main_models.CreateUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.create_user_auth_config_with_options(request, runtime)

    async def create_user_auth_config_async(
        self,
        request: main_models.CreateUserAuthConfigRequest,
    ) -> main_models.CreateUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_user_auth_config_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_user_auth_config_with_options(
        self,
        request: main_models.DeleteUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_auth_config_with_options_async(
        self,
        request: main_models.DeleteUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_auth_config(
        self,
        request: main_models.DeleteUserAuthConfigRequest,
    ) -> main_models.DeleteUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_user_auth_config_with_options(request, runtime)

    async def delete_user_auth_config_async(
        self,
        request: main_models.DeleteUserAuthConfigRequest,
    ) -> main_models.DeleteUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_auth_config_with_options_async(request, runtime)

    def disable_flow_with_options(
        self,
        request: main_models.DisableFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_flow_with_options_async(
        self,
        request: main_models.DisableFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_flow(
        self,
        request: main_models.DisableFlowRequest,
    ) -> main_models.DisableFlowResponse:
        runtime = RuntimeOptions()
        return self.disable_flow_with_options(request, runtime)

    async def disable_flow_async(
        self,
        request: main_models.DisableFlowRequest,
    ) -> main_models.DisableFlowResponse:
        runtime = RuntimeOptions()
        return await self.disable_flow_with_options_async(request, runtime)

    def enable_flow_with_options(
        self,
        request: main_models.EnableFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_flow_with_options_async(
        self,
        request: main_models.EnableFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_flow(
        self,
        request: main_models.EnableFlowRequest,
    ) -> main_models.EnableFlowResponse:
        runtime = RuntimeOptions()
        return self.enable_flow_with_options(request, runtime)

    async def enable_flow_async(
        self,
        request: main_models.EnableFlowRequest,
    ) -> main_models.EnableFlowResponse:
        runtime = RuntimeOptions()
        return await self.enable_flow_with_options_async(request, runtime)

    def generate_user_session_token_with_options(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserSessionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not DaraCore.is_null(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserSessionToken',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserSessionTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_user_session_token_with_options_async(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUserSessionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_id):
            query['ChatbotId'] = request.chatbot_id
        if not DaraCore.is_null(request.expire_second):
            query['ExpireSecond'] = request.expire_second
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.integrate_id):
            query['IntegrateId'] = request.integrate_id
        if not DaraCore.is_null(request.user_avatar):
            query['UserAvatar'] = request.user_avatar
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUserSessionToken',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUserSessionTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_user_session_token(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
    ) -> main_models.GenerateUserSessionTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_user_session_token_with_options(request, runtime)

    async def generate_user_session_token_async(
        self,
        request: main_models.GenerateUserSessionTokenRequest,
    ) -> main_models.GenerateUserSessionTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_user_session_token_with_options_async(request, runtime)

    def get_flow_with_options(
        self,
        request: main_models.GetFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_with_options_async(
        self,
        request: main_models.GetFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow(
        self,
        request: main_models.GetFlowRequest,
    ) -> main_models.GetFlowResponse:
        runtime = RuntimeOptions()
        return self.get_flow_with_options(request, runtime)

    async def get_flow_async(
        self,
        request: main_models.GetFlowRequest,
    ) -> main_models.GetFlowResponse:
        runtime = RuntimeOptions()
        return await self.get_flow_with_options_async(request, runtime)

    def get_user_auth_config_with_options(
        self,
        request: main_models.GetUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_auth_config_with_options_async(
        self,
        request: main_models.GetUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_auth_config(
        self,
        request: main_models.GetUserAuthConfigRequest,
    ) -> main_models.GetUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.get_user_auth_config_with_options(request, runtime)

    async def get_user_auth_config_async(
        self,
        request: main_models.GetUserAuthConfigRequest,
    ) -> main_models.GetUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_user_auth_config_with_options_async(request, runtime)

    def invoke_action_with_sse(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.InvokeActionResponse, None, None]:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
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
                    main_models.InvokeActionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def invoke_action_with_sse_async(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.InvokeActionResponse, None, None]:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
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
                    main_models.InvokeActionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def invoke_action_with_options(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeActionResponse:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_action_with_options_async(
        self,
        tmp_req: main_models.InvokeActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvokeActionResponse:
        tmp_req.validate()
        request = main_models.InvokeActionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_config):
            request.auth_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_config, 'AuthConfig', 'json')
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        if not DaraCore.is_null(tmp_req.headers):
            request.headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        if not DaraCore.is_null(tmp_req.path):
            request.path_shrink = Utils.array_to_string_with_specified_style(tmp_req.path, 'Path', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.action_id):
            query['ActionId'] = request.action_id
        if not DaraCore.is_null(request.action_version):
            query['ActionVersion'] = request.action_version
        if not DaraCore.is_null(request.auth_config_shrink):
            query['AuthConfig'] = request.auth_config_shrink
        if not DaraCore.is_null(request.body_shrink):
            query['Body'] = request.body_shrink
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not DaraCore.is_null(request.path_shrink):
            query['Path'] = request.path_shrink
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAction',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_action(
        self,
        request: main_models.InvokeActionRequest,
    ) -> main_models.InvokeActionResponse:
        runtime = RuntimeOptions()
        return self.invoke_action_with_options(request, runtime)

    async def invoke_action_async(
        self,
        request: main_models.InvokeActionRequest,
    ) -> main_models.InvokeActionResponse:
        runtime = RuntimeOptions()
        return await self.invoke_action_with_options_async(request, runtime)

    def launch_flow_with_options(
        self,
        request: main_models.LaunchFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_flow_with_options_async(
        self,
        request: main_models.LaunchFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_flow(
        self,
        request: main_models.LaunchFlowRequest,
    ) -> main_models.LaunchFlowResponse:
        runtime = RuntimeOptions()
        return self.launch_flow_with_options(request, runtime)

    async def launch_flow_async(
        self,
        request: main_models.LaunchFlowRequest,
    ) -> main_models.LaunchFlowResponse:
        runtime = RuntimeOptions()
        return await self.launch_flow_with_options_async(request, runtime)

    def list_user_auth_configs_with_options(
        self,
        request: main_models.ListUserAuthConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAuthConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAuthConfigs',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAuthConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_auth_configs_with_options_async(
        self,
        request: main_models.ListUserAuthConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAuthConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAuthConfigs',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAuthConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_auth_configs(
        self,
        request: main_models.ListUserAuthConfigsRequest,
    ) -> main_models.ListUserAuthConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_user_auth_configs_with_options(request, runtime)

    async def list_user_auth_configs_async(
        self,
        request: main_models.ListUserAuthConfigsRequest,
    ) -> main_models.ListUserAuthConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_auth_configs_with_options_async(request, runtime)

    def update_flow_with_options(
        self,
        request: main_models.UpdateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        request: main_models.UpdateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.flow_desc):
            query['FlowDesc'] = request.flow_desc
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_template):
            query['FlowTemplate'] = request.flow_template
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow(
        self,
        request: main_models.UpdateFlowRequest,
    ) -> main_models.UpdateFlowResponse:
        runtime = RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    async def update_flow_async(
        self,
        request: main_models.UpdateFlowRequest,
    ) -> main_models.UpdateFlowResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_with_options_async(request, runtime)

    def update_user_auth_config_with_options(
        self,
        request: main_models.UpdateUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config):
            query['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.auth_config_name):
            query['AuthConfigName'] = request.auth_config_name
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_auth_config_with_options_async(
        self,
        request: main_models.UpdateUserAuthConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserAuthConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_config):
            query['AuthConfig'] = request.auth_config
        if not DaraCore.is_null(request.auth_config_id):
            query['AuthConfigId'] = request.auth_config_id
        if not DaraCore.is_null(request.auth_config_name):
            query['AuthConfigName'] = request.auth_config_name
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_version):
            query['ConnectorVersion'] = request.connector_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserAuthConfig',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_auth_config(
        self,
        request: main_models.UpdateUserAuthConfigRequest,
    ) -> main_models.UpdateUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return self.update_user_auth_config_with_options(request, runtime)

    async def update_user_auth_config_async(
        self,
        request: main_models.UpdateUserAuthConfigRequest,
    ) -> main_models.UpdateUserAuthConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_user_auth_config_with_options_async(request, runtime)

    def withdraw_flow_with_options(
        self,
        request: main_models.WithdrawFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_flow_with_options_async(
        self,
        request: main_models.WithdrawFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawFlow',
            version = '2023-09-04',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_flow(
        self,
        request: main_models.WithdrawFlowRequest,
    ) -> main_models.WithdrawFlowResponse:
        runtime = RuntimeOptions()
        return self.withdraw_flow_with_options(request, runtime)

    async def withdraw_flow_async(
        self,
        request: main_models.WithdrawFlowRequest,
    ) -> main_models.WithdrawFlowResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_flow_with_options_async(request, runtime)
