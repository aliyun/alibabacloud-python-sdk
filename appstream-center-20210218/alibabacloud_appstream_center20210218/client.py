# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_appstream_center20210218 import models as main_models
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
        self._endpoint = self.get_endpoint('appstream-center', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def expire_login_token_with_options(
        self,
        request: main_models.ExpireLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpireLoginTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExpireLoginToken',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpireLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def expire_login_token_with_options_async(
        self,
        request: main_models.ExpireLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExpireLoginTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExpireLoginToken',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExpireLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expire_login_token(
        self,
        request: main_models.ExpireLoginTokenRequest,
    ) -> main_models.ExpireLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.expire_login_token_with_options(request, runtime)

    async def expire_login_token_async(
        self,
        request: main_models.ExpireLoginTokenRequest,
    ) -> main_models.ExpireLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.expire_login_token_with_options_async(request, runtime)

    def get_auth_code_with_options(
        self,
        request: main_models.GetAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_user):
            body['AutoCreateUser'] = request.auto_create_user
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthCode',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_code_with_options_async(
        self,
        request: main_models.GetAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_create_user):
            body['AutoCreateUser'] = request.auto_create_user
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not DaraCore.is_null(request.policy):
            body['Policy'] = request.policy
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthCode',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_code(
        self,
        request: main_models.GetAuthCodeRequest,
    ) -> main_models.GetAuthCodeResponse:
        runtime = RuntimeOptions()
        return self.get_auth_code_with_options(request, runtime)

    async def get_auth_code_async(
        self,
        request: main_models.GetAuthCodeRequest,
    ) -> main_models.GetAuthCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_auth_code_with_options_async(request, runtime)

    def get_sts_token_with_options(
        self,
        request: main_models.GetStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStsTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.expiration):
            body['Expiration'] = request.expiration
        if not DaraCore.is_null(request.external_id):
            body['ExternalId'] = request.external_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStsToken',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sts_token_with_options_async(
        self,
        request: main_models.GetStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStsTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.expiration):
            body['Expiration'] = request.expiration
        if not DaraCore.is_null(request.external_id):
            body['ExternalId'] = request.external_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStsToken',
            version = '2021-02-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sts_token(
        self,
        request: main_models.GetStsTokenRequest,
    ) -> main_models.GetStsTokenResponse:
        runtime = RuntimeOptions()
        return self.get_sts_token_with_options(request, runtime)

    async def get_sts_token_async(
        self,
        request: main_models.GetStsTokenRequest,
    ) -> main_models.GetStsTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_sts_token_with_options_async(request, runtime)
