# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appstream_center20210218 import models as appstream_center_20210218_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def expire_login_token_with_options(
        self,
        request: appstream_center_20210218_models.ExpireLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210218_models.ExpireLoginTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExpireLoginToken',
            version='2021-02-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210218_models.ExpireLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def expire_login_token_with_options_async(
        self,
        request: appstream_center_20210218_models.ExpireLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210218_models.ExpireLoginTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExpireLoginToken',
            version='2021-02-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210218_models.ExpireLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expire_login_token(
        self,
        request: appstream_center_20210218_models.ExpireLoginTokenRequest,
    ) -> appstream_center_20210218_models.ExpireLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.expire_login_token_with_options(request, runtime)

    async def expire_login_token_async(
        self,
        request: appstream_center_20210218_models.ExpireLoginTokenRequest,
    ) -> appstream_center_20210218_models.ExpireLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.expire_login_token_with_options_async(request, runtime)

    def get_auth_code_with_options(
        self,
        request: appstream_center_20210218_models.GetAuthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210218_models.GetAuthCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_user):
            body['AutoCreateUser'] = request.auto_create_user
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAuthCode',
            version='2021-02-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210218_models.GetAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_code_with_options_async(
        self,
        request: appstream_center_20210218_models.GetAuthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210218_models.GetAuthCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_user):
            body['AutoCreateUser'] = request.auto_create_user
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.external_user_id):
            body['ExternalUserId'] = request.external_user_id
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAuthCode',
            version='2021-02-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210218_models.GetAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_code(
        self,
        request: appstream_center_20210218_models.GetAuthCodeRequest,
    ) -> appstream_center_20210218_models.GetAuthCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_code_with_options(request, runtime)

    async def get_auth_code_async(
        self,
        request: appstream_center_20210218_models.GetAuthCodeRequest,
    ) -> appstream_center_20210218_models.GetAuthCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_code_with_options_async(request, runtime)
